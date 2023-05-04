class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__count = 0
        self.__weight = 0
        self.__items = []

    def __str__(self):
        if self.__count == 1:
            item_term = "item"
        else:
            item_term = "items"
        return f"{self.__count} {item_term} ({self.__weight} kg)"

    def add_item(self, item: Item):
        if (item.weight() + self.__weight) < self.__max_weight:
            self.__items.append(item)
            self.__count += 1
            self.__weight += item.weight()

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return self.__weight

    def heaviest_item(self):
        heaviest = self.__items[0]

        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest


class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []
        self.__current_weight = 0

    def __str__(self):
        if len(self.__suitcases) == 1:
            item_term = "suitcase"
        else:
            item_term = "suitcases"
        suitcases = len(self.__suitcases)
        remaining_space = self.__max_weight - self.__current_weight
        return f"{suitcases} {item_term}, space for {remaining_space} kg"

    def add_suitcase(self, suitcase: Suitcase):
        if self.__max_weight > (self.__current_weight + suitcase.weight()):
            self.__suitcases.append(suitcase)
            self.__current_weight += suitcase.weight()

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()


if __name__ == "__main__":
    # items to add
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)
    # adding items to first suitcase
    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)
    # adding items to second suitcase
    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)
    # adding both suitcases to one cargo hold
    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)
    # printing all items stored in the cargo hold
    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
