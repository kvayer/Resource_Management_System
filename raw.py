class Raw:
    def __init__(self, raw_name: str, amount: int):
        self.raw_name = raw_name
        self.amount = amount

    def get_raw_name(self):
        return self.raw_name

    def get_raw_amount(self):
        return self.amount

    def add_item(self, amount: int):
        self.amount += amount

    def remove_item(self, amount: int):
        self.amount -= amount

    def abillity_to_remove(self, amount: int):
        if self.amount - amount < 0:
            return False
        else:
            return True

