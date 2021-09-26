from app_name.cls_sample.owner import Owner


class Dog:
    """
    犬の各属性値やヘルパー関数を保持する

    Attributes
    ----------
    name : str
        この犬の名前
    owner : Owner
        この犬のオーナー
    """

    def __init__(self, name: str, owner: Owner) -> None:
        self._name = name
        self._owner = owner

    def show(self) -> None:
        """この犬の情報を表示する"""
        print("Bow wow.. I'm {}. My owner is {}.".format(self._name, self._owner.name))

    @property
    def name(self) -> str:
        """名前を返す

        Returns
        -------
        str
            名前
        """
        return self._name
