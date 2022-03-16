from abstractions.lista_duplamente_encadeada import ListaDuplamenteEncadeada
from abstractions.pagefault import PageFault


class TestSuitLRU:
    def test(referenced_pages):
        page_faults = 0
        lista = ListaDuplamenteEncadeada()

        # print('Iniciando teste de PageFaults com LRU')

        for referenced_page in referenced_pages:
            try:
                lista.inserir_na_frente(referenced_page)
            except PageFault:
                page_faults += 1

        # print(f'--> Páginas na memória: {lista.get_items()}')
        print(f'--> Quantidade de PageFaults: {page_faults}')
