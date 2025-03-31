import os

# Define package name
package_name = "prarthana_package"

# Define the directory structure
structure = [
    f"{package_name}/",  # Main project folder
    f"{package_name}/prarthana/",  # Package folder
    f"{package_name}/prarthana/__init__.py",
    f"{package_name}/prarthana/math_utils.py",
    f"{package_name}/prarthana/string_utils.py",
    f"{package_name}/setup.py",
    f"{package_name}/README.md",
    f"{package_name}/LICENSE",
    f"{package_name}/.gitignore",
]

# Create directories and files
for path in structure:
    if path.endswith("/"):
        os.makedirs(path, exist_ok=True)
    else:
        with open(path, "w") as f:
            if "math_utils.py" in path:
                f.write("def add(a, b):\n    return a + b\n")
            elif "string_utils.py" in path:
                f.write("def greet(name):\n    return f'Hello, {name}!'\n")
            elif "__init__.py" in path:
                f.write("from .math_utils import add\nfrom .string_utils import greet\n")
            elif "setup.py" in path:
                f.write("""from setuptools import setup, find_packages

setup(
    name="prarthana_package",
    version="0.1",
    author="Prarthana",
    author_email="your_email@example.com",
    description="A simple package with math and string utilities",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GKPrarthana/prarthana_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
""")
            elif "README.md" in path:
                f.write("# Prarthana Package\n\nA simple Python package with math and string utilities.")
            elif ".gitignore" in path:
                f.write("__pycache__/\n*.pyc\n*.pyo\n*.pyd\n*.egg-info/\ndist/\nbuild/\n")

print("✅ Package structure created successfully!")
