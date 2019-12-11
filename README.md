
# passwd-checker 

[![Build Status](https://travis-ci.org/universami/passwd-checker.svg?branch=master)](https://travis-ci.org/universami/passwd-checker)

Check passwords against Daniel Miessler's SecLists & other custom requirements

## Installing

Using pip:

```bash
$ pip install passwd-checker
```
----------------------------

## Examples

Check a password against SecLists

```python
import passwd_checker.checker as checker

level = 1 # The level of the check can be between 1-4
checker.seclist('password', level) # Returns True

level = 4
checker.seclist('th1s-P4ssw0rd-1s-n0T-c0mm0n', level) # Returns False

# Level 1: 1k passwords
# Level 2: 10k passwords
# Level 3: 100k password
# Level 4: 1 million passwords
```

-------------------------------

## Development

Run unit tests

```bash
$ python test.py
```

Update the *version* and *download_url* in *setup.py*

Build the module

```bash
$ python setup.py sdist bdist_wheel
```

Release (Github)

```bash
$ git tag 0.x.x

$ git push --tags
```
Release (PyPi)

```bash
$ python -m twine upload dist/*
```
