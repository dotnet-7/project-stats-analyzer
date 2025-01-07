import unittest
from project_stats.file_utils import load_ignore_patterns, should_ignore

class TestFileUtils(unittest.TestCase):
    def test_load_ignore_patterns(self):
        patterns = load_ignore_patterns("tests/test_ignore.txt")
        self.assertIn("*.pyc", patterns)
        self.assertIn("node_modules", patterns)

    def test_should_ignore(self):
        patterns = ["*.pyc", "node_modules", "test/"]
        self.assertTrue(should_ignore("example.pyc", patterns))
        self.assertTrue(should_ignore("node_modules/file.js", patterns))
        self.assertFalse(should_ignore("example.py", patterns))

if __name__ == "__main__":
    unittest.main()
