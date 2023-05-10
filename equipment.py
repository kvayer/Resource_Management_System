class Equipment:
    def __init__(self, name: str, status: str):
        self.name = name
        self.status = status

    def get_equip_name(self):
        return self.name

    def get_equip_status(self):
        return self.status

    def new_status(self, new_status: str):
        self.status = new_status