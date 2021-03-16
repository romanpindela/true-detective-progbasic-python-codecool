from whatif import *


def test_is_twodigit_odd():
    assert is_twodigit_odd(5) is False
    assert is_twodigit_odd(15) is True
    assert is_twodigit_odd(115) is False


def test_has_access():
    assert has_access(42, [142, 143], 11, True, 10, True, True, False) is True
    assert has_access(42, [142, 143], 11, True, 10, True, False, True) is True
    assert has_access(42, [142, 143], 11, True, 10, True, False, False) is False
    assert has_access(42, [142, 143], 11, True, 143, True, False, False) is True
    assert has_access(42, [142, 143], 11, True, 143, False, False, False) is False
    assert has_access(42, [142, 143], 11, True, 143, False, False, True) is True
    assert has_access(42, [142, 143], 42, True, 10, False, False, False) is True
    assert has_access(42, [142, 143], 42, False, 10, False, False, False) is False
    assert has_access(42, [142, 143], 42, False, 10, False, False, True) is True


def test_is_leap_year():
    assert is_leap_year(1995) is False
    assert is_leap_year(1996) is True
    assert is_leap_year(1997) is False
    assert is_leap_year(1998) is False
    assert is_leap_year(1999) is False
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False


def test_is_sunday():
    assert is_sunday(1, 'M') is False
    assert is_sunday(6, 'M') is False
    assert is_sunday(7, 'M') is True
    assert is_sunday(7, 'W') is False
    assert is_sunday(6, 'W') is False
    assert is_sunday(5, 'W') is True
    assert is_sunday(32, 'F') is False


def test_should_bring_umbrella():
    assert should_bring_umbrella(True, 2, True, False, False, False, False, False) is True
    assert should_bring_umbrella(True, 7, True, False, False, False, False, False) is False
    assert should_bring_umbrella(False, 0, True, False, False, False, False, False) is False
    assert should_bring_umbrella(False, 0, True, False, True, False, False, False) is True
    assert should_bring_umbrella(False, 0, True, False, False, False, True, False) is True
    assert should_bring_umbrella(False, 6, True, True, True, True, True, False) is True
    assert should_bring_umbrella(False, 7, True, True, True, True, True, False) is False
    assert should_bring_umbrella(False, 0, False, False, False, False, False, False) is False
    assert should_bring_umbrella(False, 0, False, False, False, False, False, True) is True
    assert should_bring_umbrella(False, 8, False, False, False, False, False, True) is False


def test_should_take_a_nap():
    assert should_take_a_nap(False, False, False, False, False, False, False) is False
    assert should_take_a_nap(True, True, False, False, False, False, False) is False
    assert should_take_a_nap(True, False, True, False, False, False, False) is False
    assert should_take_a_nap(True, False, False, False, False, False, False) is False
    assert should_take_a_nap(True, False, False, False, False, True, False) is True
    assert should_take_a_nap(True, False, False, False, False, False, True) is True
    assert should_take_a_nap(True, False, False, True, True, False, False) is False
    assert should_take_a_nap(True, False, False, True, False, False, True) is True
    assert should_take_a_nap(True, False, False, True, False, True, True) is True
