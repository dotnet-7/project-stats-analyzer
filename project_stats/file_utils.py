import os

def load_ignore_patterns(ignore_file):
    """
    Load ignore patterns from the ignore.txt file.
    """
    ignore_patterns = []
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r', encoding='utf-8') as f:
            for line in f:
                rule = line.strip()
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
