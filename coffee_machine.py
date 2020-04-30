class Machine:
    def __init__(self):
        self.water_amount = 400
        self.milk_amount = 540
        self.coffee_amount = 120
        self.cup_quantity = 9
        self.money_amount = 550

    def show_status(self):
        print("The coffee machine has:")
        print(f"{self.water_amount} of water")
        print(f"{self.milk_amount} of milk")
        print(f"{self.coffee_amount} of coffee beans")
        print(f"{self.cup_quantity} of disposable cups")
        print(f"{self.money_amount} of money")

    def choose_action(self):
        print("Write action (buy, fill, take, remaining, exit):")
        choose = input()
        if choose == "buy":
            self.buy_coffee()
        elif choose == "fill":
            self.fill_machine()
        elif choose == "take":
            self.take_money()
        elif choose == "remaining":
            self.show_status()
        else:
            exit()

    def buy_coffee(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choose = input()
        if choose == "1":
            if self.is_resource(250, 0, 16):
                self.make_coffee(250, 0, 16, 4)

        elif choose == "2":
            if self.is_resource(350, 75, 20):
                self.make_coffee(350, 75, 20, 7)

        elif choose == "3":
            if self.is_resource(200, 100, 12):
                self.make_coffee(200, 100, 12, 6)
        else:
            self.choose_action()

    def fill_machine(self):
        print("Write how many ml of water do you want to add:")
        self.water_amount += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk_amount += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_amount += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cup_quantity += int(input())

    def take_money(self):
        print(f"I gave you ${self.money_amount}")
        self.money_amount = 0

    def is_resource(self, water, milk, coffee,):
        if self.water_amount < water:
            print("Sorry, not enough water!")
            return False
        if self.milk_amount < milk:
            print("Sorry, not enough milk!")
            return False
        if self.coffee_amount < coffee:
            print("Sorry, not enough coffee!")
            return False
        if self.cup_quantity < 1:
            print("Sorry, not enough cups!")
            return False
        return True

    def make_coffee(self, water, milk, coffee, money):
        self.water_amount -= water
        self.milk_amount -= milk
        self.coffee_amount -= coffee
        self.cup_quantity -= 1
        self.money_amount += money
        print("I have enough resources, making you a coffee!")


coffee_machine = Machine()

while True:
    coffee_machine.choose_action()
