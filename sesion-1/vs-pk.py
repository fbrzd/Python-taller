# valores iniciales
pi_ataque = 15
pi_vida = 15

ch_ataque = 10
ch_vida = 20

turno = 0

# bucle para el combate
while pi_vida > 0 and ch_vida > 0:

    print("turno",turno,"pikachu", pi_vida,"charmander", ch_vida)
    input()
    
    if turno == 0: # ataca charmander
        print("ataca charmander")
        pi_vida = pi_vida - ch_ataque # 15 - 10 = 5
    
    if turno == 1: # ataca pikachu
        print("ataca pikachu")
        ch_vida = ch_vida - pi_ataque # 20 - 15 = 5

    turno = 1 - turno

# se define al ganador
if ch_vida > 0:
	print("gana charmander!")

if pi_vida > 0:
	print("gana pikachu!")