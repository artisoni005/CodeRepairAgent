import os


def read_python_file(file_path):
    """
    Read Python source code from a file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def save_repaired_code(original_file_name, repaired_code):
    """
    Save repaired code into a new Python file.
    """

    base_name = os.path.basename(original_file_name)

    name, extension = os.path.splitext(base_name)

    repaired_file_name = f"repaired_{name}{extension}"

    with open(repaired_file_name, "w", encoding="utf-8") as file:
        file.write(repaired_code)

    return repaired_file_name 