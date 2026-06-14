import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from matcher import compare


def test_matcher_returns_dict():
    result = compare(
        "AWS Linux Terraform"
    )

    assert isinstance(result, dict)
