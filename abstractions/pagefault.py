class PageFault(Exception):
    def __init__(self):
        super().__init__('PageFault')
