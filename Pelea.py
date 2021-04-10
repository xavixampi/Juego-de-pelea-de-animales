#importamos la libreria random
from random import choice

#Inicio
print('Bienvenido a AnimalFight')
Tu_nombre = input('Introduce tu nombre:')

#Selección de personaje
print('\nPulsa 1 para jugar con Panda.\nPulsa 2 para jugar con Serpiente. \nPulsa 3 para jugar con León.\nPulsa 4 para jugar con Águila.')
Tu_personaje = int(input('\nIntroduce el número:'))
#Características del personaje
if Tu_personaje == (1):
    Nombre_personaje = ('Panda')
    Tu_salud = 100
    Tu_ataque = 20
    Rivales =['Serpiente', 'León' , 'Águila']

if Tu_personaje == (2):
    Nombre_personaje = ('Serpiente')
    Tu_salud = 75
    Tu_ataque = 50
    Rivales = ['Panda', 'León', 'Águila']

if Tu_personaje == (3):
     Nombre_personaje = ('León')
     Tu_salud = 80
     Tu_ataque = 35
     Rivales = ['Panda' ,'Serpiente', 'Águila']

if Tu_personaje == (4):
     Nombre_personaje = ('Águila')
     Tu_salud = 75
     Tu_ataque = 40
     Rivales = ['Panda' , 'Serpiente' , 'León']
#Selección del primer rival
if Tu_personaje == (1):
    primer_rival = choice(Rivales)
    print(Tu_nombre , 'jugará con' , Nombre_personaje)
    print(Nombre_personaje, 'luchará contra' , primer_rival)
    
if Tu_personaje == (2):
    primer_rival = choice(Rivales)
    print(Tu_nombre , 'jugará con' , Nombre_personaje)
    print(Nombre_personaje , 'luchará contra' , primer_rival)
    
if Tu_personaje == (3):
    primer_rival = choice(Rivales)
    print(Tu_nombre , 'jugará con' , Nombre_personaje)
    print(Nombre_personaje , 'luchará contra' , primer_rival)
    
if Tu_personaje == (4):
    primer_rival = choice(Rivales)
    print(Tu_nombre , 'jugará con' , Nombre_personaje,'\n')
    print(Nombre_personaje , 'luchará contra' , primer_rival,'\n')
    
#Características del rival
if primer_rival == ('Panda'):
    Nombre_rival = ('Panda')
    salud_rival = 100
    Ataque_rival = 20

if primer_rival == ('Serpiente'):
    Nombre_rival = ('Serpiente')
    salud_rival = 70
    Ataque_rival = 50

if primer_rival == ('León'):
    Nombre_rival = ('León')
    salud_rival = 80
    Ataque_rival = 35

if primer_rival == ('Águila'):
    Nombre_rival = ('Águila')
    salud_rival = 75
    Ataque_rival = 40

#Estado de la partida
if Tu_salud>0 and salud_rival>0:
    estado_partida = ('Activa')

#Pociones
Pocion = 20
#Turnos de ataque
while estado_partida == ('Activa'):
    Tu_turno = input ('Pulsa A para atacar, Pulsa B para curar|')
    if Tu_turno == ('A'):
        salud_rival= salud_rival - Tu_ataque
        print(Nombre_personaje , ' Ha atacado, ahora' , Nombre_rival , 'tiene' ,salud_rival, 'puntos de salud')
    if Tu_turno == ('B'):
        Tu_salud = Tu_salud + Pocion
        print(Tu_nombre , 'ha curado a' , Nombre_personaje , 'con una pocion, ahora tiene' , Tu_salud , 'puntos de salud')
    
    opciones_rival=['A', 'B']
    Turno_rival = choice(opciones_rival)
    if Turno_rival == ('A'):
        Tu_salud= Tu_salud - Ataque_rival
        print(Nombre_rival , 'ha atacado, ahora' , Nombre_personaje, 'tiene', Tu_salud, 'puntos de salud')
    if Turno_rival ==('B'):
        salud_rival = salud_rival + 20
        print(Nombre_rival, 'se ha curado, ahora tiene' ,salud_rival, 'puntos de salud')
    #Victoria o derrota
    if Tu_salud == 0 or Tu_salud<0:
        estado_partida = 4
    if salud_rival == 0 or salud_rival<0:
        estado_partida = 5

#Fin de la partida
if estado_partida==4:
    print('\n',Nombre_personaje, 'ha muerto', Nombre_rival , 'ha ganado el combate')
if estado_partida == 5:
    print('\n',Nombre_personaje, 'ha matado a ', Nombre_rival , 'así que ha ganado el combate')



