from LC import *
from AB import *
from Arbre import *
import random as rd

global hide
hide = False

global c1,c2,cf,k,bw
bw = False

global num
num = 0
global strkb,inputkb
strkb = ''
inputkb = False
global selected,chaining,editing
selected = False
chaining = False
editing = False

def setup() :
    global selected, chaining, editing
    size(1000,700)
    ################################### images
    global logo_img
    global cc_img
    logo_img = loadImage("logo.png")
    cc_img = loadImage("cc.png")
    ################################### menus
    global lmh,lm,lcm,mam,nbm,nnm
    lmh = Lemenuhaut()
    lm = Lemenu(120)
    ################################### Mode liste chainee
    lcm = ListeChainee()
    mam = Maillon('v')
    global lesMaillons
    lesMaillons = []
    global lesListes
    lesListes = []
    ################################### Mode Arbre binaire
    nbm = NoeudBin('v')
    global lesNoeudsBin
    lesNoeudsBin = []
    ################################### Mode Arbre
    nnm = Noeud('v')
    global lesNoeuds
    lesNoeuds = []
    
    
def draw() :
    global lesMaillons, lesListes, lesNoeudsBin
    #################################### Menu commun
    global lmh,lcm,mam,nnm
    global selected, chaining, editing
    background(cf)
    ####################################
    x = mouseX
    y = mouseY
    lm.draw()
    lmh.draw()
    if lm.visible : menuSpe(lmh.active)
    #################################### Dessins des elements
    if lmh.active == 0 :
        for m in lesMaillons :
            m.draw()
        for l in lesListes :
            l.draw()
    if lmh.active == 1 :
        for n in lesNoeudsBin :
            n.draw()
    if lmh.active == 2 :
        for n in lesNoeuds :
            n.draw()
    #################################### Deplacement ou chainage
    if selected : moveSelected(x,y)
    if chaining : chainSelected(x,y)
    #################################### visualisation input keyboard    
    
    if inputkb :
        x = width - 1.75 * lm.w 
        y = 80
        # rectMode(CENTER) 
        textAlign(CENTER)
        fill(c1)
        rect(x-50,y-10,100,20)
        rect(x-50,y+10,100,20)
        fill(k)
        textSize(12)
        text("enter value",x,y+6)
        text(strkb,x,y+26)
    

###########################################################
#                  CLAVIER  + SOURIS                      #
###########################################################     

def mousePressed():
    global lmh,lesMaillons,lesListes,lesNoeudsBin,lcm,mam,strkb,inputkb,lminput
    global selected,chaining,editing
    x = mouseX
    y = mouseY
    # Liste Chainee :
    if mouseButton == LEFT:
        if selected :
            deselectAll()
        elif chaining :
            target(lmh.active,x,y)
            deselectAll()
        else :
            if (select(lmh.active,x,y)) : 
                pass
            else :
                deselectAll()
                pass
        
    if mouseButton == RIGHT :
        print("RIGHT")
        #################################################### Liste Chainee (0)
        if lmh.active == 0 :
            ade = addObject(lcm,x,y,ListeChainee,lesListes,"lst") or addObject(mam,x,y,Maillon,lesMaillons)
            if not(ade) :
                editing = setValue(lesListes,x,y) or setValue(lesMaillons,x,y)
        if lmh.active == 1 :
            ade = addObject(nbm,x,y,NoeudBin,lesNoeudsBin)
            if not(ade) :
                editing = setValue(lesNoeudsBin,x,y) 
                print(editing)
        if lmh.active == 2 :
            if not(addObject(nnm,x,y,Noeud,lesNoeuds)) :
                editing = setValue(lesNoeuds,x,y)  
        
                
def setValue(lst,x,y) :
    '''
    Parmi la liste lst, cherche quel element e est concerne par le clic
    Et lance le mode inputkb pour saisir la valeur ou le nom.
    '''
    global lminput,inputkb,editing
    if not(hide) :
        for e in lst :
            if e.clic(x,y) == 1 :
                inputkb = True
                lminput = e 
                e.edited = True 
                print(e)
                return True
    return False         
                    
def addObject(elt,x,y,Objet,lst,v="v") :
    '''
    Si l'objet-menu elt est concene par le clic,
    cree un objet m de la classe Objet et le met dans la liste lst
    '''
    global selected
    if elt.clic(x,y) == 1 :
            m = Objet(v)
            m.x = x
            m.y = y
            m.selected = True
            selected = True
            lst.append(m)
            return True
    return False


def deselectAll() :
    '''
    Pour toutes les instances d'objets presents dans les differentes listes
    On met l'attribut select a False.
    '''
    global editing, selected, chaining
    for e in lesListes + lesMaillons + lesNoeudsBin + lesNoeuds :
        e.selected = False
        e.edited = False
        # e.chainingGauche = False
        # e.chainingDroit = False
        # e.chaining = False
        e.chained = False
    selected = False
    editing = False
    chaining = False 
    
