import minifb
import random

# ACCION ALEATORIA
def use(date=0, user=None, act="rnd"):
    for p in range(PERTIME):
        if act == "rnd":
            random.choice(DENSITY)(date, exp_user=user)
        if act == "sign": rnd_sign()
        if act == "post": rnd_post(date, exp_user=user)
        if act == "mess": rnd_mess(date, exp_user=user)
        if act == "like": rnd_like()

# REGISTRA ALGUIEN ALEATORIO
def rnd_sign(date=0, exp_user=None):
    name = random.choice(("usuario", "anonymus", "fulanoide")) + str(len(minifb.USERS))
    minifb.SignUp(name,"pasw")

# ALGUIEN ALEATORIO POSTEA
def rnd_post(date=0, exp_user=None):
    while 1:
        user = random.choice(minifb.USERS)
        if user != exp_user: break
    random.shuffle(WORDS)
    
    user.post(' '.join(WORDS[:5]), date)

# MENSAJE ENTRE USUARIOS ALEATORIOS
def rnd_mess(date=0, exp_user=None):
    while 1:
        n = random.randrange(1,len(minifb.USERS))
        user1 = minifb.USERS[n]
        if user1 != exp_user: break
    user2 = minifb.USERS[n-random.randrange(n)-1]
    
    random.shuffle(WORDS)
    user1.send(user2.name ,' '.join(WORDS[:3]), date)

# LIKE A POST ALEATORIO
def rnd_like(date=0, exp_user=None):
    pub = random.choice(minifb.PUBLICATIONS)
    while 1:
        user = random.choice(minifb.USERS)
        if user != exp_user: break
    user.like(pub.userNoticed.name, pub.date)

WORDS = ["texto", "aleatorio", "estoy", "si", "ahora", "NO", "mañana", "dragon", ", verdad?", "IA"]
PERTIME = 1
DENSITY = [rnd_sign]*1 + [rnd_post]*3 + [rnd_mess]*3 + [rnd_like]*4
DENSITY = tuple(DENSITY)
