 #on import les modules nécessaires
import pygame
from pygame.locals import *

#initialisation de pygame
pygame.init()

#création de la fenêtre de jeu
fenetre = pygame.display.set_mode((1200,750))
pygame.display.set_caption("Le Labyrinthe de Bouboub")


#Affichage du menu
## On ne met pas ceci dans la boucle principale sinon l'image se reaffiche a chaque boucle du while
background = pygame.image.load("menu.png").convert()
fenetre.blit(background, (0,0))
pygame.display.flip()
clic_jouer = pygame.Rect(360,173,478,190)
pygame.mixer.init(44600, -16, 2, 500)
sample = pygame.image.load("sample.png").convert_alpha()
sample2 = pygame.image.load("sample.png").convert_alpha()
bouboub = pygame.image.load("bouboub.png").convert_alpha()
cle = pygame.image.load("cle.png").convert_alpha()
Tbouton = pygame.image.load("tonneau_rouge.png").convert_alpha()
Tbouton_activé = pygame.image.load("tonneau_vert.png").convert_alpha()

marche = pygame.mixer.Sound("marche2.ogg")
son_door = pygame.mixer.Sound("door.ogg")
son_portefinale = pygame.mixer.Sound("portefinale.ogg")
son_clef = pygame.mixer.Sound("clef.ogg")
son_tonneau = pygame.mixer.Sound("interrupteur.ogg")

textbox = pygame.image.load("textbox.png").convert()
myfont = pygame.font.SysFont("comic",40)
myfont2 = pygame.font.SysFont("comicsansms",30)
blanc = (255,255,255)

clock = pygame.time.Clock()
clock.tick(60)

marchDroite=[pygame.image.load('noneim_droite.png'),pygame.image.load('noneim_droite2.png'),pygame.image.load('noneim_droite.png'),pygame.image.load('noneim_droite3.png'),pygame.image.load('noneim_droite.png'),pygame.image.load('noneim_droite2.png'),pygame.image.load('noneim_droite3.png')]
marchGauche=[pygame.image.load('noneim_gauche.png'),pygame.image.load('noneim_gauche2.png'),pygame.image.load('noneim_gauche.png'),pygame.image.load('noneim_gauche3.png'),pygame.image.load('noneim_gauche.png'),pygame.image.load('noneim_gauche2.png'),pygame.image.load('noneim_gauche3.png')]
marchHaut=[pygame.image.load('noneim_dos.png'),pygame.image.load('noneim_dos2.png'),pygame.image.load('noneim_dos.png'),pygame.image.load('noneim_dos3.png'),pygame.image.load('noneim_dos.png')]
marchBas=[pygame.image.load('noneim_face.png'),pygame.image.load('noneim_face2.png'),pygame.image.load('noneim_face.png'),pygame.image.load('noneim_face3.png'),pygame.image.load('noneim_face.png')]
immob=pygame.image.load('noneim_face.png')


salle0 = pygame.image.load("sample.png").convert_alpha()
salle1 = pygame.image.load("room.png").convert_alpha()
salle2 = pygame.image.load("room 2.png").convert_alpha()
salle2_1 = pygame.image.load("room2_1.png").convert_alpha()
salle3 = pygame.image.load("room3.png").convert_alpha()
salle3_1 = pygame.image.load("room3_1.png").convert_alpha()
salle4 = pygame.image.load("room4.png").convert_alpha()
salle5 = pygame.image.load("room5.png").convert_alpha()
salle6 = pygame.image.load("room6.png").convert_alpha()
salle7 = pygame.image.load("room7.png").convert_alpha()
findujeu = sample
fin=[pygame.image.load("fin1.png"),pygame.image.load("fin2.png"),pygame.image.load("fin3.png"),pygame.image.load("fin4.png"),pygame.image.load("fin5.png")]
salle = salle7

vit = 1


objet = []
activable = []

class Mur:
    def __init__(self, murx, mury,p):
        global objet, objetY, objetX
        self.sprite = sample
        self.x = murx
        self.y = mury
        objet.append(self)

inventaire = []

