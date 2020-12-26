class Employee:
    def __init__(self,first,last,domain) -> None:
        self.first = first
        self.last = last 
        self.domain = domain 
        self.email = self.buildemail()       

    def buildemail(self): 
        return (self.first +self.last + '@'  +self.domain).lower()
        
    def mydetails(self) -> None:
        print(f'{emp2.first} {emp2.last} has the email {emp2.email}')


emp2 = Employee('V','S','hellogames')
emp2.mydetails()
