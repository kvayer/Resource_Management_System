class Warehouse:
    # склад, где находятся продукты. изменение продуктов
    def __init__(self):
        self.products = {}

    def add_product(self, product_name: str, quantity: int):
        if product_name in self.products:
            self.products[product_name] += quantity
        else:
            self.products[product_name] = quantity

    def can_use_product(self, product_name: str, quantity: int):
        if product_name in self.products:
            if self.products[product_name] - quantity >= 0:
                return True # можно удалить
            else:
                return False # нельзя удалить
        return None # такого продукта вообще нет на складе

    def remove_product(self, product_name: str, quantity: int):
        if product_name in self.products:
            if self.products[product_name] >= quantity:
                self.products[product_name] -= quantity
                if self.products[product_name] == 0:
                    del self.products[product_name]
            else:
                return False # на складе нет достаточного количества продукта product_name
        else:
            return None # продукт product_name отсутствует на складе
        return True # удаление продукта product_name прошло успешно

    def get_product_quantity(self, product_name: str):
        if product_name in self.products:
            return self.products[product_name]
        else:
            return 0

    # def list_products(self):
    #     for product_name, quantity in self.products.items():
    #         print(f"{product_name}: {quantity}")

    def print_stock_info(self):
        print("Состояние склада:")
        if self.products:
            for product_name, quantity in self.products.items():
                print(f"{product_name}: {quantity}")
        else:
            print("Склад пуст.")
