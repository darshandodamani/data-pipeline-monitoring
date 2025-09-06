import unittest
import sys
import os


class TestBasic(unittest.TestCase):

    def test_python_version(self):
        """Test that we're running Python 3.6+"""
        self.assertGreaterEqual(sys.version_info.major, 3)
        self.assertGreaterEqual(sys.version_info.minor, 6)

    def test_project_structure(self):
        """Test that required directories exist"""
        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))

        # Check for key directories/files
        expected_items = ['etl', 'dags', 'docker', 'requirements.txt']

        for item in expected_items:
            item_path = os.path.join(project_root, item)
            self.assertTrue(
                os.path.exists(item_path),
                f"{item} should exist in project root"
            )


if __name__ == '__main__':
    unittest.main()
