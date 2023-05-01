class Inventory:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity

    def add_item(self, qty):
        self.quantity += qty

    def remove_item(self, qty):
        self.quantity -= qty

    def get_quantity(self):
        return self.quantity

class Equipment:
    def __init__(self, equip_name, status):
        self.equip_name = equip_name
        self.status = status

    def set_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status

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
inv1 = Inventory("Стул", 50)
inv2 = Inventory("Стол", 20)
equip1 = Equipment("Компьютер", "в работе")
equip2 = Equipment("Принтер", "в ремонте")
report = Reporting([inv1, inv2], [equip1, equip2])
report.print_inventory()
report.print_equipment()
planner = PurchasePlanning([inv1, inv2])
demand_forecast = planner.forecast_demand("Стол", 6)
print(f"Прогноз спроса на столы на следующие 6 месяцев: {demand_forecast}")
