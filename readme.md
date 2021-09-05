[![Build](https://img.shields.io/github/workflow/status/cbuschka/ansible-vault-var/build)](https://github.io/cbuschka/ansible-vault-var) [![PyPI](https://img.shields.io/pypi/v/ansible-vault-var)](https://pypi.org/project/ansible-vault-var/) [![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://github.com/cbuschka/ansible-vault-var/blob/main/license.txt)

# ansible-vault-var - Get and set encrypted values in vars yaml file.

## Features

* get encrypted value as plain text from ansible vars yaml file
* set encrypted value from plain text in ansible vars yaml file

## Prerequisites

* GNU make
* python >= 3.6
* pipenv

## Usage

### Get variable

```
python3 -m ansible_vault_var --vault-password-file=vault_password.txt \
	get_var --var-name=secret_ingredient --vars-file=secret_vars.yml
```

### Set variable

```
python3 -m ansible_vault_var --vault-password-file=vault_password.txt \
	set_var --var-name=secret_ingredient --vars-file=secret_vars.yml --new-var-value=salt
```

Copyright (c) 2021 by [Cornelius Buschka](https://github.com/cbuschka).

[MIT](./license.txt)
