from unittest import TextTestResult
from abstractions.fila import Fila


class TestSuitFifo:

    def test(referenced_pages):
        page_faults = 0
        fila = Fila()

        # print('Iniciando teste de PageFaults com FIFO')

        for referenced_page in referenced_pages:
            if referenced_page not in fila.get_items():
                if (not fila.is_full or fila.is_empty):
                    fila.enqueue(referenced_page)
                else:
                    fila.dequeue()
                    fila.enqueue(referenced_page)
                page_faults += 1

        # print(f'--> Páginas na memória: {fila.get_items()}')
        print(f'--> Quantidade de PageFaults: {page_faults}')
