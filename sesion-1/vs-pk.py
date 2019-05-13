pi_ataque = 15
pi_vida = 15

ch_ataque = 10
ch_vida = 20

turno = 0

# bucle para el combate
while pi_vida > 0 and ch_vida > 0:

    input()
    input()

    if turno == 0: # ataca charmander
    	pi_vida = pi_vida - ch_atque # 15 - 10 = 5
    
    if turno == 1: # atacar pikachu
    	ch_vida = ch_vida - pi_ataque # 20 - 15 = 5

    turno = 1 - turno

# se define al ganador
if ch_vida > 0:
	print("gana charmander!")

if pi_vida > 0:
	print("gana pikachu!")