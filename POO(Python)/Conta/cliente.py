class Cliente:
    
    def __init__(self, nome) :
        self.__nome = nome
    
    @property #faz com que voce chame um metodo ou função sem precisar botar () pra ser executada 
    def nome(self):
        print("chamando @ property nome()")
        return self.__nome.title()  
    
    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome    