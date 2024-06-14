### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:
    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollars = int(input("how many ($1) dollars?: "))
        half = int(input("how many half dollars?: ")) * 0.50
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        return dollars + half + quarters + nickels

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"${change} is your change.")
            return True
        else:
            print("Sorry, you don't have enough money. Money refunded")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item] # deduct the resources by what is used to make the sandwich
        print(f"Here is your {sandwich_size} sandwich. Bon appetit!")

    def report(self):
        for item, amount in self.machine_resources.items():
            print(f"{item}: {amount} slice(s)")


### Make an instance of SandwichMachine class and write the rest of the codes ###
def main():
    machine = SandwichMachine(resources)
    while True:
        choice = input("What would you like? (small / medium / large / off / report): ")
        if choice == "off":
            print("Turning off machine")
            break
        elif choice == "report":
            machine.report()
        elif choice in recipes:
            if machine.check_resources(recipes[choice]["ingredients"]):  # check we have resources to make the sandwich
                print(f"The cost of a {choice} sandwich is ${recipes[choice]["cost"]}") # say how sandwich costs
                payment = machine.process_coins()  # call the process_coins method that stores the user's payment
                if machine.transaction_result(payment, recipes[choice]["cost"]):  # check if the user has enough money
                    machine.make_sandwich(choice, recipes[choice]["ingredients"])  # if they do, we make the sandwich
            else:
                print(f"We don't have enough ingredients to make a {choice} sandwich")
        else:
            return


if __name__ == "__main__":
    main()
