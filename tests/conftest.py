
# tests/conftest.py
import sys
from pathlib import Path

# Get the path to the project root directory (one level up from 'tests')
project_root = Path(__file__).resolve().parent.parent

# Add the project root to sys.path
sys.path.insert(0, str(project_root))