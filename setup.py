import os
import subprocess
import re

import setuptools


def get_readme(version):
  with open("readme.md", "r", encoding='utf-8') as f:
    return re.sub(r"]\(\./",
                  f"](https://github.com/cbuschka/ansible-vault-var/blob/v{version}/",
                  f.read())


def get_version():
  proc = subprocess.Popen(
      ["/bin/bash", "-c",
       "git describe --exact-match --tags 2>/dev/null || echo 'v0.0.0.alpha.0'"],
      shell=False,
      stdout=subprocess.PIPE,
      stderr=subprocess.STDOUT)
  stdout, stderr = proc.communicate()
  print(stdout)
  print(stderr)
  result = re.search('^v([^\n]+)\n$', stdout.decode("utf-8"), re.S)
  if not result:
    raise ValueError("Invalid version: '{}'.".format(result))
  return result.group(1)


VERSION = get_version()
long_description = get_readme(VERSION)
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(PACKAGE_ROOT, 'requirements.txt')) as f:
  REQUIREMENTS = [r.strip() for r in f.readlines()]

setuptools.setup(
    name='ansible-vault-var',
    version=VERSION,
    description='Get and set encrypted values in vars yaml file.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=('tests',)),
    namespace_packages=[],
    python_requires='>= 3.6',
    install_requires=REQUIREMENTS,
    author='Cornelius Buschka',
    author_email='cbuschka@gmail.com',
    url='https://github.com/cbuschka/ansible-vault-var',
    platforms='Posix; MacOS X',
    include_package_data=True,
    zip_safe=False,
    license='MIT License',
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Topic :: System :: Software Distribution',
    ],
)
