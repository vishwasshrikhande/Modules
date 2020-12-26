class Employee:
    first = 'Jon'
    last = 'Doe'
    domain = 'hellogames.com'
        
    def __init__(self,*args) -> None:
        if len(args) == 0: pass
        if len(args) == 1: self.first = args[0]
        if len(args) == 2: self.first,self.last = args[0],args[1] 
        if len(args) == 3: self.first,self.last,self.domain = args[0],args[1],args[2]
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
        
    def empdetails(self) -> None:
        print(f'{self.first} {self.last} may have the following email {self.buildemail()}')



class Company:
    
    def __init__(name:str,low_emp_range:int,high_emp_range:int,industry,low_rev_rng:int,high_rev_rng:int) -> None:
        super().__init__()
        

