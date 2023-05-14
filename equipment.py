class Equipment:
    # оборудование - при помощи этого изготавливаются различные продукты
    def __init__(self, name: str, status: str = None, can_work: bool = None, content: float = None):
        self.name = name
        self.status = status
        self.can_work = can_work
        self.content = content

    def get_equip_name(self):
        return self.name

    def get_equip_status(self):
        return self.status

    def new_status(self, new_status: str):
        self.status = new_status

    def get_content(self):
        return self.content

    def set_content(self, new_content: float):
        self.content = new_content

    def get_info(self):
        return f'Состояние оборудования \"{self.name}\" - {self.content}%. Статус: {self.status}'
