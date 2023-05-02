class Inventory:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity

    def add_item(self, qty):
        self.quantity += qty

    def remove_item(self, qty):
        if self.quantity - qty < 0:
            self.quantity = 0
        self.quantity -= qty

    def get_quantity(self):
        return self.quantity

class Equipment:
    def __init__(self, equip_name, status, last_time_used):
        self.equip_name = equip_name
        self.status = status
        self.last_time_used = last_time_used

    def set_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status

    def ifusing(self):
        if int(self.last_time_used) < 4:
            return True
        return False

class Reporting:
    def __init__(self, inventory_list, equipment_list):
        self.inventory_list = inventory_list
        self.equipment_list = equipment_list

    def print_inventory(self):
        for item in self.inventory_list:
            print(f"{item.item_name}: {item.get_quantity()}")

    def print_equipment(self):
        for equip in self.equipment_list:
            print(f"{equip.equip_name}: {equip.get_status()}")

class PurchasePlanning:
    def __init__(self, inventory_list):
        self.inventory_list = inventory_list

    def forecast_demand(self, item_name, num_months):
        total_quantity = 0
        for item in self.inventory_list:
            if item.item_name == item_name:
                total_quantity += item.get_quantity()
        avg_monthly_demand = total_quantity / num_months
        return avg_monthly_demand


# Пример использования классов
inv1 = Inventory("Carrot", 49)
inv2 = Inventory("Cabbage", 15)
inv3 = Inventory('Potato', 101)
inv4 = Inventory('Tomato ', 46)
inv5 = Inventory('Pepper', 34)
inv6 = Inventory('Onion ', 60)
inv7 = Inventory('Garlic', 81)
inv8 = Inventory('Cucumber', 13)
equip1 = Equipment("Кофемашина", "в работе", "0")
equip2 = Equipment("Принтер", "в ремонте", "5")
report = Reporting([inv1, inv2, inv3, inv4, inv5, inv6, inv7, inv8], [equip1, equip2])
report.print_inventory()
report.print_equipment()
planner = PurchasePlanning([inv1, inv2, inv3, inv4, inv5, inv6, inv7, inv8])
demand_forecast = planner.forecast_demand("Стол", 6)
print(f"Прогноз спроса на столы на следующие 6 месяцев: {demand_forecast}")
for equip in report.equipment_list:
    if equip.ifusing():
        print('Оборудование \"' + str(equip.equip_name) + "\"", 'не использовалось более 4х дней, поэтому было продано.')
        del equip