import pytest
from main.my.module1 import Module1


class TestModule1:
    @pytest.fixture()
    def module1(request):
        return Module1()

    def test_method(self, module1: Module1, capfd):
        module1.method()
        out, err = capfd.readouterr()
        assert out == "module1's method called.\nmodule2's method called.\n"
        assert err == ""
