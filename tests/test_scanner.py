import unittest
from unittest.mock import patch, mock_open
from antivirus.scanner import scan_file, full_device_scan

class TestScanner(unittest.TestCase):
    @patch("builtins.open", mock_open(read_data="test file data"))
    @patch("antivirus.scanner.get_file_hashes", return_value="c871988a3c6853e7e345914f142f07b6186991d1f9bb3f00e6b7ad94f20a4ad3")
    @patch("antivirus.scanner.load_virus_signature", return_value=["c871988a3c6853e7e345914f142f07b6186991d1f9bb3f00e6b7ad94f20a4ad3"])
    def test_scan_file_virus_found(self, mock_signature, mock_hash, mock_open):
        result = scan_file("test_file.txt")
        self.assertIn("Virus detected", result)

    @patch("builtins.open", mock_open(read_data="clean file data"))
    @patch("antivirus.scanner.get_file_hashes", return_value="clean_hash")
    @patch("antivirus.scanner.load_virus_signature", return_value=["c871988a3c6853e7e345914f142f07b6186991d1f9bb3f00e6b7ad94f20a4ad3"])
    def test_scan_file_clean(self, mock_signature, mock_hash, mock_open):
        result = scan_file("test_file.txt")
        self.assertIn("is clean", result)

    @patch("antivirus.scanner.scan_directory")
    def test_full_device_scan(self, mock_scan_directory):
        result = full_device_scan()
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()

