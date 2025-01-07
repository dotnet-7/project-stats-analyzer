import os
from collections import Counter
import string
from pypinyin import lazy_pinyin
from project_stats.file_utils import load_ignore_patterns, should_ignore


def convert_to_pinyin_and_symbols(content):
    """
    Convert Chinese characters in the content to pinyin.
    Non-Chinese characters, including symbols, are kept unchanged.
    """
    result = []
    for char in content:
        if '\u4e00' <= char <= '\u9fff':  # Check if the character is Chinese
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
                    chars = convert_to_pinyin_and_symbols(content)
                    char_counter.update(chars)
            except UnicodeDecodeError:
                print(f"Skipping non-text file: {file_path}")
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")
    return char_counter
