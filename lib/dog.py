class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.vets = []
        self.checkups = []

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if type(value) is int and 0 <= value:
            self._age = value
        else:
            raise ValueError("Not valid age")

    def add_checkup(self, vet, date, notes):
        if vet not in self.vets:
            self.vets.append(vet)
        new_checkup = {
            "vet": vet,
            "date": date,
            "notes": notes
        }
        self.checkups.append(new_checkup)

    def find_checkup(self,date):
        for checkup in self.checkups:
            if checkup["date"] == date:
              print(f"Checkup on {date} by {checkup['vet']}: {checkup['notes']}")
              return 
        print(f"No checkup found on {date}.")



fido = Dog(
    name = "Fido",
    age = 3,
    breed = "Golden Retriever"
)


fido.add_checkup("Doolittle", "02/12/24", "Good health!")
fido.add_checkup("Dr Ryan", "03/20/25", "Still good health")
fido.find_checkup("02/12/24")
fido.find_checkup("04/29/26")