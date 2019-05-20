import minifb
import iafb

def fstr(src,att='n',font='default',back='default',end=True):#formato para strings
	F = {'n':'0','b':'1','s':'2','i':'3','u':'4','r':'7','h':'8','c':'9'}
	C = {'black':30,'red':31,'green':32,'yellow':33,'blue':34,'magenta':35,
		 'cyan':36,'white':37,'default':39}
	try:
	    pre = "\033[" + ';'.join(map(lambda f: F[f], att))
	    pre += ';' + str(C[font]) + ';' + str(C[back]+10) + 'm'
	except:
	    pre = ''
	return pre + str(src) + '\033[0m'*end

def parse_cmd(cmds, promt=fstr("cmd: ", 'b'), unknow=fstr("unknow cmd!", 'n', 'red')):
    while 1:
        cmd = input(promt)
        if cmd == "":
            return None
        cmd = cmd.split(" ")
        if cmd[0] not in cmds: print(unknow)
        else: return cmd

def qyn(text):
    while 1:
        cmd = input(text)
        if cmd == "y" or cmd == "n": return "ny".index(cmd)

minifb.loadData("data-minifb")
user = None
date = 0

while 1:
    if user: print(fstr(user.name + " (conectado)", 'n', 'green'))
    else: print(fstr("disconected...", 'n', 'red'))
    
    cmd = parse_cmd(("new", "log", "sign", "post", "mess", "like", "out", 'q', "debug"), fstr("[%s] > "%date, 'b'))
    
    if not cmd:
        cont = minifb.LastContent(5)
        for p in cont:
            print("  [%s] %s: %s (%s likes)" % (p.date, fstr(p.userNoticed.name, 'b'), fstr(p.text, 'i'), p.likes))
    
    elif user and cmd[0] == "new":
        mes,pub = user.newContent()
        print(fstr("  messages:", 'bu'))
        for m in mes:
            print("  %s: %s" % (m.origin.name, fstr(m.text, 'i')))
        
        print(fstr("  publications:", 'bu'))
        for p in pub:
            print("  [%s] %s (%s likes)" % (p.date, fstr(p.text, 'i'), p.likes))
    
    elif cmd[0] == "log": user = minifb.LogIn(cmd[1], cmd[2])
    
    elif cmd[0] == "out": user = None
    
    elif cmd[0] == "sign": minifb.SignUp(cmd[1], cmd[2])
    
    elif user and cmd[0] == "post":
        text = input(fstr("  text: ", 'b'))
        user.post(text, date)
    
    elif user and cmd[0] == "mess":
        text = input(fstr("  text: ", 'b'))
        user.send(cmd[1], text, date)
    
    elif user and cmd[0] == "like": user.like(cmd[1], int(cmd[2]))
    
    elif cmd[0] == 'q': break
    
    elif cmd[0] == "debug":
        counts = (len(minifb.USERS), len(minifb.PUBLICATIONS), len(minifb.MESSAGES))
        print(fstr("# USER: %s\n# PUBL: %s\n# MESS: %s" % counts, 'i', 'blue'))

    iafb.use(date, user)
    date += 1

minifb.saveData("data-minifb")