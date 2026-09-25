# 🛡️ CodeRepair AI

### AI-Powered Code Vulnerability Detection, Auto-Repair & Validation

🚀 **Live Demo:** [Try CodeRepair AI]((https://coderepairagent-fxrot3oe4l6p7rbwngu7tc.streamlit.app/))

CodeRepair AI is a Python-based code security assistant that analyzes Python source code, detects common security vulnerabilities, generates safer repaired code, validates the repair, and automatically creates a corrected Python file.

The project combines **static code analysis, AI-assisted repair, local fallback repair, and automated validation** into a simple Streamlit dashboard.

---

## 🚀 Features

### 🔍 1. Vulnerability Detection

CodeRepair AI scans Python source code and detects common security problems such as:

* Dangerous `eval()`
* Dangerous `exec()`
* Command injection through `os.system()`
* Shell injection through `subprocess.run(..., shell=True)`
* Hardcoded passwords
* Hardcoded API keys
* Hardcoded tokens and secrets
* Python syntax errors

The scanner uses Python's built-in **AST module** and regular expressions.

---

### 📁 2. Python File Upload

Users can upload an existing Python `.py` file directly through the Streamlit dashboard.

Example:

```text
test_vulnerable.py
```

The application reads the uploaded source code and performs security analysis automatically.

---

### 🤖 3. Automated Code Repair

After vulnerabilities are detected, the Repair Agent attempts to generate corrected code.

The project supports:

* Gemini API-based AI repair
* Local rule-based repair fallback

This means the application can continue working even when the AI API is temporarily unavailable.

---

### 🔄 4. Before & After Code Comparison

The dashboard displays:

```text
❌ Original Code
        ↓
🤖 Repaired Code
```

This allows users to visually compare the vulnerable code with the generated repair.

---

### 🧪 5. Automated Repair Validation

The repaired code is validated using two checks:

#### Syntax Validation

The application checks whether the repaired Python code is syntactically valid using Python's `ast` module.

#### Security Validation

The repaired code is scanned again to check whether the known vulnerabilities detected by the scanner are still present.

```text
Original Code
      ↓
Security Scan
      ↓
Repair
      ↓
Syntax Validation
      ↓
Security Re-scan
      ↓
Final Result
```

---

### 📄 6. Automatic Repaired File Generation

One of the main features of CodeRepair AI is automatic repaired-file creation.

For example:

```text
Uploaded:
test_vulnerable.py

Generated:
repaired_test_vulnerable.py
```

The corrected code is automatically written into the generated Python file.

Users can also download the repaired file directly from the Streamlit dashboard.

---

### 📊 7. Security Dashboard

The dashboard displays vulnerability statistics such as:

* Total Issues
* High Risk Issues
* Medium Risk Issues
* Low Risk Issues

Each detected vulnerability also shows:

* Vulnerability type
* Severity
* Line number
* Explanation of the security risk

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │   Python File       │
                    │      Upload         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Static Scanner   │
                    │   AST + Regex       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Vulnerability       │
                    │ Detection           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Repair Agent     │
                    │ Gemini / Local      │
                    │ Repair Engine       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Repaired Code    │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
          ┌─────────────────┐   ┌──────────────────┐
          │ Syntax          │   │ Security         │
          │ Validation      │   │ Re-scan          │
          └────────┬────────┘   └────────┬─────────┘
                   │                     │
                   └──────────┬──────────┘
                              ▼
                    ┌─────────────────────┐
                    │ Final Validation    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ repaired_file.py    │
                    │ + Download          │
                    └─────────────────────┘
```

---

## 📂 Project Structure

```text
CodeRepairAgent/
│
├── venv/
│
├── scanner.py
├── repair_agent.py
├── tester.py
├── file_repair.py
├── main.py
├── app.py
│
├── test_vulnerable.py
├── repaired_test_vulnerable.py
│
├── .env
├── .gitignore
└── README.md
```

### File Description

| File              | Purpose                                                  |
| ----------------- | -------------------------------------------------------- |
| `scanner.py`      | Detects security vulnerabilities using AST and regex     |
| `repair_agent.py` | Generates repaired code using Gemini or local fallback   |
| `tester.py`       | Performs syntax and security validation                  |
| `file_repair.py`  | Reads and creates repaired Python files                  |
| `main.py`         | Command-line testing of the complete workflow            |
| `app.py`          | Streamlit web dashboard                                  |
| `.env`            | Stores the Gemini API key                                |
| `.gitignore`      | Prevents sensitive/unnecessary files from being uploaded |
| `README.md`       | Project documentation                                    |

---

## 🧠 Technologies Used

### Programming Language

* Python

### Python Libraries

* `ast`
* `re`
* `os`
* `google-genai`
* `python-dotenv`
* `streamlit`

### AI

* Google Gemini API
* AI-assisted code repair

### Security Analysis

* Python Abstract Syntax Tree (AST)
* Regular Expression-based pattern detection
* Static analysis

### Interface

* Streamlit

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/artisoni005/CodeRepairAgent.git
```

```bash
cd CodeRepairAgent
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install google-genai python-dotenv streamlit
```

---

## 🔑 Gemini API Configuration

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Do **not** upload your actual API key to GitHub.

The `.gitignore` file should contain:

```text
venv/
.env
__pycache__/
```

---

## ▶️ Run the Application

Start the Streamlit dashboard using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🖥️ How to Use

## Step 1 — Upload a Python File

Open the CodeRepair AI dashboard and upload a `.py` file.

For example:

```text
test_vulnerable.py
```

---

## Step 2 — Scan the Code

Click:

```text
🔍 Scan & Repair Code
```

The scanner analyzes the uploaded source code.

---

## Step 3 — Review Vulnerabilities

The dashboard displays detected issues.

Example:

```text
🔴 Command Injection Risk
Severity: HIGH
Line: 7

🔴 Dangerous eval()
Severity: HIGH
Line: 9

🟠 Hardcoded Secret
Severity: MEDIUM
Line: 3
```

---

## Step 4 — Generate Repair

The Repair Agent generates a safer version of the source code.

The application uses the Gemini API when available and can fall back to local repair rules when the API is unavailable.

---

## Step 5 — Compare Code

The dashboard displays:

```text
❌ Before

Original vulnerable code
```

and:

```text
✅ After

Generated repaired code
```

---

## Step 6 — Validate the Repair

The repaired code is checked for:

```text
🐍 Syntax Validation
        +
🛡️ Security Validation
```

---

## Step 7 — Generate Repaired File

The application automatically creates:

```text
repaired_test_vulnerable.py
```

The file contains the generated repaired code.

It can also be downloaded from the dashboard.

---

# 🧪 Example Vulnerable Code

The following code can be used to test CodeRepair AI:

```python
import os

password = "admin123"

user_input = input("Enter command: ")

os.system(user_input)

eval(user_input)
```

The scanner should detect multiple security issues.

---

# 🔍 Detection Pipeline

```text
Python Source File
        ↓
AST Parsing
        ↓
Pattern Detection
        ↓
Vulnerability Report
        ↓
Repair Agent
        ↓
Repaired Source Code
        ↓
Syntax Validation
        ↓
Security Re-scan
        ↓
Repaired Python File
```

---

# 🛡️ Security Rules Currently Implemented

| Vulnerability                     | Detection Method | Severity |
| --------------------------------- | ---------------- | -------- |
| `eval()`                          | AST              | HIGH     |
| `exec()`                          | AST              | HIGH     |
| `os.system()`                     | AST              | HIGH     |
| `subprocess.run(..., shell=True)` | AST              | HIGH     |
| Hardcoded Password/Secret         | Regex            | MEDIUM   |
| Syntax Error                      | AST parsing      | HIGH     |

---

# 🎯 Why CodeRepair AI?

Traditional code editors can identify syntax problems, but secure coding requires identifying potentially dangerous programming patterns as well.

CodeRepair AI combines:

```text
Detection
   +
Explanation
   +
Automated Repair
   +
Validation
   +
Repaired File Generation
```

This creates an end-to-end prototype for automated secure-code refinement.

---

# 🚧 Current Limitations

This project is currently a prototype.

### 1. Limited Vulnerability Rules

The scanner currently detects a defined set of Python security patterns rather than every possible vulnerability.

### 2. Static Validation

The validation system currently performs:

* Syntax validation
* Static security re-scanning

It does not provide a full isolated runtime sandbox.

### 3. AI Dependency

Gemini-based repair depends on API availability and model access.

A local fallback repair engine is included for supported vulnerability patterns.

### 4. Python Focus

The current implementation primarily supports Python source code.

---

# 🚀 Future Scope

The project can be extended with:

* 🐳 Docker-based isolated code execution
* 🌳 Tree-sitter parsing
* 🔗 Code Property Graph (CPG)
* 🌐 Multi-language support
* 🧪 Automatic unit-test generation
* 🔐 More vulnerability detection rules
* 📊 Security analytics dashboard
* 🤖 Advanced code-specialized models
* 🧩 Multi-agent architecture
* ☁️ Cloud deployment
* 👤 Per-user API key management
* 🔄 Automatic repair-and-retest loops
* 📈 Vulnerability history and reporting

---

# 🏆 Hackathon Objective

CodeRepair AI is designed as a prototype for an agentic code analysis workflow:

```text
Scan
 ↓
Understand
 ↓
Detect
 ↓
Repair
 ↓
Validate
 ↓
Generate Corrected File
```

The goal is to demonstrate how automated code analysis and AI-assisted repair can be combined into a practical developer security tool.

---

# 👩‍💻 Author

**Arti Soni**

GitHub: `artisoni005`

---

## ⭐ Project Workflow

```text
             CODE FILE
                 │
                 ▼
        ┌─────────────────┐
        │ Security Scanner│
        └────────┬────────┘
                 │
                 ▼
        Vulnerabilities
                 │
                 ▼
        ┌─────────────────┐
        │  Repair Agent   │
        └────────┬────────┘
                 │
                 ▼
          Repaired Code
                 │
        ┌────────┴────────┐
        ▼                 ▼
   Syntax Check      Security Check
        │                 │
        └────────┬────────┘
                 ▼
       Repaired Python File
                 │
                 ▼
             DOWNLOAD
```

**CodeRepair AI — Detect → Explain → Repair → Validate → Generate**