class BlocAct:
    def __init__(self,murx, mury, sprite, typeObjet, typeBloc,liste):
        global objet, objetY, objetX
        self.x = murx
        self.y = mury
        self.sprite = sample
        if sprite == 1:
            self.sprite = sample
        elif sprite == 2:
            self.sprite = cle
        elif sprite == 3:
            self.sprite = Tbouton
        objet.append(self)
        activable.append(self)
        self.type = typeBloc
        self.objet = typeObjet
        self.use = 0
        self.liste = liste



listtp = []
class tp:
    def __init__(self,murx,mury,lieux,lieuy):
        self.x = murx
        self.y = mury
        listtp.append(self)
        self.use = 1
        self.lieux = lieux
        self.lieuy = lieuy

x = 316
vit = 1
y = 114
m = 1
coord = False
act = False
quitter = False
menu = False
Poubelle = []
walkCount = 0
vitanim = 15
musique = 1

def deplacement():
    # Ici, collisions() me dira si il y a, et ou, un objet se trouve par rapport a mon personnage;
    collisions()
    for event in pygame.event.get():
        global x, y, objet_droite, objet_haut, objet_bas, objet_gauche, quitter, m, coord, act, objet, objetX, objetY, menu, vit
        global walkCount
        #DROITE
        if event.type == pygame.KEYDOWN and event.key == K_d and objet_droite == False:
            pas = vitanim
            while objet_droite == False or tp == False:
                collisions()
                collisions3()
                x += vit*3
                perso = image(4)
                update()
                for i in listtp:
                    if i.use < 0:
                        return
                if pas == vitanim:
                    if walkCount + 1 ==5:
                        walkCount = 0
                    walkCount +=1
                    pas = 0
                pas += 1

                fenetre.blit(marchDroite[walkCount], (x,y))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYUP and event.key == K_d :
                        objet_droite = True
                        return
        #HAUT
        if event.type == pygame.KEYDOWN and event.key == K_z and objet_haut == False:
            pas = vitanim
            while objet_haut == False or tp == False and vit !=0:
                collisions()
                collisions3()
                y -= vit*3
                perso = image(1)
                update()
                for i in listtp:
                    if i.use < 0:
                        return
                if pas == vitanim:
                    if walkCount + 1 ==5:
                        walkCount = 0
                    walkCount +=1
                    pas = 0
                pas += 1
                fenetre.blit(marchHaut[walkCount], (x,y))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP and event.key == K_z:
                        objet_haut = True
                        return
        #GAUCHE
        if event.type == pygame.KEYDOWN and event.key == K_q and  objet_gauche == False:
            pas = vitanim
            while objet_gauche == False or tp == False and vit !=0:
                collisions()
                collisions3()
                x -= vit*3
                perso = image(2)
                update()
                for i in listtp:
                    if i.use < 0:
                        return
                if pas == vitanim:
                    if walkCount + 1 ==5:
                        walkCount = 0
                    walkCount +=1
                    pas = 0
                pas += 1
                fenetre.blit(marchGauche[walkCount], (x,y))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP and event.key == K_q:
                        objet_gauche = True
                        return

        #BAS
        if event.type == pygame.KEYDOWN and event.key == K_s and objet_bas == False:
            pas = vitanim
            while objet_bas == False or tp == False and vit !=0:
                collisions()
                collisions3()
                y += vit*3
                perso = image(3)
                update()
                for i in listtp:
                    if i.use < 0:
                        return
                if pas == vitanim:
                    if walkCount + 1 ==5:
                        walkCount = 0
                    walkCount +=1
                    pas = 0
                pas += 1
                fenetre.blit(marchBas[walkCount], (x,y))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP and event.key == K_s:
                        objet_bas = True
                        return

        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                coord = True
            if event.key == K_e:
                act = True

        if event.type == QUIT or event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            quitter = True



