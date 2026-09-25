import ast


def validate_code(code):
    try:
        ast.parse(code)

        return {
            "status": "PASS",
            "message": "Repaired code is syntactically valid."
        }

    except SyntaxError as e:

        return {
            "status": "FAIL",
            "message": f"Syntax error at line {e.lineno}: {e.msg}"
        }


def validate_security(code, scanner):

    vulnerabilities = scanner(code)

    if len(vulnerabilities) == 0:

        return {
            "status": "PASS",
            "message": "No known security vulnerabilities detected."
        }

    return {
        "status": "FAIL",
        "message": f"{len(vulnerabilities)} security issue(s) still detected.",
        "vulnerabilities": vulnerabilities
    }