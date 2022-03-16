class QueueWithRBit:

    def __init__(self):
        self.__items = []
        self.__referenced_list = []

    def enqueue(self, item):
        self.__items.insert(0, item)
        self.__referenced_list.insert(0, True)

    def dequeue(self):
        self.__referenced_list.pop()
        self.__items.pop()

    def get_items(self):
        return self.__items

    def give_second_chance(self, referenced_page):
        while(True):
            if self.__is_first_referenced():
                self.__send_to_end()
            else:
                self.dequeue()
                self.enqueue(referenced_page)
                return False

    def set_is_referenced(self, item):
        index = self.__items.index(item)
        self.__referenced_list[index] = True

    def __get_first_item(self):
        return self.__items[self.size-1]

    def __is_first_referenced(self):
        return self.__referenced_list[self.size-1]

    def __send_to_end(self):
        item = self.__get_first_item()

        self.dequeue()
        self.__items.insert(0, item)
        self.__referenced_list.insert(0, False)

    @property
    def size(self) -> int:
        return len(self.__items)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def max_size(self) -> int:
        return 64

    @property
    def is_full(self) -> bool:
        return self.size == self.max_size
