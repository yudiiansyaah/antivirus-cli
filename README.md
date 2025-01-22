# Antivirus Tool

An open-source antivirus tool to scan files and detect malicious content.

## Features
- File scanning and type detection
- Virus definition updates
- Open-source and easy to use

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YudS/antivirus_tool.git
   cd antivirus
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```bash
   python main.py
   ```

## License
### MIT License


---

### **4. Publish on GitHub**
1. Create a GitHub repository for your project.
2. Push the project files:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YudS/antivirus_tool.git
   git push -u origin main

5. Distibute via PyPI
- Install tools:
   ``` bash
   pip install twine wheel
   ```
- Build your packages:
   ``` bash
   python setup.py sdist bdist_wheel
   ```
- Upload to PyPI:
   ``` bash
   twine upload dist/*
   '''
# antivirus_tool
# antivirus-project
# antivirus-cli