def target(mode,x,y) :
    if mode == 0 :
        lst = lesMaillons + lesListes
    if mode == 1 :
        lst = lesNoeudsBin
    if mode == 2 :
        lst = lesNoeuds
    for m in lst :
        if m.chaining :
            m.chained = False
            print(m)
            for ms in lst :
                if ms.clic(x,y) :
                    print(ms)            
                    m.chain(ms)
                    m.chained = True
            print(m.chained)
            if not(m.chained) :
                m.chain()
            m.chainingFalse()
                  

                                    
def select(mode,x,y) :
    '''
    Change les attributs selected ou chaining en fonction de l'objet
    concerne par le clic
    '''
    global selected,chaining
    deselectAll()
    if mode == 0 :
        lst = lesMaillons + lesListes
    if mode == 1 :
        lst = lesNoeudsBin
    if mode == 2 :
        lst = lesNoeuds
    for e in lst  : 
        e.tmp = e.clic(x,y)
        if e.tmp :
            print(e.tmp)
            e.selected = (e.tmp <= 1)
            e.chaining = e.tmp
            if e.chaining : chaining = (e.tmp > 1)
            if e.selected : selected = True
            return True
    return False
    
            
def moveSelected(x,y) :
    '''
    Place l'element actuellement selectionne en x,y
    '''
    for e in lesListes + lesMaillons + lesNoeudsBin + lesNoeuds :
        if e.edited : 
            return True
        if e.selected : # and not e.edited:
            e.x = x
            e.y = y
            return True
    return False

def chainSelected(x,y) :
    '''
    Trace le fil, depuis l'element en train d'etre chaine
    '''
    for e in lesMaillons + lesListes + lesNoeudsBin + lesNoeuds :
        if e.chaining :
            noFill()
            strokeWeight(1)
            bezier(x- 5 ,y + 12, x- 50, y+ 12, e.ct()['x']+25, e.ct()['y'], e.ct()['x'],e.ct()['y'])
            fill(k)
            triangle(x - 5,y +12 ,x - 10 ,y +17,x - 10,y +9) 
            fill(0,0,0)
            return True
    return False
        

def keyPressed():
    global inputkb,strkb,lminput,hide
    global lmh,lm
    global lmh,lesMaillons,lesListes,lesNoeudsBin,lcm,mam,strkb,inputkb,lminput
    global selected,chaining,editing
    global lesMaillons
    global num
    if inputkb :
        if key == '\n' or not lminput.edited : 
            inputkb = False
            lminput.setlabel(strkb)
            strkb = ''
            deselectAll()
            editing = False
            return False
        strkb = strkb + key
        return True
    if key == '\t' and not(hide) :
        deselectAll()
        lmh.switch()
    if key == 's' :
        numero = format(num, '05d')
        save(str(numero)+"_TADviewer"+".png")
        num = num + 1
    if key == 'h' :
        lmh.visible = not(lmh.visible)
        lm.visible = not(lm.visible)
        hide = not(hide)
    if key == 'g' :
        if lmh.active == 0 :
            for m in lesMaillons :
                m.snapgrid()
    if key == 'd' :
        selectOutput("Select a file to write to:", "fileOSelected")
    
    if key == 'l' :
        selectInput("Select a file to process:", "fileLSelected")
        
    if key == 'k' :
        switchWBCol()
        # Changer les valeurs des couleurs (random !!)

def saveDatas(path) :
    path = path.split('.')
    print(path[0])
    path = path[0] + '.tdv'
    if lmh.active == 0 :
        # Ajouter une id dans les objets
        for m in lesMaillons :
            m.save()
        for l in lesListes :
            l.save()
    if lmh.active == 1 :
        for n in lesNoeudsBin :
            n.save()
    if lmh.active == 2 :
        for n in lesNoeuds :
            n.save()
    words = "apple bear cat dog"
    list = split(words, ' ')
    # Writes the strings to a file, each on a separate line
    saveStrings(path, list)

def fileLSelected(selection):
    if selection == None:
        print("Window was closed or the user hit cancel.")
    else:
        loadDatas(selection.getAbsolutePath())

def fileOSelected(selection):
    if selection == None:
        print("Window was closed or the user hit cancel.")
    else:
        saveDatas(selection.getAbsolutePath())

def loadDatas(path) :
    print(path)
    lines = loadStrings(path)
    print("there are %i lines" % len(lines))
    for line in lines:
        print(line)
    

###########################################################
#          SWITCH BLACKWHITE <> COLOR                     #
###########################################################
def switchWBCol():
    global c1,c2,cf,k,bw
    if bw :
        c1 = color(220,220,220)
        c2 = color(200,200,200)
        cf = color(255,255,255)
        k = color(0,0,0)
        bw = not(bw)
    else :
        c1 = randomDarkColor()
        c2 = randomDarkColor()
        cf = randomBrightColor()
        k = randomDarkColor()
        bw = not(bw)

