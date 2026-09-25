import os
import re

from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


class RepairAgent:

    def __init__(self):

        if API_KEY:
            self.client = genai.Client(api_key=API_KEY)
        else:
            self.client = None

    def repair_code(self, code, vulnerabilities):

        if self.client:

            try:

                vulnerability_text = ""

                for vulnerability in vulnerabilities:

                    vulnerability_text += (
                        f"Type: {vulnerability['type']}\n"
                        f"Severity: {vulnerability['severity']}\n"
                        f"Line: {vulnerability['line']}\n"
                        f"Message: {vulnerability['message']}\n\n"
                    )

                prompt = f"""
You are a secure code repair agent.

Repair the following Python code.

Detected vulnerabilities:

{vulnerability_text}

Requirements:

1. Fix all detected security vulnerabilities.
2. Preserve the original functionality as much as possible.
3. Do not introduce new security problems.
4. Return only Python code.
5. Do not use Markdown code fences.

Original code:

{code}
"""

                response = self.client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                return response.text

            except Exception as e:

                print("\nGemini API unavailable.")
                print("Using local repair engine instead.\n")

        return self.local_repair(code, vulnerabilities)

    def local_repair(self, code, vulnerabilities):

        repaired_code = code

        for vulnerability in vulnerabilities:

            vulnerability_type = vulnerability["type"]

            if vulnerability_type == "Hardcoded Secret":

                repaired_code = re.sub(
                    r"(password|passwd|api_key|secret|token)\s*=\s*['\"][^'\"]+['\"]",
                    r"\1 = os.getenv('\1')",
                    repaired_code,
                    flags=re.IGNORECASE
                )

                if "import os" not in repaired_code:
                    repaired_code = "import os\n\n" + repaired_code

            elif vulnerability_type == "Dangerous eval()":

                repaired_code = re.sub(
                    r"eval\s*\((.*?)\)",
                    r"input(\1)",
                    repaired_code
                )

            elif vulnerability_type == "Dangerous exec()":

                repaired_code = re.sub(
                    r"exec\s*\((.*?)\)",
                    r"print(\1)",
                    repaired_code
                )

            elif vulnerability_type == "Command Injection Risk":

                repaired_code = re.sub(
                    r"os\.system\s*\((.*?)\)",
                    r"print('Command blocked for security')",
                    repaired_code
                )

            elif vulnerability_type == "Shell Injection Risk":

                repaired_code = re.sub(
                    r"subprocess\.run\s*\((.*?)\)",
                    r"print('Shell command blocked for security')",
                    repaired_code
                )

        return repaired_code