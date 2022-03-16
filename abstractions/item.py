class Item:
    def __init__(self, page: int):
        self.__page = page
        self.__anterior: Item = None
        self.__proximo: Item = None

    @property
    def page(self) -> int:
        return self.__page

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, next):
        self.__anterior = next

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, next):
        self.__proximo = next
