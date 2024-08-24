class RailwayForm :
    formType = "RailwayForm"
    def printData(self) :
        print(f"name is {self.name}")
        print(f"train is {self.train}")

rajuApplication = RailwayForm()
rajuApplication.name = "raju"
rajuApplication.train = "rajdhani Express"
rajuApplication.printData()