def randomDarkColor() :
    return color(rd.randint(0,180),rd.randint(0,180),rd.randint(0,180))

def randomBrightColor() :
    return color(rd.randint(200,255),rd.randint(200,255),rd.randint(200,255))


###########################################################
#                       MENU A DROITE                     #
###########################################################

# Illustrations Icones :
# Grille 12 par 12 : largeur d'un carré = g
# logo ocupe un carré de 10*g
# avec une marge de g

class Lemenu() :
    def __init__(self,w) :
        self.menu = [mlf,cc_auteur]
        self.w = w
        self.visible = True
    
    def draw(self) :
        if not(self.visible) :
            return False
        sep(self.w)
        for i in range(len(self.menu)) :
            self.menu[i](width-self.w,height-self.w*(i+1))

#################################################### Liste Chainee (0)
def menuLC() :
    # A supprimer voir fonction suivante
    global lm,lcm,mam
    lcm.x = width - 32
    lcm.y = 110
    lcm.draw()
    mam.x = width - 85
    mam.y = 170
    mam.draw()
    textAlign(CENTER)
    textSize(14)
    text('right-clic to add',width - lm.w // 2, 55)
    text('right-clic to set value',width - 1.75 * lm.w , 55)
    
def menuSpe(mode) :
    global lm
    global lmh,lcm,mam,nnm
    fill(k)
    if mode == 0 :
        global lcm,mam
        lcm.x = width - 32
        lcm.y = 110
        lcm.draw()
        mam.x = width - 85
        mam.y = 170
        mam.draw()
    if mode == 1 :
        global nbm
        nbm.x = width - 85
        nbm.y = 170
        nbm.draw()
    if mode == 2 :
        global nnm
        nnm.x = width - 85
        nnm.y = 170
        nnm.draw()
    textAlign(CENTER)
    textSize(14)
    text('right-clic to add',width - lm.w // 2, 55)
    text('right-clic to set value',width - 1.75 * lm.w , 55)

def cc_auteur(x,y) :
    w = width - x
    g = w / 12
    cc(x,y)
    auteur(x,y+4*g)
    pass

def sep(w) :
    stroke(k)
    line(width-w,0,width-w,height)

def mlf(x,y) :
    w = width - x
    g = w / 12
    global logo_img
    image(logo_img,x+g,y+2*g,10*g,8*g)

def floppydisc(x,y):
    rectMode(CORNER)
    w = width - x
    g = w / 12
    fill(k)
    rect(x+g, y+g , g*10 , g*10,10,10,10,10)
    fill(cf)
    noStroke()
    triangle(x+g-1,y+g-1,x+g*4,y+g-1,x+g-1,y+g*4)
    ellipse(x+g*6.5,y+g*6,g*4,g*4)
    rectMode(CENTER)
    fill(k)
    rect(x+g*6.5,y+g*6,g,g)
    fill(cf)
    stroke(k)
    rect(x+g*6.5,y+g*10,5*g,2*g)
    rectMode(CORNER)

def vid(x,y) :
    pass
    
def cc(x,y) :
    w = width - x
    g = w / 12
    global cc_img
    image(cc_img,x+g,y+4*g,10*g,4*g)
    #     image(cc, width-88,height-230,70,30)
    
def auteur(x,y) :
    w = width - x
    g = w / 12
    fill(k)
    textAlign(LEFT)
    textSize(int(w//8))
    text("Francois Boyer",x+g,y+6*g)
    pass
    

###########################################################
#                       MENU HAUT                         #
###########################################################

class Lemenuhaut() :
    def __init__(self) :
        self.tab = ['L.C.','A.B.','Arbre']
        self.help = ['Press tab to change mode',
                     'Press h to hide menus','Press k to switch WB<->color','Press s to screenshoot']
                     #'Press g to snap grid','Press l to load datas','Press d to save datas']
        self.active = 0
        self.visible = True
        pass
    
    def draw(self) :
        if not(self.visible) :
            return False
        fill(k)
        rect(0,0,width,30)
        textSize(20)
        mi = 0
        for m in self.tab :
            if mi == self.active :
                fill(c1)
                rect(mi*100,0,100,30)
                fill(k)
                text(m,mi * 100 + 20, 25)
            else :
                fill(cf)
                text(m,mi * 100 + 20, 25)
            mi = mi + 1
        fill(cf)
        lh = len(self.help)
        fc = (frameCount // 90) % lh
        text(self.help[fc],mi * 100 + 20, 25)
    
    def switch(self) :
        self.active = self.active + 1
        if self.active >= len(self.tab) :
            self.active = 0


                
        

    
