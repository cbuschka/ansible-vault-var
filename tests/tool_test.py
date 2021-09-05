import unittest
from io import StringIO, BytesIO, TextIOWrapper

from bytesbufio import BytesBufferIO

from ansible_vault_var.tool import Tool

VAULT_PASSWORD = "asdfasdf"
SECRET_VARS = """
secret_ingredient: !vault |
  $ANSIBLE_VAULT;1.1;AES256
  62386330363038383366333165373565373931663964363532336238613164306232393463376133
  6633313163666264383236336164656335383165623462650a336230613836333231333865656435
  61383830633137623863356138353436653038656534626532656137393863316231393132386636
  6665373133383036390a636466333663336563303533666463366261373164303237666663656564
  3635
secret_ingredient2: !vault |
  $ANSIBLE_VAULT;1.1;AES256
  30666437333137383962323561303130376139626264663465313963396436326234626262366130
  3031363564326361393139386532383165636461636465350a333238626437666231633136356162
  31663835383762383339306230623339363934633063613466656561383138333539356330356162
  3137643639656534660a356363383638653162623336623066383862336464333530393030373564
  6661
"""


class ToolTest(unittest.TestCase):
  def setUp(self) -> None:
    self.tool = Tool(vault_password="asdfasdf")

  def test_get_var(self):
    self.tool.load_vars(vars_file=StringIO(initial_value=SECRET_VARS))
    secret_ingredient = self.tool.get_var("secret_ingredient")
    self.assertEqual("butter", secret_ingredient)

  def test_set_var(self):
    self.tool.load_vars(vars_file=StringIO(initial_value=SECRET_VARS))
    self.tool.set_var("secret_ingredient2", value="pepper")
    bytesbuf = BytesBufferIO()
    self.tool.save_vars(vars_file=TextIOWrapper(bytesbuf, encoding='utf-8'))
    self.tool.load_vars(vars_file=BytesIO(bytesbuf.getvalue()))
    secret_ingredient = self.tool.get_var("secret_ingredient2")
    self.assertEqual("pepper", secret_ingredient)
