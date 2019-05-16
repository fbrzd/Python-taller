import ia as ia1
import ia2 as ia2
from random import randrange

def fstr(src,att='n',font='default',back='default',end=True): # formato para strings
	F = {'n':'0','b':'1','s':'2','i':'3','u':'4','r':'7','h':'8','c':'9'}
	C = {'black':30,'red':31,'green':32,'yellow':33,'blue':34,'magenta':35,
		 'cyan':36,'white':37,'default':39}
	try:
	    pre = "\033[" + ';'.join(map(lambda f: F[f], att))
	    pre += ';' + str(C[font]) + ';' + str(C[back]+10) + 'm'
	except:
	    pre = ''
	return pre + str(src) + '\033[0m'*end

def check(tab):
    # check horizontal
    for i in (0,1,2):
        if "x" == tab[i*3] == tab[i*3+1] == tab[i*3+2]: return 1
        if "o" == tab[i*3] == tab[i*3+1] == tab[i*3+2]: return 2
    # check vertical
    for i in (0,1,2):
        if "x" == tab[i] == tab[i+3] == tab[i+6]: return 1
        if "o" == tab[i] == tab[i+3] == tab[i+6]: return 2
    # check diagonal
    if "x" == tab[4] == tab[0] == tab[8]: return 1
    if "x" == tab[4] == tab[2] == tab[6]: return 1
    if "o" == tab[4] == tab[0] == tab[8]: return 2
    if "o" == tab[4] == tab[2] == tab[6]: return 2

def get_output(TMP, tab):
    fstr(TMP, back="white")
    ftab = tuple(' ' if x == 0 else fstr(x, 'b', 'red' if x=='x' else 'blue') for x in tab)
    return TMP % ftab

# LOAD
with open("tmp-ttt") as f:
    TMP = ''.join(f.readlines())

tab = [0,0,0,0,0,0,0,0,0]

# CHOICE FIRST
if randrange(2):
    ia1.mi_signo = "x"
    ia2.mi_signo = "o"
    whos = (ia1, ia2)

else:
    ia2.mi_signo = "x"
    ia1.mi_signo = "o"
    whos = (ia2,ia1)

print(fstr(whos[0].name, 'bu'), fstr(whos[0].mi_signo, 'b', 'red'),
    fstr("VS"),
    fstr(whos[1].name, 'bu'), fstr(whos[1].mi_signo, 'b', 'blue'))

# PLAY
turn = 0
while not check(tab):
    # IA PIENSA Y JUEGA
    index = whos[turn%2].play(tab)
    
    # ACTUALIZAR TABLERO
    if tab[index] == 0: tab[index] = whos[turn%2].mi_signo
    else:
        tab[index] = whos[turn%2].mi_signo
        print(get_output(TMP, tab))
        print(fstr("movimiento ilegal de la ia: "+whos[turn%2].name+"!", 'b', 'red'))
        exit()
    
    # MOSTRAR
    print(get_output(TMP, tab))
    input("...")
    print("\033[7A")

    turn += 1

input("\033[5Bwin "+whos[turn%2-1].name+"!")