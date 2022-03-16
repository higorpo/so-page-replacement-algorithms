from config.config import TOTAL_QUADROS_MAX
from .pagefault import PageFault
from .item import Item


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__head: Item = None
        self.__tail: Item = None
        self.__atual: Item = None

    def __repr__(self):
        return str(self.__head)

    def __ir_para_primeiro(self):
        self.__atual = self.__head
        return self.__atual

    def __ir_para_ultimo(self):
        if self.__head is None:
            return None

        self.__atual = self.__tail
        return self.__atual

    def acessar_atual(self):
        return self.__atual

    def inserir_na_frente(self, item: int, checkPageFault=True):
        if self.size < self.max_size:
            if self.buscar(item, True):
                self.get_item(item)
                self.excluir_atual()
                self.inserir_na_frente(item, False)
                return
            else:
                new_item = Item(item)
                first = self.__ir_para_primeiro()

                if first is not None:
                    first.anterior = new_item
                    new_item.proximo = first
                    first = new_item
                else:
                    first = new_item
                    self.__tail = first

                self.__head = new_item
                self.__atual = new_item
                if checkPageFault:
                    raise PageFault
        else:
            if self.buscar(item, True):
                self.get_item(item)
                self.excluir_atual()
                self.inserir_na_frente(item, False)
                return
            else:
                self.excluir_ult()
                self.inserir_na_frente(item, False)
                if checkPageFault:
                    raise PageFault

    def get_items(self):
        items = []
        pointer = self.__head

        while pointer != None:
            items.append(pointer.page)
            pointer = pointer.proximo

        return items

    def get_item(self, item) -> Item:
        self.__ir_para_primeiro()
        while self.__atual is not None:
            if self.__atual.page == item:
                return self.__atual
            else:
                self.__atual = self.__atual.proximo

    def excluir_atual(self):
        if self.__head.proximo is None:
            self.excluir_prim()
        elif self.__atual.proximo is None:
            self.excluir_ult()
        elif self.__atual == self.__head:
            self.excluir_prim()
        else:
            self.__atual.anterior.proximo = self.__atual.proximo
            self.__atual.proximo.anterior = self.__atual.anterior
            self.__atual = self.__atual.anterior

    def excluir_prim(self):
        if self.__head is None:
            raise Exception('Você não tem elementos')
        else:
            self.__head = self.__head.proximo
            self.__head.__anterior = None
            self.__atual = self.__head

    def excluir_ult(self):
        self.__ir_para_ultimo()
        if self.__ir_para_ultimo() is not None:
            self.__atual = self.__atual.anterior
            self.__atual.proximo = None
            self.__tail = self.__atual
        else:
            raise Exception('Você não tem elementos')

    def buscar(self, key, resetPosition=False):
        old_atual = self.__atual

        if self.__atual is None:
            return False

        self.__ir_para_primeiro()
        while self.__atual.page != key and self.__atual.proximo != None:
            self.__atual = self.__atual.proximo

        if self.__atual.page == key:
            if resetPosition == True:
                self.__atual = old_atual
            return True
        else:
            if resetPosition == True:
                self.__atual = old_atual
            return False

    def print_all(self):
        pointer = self.__head

        while pointer != None:
            print(pointer.page)
            pointer = pointer.proximo

    @property
    def size(self):
        size = 0
        pointer = self.__head
        while pointer != None:
            pointer = pointer.proximo
            size += 1
        return size

    @property
    def max_size(self):
        return TOTAL_QUADROS_MAX
