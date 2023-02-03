class Product:
    def __init__(self,brand,model,s_number):
        self.brand = brand
        self.model = model
        self._s_number = s_number #PRIVATE ATRIBUTE
    
    @property
    def nome(self): #GET
        return self._s_number

    @nome.setter
    def nome(self, s_number): #SET
        self._s_number = s_number    

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.s_number}"

class Guitar(Product):  #SUBCLASSES 
    def __init__(self, brand, model,s_number, n_strings, color, fretboard, pickups):
        super().__init__(brand, model, s_number) #O QUE ESTA SENDO PUXADO DA CLASSE MAE
        self.n_strings = n_strings  #ATRIBUTO NOVO QUE ESTA SENDO CRIADO DENTRO DA SUBCLASSE
        self.color = color
        self.fretboard = fretboard
        self.pickups = pickups
    def __str__(self):
        return f'Brand: {self.brand} - Model: {self.model} - Serial Number: {self.s_number} - Color: {self.color} - Fretboard: {self.fretboard} - Pickups: {self.pickups} '   

class Amp(Product):
    def __init__(self,brand,model,s_number,watts):
        super().__init__(brand, model,s_number)
        self.watts = watts
    def __str__(self):
        return f'Brand: {self.brand} - Model: {self.model} - Serial Number: {self.s_number} - Watts: {self.watts}'
        
    
guitar1 = Guitar("Charvel", "San Dimas","0085","6","White","Maple","2" )
amp1 = Amp("Marshall", "JCM 800", "0021", "100W")

products = [guitar1, amp1]

for product in products:
    print(product)