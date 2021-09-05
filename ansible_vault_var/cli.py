import argparse
import os
import sys

from ansible_vault_var import console
from ansible_vault_var.tool import Tool


def parse_args(args):
  arg_parser = argparse.ArgumentParser(description="Manage encrypted vars in yaml file.")
  vault_password_source_group = arg_parser.add_mutually_exclusive_group(required=True)
  vault_password_source_group.add_argument('--vault-password-file', type=str, dest="vault_password_file",
                                           help='the vault password file')
  vault_password_source_group.add_argument('--vault-password', type=str, dest="vault_password",
                                           help='the vault password')
  subparsers = arg_parser.add_subparsers(dest="subcommand")
  get_var_arg_parser = subparsers.add_parser('get_var', aliases=[])
  get_var_arg_parser.add_argument('--var-name', type=str, dest="var_name", help='the var name', required=True)
  get_var_arg_parser.add_argument('--vars-file', type=str, dest="vars_file", help='the vars file to read and write',
                                  required=True)
  set_var_arg_parser = subparsers.add_parser('set_var', aliases=[])
  set_var_arg_parser.add_argument('--var-name', type=str, dest="var_name", help='the var name', required=True)
  set_var_arg_parser.add_argument('--vars-file', type=str, dest="vars_file", help='the vars file to read and write',
                                  required=True)
  var_value_source_group = set_var_arg_parser.add_mutually_exclusive_group(required=True)
  var_value_source_group.add_argument('--new-var-value', type=str, dest="new_var_value", help='the new var value')
  var_value_source_group.add_argument('--new-var-value-file', type=str, dest="new_var_value_file",
                                      help='file to read the new var value from')
  return arg_parser.parse_args(args)


def set_var(args, *, tool, console):
  if os.path.isfile(args.vars_file):
    tool.load_vars(vars_file=args.vars_file)
  if args.new_var_value:
    new_var_value = args.new_var_value
  else:
    with open(args.new_var_value_file, 'r') as f:
      new_var_value = f.read().strip()
  tool.set_var(args.var_name, value=new_var_value)
  tool.save_vars(vars_file=args.vars_file)
  console.print_out(f"Secret var {args.var_name} changed, file {args.vars_file} written.", flush=True)


def get_var(args, *, tool, console):
  tool.load_vars(vars_file=args.vars_file)
  var_value = tool.get_var(var_name=args.var_name)
  if var_value is None:
    console.print_err(f"{args.var_name} is undefined.", flush=True)
    sys.exit(1)
  console.print_out(f"{args.var_name}: {var_value}", flush=True)


def main():
  args = parse_args(sys.argv[1:])
  tool = Tool(vault_password=args.vault_password,
              vault_password_file=args.vault_password_file)
  if args.subcommand == "get_var":
    get_var(args, tool=tool, console=console.console)
  elif args.subcommand == "set_var":
    set_var(args, tool=tool, console=console.console)
