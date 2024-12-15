# WerkzeugSecurityCLI

A CLI wrapper around

- `werkzeug.security.generate_password_hash`
- `werkzeug.security.check_password_hash`

for generating and checking [`werkzeug.security`](https://werkzeug.palletsprojects.com/en/stable/utils/#module-werkzeug.security) password hashes on the command line

## Disclaimer!

Not associated with [Werkzeug](https://github.com/pallets/werkzeug/) in any way! (other than using their wonderful software :D)

## Examples

```
$ HASH=$(wzscli generate my-test-password-123)
$ echo "${HASH}"
scrypt:32768:8:1$pyMfKdIqwYxw0GOT$6d49052bdf9cffb2288d7cb198d7bed5566f284932dad0c74b3948866b1468220afd93e9aa17069c4a2403d33747e5e71981c3c552d751a0e249642b6641bac5
$ wzscli check "${HASH}" my-test-password-12
False
$ wzscli check "${HASH}" my-test-password-123
True
```

One can supply the `password` positional argument directly in the command line argv as above, or supply `-` to read the password from stdin using Python's `getpass` module as below

```
$ HASH=$(wzscli generate -)
> Password: # sneedy-feedy
$ wzscli check "${HASH}" -
> Password: # sneedy-feedy
True
```

## Installing

Available on PyPI as [WerkzeugSecurityCLI](https://pypi.org/project/WerkzeugSecurityCLI/).

I like to use `pipx` to manage Python CLI utils:

```
$ pipx install WerkzeugSecurityCLI
```
