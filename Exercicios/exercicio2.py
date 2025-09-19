def corrida(corredor1distancia,corredor1tempo,corredor2distancia,corredor2tempo):
    corredor1velocidade = corredor1distancia/corredor1tempo
    corredor2velocidade = corredor2distancia/corredor2tempo
    if corredor1velocidade > corredor2velocidade:
     print("o corredor 1 é o mais rapido")
    else:
       print("o corredor 2 é o mais rapido")



corrida(2,3,5,7)
corrida(3,1,5,7)
