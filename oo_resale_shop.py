from computer import Computer
from typing import Dict, Optional

class ResaleShop:

 # What attributes will it need?
    inventory : Dict[int, Dict] = {}
    itemID = 0
    item_id: int
    new_price: int
    new_os: Optional[str] = None


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, id:int, np:int, no:Optional[str]=None, inv:Dict[int, Dict] = {}, iid = 0):
        self.inventory = inv
        self.id = id
        self.new_price = np
        self.new_os = no
        self.itemID = iid
        
    # What methods will you need?

    def buy(self: Dict):
        global itemID
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = Computer
        print("Buying Item ID:", self.itemID)
        print("Adding to inventory...")
        print("Done.\n")
        return self.itemID
        
    
    def update_price(self):
     if self.id in self.inventory:
        self.inventory[self.id]["price"] = self.new_price
     else:
        print("Item", self.id, "not found. Cannot update price.")

    def sell(self):
     if self.id in self.inventory:
        del self.inventory[self.id]
        print("Item", self.id, "sold!")
     else: 
         print("Item", self.id, "not found. Please select another item to sell.")

    def print_inventory(self):
    # If the inventory is not empty
     if self.inventory:
        # For each item
        for self.id in self.inventory:
            # Print its details
            print("Confirming inventory...")
            print("INVENTORY: \n Item ID:", self.id, self.inventory)
     else:
        print("No inventory to display.")

    def refurbish(self):
        if self.id in self.inventory:
            computer = self.inventory[self.id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if self.new_os is not None:
                computer["operating_system"] = self.new_os # update details after installing new OS
        else:
            print("Item", self.id, "not found. Please select another item to refurbish.")
        
    def banner(self):
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)
                  
def main():
    firstComputer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    firstComputer.computer()
    banner = ResaleShop(1, 1500)
    banner.banner()
    buying = ResaleShop(1, 1500)
    buying.buy()
    check_inventory = ResaleShop(1, 1500)
    check_inventory.print_inventory()
    updateprice = ResaleShop(1, 1500)
    updateprice.update_price()
    refurb = ResaleShop(1, 1500)
    refurb.refurbish()
    inventory = ResaleShop(1, 1500)
    inventory.print_inventory()


    
    
main()