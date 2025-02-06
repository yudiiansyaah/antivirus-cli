import unittest
from antivirus.updater import update_virus_definitions

class TestUpdater(unittest.TestCase):
    def test_update_virus_definitions(self):
        result = update_virus_definitions()
        self.assertEqual(result, None) 

if __name__ == "__main__":
    unittest.main()

