# Notes : Regler les longues celulles
# Probleme avec les marges et le centrage
# de l'origine du pointeur
# Tenter le snapgrid


global c1,c2,cf,k
c1 = color(220,220,220)
c2 = color(200,200,200)
cf = color(255,255,255)
k = color(0,0,0)
global TNone


###########################################################
#               L.C :   MAILLON                           #
###########################################################

        
class Maillon:
    def __init__(self, v, s=None):
        self.valeur = v   # La valeur courante
        self.suivant = s  # pointe le Maillon suivant
        self.x = 10
        self.y = 10
        self.selected = False
        self.edited = False
        self.chaining = False
        self.ctab = [(self.x+25, self.y+37)]
        self.chained = False
        self.w = 50
        '''
        if len(str(self.valeur))>5 : 
            self.w = map(len(str(self.valeur))-5,0,5,50,100)
        '''
        
    def save(self):
        # Retourne une string qui decrit le maillon
        pass
        
    def ct(self) :
        return {'x':self.x+25, 'y':self.y+37}
    
    def setsize(self) :
        pass
        '''
        if len(str(self.valeur))>5 : 
            self.w = map(len(str(self.valeur))-5,0,5,50,100)
        '''
        
    def setlabel(self,st):
        self.valeur = st
        self.setsize()
        
    def chain(self,ms = None) :
        self.suivant = ms
    
    def __repr__(self):
        s = '(' + str(self.valeur) + ',' + str(self.suivant) + ')' 
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
        
        if self.suivant is None :
            fill(0,0,0)
            TNone(x+self.w//2,y+25+3)
        else :
            fill(0,0,0)
            ellipse(x+self.w//2,y+25+12,8,8)
            noFill()
            # Ajouter un controle si gauche ou droite de son suivant
            strokeWeight(1)
            bezier(self.suivant.x - 5 ,self.suivant.y + 12, self.suivant.x - 50, self.suivant.y + 12, x + 70,y+37, x+25, y+37)
            fill(0,0,0)
            triangle(self.suivant.x - 5 ,self.suivant.y + 12,self.suivant.x - 10 ,self.suivant.y + 7,self.suivant.x - 10 ,self.suivant.y + 17)
        textAlign(CENTER)
        text(self.valeur,x+self.w//2,y+17)  
    
    def clic(self,x,y) :
        if x>=self.x and x<=self.x + self.w and y>=self.y and y<=self.y+25 :
            return 1 
        if x>=self.x and x<=self.x + self.w and y>self.y+25 and y<=self.y+50 :
            return 2 
        return False
    
    def chainingFalse(self) :
        self.chaining = False

    def move(self) :
        pass
    
    def snapgrid(self) :
        pass
    
    
        

###########################################################
#               L.C :   LISTE CHAINEE                     #
###########################################################

class ListeChainee:
    def __init__(self, name = "lst"):
        """Initialise une liste vide."""
        self.premier = None
        self.selected = False
        self.chaining = False
        self.edited = False
        self.x = 200
        self.y = 200
        self.ctab = [(self.x-10, self.y+10)]
        self.name = name
        delta = map(len(self.name),0,9,25,110)
        self.w = delta
    
    def save(self):
        # Retourne une string qui decrit le maillon
        pass
        
    def ct(self) :
        return {'x':self.x-10, 'y':self.y+10}
        
    def setsize(self) :
        delta = map(len(self.name),0,9,25,110)
        self.w = delta
        
    def chain(self,ms = None) :
        self.premier = ms
    
    def setlabel(self,st):
        self.name = st
        self.setsize()

    def __repr__(self):
        """Permet un print de la liste chainee."""
        if len(self) == 0 :
          return '[]'
        elif len(self) == 1:
          v1 = self.premier.valeur
          return '[' + str(v1) + ']'
        else :
          v1 = self.premier.valeur
          m2 = self.premier.suivant
          souslst = ListeChainee()
          souslst.premier = m2
          return '[' + str(v1) + ',' + str(souslst)[1:-1] + ']'
  
    def draw(self):
        x = self.x
        y = self.y
        if self.selected : 
            fill(255,0,0)
        elif self.edited :
            fill(0,255,0)
        else :
            fill(c1)
        # Rectangle (+ point)
        rectMode(CENTER)
        rect(x-10,y+10,20,20)
        # Rectangle avec nom 
        rectMode(CORNERS)    
        rect(x-self.w,y,x-20,y+20)
        fill(0,0,0)
        textSize(18)
        textAlign(RIGHT)
        text(self.name,x - 23,y + 17)
        # Point
        fill(0,0,0)
        ellipse(x - 10,y + 10,8,8)
        rectMode(CORNER)
        noFill()
        if self.selected : 
            fill(255,0,0)
        elif self.edited :
            fill(0,255,0)
        else :
            fill(c1)
        if self.premier is None :
            rect(x + 20,y - 20,50,50)
            fill(0,0,0)
            TNone(x+45,y)
            strokeWeight(1)
            noFill()
            bezier(x - 10 ,y + 10, x + 20 , y + 10, x - 10, y - 5, x + 18, y - 5)
            fill(0,0,0)
            triangle(x + 13, y - 2 ,x + 13, y - 8,x + 18, y - 5)
        else :
            strokeWeight(1)
            noFill()
            bezier(x - 10 ,y + 10, x + 20 , y + 10, self.premier.x - 50, self.premier.y + 12, self.premier.x - 5 ,self.premier.y + 12)
            fill(0,0,0)
            triangle(self.premier.x - 5 ,self.premier.y + 12,self.premier.x - 10 ,self.premier.y + 7,self.premier.x - 10 ,self.premier.y + 17)
            fill(0,0,0)
            
    def clic(self,x,y) :
        if x>=self.x - self.w and x< self.x - 20  and y>=self.y and y<=self.y + 20 :
            return 1
        if x>=self.x - 20 and x<= self.x  and y>=self.y and y<=self.y + 20 :
            return 2
        return False 
    
    def chainingFalse(self) :
        self.chaining = False
  
    def ajoutEnTete(self, x):
        """Insere elem en tete de liste en creant un nouveau maillon"""
        m = Maillon(x,self.premier)
        self.premier = m
        
    def supprimeEnTete(self):
        """Supprime l'element en tete et retourne ce dernier"""
        if self.premier is None :
          raise NameError('Impossible de supprimer sur une liste vide')
        v = self.premier.valeur
        self.premier = self.premier.suivant
        return v
    
    def __len__(self) :
        """Renvoie le nombre d'elements presents dans la liste."""
        if self.premier is None :
          return 0
        else :
          m2 = self.premier.suivant
          souslst = ListeChainee()
          souslst.premier = m2
          return len(souslst) + 1
          
    '''
    def __len__(self):
        """Renvoie le nombre d'elements presents dans la liste."""
        l = 0
        m = self.premier
        while not(m is None) :
            l = l + 1
            m = m.suivant
        return l
    '''

    def __getitem__(self,i):
        """Renvoit l'element d'indice i"""
        if len(self) == 0 :
          raise NameError('L\'indice n\'est pas valide')
        if i == 0 :
          v1 = self.premier.valeur
          return v1
        else :
          m2 = self.premier.suivant
          souslst = ListeChainee()
          souslst.premier = m2
          return souslst[i-1]

    '''
    def __getitem__(self,i):
        """Renvoit l'element d'indice i"""
        if len(self) <= i :
          raise NameError('L\'indice n\'est pas valide')
        m = self.premier
        cpt = 0
        while cpt < i:
            m = m.suivant
            cpt += 1
        return m.valeur
    '''
    
    def modifieElement(self,i,x):
        """Change la valeur a l'indice i"""
        if len(self) <= i :
          raise NameError('L\'indice n\'est pas valide')
        m = self.premier
        cpt = 0
        while cpt < i:
            m = m.suivant
            cpt += 1
        m.valeur = x

    def prolonge(self,other) :
        """Prolonge la presente liste par l'autre"""
        m = self.premier
        while not(m.suivant is None) :
            m = m.suivant
        m.suivant = other.premier

    def insereElement(self,i,x):
        """Insere une valeur a l'indice i"""
        mi = Maillon(x)
        if i == 0 :
          mi.suivant = self.premier
          self.premier = mi
        else :
          c = 0
          m = self.premier
          while c < i - 1 :
            m = m.suivant
            c = c + 1
          mi.suivant = m.suivant
          m.suivant = mi

def TNone(x,y) :
    rect(x-2,y,2,15)
    rect(x-10,y+15,20,2)
    pass
