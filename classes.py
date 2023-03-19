class Subscriber:
    
    def __init__(self, index, name, phone):
        self.index = index
        self.name = name
        self.phone = phone

    def update(self, name, phone):
        self.name = name
        self.phone = phone