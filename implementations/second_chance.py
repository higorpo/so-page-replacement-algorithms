from abstractions.queuewithrbit import QueueWithRBit


class TestSuitSecondChance:
    def test(referenced_pages):
        queue = QueueWithRBit()
        page_faults = 0

        for referenced_page in referenced_pages:
            if referenced_page not in queue.get_items():
                if (queue.is_empty or not queue.is_full):
                    queue.enqueue(referenced_page)
                    page_faults += 1
                else:
                    queue.give_second_chance(referenced_page)
                    page_faults += 1
            else:
                queue.set_is_referenced(referenced_page)

        # print(f'--> Páginas na memória: {queue.get_items()}')
        print(f'--> Quantidade de PageFaults: {page_faults}')
