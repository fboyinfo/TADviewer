

global c1,c2,cf,k
c1 = color(220,220,220)
c2 = color(200,200,200)
cf = color(255,255,255)
k = color(0,0,0)
global TNone


class Noeud :
    def __init__(self, v):
        self.valeur = v 
        self.enfants = []
        self.x = 10
        self.y = 10
        self.selected = False
        self.edited = False
        self.chaining = False
        self.chained = False
        self.w = 50 
    
    def save(self):
        # Retourne une string qui decrit le maillon
        pass
    
    def ct(self) :
        print(self.chaining)
        ctab = [{'x':self.x+25, 'y':self.y+37}]
        for i in range(len(self.enfants)) :
            ctab.append({'x':self.x+i*10+5,'y':self.y+65})
        return ctab[self.chaining-2]
        
    def chain(self,ms = None) :
        if self.chaining == 2 :
            self.enfants.append(ms)
        if self.chaining >= 3 :
            self.enfants[self.chaining-3] = ms
        # Suppression des None
        self.enfants = [e for e in self.enfants if e]
        
    def setlabel(self, st) :
        self.valeur = st
    
    def chainingFalse(self) :
        self.chaining = False

    def clic(self,x,y) :
        if x>=self.x and x<=self.x + self.w and y>=self.y and y<=self.y + 25 :
            return 1 
        if x>=self.x and x<=self.x + self.w  and y>self.y + 25  and y<=self.y + 50 :
            print(self)
            return 2
        for i in range(len(self.enfants)) :
            if x>=self.x+i*10 and x<=self.x+i*10+10  and y>self.y +60  and y<=self.y + 70 :
                return i+3
        return False
    
    def __repr__(self):
        s = '(' + str(self.valeur) + ',' + str(self.enfants) + ')' 
        return s
    
    
    
    def draw(self):
        x = self.x
        y = self.y
        if self.selected : 
            fill(255,0,0)
        elif self.edited :
            fill(0,255,0)
        else :
            fill(c1)
        rect(x,y,50,50)
        if self.selected : 
            fill(200,0,0)
        elif self.edited :
            fill(0,200,0)
        else :
            fill(c2)
        rect(x,y,50,25)
        noFill()
        rect(x,y+25,50,25)
        if len(self.enfants)==0 :
            fill(0,0,0)
            TNone(x+25,y+25+3)
        else :
            fill(0,0,0)
            ellipse(x+25,y+25+12,8,8)
            noFill()
            strokeWeight(1)
            bezier(x , y + 65 , x - 50 , y + 65 , x + 25 , y + 50, x + 25 , y + 37)
            fill(k)
            triangle(x, y + 65 , x - 5, y + 68 , x - 5, y + 62 )
            for i in range(len(self.enfants)) :
                fill(c2)
                rect(x+i*10,y+60,10,10)
                fill(k)
                ellipse(x+i*10+5,y+65,6,6)
                fils = self.enfants[i]
                noFill()
                bezier(fils.x +25 ,fils.y - 10, fils.x +25, fils.y - 30 , x+i*10+5,y+120, x+i*10+5,y+65)
                fill(0,0,0)
                triangle(fils.x +20 ,fils.y -10,fils.x +30 ,fils.y -10,fils.x +25 ,fils.y -5)
        

        textAlign(CENTER)
        text(self.valeur,x+25,y+17)


        
def TNone(x,y) :
    rect(x-2,y,2,15)
    rect(x-10,y+15,20,2)
    pass
    
