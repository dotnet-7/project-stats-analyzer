# Project Stats Analyzer

## Overview

**Project Stats Analyzer** is a Python tool designed to analyze the contents of a project directory. It scans all text files within the directory, excluding specified files and directories, and provides a detailed count of characters, symbols, and even Chinese pinyin within the project.

This tool is particularly useful for developers, linguists, or anyone who wants to gain insights into the textual composition of their project files.

## Features
Character Frequency Analysis: Counts the frequency of letters, symbols, and Chinese pinyin in text files.
Customizable Ignore Rules: Allows users to define files and directories to exclude using an ignore.txt file.
Error Handling: Skips non-text files (e.g., .pyc files) and provides meaningful error messages for inaccessible files.
Directory Traversal: Recursively scans all files in the specified project directory.
## How It Works
The tool reads an ignore.txt file to determine which files and directories should be excluded from analysis.
It traverses the specified project directory, analyzing all text files while ignoring binary files (e.g., .pyc files) and user-defined patterns.
It counts characters, symbols, and Chinese pinyin from the text files and provides a summary of the results.
## Installation
Clone this repository:

```bash
git clone https://github.com/your-username/project-stats-analyzer.git
cd project-stats-analyzer
```
Create a virtual environment (optional but recommended):

```bash 
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage
1. Prepare an ignore.txt file:

Create an ignore.txt file in the project root directory.
Add patterns or filenames to exclude. For example:
```
__pycache__
*.pyc
*.log
node_modules/
```

2. Run the script:

* Modify the main.py file to set the desired project directory and ignore.txt path:
    
```python
project_directory = "/path/to/your/project"
ignore_file = "/path/to/ignore.txt"
```

* Run the script:

```bash
python main.py
```

3. View the results:

* The script will output the frequency of characters, symbols, and Chinese pinyin to the console.
## Configuration
### Ignore Rules
The tool uses an ignore.txt file to define which files and directories should be excluded. The following patterns can be used:

* __pycache__: Exclude a specific folder.
* *.pyc: Exclude files with a specific extension.
* node_modules/: Exclude a specific folder and its contents.
* *.log: Exclude log files.
### Default Ignore Rules
Even without an ignore.txt file, the tool will automatically ignore:

* __pycache__ directories.
* .pyc files.
## Example Output

After running the script, you might see an output like this:
```
Character Frequency Analysis:
a: 1234
b: 567
c: 890
...
Symbol Frequency:
,: 78
.: 45
...
```
## Error Handling
* Non-Text Files: Skips binary files (e.g., .pyc) and logs a warning: ``` Skipping non-text file: ./__pycache__/config.cpython-312.pyc```.
* Missing Files: If the specified project directory or ignore.txt file is missing, the tool will notify the user.
## Contributing
Contributions are welcome! If you'd like to improve the tool or add new features, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.