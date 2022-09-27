import cmath
class Punto_plano:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f'({self.x};{self.y})'

    def cuadrante(self):
        c=0
        if self.x == 0  and self.y == 0:
            c=0
        
        elif self.x >=0 and self.y >=0:
            c=1

        elif self.y>=0 and self.x <= 0:
            c=2
        
        elif self.y <=0 and self.x <= 0:
            c=3

        else:
            c=4

    def distancia_origen(self):
        return cmath.sqrt(self.x**2 + self.y**2)

    def distancia_punto (self,pto):
        return cmath.sqrt( (self.x - pto.x )**2 + (self.y - pto.y)**2)


#programa principal

#punto 1
x1=float(input('Ingrese x1: '))
y1=float(input('Ingrese y1: '))

pto1=Punto_plano(x1,y1)

print(pto1)
print(f'Distancia al origen: {pto1.distancia_origen()}')



#punto 2
x2=float(input('Ingrese x2: '))
y2=float(input('Ingrese y2: '))

pto2=Punto_plano(x2,y2)


print(pto2)
print(f'Distancia al origen desde el punto {pto2} es: {pto2.distancia_origen()}')



print(f'Distancia del {pto1} al {pto2} es: {pto2.distancia_punto(pto1)}')




