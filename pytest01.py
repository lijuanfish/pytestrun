import pytest

class Test01:
    def setup_class(self):
        print("setup开始")

    def teardown_class(self):
        print("teardown结束")
/'' \
 ''
    def test_login1(self):
        print("正在登陆1")

    def test_login2(self):
        print("正在登陆2")

if __name__ == '__main__':
    pytest.main(["-s","pytest01.py"])
