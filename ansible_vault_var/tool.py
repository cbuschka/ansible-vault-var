from ansible.constants import DEFAULT_VAULT_ID_MATCH
from ansible.parsing.vault import VaultLib
from ansible.parsing.vault import VaultSecret

from .vars_yaml import load_vars_yaml, save_vars_yaml, VaultTag


class Tool(object):
  def __init__(self, *, vault_password=None, vault_password_file=None):
    self.vars_dict = {}
    self.vault_lib = self._create_vault_lib(vault_password=vault_password, vault_password_file=vault_password_file)

  def load_vars(self, vars_file) -> None:
    self.vars_dict = load_vars_yaml(vars_file)

  def save_vars(self, vars_file) -> None:
    return save_vars_yaml(self.vars_dict, vars_file)

  def set_var(self, var_name, *, value=None):
    self.vars_dict[var_name] = VaultTag(self._encrypt_value(value))

  def get_var(self, var_name):
    var_value = self.vars_dict.get(var_name, None)
    if var_value is None:
      return None
    if isinstance(var_value, VaultTag):
      var_value = self._decrypt_value(var_value.value)
    return var_value

  def _decrypt_value(self, encrypted_value) -> str:
    return self.vault_lib.decrypt(encrypted_value.encode("UTF-8")).decode("UTF-8")

  def _encrypt_value(self, plaintext_value: str) -> str:
    return self.vault_lib.encrypt(plaintext_value).decode("UTF-8")

  def _create_vault_lib(self, vault_password: str = None, vault_password_file: str = None):
    if vault_password_file:
      with open(vault_password_file, 'r') as f:
        vault_password = f.read()

    return VaultLib([(DEFAULT_VAULT_ID_MATCH, VaultSecret(vault_password.encode("UTF-8")))])
