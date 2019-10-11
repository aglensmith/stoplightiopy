# stoplightio.py

## Usage

```shell
usage: python stoplightio.py [-h] [--build ID [ID ...]] [--token TK]
                             [--domains ID] [--config ID] [--redirects ID]

stoplightio.py CLI

optional arguments:
  -h, --help           show this help message and exit
  --build ID [ID ...]  build a list of domain ids
  --token TK           StoplightIO API Token
  --domains ID         return a list of domains for project [ID]
  --config ID          get the config for domain [ID]
  --redirects ID       get the redirects for domain [ID]
```

To authenticate the API, supply a token using the `--token` switch:

```shell

```

If a token isn't supplied with `--token`, stoplightio.py will look for an environment variable called `SL_API_TOKEN` and use its value for authentication. Set the environment variable in the terminal or in your `.bashrc` file:

```shell
# run in terminal or add to .bashrc
export SL_API_TOKEN={token}
```