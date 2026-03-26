"""Smoke tests for the application entrypoint."""

import subprocess
import sys
import unittest


class MainEntrypointSmokeTest(unittest.TestCase):
    """Verify the app entrypoint runs and returns the expected output."""

    def test_main_entrypoint_output(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "src.main"],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.stdout.strip(), "Hello from codexAPP")


if __name__ == "__main__":
    unittest.main()
