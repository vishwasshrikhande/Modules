class Employee:
    first = 'Jon'
    last = 'Doe'
    domain = 'hellogames.com'

    def __init__(self,first,last,domain) -> None:
        self.first = first
        self.last = last 
        self.domain = domain 
        self.email = self.buildemail()       


    def name_rules(self):
        # names and their cleanup will have the folloing rules
        # no salutations for building email id
        # no titles
        pass
        
    def domain_rules(self):
        # domains should have a .
        #
        #
        pass

    def buildemail(self):
        # emails can be build using following rules
        # fn + ln + @ + domain
        # 1st char of fn + ln + @ + domain
        # fn + 1st char of ln + @ + domain
        # fn + . + ln + @ + domain
        # fn + _ + ln + @ + domain
        # finally all should be lower cases, no numbers or special characters
        emails = []
        emails.append((self.first[0] +self.last + '@'  +self.domain).lower())
        emails.append((self.first +self.last[0] + '@'  +self.domain).lower())
        emails.append((self.first +'.'+ self.last + '@'  +self.domain).lower())
        emails.append((self.first +'_'+ self.last + '@'  +self.domain).lower())
        emails.append((self.first +self.last + '@'  +self.domain).lower()) 
        return emails
        
    def mydetails(self) -> None:
        print(f'{self.first} {self.last} may have the following email {self.buildemail()}')

        



emp2 = Employee('Jehan','Dole','hellogames')
emp2.mydetails()