def collisions():
    # Cette fonction est appelée avant celle des déplacements ; elle verifie la
    # position des objets de la classe Mur en lisant les coordonnées inscrites
    # dans les listes objetX[i] et objetY[i], ou i+1 represente un objet mur{i};

    global vit, x, y, objet_droite, objet_haut, objet_bas, objet_gauche, Mur, objet
    objet_gauche = False
    objet_droite = False
    objet_haut = False
    objet_bas = False
    #Ne pas sortir de l'écran;
    if x>0 and x-10<=0:
        objet_gauche = True
    if x<1200 and x+64>1199:
        objet_droite = True
    if y>0 and y-10<=0:
        objet_haut = True
    if y<750 and y+64>750:
        objet_bas = True

    #Détéction d'un objet de la class Mur;
    for i in objet:
        if y+68>=i.y and y<i.y and x+50>=i.x and x<=i.x+50 and i.sprite != sample2:
            objet_bas = True

        elif y-4<=i.y+64 and y>i.y  and x+50>=i.x and x<=i.x+50 and i.sprite != sample2:
            objet_haut = True

        elif x>i.x and x<=i.x+64 and y<=i.y+62 and y+62>i.y and i.sprite != sample2:
            objet_gauche = True

        elif x<=i.x and x+60>i.x and y<=i.y+62 and y+62>i.y and i.sprite != sample2:
            objet_droite = True


m = 1 ## CA CORRESPOND A LIMAGE
def collisions2():
    global m, afficher
    for i in activable:
        if y+68>=i.y and y<i.y and x+50>=i.x and x<=i.x+50 and i.sprite != sample2:
            update()
            m = 3
            i.use += 1

        elif y-4<=i.y+64 and y>i.y and x+50>=i.x and x<=i.x+50 and i.sprite != sample2:
            update()
            m = 1
            i.use += 1

        elif x>i.x and x<=i.x+64 and y<=i.y+62 and y+62>i.y and i.sprite != sample2:
            update()
            m = 2
            i.use += 1

        elif x<=i.x and x+60>i.x and y<=i.y+62 and y+62>i.y and i.sprite != sample2:
            update()
            m = 4
            i.use += 1

        if i.use == 1:
                perso = image(m)
                (i.liste).append(i.objet)
                i.use = 2
                if i.type == 1:
                    i.sprite = sample
                if i.type == 2:
                    i.sprite = sample2
                if i.type == 3:
                    i.sprite = Tbouton_activé

                update()
                fenetre.blit(perso.sprite, (x, y))
                pygame.display.update()




def collisions3():
    global x,y
    for i in listtp:
        if i.x<x+40 and i.y<y+64 and i.y+64>y+30 and i.x+64>x+26:
            i.use = -(i.use)
            for t in range(10):
                fenetre.blit(noir, (0, 0))
                pygame.display.update()
            x = i.lieux
            y = i.lieuy
            update()




class image:
    def __init__(self, m):
        if m == 1: #haut
            sprite = pygame.image.load("noneim_dos.png").convert_alpha()
        if m == 2: # gauche
            sprite = pygame.image.load("noneim_gauche.png").convert_alpha()
        if m == 3: #bas
            sprite = pygame.image.load("noneim_face.png").convert_alpha()
        if m == 4: #droite
            sprite = pygame.image.load("noneim_droite.png").convert_alpha()

        self.sprite = sprite

def musique1():
        pygame.mixer.music.fadeout(2000)
        pygame.mixer.music.stop()
        pygame.mixer.music.load("audio.ogg")
        pygame.mixer.music.play()

def musique2():
        pygame.mixer.music.fadeout(2000)
        pygame.mixer.stop()
        pygame.mixer.music.load("quizz.ogg")
        pygame.mixer.music.play()

def musique3():
        pygame.mixer.music.fadeout(2000)
        pygame.mixer.stop()
        pygame.mixer.music.load("sortie.ogg")
        pygame.mixer.music.play()

def update():
    fenetre.fill((50,50,50))
    fenetre.blit(salle, (64, 64))
    for i in activable:
        fenetre.blit(i.sprite,(i.x,i.y))


def coords():
    #Fonction non appelée mais qui permet de verifier certaines caractéristiques en appuyant sur espace;
    print(x,y, objet_gauche, objet_droite, objet_haut, objet_bas)
    print(len(objet))
    print("liste clef",CleF)

def core():
    global coord, menu, boucle_jeu, boucle_principale, act, salle
    for i in range(30):
        deplacement()
    if quitter == True:
        salle = salle0
        boucle_jeu = False
        boucle_principale = False
    elif coord == True:
        coords()
        coord = False
    elif act == True:
        son_tonneau.play()
        collisions2()
        act = False


