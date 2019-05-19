from turtle import Turtle
import random

def parse_cmd(cmds, promt="cmd: ", unknow="unknow cmd!"):
    while 1:
        cmd = input(promt)
        if cmd == "":
            return None
        cmd = cmd.split(" ")
        if cmd[0] not in cmds: print(unknow)
        else: return cmd

class DrunkedTurtle(Turtle):
    def __init__(self, drunk=100):
        Turtle.__init__(self,'turtle')
        self.drunk = drunk
    
    def avanzar(self,dist):
        c_dist = 0
        while dist > c_dist:
            
            if self.drunk > 0:
                self.color("red")
                r_dist = random.randrange(int(dist/10), int(3*dist/10))
                r_ang = random.choice((-1, 1)) * random.randrange(30,60)
            else:
                self.color("blue")
                r_dist = dist
                r_ang = 0
            
            self.left(r_ang)
            self.forward(r_dist)
            
            c_dist += r_dist
            self.drunk -= r_dist

dt = DrunkedTurtle()

while 1:
    cmd = parse_cmd(("q", "drunk", "go"))

    if not cmd:
        dt.reset()
        continue
    if cmd[0] == "drunk":
        dt.drunk = int(cmd[1])
    if cmd[0] == "go":
        dt.avanzar(int(cmd[1]))
    if cmd[0] =='q':
        break