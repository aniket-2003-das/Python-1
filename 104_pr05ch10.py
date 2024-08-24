class Train:
    def __init__(self, name, fair, seats):
        self.name = name
        self.fair = fair
        self.seats = seats
    
    def getStatus(self):
        print(f"the name of train is {self.name}.")
        print(f"the fair of train is {self.fair}.")
        print(f"the seats of train is {self.seats}.")

    def fairInfo(self):
        print(f"the price of train ticket is RS- {self.fair}.")
    
    def bookTicket(self):
        if(self.seats)>0:
            print(f"your ticket has been booked and \n your seat no is - {self.seats}")
            self.seats = self.seats - 1
        else:
            print("no seats. kindly book in tatkal.")

    def cancelTicket(self,):
        pass

intercity = Train("intercity", 90, 300)
intercity.getStatus()
intercity.fairInfo()

# booking tickets.
intercity.bookTicket()
intercity.getStatus()
