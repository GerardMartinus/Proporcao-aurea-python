import turtle

janela = turtle.Screen()
from turtle import *

antes = 0
comeco = 1
fibonacci = 1

quadrados = input("Quantos quadrados você quer?")

begin_fill()
for i in range(int(quadrados)):
    print(str(i) + ". " + str(fibonacci))

    color('black', 'white')
    for f in range(6):
        forward(2 * fibonacci)
        if f < 5: right(90)

    fibonacci = comeco + antes
    antes = comeco
    comeco = fibonacci


end_fill()
done()