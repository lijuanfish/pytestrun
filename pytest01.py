import pytest

class Test01:
    def setup_class(self):
        print("setup")

    def teardown_class(self):
        print("teardown")

    def test_login1(self):
        print("123")

    def test_login2(self):
        print("234")

