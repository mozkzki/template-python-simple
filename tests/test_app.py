import time

import pytest
from app import login


class TestMain:
    def test_login(self):
        result = login("foo", "xxxxx")
        assert result == "call module1 done."

    @pytest.mark.slow
    def test_login_slow(self):
        result = login("bar", "xxxxx")
        time.sleep(2)
        assert result == "call module1 done."