#Boucle principale qui fait tourner la fenetre et affiche premierement le menu
boucle_principale = True
boucle_jeu = False
while boucle_principale:
    for event in pygame.event.get(): ##pygame.event.get() est une liste d'evenements
        if  event.type == QUIT or event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            boucle_principale = False

    boucle_menu = True
    #boucle du menu qui se ferme en cliquant sur le bouton et qui se change en boucle_jeu
    while boucle_menu:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                boucle_menu = False
                boucle_principale = False
            elif event.type == MOUSEBUTTONUP: ##Detection du clique
                if event.button == 1:
                    if clic_jouer.collidepoint(event.pos): ##Detection de la collision
                        son_door.play()
                        noir=pygame.image.load("noir.png")
                        gris=pygame.image.load("gris.png")
                        for i in range(12):
                            fenetre.blit(noir, (0, 0))
                            pygame.display.update()
                        fenetre.fill((0,0,0))
                        for i in range(10):
                            fenetre.blit(gris, (0, 0))
                            pygame.display.update()
                        fenetre.fill((50,50,50)) ## Ecran noir
                        pygame.display.update() ## Rfaraichir l'ecran
                        boucle_menu = False
                        boucle_jeu = True


    update()
    perso = image(3)
    fenetre.blit(perso.sprite, (x, y))
    pygame.display.update()
    salle = salle1
    o= 0
    l = 0
    k = 0
    vit = 1
    Cle1 = False
    bab = False
    questionnaire = False
    CleF = []
    joie = 0

    Scene1 = False
    Scene2 = False

    musique1()


    while boucle_jeu:

        if len(CleF) == 2:
            salle2 = salle2_1


        if salle == salle1:
            objet.clear()
            activable.clear()
            listtp.clear()
            update()
            for i in range(1,8):
                objet.append(Mur(i*64,25,1))
                objet.append(Mur(64,i*64,1))
                objet.append(Mur(6*64,i*64,1))

            for i in range(3):
                objet.append(Mur((3+i)*64-128,9*64-128,1))
                objet.append(Mur((7+i)*64-128,9*64-128,1))

            objet.append(Mur(384-128,307-128,1))
            objet.append(Mur(126,252,1))
            objet.append(Mur(448-128,307-128,1))
            tp1 = tp(64*4,9*64-15,192,150)
            perso = image(1)
            update()
            fenetre.blit(perso.sprite, (x, y))
            pygame.display.update()
            if Scene1 == False:
                text = myfont.render("Tiens ?",200,blanc)
                text2 = myfont.render("Où suis-je ?",200,blanc)
                text3 = myfont.render("(Appuyez sur ZQSD pour vous déplacer.)",200,blanc)
                text4 = myfont.render("(Appuyez sur E pour intéragir.)",200,blanc)
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text,(200,550))
                pygame.display.update()
                pygame.time.wait(2000)
                fenetre.blit(text2,(320,550))
                pygame.display.update()
                pygame.time.wait(1000)
                fenetre.blit(text3,(200,600))
                pygame.display.update()
                pygame.time.wait(1000)
                fenetre.blit(text4,(200,650))
                pygame.display.update()
                Scene1 = True




        while salle == salle1:
            core()
            if tp1.use < 0:
                salle = salle2
                tp1.use = 1
                perso = image(3)


        if salle == salle2:
            objet.clear()
            activable.clear()
            listtp.clear()

            update()
            if Scene2 == False:
                text = myfont.render("Il semblerait que je doive ouvrir cette porte.",200,blanc)
                text2 = myfont.render("Il faut que je trouve 2 clés !",200,blanc)
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text,(200,550))
                fenetre.blit(perso.sprite, (x, y))
                pygame.display.update()
                pygame.time.wait(1000)
                fenetre.blit(text2,(200,600))
                fenetre.blit(perso.sprite, (x, y))
                pygame.display.update()
                pygame.time.wait(2000)
                Scene2 = True


            tp2 = tp(192,80,256,450)
            tp3 = tp(773,468,128,180)
            tpFin = tp(540,20,0,0)
            for i in range(1,13):
                objet.append(Mur(64*i,64*9,1))
                objet.append(Mur(64,64*i,1))
                objet.append(Mur(768,64*(i-7),1))
            for i in range(4):
                objet.append(Mur(128+(64*(i-3)),80,1))
                objet.append(Mur((256+64*i),80,1))
                objet.append(Mur((640+64*i),80,1))

            if len(CleF) != 2:
                objet.append(Mur(540,30,1))
            else :
                musique3()
            objet.append(Mur((687),129,1))
            objet.append(Mur(768,520,1))
            objet.append(Mur(768,360,1))
            update()
            fenetre.blit(perso.sprite, (x, y))
            pygame.display.update()


        while salle == salle2:
            core()
            if tp2.use < 0:
                salle = salle1
                update()
                tp2.use = 1
            if tp3.use < 0:
                salle = salle3
                tp3.use = 1
                perso = image(4)
            if tpFin.use < 0:
                salle = findujeu
                tpFin.use= 1



        if salle == salle3:
            objet.clear()
            activable.clear()
            listtp.clear()
            update()
            Table = BlocAct(392,100,1,1,1,Poubelle)
            for i in range(1,17):
                objet.append(Mur(64*i,64*10,1))
                objet.append(Mur(64*i,64-35,1))
                objet.append(Mur(64,192+64*i,1))

            for i in range(2,7):
                objet.append(Mur(64*7,64*i-35,1))
                objet.append(Mur(64*9,64*i-35,1))
                objet.append(Mur(64*16,64*i-35,1))

            for i in range(2,6):
                objet.append(Mur(64*i,322,1))
                objet.append(Mur(64*i,322+31,1))

            for i in range(2):
                if Cle1 == False:
                    objet.append(Mur(128+64*i,514-45,1))
                    objet.append(Mur(896+64*i,158-70,1))
                objet.append(Mur(64*16,64*(i+8),1))


            objet.append(Mur(64*8,64*6-35,1))
            objet.append(Mur(64,100,1))
            objet.append(Mur(700,186,1))
            objet.append(Mur(828,186,1))
            objet.append(Mur(700,186+128,1))
            objet.append(Mur(828,186+128,1))
            tp3 = tp(70,202,710,438)
            tp4 = tp(975+40,464,120,306)
            tp7 = tp(120,460,330,296)
            update()
            fenetre.blit(perso.sprite, (x, y))
            pygame.display.update()

        while salle == salle3:
            core()
            if tp3.use < 0:
                salle = salle2
                perso = image(2)
                fenetre.blit(perso.sprite, (x, y))
                pygame.display.update()
                tp3.use = 1
            if tp4.use < 0:
                salle = salle4
                perso = image(4)
                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                tp4.use = 1
            if tp7.use < 0:
                salle = salle7
                perso = image(4)
                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                tp7.use = 1

            if Table.use== 2:

                text = myfont.render("Observez bien autour de vous!",200,blanc)
                update()
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text,(200,550))

                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                pygame.time.wait(1000)
                Table.use=0


        if salle == salle4:
            objet.clear()
            activable.clear()
            listtp.clear()
            update()
            Table2 = BlocAct(385,190,1,1,1,Poubelle)
            for i in range(7):
                objet.append(Mur(64*(i-2),514,3))
                objet.append(Mur(64*(i-1),514+64-35,3))
                objet.append(Mur(64*(i+3),514-163,3))
                objet.append(Mur(64*(i+3),514-163-4*64,3))
                objet.append(Mur(64*(i),700,3))

            for i in range(6):
                objet.append(Mur(64*(i+7),514,2))
                objet.append(Mur(64*(i+7),514+64,2))
                objet.append(Mur(64,44+64*(i-2)-20,2))
                objet.append(Mur(64,44+64*(i+5)+30,2))


            for i in range(15):
                objet.append(Mur(64*(i+1),31,4))
                objet.append(Mur(64*(i+7),514+128,4))

            for i in range(11):
                objet.append(Mur(64*(i+3),514-227,2))

            for i in range(9):
                objet.append(Mur(64*(i+4),514-227-30,2))

            objet.append(Mur(64*16,64*2-50,2))
            objet.append(Mur(64*16,64*4-20,2))
            objet.append(Mur(64*16,64*6,2))
            objet.append(Mur(64*16,64*9-20,2))
            objet.append(Mur(64*10,210,2))
            objet.append(Mur(64*6,192,2))
            tp5 = tp(70,306,950,440)
            if bab == False:
                tp5_1 = tp(972+40,468,120,306)
                tp5_2 = tp(972+40,325-30,120,306)
                tp5_3 = tp(972+40,202-10,120,306)
            if bab == True:
                tp5_1 = tp(972+40,468,90,176)
                tp5_2 = tp(972+40,325-30,90,176)
                tp5_3 = tp(972+40,202-10,90,176)
            tp6 = tp(140,650,254,120)
            update()
            fenetre.blit(perso.sprite, (x, y))
            pygame.display.update()


        while salle == salle4:
            core()
            if tp5.use < 0 :
                salle = salle3
                perso = image(2)
                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                tp5.use = 1

            if tp5_1.use < 0:
                salle = salle4
                perso = image(4)
                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                tp5_1.use = 1
                if bab == False:
                    k = 1
                else :
                    salle = salle6
                    x = 130
                    y = 176

            if tp5_2.use < 0:
                salle = salle4
                perso = image(4)
                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                tp5_2.use = 1
                if bab == False:
                    o = 1
                else :
                    salle = salle6
                    x = 130
                    y = 176

            if tp5_3.use < 0:
                if bab == False:
                    salle = salle4
                    perso = image(4)
                    fenetre.blit(perso.sprite, (x,y))
                    pygame.display.update()
                    tp5_3.use = 1
                    l = 1
                else :
                    salle = salle6
                    x = 130
                    y = 176

            if tp6.use < 1:
                salle = salle5
                perso = image(4)
                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                tp6.use = 1

            if o+l+k == 3 and bab == False:
                bab = True
                text = myfont.render("Il ne s'est rien passé... ou du moins ?",False,blanc)
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text,(200,550))
                pygame.display.update()
                pygame.time.wait(2000)
                update()
                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                o = 2

            if Table2.use == 2:

                text = myfont.render("Persévérance est clé de réussite.",200,blanc)
                update()
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text,(200,550))
                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                pygame.time.wait(1000)
                Table2.use = 0

        if salle == salle5:
            objet.clear()
            activable.clear()
            listtp.clear()
            update()

            for i in range(4):
                objet.append(Mur(252+(i*64),30,2))
            for i in range(2):
                objet.append(Mur(192,142+(i*64),2))
                objet.append(Mur(510,142+(i*64),2))
            objet.append(Mur(90,206,2))
            objet.append(Mur(582,206,2))
            for i in range(6):
                objet.append(Mur(648,252+(i*64),2))
                objet.append(Mur(54,252+(i*64),2))
            for i in range(10):
                objet.append(Mur(116+(i*52),662,2))

            if Cle1 == False:
                tonneaulist = []
                Ta = BlocAct(255,338,3,3,3,tonneaulist)
                Tb = BlocAct(448,338,3,2,3,tonneaulist)
                Tc = BlocAct(255,498,3,1,3,tonneaulist)
                Td = BlocAct(448,498,3,4,3,tonneaulist)

            elif Cle1 == True:
                objet.append(Mur(260,340,1))
                objet.append(Mur(260,500,1))
                objet.append(Mur(450,500,1))
                objet.append(Mur(450,340,1))

            tp7= tp(254,70,135+64,576+44)


            update()
            perso = image(3)
            fenetre.blit(perso.sprite, (x, y))
            pygame.display.update()


        while salle == salle5:
            if Ta.use >= 2 and Tb.use >= 2 and Tc.use >= 2 and Td.use >= 2 and tonneaulist ==[1,2,3,4] and Cle1 == False:

                text = myfont.render("Un passage s'est ouvert !",False,blanc)
                son_portefinale.play()
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text,(200,550))
                pygame.display.update()
                pygame.time.wait(1000)
                salle3 = salle3_1
                Cle1 = True

            elif Ta.use >= 2 and Tb.use >= 2 and Tc.use >= 2 and Td.use >= 2 and tonneaulist !=[1,2,3,4] and Cle1 == False:
                activable.clear()
                tonneaulist =[]
                text = myfont.render("Raté!",False,blanc)
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text,(200,550))
                pygame.display.update()
                pygame.time.wait(1000)
                update()
                Ta = BlocAct(255,338,3,3,3,tonneaulist)
                Tb = BlocAct(448,338,3,2,3,tonneaulist)
                Tc = BlocAct(255,498,3,1,3,tonneaulist)
                Td = BlocAct(448,498,3,4,3,tonneaulist)
                update()
                fenetre.blit(perso.sprite, (x, y))
                pygame.display.update()
            core()
            if tp7.use < 1:
                salle = salle4
                tp7.use = 1
                perso = image(4)
        if salle == salle6:
            objet.clear()
            activable.clear()
            listtp.clear()
            update()
            tp8 =  tp(68,176,972,150)

            cle2F = False
            for i in range(15):
                objet.append(Mur(50+(64*i),20,2))
            objet.append(Mur(480,75,2))
            objet.append(Mur(40,86,2))
            for i in range(5):
                objet.append(Mur(46,250+(64*i),2))
            for i in range(10):
                objet.append(Mur(904,22+(64*i),2))
            for i in range(15):
                objet.append(Mur(42+(64*i),510,2))

            fenetre.blit(perso.sprite,(x,y))
            pygame.display.update()

            if questionnaire == False:
                fenetre.blit(bouboub,(450,230))
                pygame.display.update()
                text = myfont.render("Voila Bouboub en personne !!!!",200,blanc)
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text,(200,550))
                musique2()
                pygame.display.update()
                pygame.time.wait(3500)
                text = myfont2.render("- Je vais te poser quelques questions...",200,blanc)
                musique = 2
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text,(200,550))
                pygame.display.update()
                pygame.time.wait(3500)

                question1 = False
                reponse1 = pygame.Rect(200,650,50,100)
                reponse2 = pygame.Rect(400,650,400,100)
                text = myfont2.render("- Suis-je le plus malin ? (Cliquez sur la réponse.)",200,blanc)
                text2 = myfont.render("Non...",200,blanc)
                text3 = myfont.render("Oui Bouboub, tu es très malin!",200,blanc)
                while question1 == False:
                    fenetre.blit(textbox,(175,520))
                    fenetre.blit(text,(200,550))
                    fenetre.blit(text2,(200,650))
                    fenetre.blit(text3,(400,650))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONUP: ##Detection du clique
                            if event.button == 1:
                                if reponse1.collidepoint(event.pos):
                                    text4 = myfont2.render("- Me voila fort déçu...",200,blanc)
                                    joie -= 1
                                    question1 = True
                                elif reponse2.collidepoint(event.pos):
                                    text4 = myfont2.render("- Excellente réponse! Nous ne pouvious douter !",200,blanc)
                                    joie += 1
                                    question1 = True
                question2 = False
                update()
                fenetre.blit(bouboub,(450,230))
                fenetre.blit(perso.sprite,(x,y))

                if question2 == False:
                    reponse1 = pygame.Rect(200,650,150,100)
                    reponse2 = pygame.Rect(500,650,300,100)
                    text = myfont2.render("- Bien, passons. Qui est le plus beau ?",200,blanc)
                    text2 = myfont.render("Toi Bouboub!",200,blanc)
                    text3 = myfont.render("Difficile de répondre...",200,blanc)
                    while question2 == False:
                        fenetre.blit(textbox,(175,520))
                        fenetre.blit(text4,(200,550))
                        fenetre.blit(text,(200,575))
                        fenetre.blit(text2,(200,650))
                        fenetre.blit(text3,(500,650))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == MOUSEBUTTONUP: ##Detection du clique
                                if event.button == 1:
                                    if reponse1.collidepoint(event.pos):
                                        text4 = myfont2.render("- Cela va de soi!",200,blanc)
                                        joie += 1
                                        question2 = True
                                    elif reponse2.collidepoint(event.pos):
                                        text4 = myfont2.render("- Je pense que la réponse est pourtant évidente..",200,blanc)
                                        joie -= 1
                                        question2 = True
                update()
                fenetre.blit(bouboub,(450,230))
                fenetre.blit(perso.sprite,(x,y))
                question3 = False
                if question3 == False:
                    fenetre.blit(textbox,(175,520))
                    fenetre.blit(text4,(200,550))
                    text = myfont2.render("- Pour finir.... ",200,blanc)
                    fenetre.blit(text,(200,600))
                    pygame.display.update()
                    pygame.time.wait(3000)

                    text = myfont2.render("- Résous ce calcul !",200,blanc)
                    text2 = myfont.render("Euuuuuh...",200,blanc)
                    text3 = myfont.render("Facile !",200,blanc)
                    reponse1 = pygame.Rect(200,650,50,100)
                    reponse2 = pygame.Rect(650,650,100,100)
                    equation = pygame.image.load("lol.png").convert_alpha()
                    fenetre.blit(textbox,(175,520))
                    fenetre.blit(equation,(210,560))
                    fenetre.blit(text,(200,530))
                    fenetre.blit(text2,(200,675))
                    fenetre.blit(text3,(650,675))
                    pygame.display.update()
                    while question3==False:
                        for event in pygame.event.get():
                                if event.type == MOUSEBUTTONUP: ##Detection du clique
                                    if event.button == 1:
                                        if reponse1.collidepoint(event.pos):
                                            text4 = myfont2.render("- Comment ca 'Euuuuh' ?",200,blanc)
                                            joie -= 1
                                            question3 = True
                                        elif reponse2.collidepoint(event.pos):
                                            text4 = myfont2.render("-Ahahaha ! On est d'accord !",200,blanc)
                                            joie += 1
                                            question3 = True

                if joie > 0:
                    text5 = myfont2.render("*Bouboub est joyeux. Bien joué ! ",200,blanc)
                    text6 = myfont2.render("-Tu mérites d'être recompensé !",200,blanc)
                elif joie < 0:
                    text5 = myfont2.render("*Bouboub est énervé. Pas de chance ! ",200,blanc)
                    text6 = myfont2.render("*Dans sa colère, Bouboub fait tomber une clé !",200,blanc)

                musique1()
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text4,(200,530))
                pygame.display.update()
                pygame.time.wait(2000)
                update()
                fenetre.blit(textbox,(175,520))
                fenetre.blit(text5,(200,530))
                fenetre.blit(text6,(200,600))
                fenetre.blit(bouboub,(450,230))
                fenetre.blit(perso.sprite,(x,y))
                pygame.display.update()
                pygame.time.wait(2000)
                joie = 0
                for i in range(12):
                    pygame.time.wait(50)
                    fenetre.blit(noir,(0,0))
                    pygame.display.update()

                update()
                fenetre.blit(perso.sprite,(x,y))
                pygame.display.update()
                questionnaire = True

            prise = False
            if questionnaire == True:
                for i in range(len(CleF)):
                    if CleF[i] == "cle2":
                        prise = True
                if prise == False:
                    CleF2 = BlocAct(450,230,2,"cle2",2,CleF)

            update()
            fenetre.blit(perso.sprite,(x,y))
            pygame.display.update()


        while salle == salle6:
            core()
            if tp8.use < 0:
                salle = salle4
                perso = image(2)
                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                tp8.use = 1


        if salle == salle7:
            objet.clear()
            activable.clear()
            listtp.clear()
            update()
            perso = image(2)
            prise2 = False
            for i in range(8):
                objet.append(Mur(50,192+(64*i),2))
                objet.append(Mur(38+(64*i),570,2))
            objet.append(Mur(394,214,2))

            for i in range(4):
                objet.append(Mur(394,302+(64*i),2))
            for i in range(5):
                objet.append(Mur(48+(64*i),140,2))

            for i in range(len(CleF)):
                    if CleF[i] == "cle1":
                        prise2 = True
            if prise2 == False:
                CleF1 = BlocAct(230,510,2,"cle1",1,CleF)

            tp9 = tp(370,296,180,430)
            update()
            fenetre.blit(perso.sprite,(x,y))
            pygame.display.update()

        while salle == salle7:
            core()
            if tp9.use < 0:
                salle = salle3
                perso = image(4)
                fenetre.blit(perso.sprite, (x,y))
                pygame.display.update()
                tp9.use = 1


        if salle == findujeu:
            objet.clear()
            activable.clear()
            listtp.clear()
            fenetre.fill((0,0,0))
            pygame.display.update()
            pygame.time.wait(2000)
            imgfin=0
            for i in range(4):
                imgfin+= 1
                for i in range(12):
                    pygame.time.wait(50)
                    fenetre.blit(fin[imgfin],(0,0))
                    pygame.display.update()
            pygame.display.update()


        while salle == findujeu:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == pygame.KEYDOWN and event.key == K_ESCAPE or event.type == MOUSEBUTTONUP:
                    salle = salle0
                    boucle_jeu = False
                    boucle_principale = False


pygame.quit()
