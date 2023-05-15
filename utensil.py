class Utensil:
    # посуда и пренадлежность - то, чем едят и то, на чем едят (коробки пиццы, стаканы для кофе, салфетки, тарелки, перчатки)
    def __init__(self, utensil_name: str, amount: int):
        self.utensil_name = utensil_name
        self.amount = amount

    def get_utensil_name(self):
        return self.utensil_name

    def get_utensil_amount(self):
        return self.amount

    def add_item(self, amount: int):
        self.amount += amount

    def remove_item(self, amount: int):
        if self.abillity_to_remove(amount):
            self.amount -= amount
            return True # удаление прошло успешно
        return False # удаление не удалось

    def set_item(self, amount: int):
        self.amount = amount

    def abillity_to_remove(self, amount: int):
        if self.amount - amount < 0:
            return False
        else:
            return True
