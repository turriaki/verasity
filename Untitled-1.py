
class Tamagochi:
    def __init__(self,nom,ham,ani,ener):

        self.nombre=nom
        self.hambre=ham
        self.animo=ani
        self.energia=ener

    def jugar(self):
        self.animo+=1
        self.energia-=1

    def alimentar(self):
        self.animo+=1
        self.hambre-=1

    def dormir(self):
        self.hambre+=1
        self.energia+=1

    def pasar(self):
        self.animo-=1
        self.hambre+=1
        self.energia-=1

    def __str__(self):
        return(f'nombre:{self.nombre}  Hambre: {self.hambre} Animo: {self.animo} Energia: {self.energia}')

t=Tamagochi('Tamagochito',10,10,10)
t.dormir()
t.jugar()
t.alimentar()
t.pasar()
print(t)


