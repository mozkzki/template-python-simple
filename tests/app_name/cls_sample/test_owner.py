import pytest
from app_name.cls_sample.owner import Owner


class TestOwner:
    def setup(self):
        print("<<setup done>> ", end="")

    def tear_down(self):
        print(" <<tear_down done>>", end="")

    @pytest.fixture()
    def owner1(request):
        return Owner("Taro", 35, "Kanagawa")

    def test_past(self):
        o = Owner("Jiro", 20, "Tokyo")
        o.past(16)
        assert o.name == "Jiro"
        assert o.age == 36
        assert o.address == "Tokyo"

    def test_move(self, owner1: Owner):
        owner1.move("Nagoya")
        owner1.address == "Nagoya"

    def test_past_and_show(self, owner1: Owner):
        owner1.past(10)
        owner1.show()
        assert owner1.age == 45

    def test_direct_change(self, owner1: Owner):
        # 本当は変更手段を2つ用意すべきではない
        owner1.address = "Tokyo"
        assert owner1.address == "Tokyo"
