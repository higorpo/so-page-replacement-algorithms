import random


class TestSuitNRU:
    def __init__(self):
        self.__tabela: dict = {}
        self.__classes = {
            'classe0': [], 'classe1': [],
            'classe2': [], 'classe3': []
        }
        self.__max_size = 64
        self.__page_faults = 0

    def __reset_data(self):
        self.__tabela: dict = {}
        self.__page_faults = 0
        self.__reset_classes()

    def __reset_classes(self):
        self.__classes = {
            'classe0': [], 'classe1': [],
            'classe2': [], 'classe3': []
        }

    def __add_to_tabela(self, referenced_page):
        self.__tabela[referenced_page] = {
            'referenced': True,
            'modified': random.choice([False, True]),
        }

    def __find_classes(self):
        for allocated_page in self.__tabela.keys():
            referenced = self.__tabela[allocated_page].get(
                'referenced'
            )
            modified = self.__tabela[allocated_page].get(
                'modified'
            )

            classe0 = self.__classes['classe0']
            classe1 = self.__classes['classe1']
            classe2 = self.__classes['classe2']
            classe3 = self.__classes['classe3']

            # Adiciona classe dependendo do contexto
            if (not referenced and not modified):
                classe0.append(allocated_page)
            elif (not referenced and modified):
                classe1.append(allocated_page)
            elif (referenced and not modified):
                classe2.append(allocated_page)
            elif (referenced and modified):
                classe3.append(allocated_page)

    def __random_delete_lowest_class(self):
        self.__find_classes()

        classe0 = self.__classes['classe0']
        classe1 = self.__classes['classe1']
        classe2 = self.__classes['classe2']
        classe3 = self.__classes['classe3']

        index_to_delete = None

        if(len(classe0) > 0):
            index_to_delete = random.choice(classe0)
        elif(len(classe1) != 0):
            index_to_delete = random.choice(classe1)
        elif(len(classe2) != 0):
            index_to_delete = random.choice(classe2)
        elif(len(classe3) != 0):
            index_to_delete = random.choice(classe3)

        self.__tabela.pop(index_to_delete)

    def __not_in_table(self, referenced_page):
        if (len(self.__tabela) == 0 or len(self.__tabela) < self.__max_size):
            self.__add_to_tabela(referenced_page)
            self.__page_faults += 1
        elif(len(self.__tabela) == self.__max_size):
            self.__random_delete_lowest_class()

            self.__add_to_tabela(referenced_page)

            self.__reset_classes()

            self.__page_faults += 1

    def test(self, referenced_pages):
        need_reset_referenced_pages = 0
        self.__page_faults = 0

        self.__reset_data()

        for referenced_page in referenced_pages:
            if referenced_page not in self.__tabela:
                self.__not_in_table(referenced_page)
            else:
                self.__tabela[referenced_page]['referenced'] = True

            # Reseta páginas referenciadas para o bom funcionamento do algoritmo.
            need_reset_referenced_pages += 1
            if(need_reset_referenced_pages == 3):
                for page in self.__tabela:
                    self.__tabela[page].update(referenced=0)
                need_reset_referenced_pages = 0

        keys_str = str(self.__tabela.keys())
        formatted_str = keys_str.replace('dict_keys(', '').replace(')', '')

        # print(f'--> Páginas na memória: {formatted_str}')
        print(f'--> Quantidade de PageFaults: {self.__page_faults}')
