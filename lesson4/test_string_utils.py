import pytest
from string_utils import StringUtils


@pytest.mark.parametrize('string, result', [
   ("eva", "Eva"), ("Вася", "Вася"),
   ("", ""), ("1", "1")
   ])
def test_capitilize(string, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(string)
    assert res == result


@pytest.mark.parametrize('string, result', [
    (" eva", "eva"), ("   Вася", "Вася"),
    ("", ""), ("   ", "")
    ])
def test_trim(string, result):
    stringUtils = StringUtils()
    res = stringUtils.trim(string)
    assert res == result


@pytest.mark.parametrize('string, result', [
    ("e,v,a", ["e", "v", "a"]), ("", []),
    (" ", []), ("ev,a", ["ev", "a"])
    ])
def test_to_list(string, result):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("eva", "e", True), ("eva", "s", False),
    ("", "", True), ("eva", "", False), (" eva", " ", True)
    ])
def test_contains(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("eva", "e", "va"), ("eva", "s", "eva"),
    ("", "", ""), ("eva", "", "eva")
    ])
def test_delete_symbol(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("eva", "e", True), ("eva", "s", False), ("", "", True),
    ("eva", " ", False), ("eva", "E", False)
    ])
def test_starts_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("eva", "a", True), ("eva", "s", False), ("", "", True),
    ("eva", " ", False), ("eva", "A", False)
    ])
def test_end_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result', [
    ("eva eva", False), ("Вася", False), ("", True),
    ("   ", True), (",", False)
    ])
def test_is_empty(string, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == result


@pytest.mark.parametrize('lst, result', [
    (["e", "v", "a"], "e, v, a"), ([], ""),
    ([  ], ""), (["ev", "a"], "ev, a")
    ])
def test_list_to_string(lst, result):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(lst)
    assert res == result


def test_list_to_string_joiner():
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(["e", "v", "a"], "-")
    assert res == "e-v-a"
