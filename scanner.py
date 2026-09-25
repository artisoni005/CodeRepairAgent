import ast
import re


def scan_code(code):
    vulnerabilities = []

    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return [{
            "type": "Syntax Error",
            "severity": "HIGH",
            "line": e.lineno,
            "message": str(e)
        }]

    for node in ast.walk(tree):

        # Detect eval()
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id == "eval":
                    vulnerabilities.append({
                        "type": "Dangerous eval()",
                        "severity": "HIGH",
                        "line": node.lineno,
                        "message": "eval() can execute arbitrary code."
                    })

        # Detect exec()
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id == "exec":
                    vulnerabilities.append({
                        "type": "Dangerous exec()",
                        "severity": "HIGH",
                        "line": node.lineno,
                        "message": "exec() can execute arbitrary code."
                    })

        # Detect os.system()
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                if (
                    isinstance(node.func.value, ast.Name)
                    and node.func.value.id == "os"
                    and node.func.attr == "system"
                ):
                    vulnerabilities.append({
                        "type": "Command Injection Risk",
                        "severity": "HIGH",
                        "line": node.lineno,
                        "message": "os.system() can execute operating-system commands."
                    })

        # Detect subprocess.run(..., shell=True)
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                if node.func.attr == "run":
                    for keyword in node.keywords:
                        if (
                            keyword.arg == "shell"
                            and isinstance(keyword.value, ast.Constant)
                            and keyword.value.value is True
                        ):
                            vulnerabilities.append({
                                "type": "Shell Injection Risk",
                                "severity": "HIGH",
                                "line": node.lineno,
                                "message": "subprocess.run(..., shell=True) can allow command injection."
                            })

    # Detect hardcoded passwords, API keys, tokens, etc.
    lines = code.splitlines()

    for line_number, line in enumerate(lines, start=1):

        pattern = r"(password|passwd|api_key|secret|token)\s*=\s*['\"][^'\"]+['\"]"

        if re.search(pattern, line, re.IGNORECASE):
            vulnerabilities.append({
                "type": "Hardcoded Secret",
                "severity": "MEDIUM",
                "line": line_number,
                "message": "A password, API key, token, or secret appears to be hardcoded."
            })

    return vulnerabilities


if __name__ == "__main__":

    test_code = """
import os

password = "admin123"

user_input = input("Enter command: ")

os.system(user_input)

eval(user_input)
"""

    results = scan_code(test_code)

    print("\n===== CODE SECURITY SCAN =====\n")

    if not results:
        print("No vulnerabilities detected.")
    else:
        for vulnerability in results:
            print("Type:", vulnerability["type"])
            print("Severity:", vulnerability["severity"])
            print("Line:", vulnerability["line"])
            print("Message:", vulnerability["message"])
            print("-" * 40)