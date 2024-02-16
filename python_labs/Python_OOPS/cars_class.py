####CREATE AN OBJECT
class Tools:
    car_list=[]
    name = "Jenkins"
    version = 20
    date = "20/11"
    cartyres=4
    car_name=["Honda","Toyota","Maruti","Audi","Tata"]

    def cartyres1(self):
        if self.cartyres==4:
            self.car_list.append(self.car_name)
            print("Four Wheeler List is : ", self.car_list)
        else:
            print("Only TWO Wheelers are there!! No Four Wheels")

Honda = Tools()
Honda.cartyres1()
