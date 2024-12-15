"""Generate and check werkzeug.security password hashes on the command line"""

__version__ = "1.1.0"

import argparse
import getpass

import werkzeug.security

def get_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description = __doc__)

    parser_action = parser.add_subparsers(required = True, dest = "action")

    password_help = "password, or '-' to read from stdin using getpass"

    parser_action_generate = parser_action.add_parser("generate", description = (description := "werkzeug.security.generate_password_hash"), help = description)
    parser_action_generate.add_argument("password", help = password_help)
    parser_action_generate.add_argument("--method")
    parser_action_generate.add_argument("--salt-length", type = int)

    parser_action_check = parser_action.add_parser("check", description = (description := "werkzeug.security.check_password_hash"), help = description)
    parser_action_check.add_argument("pwhash")
    parser_action_check.add_argument("password", help = password_help)

    args = parser.parse_args()

    return args

def get_password(args) -> str:
    ret = args.password
    if ret == "-":
        ret = getpass.getpass()
    return ret

def main_generate(args) -> None:
    password = get_password(args)

    kwargs = {}
    if (method := args.method) is not None:
        kwargs["method"] = method
    if (salt_length := args.salt_length) is not None:
        kwargs["salt_length"] = salt_length

    print(werkzeug.security.generate_password_hash(password, **kwargs))

def main_check(args) -> None:
    password = get_password(args)

    if werkzeug.security.check_password_hash(args.pwhash, password):
        print("True")
    else:
        raise SystemExit("False")

def main() -> None:
    args = get_cli_args()

    {
        "generate": main_generate,
        "check":    main_check,
    }[args.action](args)

if __name__ == "__main__":
    main()
