# creating class for building a computer
class Computer:

    # What attributes will it need?
        description: str
        processor_type: str
        hard_drive_capacity: int
        memory: int
        operating_system: str
        year_made: int
        price: int
    # How will you set up your constructor?
        
    # Remember: in python, all constructors have the same name (__init__)
        def __init__(self, d:str, pt:str, hd:int, mem:int, ops:str, yr:int, p:int):
            self.description = d
            self.processor_type = pt
            self.hard_drive_capacity = hd
            self.memory = mem
            self.operating_system = ops
            self.year_made = yr
            self.price = p
         
    # What methods will you need?
        def computer(self):
         return(self.description, self.processor_type, self.hard_drive_capacity, self.memory, self.operating_system, self.year_made, self.price)
    
# def main():
#      firstComputer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
#      firstComputer.computer()

# main()


