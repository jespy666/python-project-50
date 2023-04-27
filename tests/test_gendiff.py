import pytest
from gendiff.gendiff import generate_diff
import json


def test_generate_diff():
    result = generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')
    with open('./tests/fixtures/flat_expected.txt', 'r') as f:
        expected = f.read()
    assert result == expected
    assert not result == ''
