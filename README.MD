# stoplightio.py

Python API Client and CLI for StoplightIO

## Installation

```shell
# clone the repo
git clone git@github.com:aglensmith/stoplightiopy.git

# move .py to user bin folder
mv stoplightiopy/stoplightio.py ~/bin
```

## Authentication
To authenticate API requests from the CLI, supply a token using the `--token` switch:

```shell
python stoplightio.py --token {token} --build {domain_id}
```

Or, store the token in an environment variable called `SL_API_TOKEN`:

```shell
# run in terminal or add to .bashrc
export SL_API_TOKEN={token}

python stoplightio.py --build {domain_id}
```

## CLI Usage

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
