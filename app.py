import sys
import os

# Ensure the root directory is in the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.web_ui import launch_app

if __name__ == "__main__":
    launch_app()
