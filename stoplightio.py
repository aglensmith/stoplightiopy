import os
import argparse
import json
import requests
import time

# Client #####################################################################
class Api(object):
    
    def __init__ (self, bearer):
        self.domain = "https://next-api.stoplight.io"
        self.bearer = bearer
        self.endpoint = None
        self.headers = {"Authorization": "Bearer " + self.bearer}
        self.content_headers = self.headers
        self.content_headers['Content-Type'] = 'application/json'
        self.resource_key = None

    def get(self, endpoint):
        r = requests.get(self.domain + endpoint, headers=self.headers)
        return json.loads(r.text)

    def post(self, endpoint, data=None):
        url = self.domain + endpoint
        r = requests.post(url, headers=self.content_headers, data=data)
        return r
    
    def put(self, endpoint, data=None):
        url = self.domain + endpoint
        r = requests.get(url, headers=self.content_headers, data=data)
        return r
    
    def delete(self, endpoint):
        url = self.domain + endpoint
        r = requests.delete(url, headers=self.headers)
        return r

    def define_key(self):
        return

class Organization(Api):

      def __init__(self, project_id, *args, **kwargs):
        super(Organization, self).__init__(*args, **kwargs)
        self.endpoint = "/docs"
        self.project_id = project_id

class Project(Api):

    def __init__(self, project_id, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)
        self.endpoint = "/docs"
        self.project_id = str(project_id)

    def get_all_domains(self):
        return self.get("/docs.list?projectId=" + self.project_id)

class Domain(Api):

    def __init__(self, domain_id, *args, **kwargs):
        super(Domain, self).__init__(*args, **kwargs)
        self.prefix = "/docs"
        self.domain_id = str(domain_id)
        self.query = "?id=" + self.domain_id
        self.url = self.prefix + "%s" + self.query

    def build(self):
      r = self.post("/docs.release?id=" + self.domain_id)
      return r

    def get_build(self, build_id):
      r = self.get("/docs.builds.info?docId=" + self.domain_id + "&id=" + str(build_id))
      return r

    def config(self, update_to=None):
        if update_to is not None:
          return self.post(self.url % ".updateConfig", data=json.dumps(update_to, ensure_ascii=False))
        else:
          return self.get(self.url % ".info")["doc"]["config"]

    def redirects(self):
        return self.config()["redirects"]

# CLI HELPERS #################################################################

def build_domains(domain_id, token, pretty):
    for id in domain_id:
        d = Domain(id, token)
        r = json.loads(d.build().text)

        if pretty and "build" in r.keys():
             b = r["build"]
             print(f"\n{b['id']} | {b['docId']} | {b['status']['code']} | {b['status']['message']}")
             
             success = False
             while not success:
                input("Press Enter to Check Build Status")
                b = d.get_build(b['id'])["build"]
                print(f"\n{b['id']} | {b['docId']} | {b['status']['code']} | {b['status']['message']}")
                success = (b['status']['code'] == "success")
        else:
            print(d.build().text)

def get_build_status(domain, build_id, token, pretty):
    
    d = Domain(domain, token)
        
    r = d.get_build(build_id)

    if pretty and "build" in r.keys():
            b = r["build"]
            # print(b[0])
            print(f"\n{b['id']} | {b['docId']} | {b['status']['code']} | {b['status']['message']}")
    else:
        print(r)

def list_domains(project_id, token):
    p = Project(project_id, token)
    for domain in p.get_all_domains()["docs"]:
        print(str(domain["id"]) + " " + domain["domain"])

def print_config(domain_id, token):
    print(Domain(domain_id, token).config())

def print_redirects(domain_id, token):
    print(Domain(domain_id, token).redirects())

def find_token(options_token, env_variable):
    if options_token:
        return options_token
    if env_variable in os.environ.keys() and len(os.environ[env_variable]) > 0:
        return os.environ[env_variable]
    else:
        raise ValueError("No StoplightIO API Token Supplied")

# CLI #########################################################################
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(prog="python stoplightio.py", description='stoplightio.py CLI')
    parser.add_argument('--build',     metavar='ID', type=int, help='build a list of domain ids', nargs='+',)
    parser.add_argument('--domain',    metavar='ID', type=int, help='store domain id')
    parser.add_argument('--status',    metavar='ID', type=int, help='get status of a build')
    parser.add_argument('--token',     metavar='TK', type=str, help='StoplightIO API Token')
    parser.add_argument('--domains',   metavar='ID', type=int, help="return a list of domains for project [ID]")
    parser.add_argument('--config',    metavar='ID', type=int, help="get the config for domain [ID]")
    parser.add_argument('--redirects', metavar='ID', type=int, help="get the redirects for domain [ID]")
    parser.add_argument('--pretty',    action="store_true",     help="pretty print?")
    options = parser.parse_args()
    
    _BEARER = find_token(options.token, "SL_API_TOKEN")

    if options.build:
        build_domains(options.build, _BEARER, options.pretty)
    if options.domains:
        list_domains(options.domains, _BEARER)
    if options.config:
        print_config(options.config, _BEARER)
    if options.redirects:
        print_redirects(options.redirects, _BEARER)
    if options.status:
        get_build_status(options.domain, options.status, _BEARER, options.pretty)
        