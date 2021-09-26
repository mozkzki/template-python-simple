import pytest
from app_name.cls_sample.person import Person


class TestPerson:
    def setup(self):
        print("<<setup done>> ", end="")

    def tear_down(self):
        print(" <<tear_down done>>", end="")

    @pytest.fixture()
    def person1(request):
        return Person("Taro", 35)

    def test_past(self):
        p = Person("Taro", 35)
        p.past(5)
        assert p.age == 40

    def test_show(self, person1: Person):
        person1.show()

    def test_past_and_show(self, person1: Person):
        person1.past(10)
        person1.show()
        assert person1.age == 45

    # setは出来ない
    def test_invalid_access(self, person1: Person):
        with pytest.raises(AttributeError):
            person1.name = "Hoge"
