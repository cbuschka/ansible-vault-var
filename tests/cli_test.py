import unittest

from ansible_vault_var.cli import parse_args


class CliTest(unittest.TestCase):
  def test_get_var(self):
    args = parse_args(
      ["--vault-password", "asdfasdf", "get_var", "--var-name", "secret_ingredient", "--vars-file", "vars.yml"])
    self.assertEqual("get_var", args.subcommand)
    self.assertEqual("asdfasdf", args.vault_password)
    self.assertEqual("secret_ingredient", args.var_name)
    self.assertEqual("vars.yml", args.vars_file)

  def test_set_var(self):
    args = parse_args(
      ["--vault-password", "asdfasdf", "set_var", "--var-name", "secret_ingredient", "--vars-file", "vars.yml",
       "--new-var-value", "salt"])
    self.assertEqual("set_var", args.subcommand)
    self.assertEqual("asdfasdf", args.vault_password)
    self.assertEqual("secret_ingredient", args.var_name)
    self.assertEqual("vars.yml", args.vars_file)
    self.assertEqual("salt", args.new_var_value)
