from config.config import TOTAL_QUADROS_MAX


class Fila:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def get_items(self):
        return self.items

    @property
    def size(self) -> int:
        return len(self.items)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def is_full(self) -> bool:
        return self.size == TOTAL_QUADROS_MAX
