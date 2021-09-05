import yaml


class VaultTag(yaml.YAMLObject):
  yaml_tag = '!vault'

  def __init__(self, value):
    self.value = value

  def __repr__(self):
    return "VaultTag(value={})".format(self.value)

  @classmethod
  def from_yaml(cls, loader, node):
    return VaultTag(node.value)

  @classmethod
  def to_yaml(cls, dumper, data):
    return dumper.represent_scalar(cls.yaml_tag, data.value, style='|')


yaml.Loader.add_constructor(VaultTag.yaml_tag, VaultTag.from_yaml)


def load_vars_yaml(vars_file):
  if isinstance(vars_file, str):
    with open(vars_file, 'r') as f:
      vars_dict = yaml.load(f, Loader=yaml.Loader)
  else:
    vars_dict = yaml.load(vars_file, Loader=yaml.Loader)
  if not vars_dict:
    return {}
  return vars_dict


def save_vars_yaml(vars_dict, vars_file):
  if isinstance(vars_file, str):
    with open(vars_file, 'w') as f:
      yaml.dump(vars_dict, f)
  else:
    yaml.dump(vars_dict, vars_file)
