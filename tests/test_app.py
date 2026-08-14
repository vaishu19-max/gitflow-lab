# flake8: noqa: E402
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import add


def test_add():
    assert add(2, 3) == 5
