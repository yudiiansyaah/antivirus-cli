import setuptools import setup, find_packages

setup (
    name="antivirus_tool",
    version="1.0.0",
    author="Yud'S",
    description="An open-source antivirus tool for scanning and detecting malicious file.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yudiiansyaah/antivirus",
    packages=find_packages(),
    install_requires=[
        "magic",
        "pyfiglet",
        "requests"

        ),
    entry_points={
        "console_scripts":[
            "antivirus=main:main",
            ],
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires='3.6',
)
