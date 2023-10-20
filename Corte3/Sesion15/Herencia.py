
class Deportista():
    def __init__(self,nombre:str,edad:int,documento:str):
        self.__nombre=nombre
        self.__edad=edad
        self.__documento=documento

    #----------Setters------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setEdad(self,edad:int):
        self.__edad=edad

    def setDocumento(self,documento:str):
        self.__documento=documento

    #----------Getters------------
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad

    def getDocumento(self):
        return self.__documento

class Futbolista(Deportista):
    def __init__(self, nombre:str,edad:int,documento:str,nombre_equipo:str,goles:int):
        super().__init__(nombre, edad, documento)
        self.nombre_equipo=nombre_equipo
        self.goles=goles
    
    #----------Setters-----------
    def setNombreEquipo(self,nombre_equipo:str):
        self.nombre_equipo=nombre_equipo

    def setGoles(self,goles:int):
        self.goles=goles
    
    #----------Getters-----------
    def getNombreEquipo(self):
        return self.nombre_equipo

    def getGoles(self):
        return self.goles
    
    #-----------Métodos-----------
    def patear(self):
        return f'el jugador {self.getNombre} acaba de anotar un gol'



def main():
    pass


if __name__=="__main__":
    main()