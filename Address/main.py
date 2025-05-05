#Assignment 8

class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city
    def DisplayAddress(self):
        print("street is:", self.street, "city is:", self.city)
    def GetStreet(self):
        return self.street
    def GetCity(self):
        return self.city
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def DisplayPerson(self):
        print("Name is:", self.name, "email is:", self.email, end = " ")
    def GetName(self):
        return self.name
    def GetEmail(self):
        return self.email
 
class Contact(Address, Person):
    def DisplayContact(self):
        self.DisplayPerson
        self.DisplayAddress
 
class Notebook():
    person = {}
    def __init__(self):
        person = {}
    
    def AddPerson(self, name, email, street, city):
        self.person[name] = [email, city, street]
 
    def DisplayInfo(self, quest):
        if quest in self.person:
            print(quest, self.person.get(quest))
        else:
            print("Unknown")
 
Note = Notebook()
Note.AddPerson("Krisalda", "krisaldamihali02@gmail.com", "Street_A", "Tirana")
Note.DisplayInfo("Krisalda")
Note.DisplayInfo("Kris")