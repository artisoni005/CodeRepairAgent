import streamlit as st

from scanner import scan_code
from repair_agent import RepairAgent
from tester import validate_code, validate_security
from file_repair import read_python_file, save_repaired_code


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="CodeRepair AI",
    page_icon="🛡️",
    layout="wide"
)


# ---------------- HEADER ----------------

st.title("🛡️ CodeRepair AI")

st.markdown(
    """
    **AI-Powered Code Vulnerability Detection, Auto-Repair & Validation**

    Upload your Python file → Detect vulnerabilities → Repair the code →
    Validate the repair → Generate a corrected Python file
    """
)

st.divider()



# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.header("⚙️ CodeRepair AI")

    st.write(
        "An intelligent code security assistant "
        "for detecting and repairing common Python vulnerabilities."
    )

    st.divider()

    st.subheader("🔍 Detection")

    st.write("• Dangerous eval()")
    st.write("• Dangerous exec()")
    st.write("• Command Injection")
    st.write("• Shell Injection")
    st.write("• Hardcoded Secrets")

    st.divider()

    st.subheader("🤖 Pipeline")

    st.write("1. Static Analysis")
    st.write("2. Vulnerability Detection")
    st.write("3. AI / Local Repair")
    st.write("4. Syntax Validation")
    st.write("5. Security Validation")
    st.write("6. Repaired File Generation")


# ---------------- FILE UPLOAD ----------------

st.subheader("📁 Upload Python File")

uploaded_file = st.file_uploader(
    "Upload the Python file you want to scan and repair:",
    type=["py"]
)


# ---------------- READ UPLOADED FILE ----------------

code = ""

if uploaded_file is not None:

    try:

        code = uploaded_file.read().decode("utf-8")

        st.success(
            f"✅ File uploaded successfully: {uploaded_file.name}"
        )

    except UnicodeDecodeError:

        st.error(
            "❌ Unable to read this file. "
            "Please upload a UTF-8 encoded Python file."
        )

        st.stop()


# ---------------- SOURCE CODE PREVIEW ----------------

if uploaded_file is not None:

    st.subheader("📄 Original Source Code")

    st.code(
        code,
        language="python"
    )

else:

    st.info(
        "👆 Upload a .py file to start the security analysis."
    )


# ---------------- SCAN BUTTON ----------------

scan_button = st.button(
    "🔍 Scan & Repair Code",
    type="primary",
    use_container_width=True
)


# ==================================================
# MAIN PROCESS
# ==================================================

