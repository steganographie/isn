from tkinter.filedialog import *
from PIL import Image

nom_image = askopenfilename(title=u"Ouvrir votre image",filetypes=[('images png','.png'),('images jpeg','.jpeg'),('images ppm','.ppm'),('images bmp','.bmp')])
#cf ligne 9 programme script_stegano_code.py

im = Image.open(nom_image)

r,g,b=im.split() #Eclate l'image en 3 bandes rouge, vert et bleu

### Détection de la couleur modifiée ###

red = list(r.getdata())  # Créée une liste contenant toutes les intensités de la bande rouge
green = list(g.getdata())
blue = list(b.getdata())

red_sum = sum(red) #Somme des intensités des rouges
green_sum =sum(green)
blue_sum = sum(blue)

taille=[red_sum, green_sum, blue_sum] #Liste contenant les valeurs des intensités des 3 couleurs

taille.sort(reverse=False) #tri dans l'ordre décroissant pour trouver la couleur la plus présente (taille[0])

if taille[0] == red_sum: #si la couleur la DEPEND DU CHOIX PRECEDENT présente est le rouge
    couleur_acc = list(r.getdata()) # alors on modifie l'intensité du rouge

if taille[0] == green_sum:
    couleur_acc = list(g.getdata())

if taille[0] == blue_sum:
    couleur_acc = list(b.getdata())

#### Décodage du texte ####

p=[str(x%2) for x in couleur_acc[0:8]]

q="".join(p)

q=int(q,2)

#lecture du message

n=[str(x%2) for x in couleur_acc[8:8*(q+1)]]

b="".join(n)

message=""

for k in range(0,q):
    l=b[8*k:8*k+8]
    message=message+chr(int(l,2))

print ("Le texte encodé dans l'image est :",message)