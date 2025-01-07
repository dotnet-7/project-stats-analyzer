import os
from collections import Counter
import string
from pypinyin import lazy_pinyin  # Import the pinyin conversion library


def load_ignore_patterns(ignore_file):
    """
    Load ignore patterns from the ignore.txt file.
    Each line in the file defines a pattern to ignore:
        - *.ext: Ignore files with the specified extension
        - folder_name: Ignore specific folders
        - specific_file: Ignore specific files
        - subpath/: Ignore paths containing the specified substring
    """
    ignore_patterns = []
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r', encoding='utf-8') as f:
            for line in f:
                rule = line.strip()
                # Skip empty lines and comments
                if rule and not rule.startswith('#'):
                    ignore_patterns.append(rule)
    return ignore_patterns


def should_ignore(file_path, ignore_patterns):
    """
    Check if a file or folder should be ignored based on the ignore patterns.
    """
    for pattern in ignore_patterns:
        if pattern.startswith('*.'):  # Ignore files with specific extensions
            if file_path.endswith(pattern[1:]):
                return True
        elif os.path.basename(file_path) == pattern:  # Ignore specific files or folders
            return True
        elif pattern in file_path:  # Ignore paths containing the pattern
            return True
    return False


def convert_to_pinyin_and_symbols(content):
    """
    Convert Chinese characters in the content to pinyin.
    Non-Chinese characters, including symbols, are kept unchanged.
    """
    result = []
    for char in content:
        if '\u4e00' <= char <= '\u9fff':  # Check if the character is Chinese
            # Convert Chinese character to pinyin
            result.extend(lazy_pinyin(char))
        elif char in string.ascii_letters:  # Keep alphabetic characters
            result.append(char.lower())
        elif char in string.punctuation or not char.isspace():  # Include symbols
            result.append(char)
    return result


def count_characters_in_project(directory, ignore_file):
    """
    Count the frequency of letters, Chinese pinyin, and symbols in all text files
    within the project directory, excluding files and folders specified in the ignore.txt file.
    """
    char_counter = Counter()
    ignore_patterns = load_ignore_patterns(ignore_file)

    for root, dirs, files in os.walk(directory):
        # Exclude ignored directories
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]

        for file in files:
            file_path = os.path.join(root, file)
            # Exclude ignored files
            if should_ignore(file_path, ignore_patterns):
                continue
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Convert Chinese characters to pinyin and include symbols
                    chars = convert_to_pinyin_and_symbols(content)
                    char_counter.update(chars)
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")
    return char_counter


# Specify the project directory and the path to the ignore.txt file
project_directory = "./"
ignore_file = "./ignore.txt"

# Count the frequency of characters
char_counts = count_characters_in_project(project_directory, ignore_file)

# Print the results
for char, count in sorted(char_counts.items()):
    print(f"{char}: {count}")
