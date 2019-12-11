from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'passwd_checker',
  packages = find_packages(),
  package_data={
    'passwd_checker': ['data/*.txt'],
    },
  version = '0.0.1',
  description = 'Check a password against SecLists & other various custom requirements',
  author = 'Universami',
  author_email = 'un1v3rs4m1@protonmail.com',
  url = 'https://github.com/universami/passwd-checker',
  download_url = 'https://github.com/universami/passwd-checker/archive/0.0.1.tar.gz',
  keywords = ['password', 'checker', 'seclist'], 
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
  ],
)
