import sys
import pytest

from pathlib import Path

src_path = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(src_path))

from mutable_default_arg import add_to_list_mutable_default, add_to_list_fixed


@pytest.mark.xfail(reason="Since the list is already initialized, the return won't be just an item.")
def test_add_to_list_mutable_default():
    result = add_to_list_mutable_default("pineapple")
    assert result == ["pineapple"]


def test_add_to_list_fixed():
    # Initialize the list and returns only the item tested.
    result = add_to_list_fixed("pineapple")
    assert result == ["pineapple"]