if scan_button:

    if uploaded_file is None:

        st.warning(
            "⚠️ Please upload a Python file first."
        )

        st.stop()


    if not code.strip():

        st.warning(
            "⚠️ The uploaded Python file is empty."
        )

        st.stop()


    # ==================================================
    # SECURITY SCAN
    # ==================================================

    st.divider()

    st.subheader("🔎 Security Analysis")

    with st.spinner(
        "Scanning source code for security vulnerabilities..."
    ):

        vulnerabilities = scan_code(code)


    # ---------------- DASHBOARD METRICS ----------------

    total = len(vulnerabilities)

    high = 0
    medium = 0
    low = 0

    for vulnerability in vulnerabilities:

        severity = vulnerability["severity"]

        if severity == "HIGH":
            high += 1

        elif severity == "MEDIUM":
            medium += 1

        elif severity == "LOW":
            low += 1


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Total Issues",
            total
        )


    with col2:

        st.metric(
            "🔴 High Risk",
            high
        )


    with col3:

        st.metric(
            "🟠 Medium Risk",
            medium
        )


    with col4:

        st.metric(
            "🟢 Low Risk",
            low
        )


    st.divider()


    # ==================================================
    # VULNERABILITY DETAILS
    # ==================================================

    if not vulnerabilities:

        st.success(
            "✅ No known security vulnerabilities detected."
        )

        st.info(
            "No repair is required because the scanner "
            "did not detect any known vulnerabilities."
        )

        st.stop()


    st.subheader("🚨 Detected Vulnerabilities")


    for number, vulnerability in enumerate(
        vulnerabilities,
        start=1
    ):

        severity = vulnerability["severity"]


        if severity == "HIGH":

            icon = "🔴"

        elif severity == "MEDIUM":

            icon = "🟠"

        else:

            icon = "🟢"


        with st.expander(
            f"{icon} {number}. {vulnerability['type']}"
        ):

            st.write(
                f"**Severity:** {severity}"
            )

            st.write(
                f"**Line:** {vulnerability['line']}"
            )

            st.write(
                "**Why is this dangerous?**"
            )

            st.info(
                vulnerability["message"]
            )


    # ==================================================
    # AI REPAIR
    # ==================================================

    st.divider()

    st.subheader("🤖 Automated Code Repair")


    with st.spinner(
        "Analyzing vulnerabilities and generating a repair..."
    ):

        agent = RepairAgent()

        repaired_code = agent.repair_code(
            code,
            vulnerabilities
        )


    # ==================================================
    # SAVE REPAIRED FILE
    # ==================================================

    repaired_file_name = save_repaired_code(
        uploaded_file.name,
        repaired_code
    )


    st.success(
        f"✅ Repaired file automatically created: "
        f"`{repaired_file_name}`"
    )


    # ==================================================
    # BEFORE / AFTER
    # ==================================================

    st.divider()

    st.subheader("🔄 Code Comparison")


    col1, col2 = st.columns(2)


    with col1:

        st.markdown("###  Before")

        st.code(
            code,
            language="python"
        )


    with col2:

        st.markdown("### ✅ After")

        st.code(
            repaired_code,
            language="python"
        )


    # ==================================================
    # DOWNLOAD REPAIRED FILE
    # ==================================================

    st.divider()

    st.subheader("📥 Repaired File")


    st.download_button(
        label="⬇️ Download Repaired File",
        data=repaired_code,
        file_name=repaired_file_name,
        mime="text/x-python",
        use_container_width=True
    )


    # ==================================================
    # VALIDATION
    # ==================================================

    st.divider()

    st.subheader("🧪 Repair Validation")


    with st.spinner(
        "Validating repaired code..."
    ):

        syntax_result = validate_code(
            repaired_code
        )

        security_result = validate_security(
            repaired_code,
            scan_code
        )


    col1, col2 = st.columns(2)


    # ---------------- SYNTAX VALIDATION ----------------

    with col1:

        st.markdown("### 🐍 Syntax Check")


        if syntax_result["status"] == "PASS":

            st.success(
                "✅ Syntax Validation Passed"
            )

            st.write(
                syntax_result["message"]
            )

        else:

            st.error(
                "❌ Syntax Validation Failed"
            )

            st.write(
                syntax_result["message"]
            )


    # ---------------- SECURITY VALIDATION ----------------

    with col2:

        st.markdown("### 🛡️ Security Check")


        if security_result["status"] == "PASS":

            st.success(
                "✅ Security Validation Passed"
            )

            st.write(
                security_result["message"]
            )

        else:

            st.warning(
                "⚠️ Security Issues Still Remain"
            )

            st.write(
                security_result["message"]
            )


            if "vulnerabilities" in security_result:

                st.write(
                    "**Remaining vulnerabilities:**"
                )

                for vulnerability in security_result[
                    "vulnerabilities"
                ]:

                    st.write(
                        f"• {vulnerability['type']} "
                        f"(Line {vulnerability['line']})"
                    )


    # ==================================================
    # FINAL RESULT
    # ==================================================

    st.divider()

    st.subheader("🏆 Final Result")


    if (
        syntax_result["status"] == "PASS"
        and security_result["status"] == "PASS"
    ):

        st.success(
            "🎉 REPAIR VERIFIED — The repaired code is "
            "syntactically valid and no known vulnerabilities remain."
        )


    elif syntax_result["status"] == "PASS":

        st.warning(
            "⚠️ The repaired code is syntactically valid, "
            "but some security issues still remain."
        )


    else:

        st.error(
            "❌ Repair validation failed. "
            "Please review the repaired code."
        )


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "CodeRepair AI • Static Analysis + AI-Assisted Repair + "
    "Automated Validation + Repaired File Generation"
)

