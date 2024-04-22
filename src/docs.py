class User:
    def __init__(self, name, password, number):
        self.name=name
        self.password=password
        self.number=number


    def toDBCollection(self):
        return{
            'name': self.name,
            'password':self.password,
            'number':self.number
        }
