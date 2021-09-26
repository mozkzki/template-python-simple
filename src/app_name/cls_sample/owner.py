from app_name.cls_sample.person import Person


class Owner(Person):
    """オーナーの各属性値やヘルパー関数を保持する

    Parameters
    ----------
    Person : [type]
        親クラス
    """

    def __init__(self, name: str, age: int, address: str) -> None:
        super().__init__(name, age)
        self._address = address

    def move(self, new_address: str) -> None:
        """オーナーの住所を更新する。

        Parameters
        ----------
        new_address : str
            新しい住所
        """
        self.__inner_move(new_address)

    def __inner_move(self, new_address: str) -> None:
        self._address = new_address

    def show(self) -> None:
        """オーナーの情報を表示する

        Notes
        ----------
            オーバライドしている
        """
        print("私は所有者の{}。{}歳です。".format(self.name, self.age), end="")

    @property
    def address(self) -> str:
        """オーナーの住所を返す

        Returns
        -------
        str
            オーナーの住所
        """
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """オーナーの住所を設定する

        Parameters
        ----------
        address : str
            オーナーの住所
        """
        self._address = address
