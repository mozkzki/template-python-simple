class Person:
    """人の各属性値やヘルパー関数を保持する"""

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def past(self, year: int) -> None:
        """指定の経過年数分、歳をとる

        Parameters
        ----------
        year : int
            経過年数
        """
        self._age += year

    def show(self) -> None:
        """この人の情報を標準出力に表示する"""
        print("私は{}。{}歳です。".format(self._name, self._age), end="")

    @property
    def name(self) -> str:
        """名前を返す

        Returns
        -------
        str
            名前
        """
        return self._name

    @property
    def age(self) -> int:
        """年齢を返す

        Returns
        -------
        int
            年齢
        """
        return self._age
