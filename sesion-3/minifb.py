class User:
    def __init__(self, name, pasw):
        self.name = name
        self.pasw = pasw
        USERS.append(self)

    def newContent(self):
        mes = list(filter(lambda m: m.userNoticed == self and not m.revised, MESSAGES))
        pub = list(filter(lambda p: p.userNoticed == self and not p.revised, PUBLICATIONS))
        for c in mes + pub:
            c.revised = 1
        return mes,pub
    
    def send(self, text, name, date):
        for u in USERS:
            if u.name == name:
                Message(self, u, text, date)
                return True
        return False
    
    def post(self, text, date):
        Publication(self, text, date)

class Content:
    def __init__(self, user, text, date):
        self.userNoticed = user
        self.text = text
        self.date = date
        self.revised = 0

class Message(Content):
    def __init__(self, userFrom, userTo, text, date):
        Content.__init__(self, userTo, text, date)
        self.origin = userFrom
        MESSAGES.append(self)

class Publication(Content):
    def __init__(self, user, text, date):
        Content.__init__(self, user, text, date)
        self.likes = 0
        self.revised = 1
        PUBLICATIONS.append(self)
    
    def like(self, user):
        self.like += 1
        self.revised = 0

# LOAD
def loadData(nf):
    KV_USERS = dict()
    with open(nf) as f:
        for l in f:
            # COMENTS & EMPTY
            if l[0] == '#' or len(l) < 2: continue
            l = l.strip()
            
            # SECCION
            if l[0] == '*':
                cur = l[1:]
                continue
            
            # LOAD USERS
            if cur == "user":
                u = User(*l.split(';'))
                KV_USERS[u.name] = u
            
            # LOAD MESSAGES
            if cur == "mess":
                usfr,usto,text,date,revs = l.split(';')
                m = Message(KV_USERS[usfr], KV_USERS[usto], text, int(date))
                m.revised = int(revs)
            
            # LOAD PUBLICATIONS
            if cur == "publ":
                us,text,date,likes,revs = l.split(';')
                p = Publication(KV_USERS[us], text, int(date))
                p.revised = int(revs)
    
    return USERS,MESSAGES,PUBLICATIONS

def LogIn(name, pasw):
    for u in USERS:
        if u.name == name:
            if pasw == u.pasw: return u
            else: return None
    return None

def SignUp(name, pasw):
    for u in USERS:
        if u.name == name: return None
    return User(name, pasw)

# INIT DATA
USERS = list()
MESSAGES = list()
PUBLICATIONS = list()

loadData("data-minifb")
