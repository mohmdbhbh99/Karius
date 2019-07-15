class Employees:
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
    def welcome(self):
        print("hello Employees")






#----------------------------------------Encapsulation------------------------------------------------
    def set_name(self,name):
        self.name = name
    def set_sal(self,salary):
        self.salary = salary
    def get_name(self):
        print(self.name)
    def get_sal(self):
        print(self.salary)
    def show_data(self):
        print(self.name,self.salary)
#-----------------------------------------------------------------------------------------------------



e1 = Employees('Memo_1',1000)
e2 = Employees('Memo_2',2000)
e3 = Employees('Memo_3',3000)



e1.get_name()
e2.show_data()
e3.set_name('dodo_3') # change the value of e3
