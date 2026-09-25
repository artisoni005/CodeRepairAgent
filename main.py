from scanner import scan_code
from repair_agent import RepairAgent
from tester import validate_code, validate_security


code = """
import os

password = "admin123"

user_input = input("Enter command: ")

os.system(user_input)

eval(user_input)
"""


print("\n===== ORIGINAL CODE =====")
print(code)


print("\n===== SECURITY SCAN =====")

vulnerabilities = scan_code(code)

if not vulnerabilities:

    print("No vulnerabilities detected.")

else:

    for vulnerability in vulnerabilities:

        print("Type:", vulnerability["type"])
        print("Severity:", vulnerability["severity"])
        print("Line:", vulnerability["line"])
        print("Message:", vulnerability["message"])
        print("-" * 40)


if vulnerabilities:

    print("\n===== AI REPAIR =====")

    agent = RepairAgent()

    repaired_code = agent.repair_code(
        code,
        vulnerabilities
    )

    print("\n===== REPAIRED CODE =====")
    print(repaired_code)


    print("\n===== SYNTAX VALIDATION =====")

    syntax_result = validate_code(repaired_code)

    print("Status:", syntax_result["status"])
    print("Message:", syntax_result["message"])


    print("\n===== SECURITY VALIDATION =====")

    security_result = validate_security(
        repaired_code,
        scan_code
    )

    print("Status:", security_result["status"])
    print("Message:", security_result["message"])


    if security_result["status"] == "FAIL":

        print("\nRemaining vulnerabilities:")

        for vulnerability in security_result["vulnerabilities"]:

            print(
                vulnerability["type"],
                "- Line",
                vulnerability["line"]
            )

else:

    print("\nNo repair required.")