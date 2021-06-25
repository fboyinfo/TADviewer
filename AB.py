# Probleme de largeur de celulles pour les grandes valeurs

global c1,c2,cf,k
c1 = color(220,220,220)
c2 = color(200,200,200)
cf = color(255,255,255)
k = color(0,0,0)
global TNone

  
class NoeudBin :
    def __init__(self, v, g=None, d= None):
        self.valeur = v 
        self.gauche = g 
        self.droit = d
        self.x = 10
        self.y = 10
        self.selected = False
        self.edited = False
        self.chaining = False
        self.chainingGauche = False
        self.chainingDroit = False
        self.chained = False
        self.w = 50 
    
    def save(self):
        # Retourne une string qui decrit le maillon
        pass
    
    def ct(self) :
        print(self.chaining)
        ctab = [{'x':self.x+12, 'y':self.y+37},{'x':self.x+37, 'y':self.y+37}]
        print(ctab)
        return ctab[self.chaining-2]
        
    def chain(self,ms = None) :
        print(self.chaining)
        if self.chaining == 2 :
            self.gauche = ms
        if self.chaining == 3 :
            self.droit = ms
            
    def setlabel(self, st) :
        self.valeur = st

    def chainingFalse(self) :
        self.chaining = False
        self.chainingGauche = False
        self.chainingDroit = False
        
    def clic(self,x,y) :
        if x >= self.x and x <= self.x + self.w and y >= self.y and y <= self.y + 25 :
            return 1
        if x >= self.x and x <= self.x + self.w // 2 and y > self.y + 25  and y <= self.y + 50 :
            return 2
        if x > self.x + self.w // 2  and x <= self.x + self.w and y > self.y + 25  and y <= self.y + 50 :
            return 3
        return False

    def __repr__(self) :
        s = '(' + str(self.gauche) + ',' + str(self.valeur) + ',' + str(self.droit) + ')' 
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
        rect(x,y,self.w,50)
        if self.selected : 
            fill(200,0,0)
        elif self.edited :
            fill(0,200,0)
        else :
            fill(c2)
        rect(x,y,self.w,25)
        noFill()
        rect(x,y+25,self.w//2,25)
        rect(x+self.w//2,y+25,self.w//2,25)
        if self.gauche is None :
            fill(0,0,0)
            TNone(x+self.w//4,y+25+3)
        else :
            fill(0,0,0)
            ellipse(x+12,y+3*self.w//4,8,8)
            noFill()
            # Ajouter un controle si gauche ou droite de son suivant
            strokeWeight(1)
            bezier(self.gauche.x +25 ,self.gauche.y - 10, self.gauche.x +25, self.gauche.y - 30 , x - 70, y+ 37, x + 12,y+25+12)
            fill(0,0,0)
            triangle(self.gauche.x +20 ,self.gauche.y -10,self.gauche.x +30 ,self.gauche.y -10,self.gauche.x +25 ,self.gauche.y -5)
        
        if self.droit is None :
            fill(0,0,0)
            TNone(x+3*self.w//4,y+25+3)
        else :
            fill(0,0,0)
            ellipse(x+3*self.w//4,y+25+12,8,8)
            noFill()
            # Ajouter un controle si gauche ou droite de son suivant
            strokeWeight(1)
            bezier(self.droit.x + 25 ,self.droit.y -10, self.droit.x +25, self.droit.y -30, x + 119, y+ 37, x + 37,y+25+12)
            fill(0,0,0)
            triangle(self.droit.x +20 ,self.droit.y -10 ,self.droit.x +30 ,self.droit.y -10,self.droit.x +25 ,self.droit.y - 5)
        
        textAlign(CENTER)
        text(self.valeur,x+25,y+17)
        
    

      
def TNone(x,y) :
    rect(x-2,y,2,15)
    rect(x-10,y+15,20,2)
    pass
