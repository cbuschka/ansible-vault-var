import sys


class Console(object):
  def __init__(self, out, err):
    self.out = out
    self.err = err

  def print_out(self, message, flush=False):
    print(message, file=self.out, flush=flush)

  def print_err(self, message, flush=True):
    print(message, file=self.err, flush=flush)


console = Console(sys.stdout, sys.stderr)
