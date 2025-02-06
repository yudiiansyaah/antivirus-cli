import unittest
from antivirus.utils import get_file_hashes, identify_file_type

class TestUtils(unittest.TestCase):
    def test_get_file_hashes(self):
        mock_file = "test file content"
        file_hash = get_file_hashes(mock_file)
        self.assertIsNotNone(file_hash)

    def test_identify_file_type(self):
        file_type = identify_file_type("test_file.txt")
        self.assertEqual(file_type, "Text File")

if __name__ == "__main__":
    unittest.main()

