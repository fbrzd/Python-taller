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
    
    def send(self, name, text, date):
        for u in USERS:
            if u.name == name:
                Message(self, u, text, date)
                return True
        return False
    
    def post(self, text, date):
        Publication(self, text, date)

    def like(self, name, date):
        for p in PUBLICATIONS:
            if p.userNoticed.name == name and p.date == date:
                p.likes += 1
                p.revised = 0
                return 1
        return 0

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
                p.likes = int(likes)
    
    return USERS,MESSAGES,PUBLICATIONS

# SAVE
def saveData(nf):
    with open(nf, 'w') as f:
        
        f.write("*user\n")
        for u in USERS:
            l = ';'.join((u.name,u.pasw))
            f.write(l + '\n')
        
        f.write("\n*mess\n")
        for m in MESSAGES:
            l = ';'.join((m.origin.name, m.userNoticed.name, m.text, str(m.date), str(m.revised)))
            f.write(l + '\n')
        
        f.write("\n*publ\n")
        for p in PUBLICATIONS:
            l = ';'.join((p.userNoticed.name, p.text, str(p.date), str(p.likes), str(p.revised)))
            f.write(l + '\n')

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

def LastContent(n):
    PUBLICATIONS.sort(key=lambda p: -p.date)
    return PUBLICATIONS[:min(n,len(PUBLICATIONS))]

# INIT DATA
USERS = list()
MESSAGES = list()
PUBLICATIONS = list()