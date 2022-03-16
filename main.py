from implementations.second_chance import TestSuitSecondChance
from implementations.fifo import TestSuitFifo
from implementations.nru import TestSuitNRU
from implementations.lru import TestSuitLRU
from utils.terminal_colors import bcolors, Terminal


def get_pages():
    file = open("./tests/test.txt", "r")
    pages = []
    for line in file:
        pages = line.split(', ')
    file.close()
    return pages


referenced_pages = get_pages()

Terminal.print(
    bcolors.OKBLUE,
    "-----------------------------FIFO------------------------------"
)
TestSuitFifo.test(referenced_pages)

Terminal.print(
    bcolors.OKCYAN,
    "----------------------------- SECOND CHANCE---------------------"
)
TestSuitSecondChance.test(referenced_pages)

Terminal.print(
    bcolors.OKGREEN,
    "----------------------------- NRU-------------------------------"
)
TestSuitNRU().test(referenced_pages)

Terminal.print(
    bcolors.OKBLUE,
    "----------------------------- LRU-------------------------------"
)
TestSuitLRU.test(referenced_pages)
