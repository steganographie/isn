import shutil
from tkinter.filedialog import *
from PIL import Image
import os

### Importer l'image via une interface graphique ###

nom_image = askopenfilename(title=u"Ouvrir votre image",filetypes=[('images png','.png'),('image jpg','.jpg'),('images jpeg','.jpeg'),('images ppm','.ppm'),('images bmp','.bmp')])
#Permet de choisir son fichier via interface graphique et enregistre le chemin sous une variable

print("Le chemin du fichier image est :",nom_image) #Affiche le chemin de l'image choisie

img = Image.open(nom_image) #Ouvre l'image pour en extraire des propriétés par la suite

### Caractéristiques de l'image ###

l, h = img.size  #Renvoie un tupple contenant (largeur,hauteur)

r, g, b = img.split()  #Renvoie un tupple, Crée 3 nouvelles images à partir de celle de base, contenant chacune des bandes originales dans l'ordre rouge, vert et bleu

#### Trouver la couleur la plus présente ####

red = list(r.getdata())  #Créée une liste contenant toutes les intensitées de la bande rouge
green = list(g.getdata()) #Pareil pour le vert
blue = list(b.getdata()) #et pour le bleu

red_sum = sum(red) #Somme des intensités rouges
green_sum =sum(green)
blue_sum = sum(blue)

taille=[red_sum, green_sum, blue_sum] #Liste contenant les valeurs des intensitées des 3 couleurs

taille.sort(reverse=False) #tri dans l'ordre décroissant, on joue sur la couleur la plus présente (taille[0])

if taille[0] == red_sum: #si la couleur la DEPEND DU CHOIX PRECEDENT présente est le rouge
    couleur_acc = list(r.getdata()) # alors on modifie l'intensité du rouge
    print("Couleur la moins présente : rouge")

if taille[0] == green_sum:
    couleur_acc = list(g.getdata())
    print("Couleur la moins présente : vert")

if taille[0] == blue_sum:
    couleur_acc = list(b.getdata())
    print("Couleur la moins présente : bleu")

#### Message à encoder ####

c = input("Entrez le texte qui sera encodé dans l'image : ")  #Demande le texte qui sera entré dans l'image

u = len(c)  #Renvoie la longeur de la chaine rentrée par l'utilisateur

v = bin(u)[2:].rjust(8, "0") #Transforme l'entree de l'utilisateur en binaire, ajuste à 8 caractères en ajoutant le caractère "0"

ascii = [bin(ord(i))[2:].rjust(8, "0") for i in c]  # Convertit en binaire la valeur decimale de chaque lettre composant la message que veut coder l'utilisateur dans l'image

### Encodage dans l'image du texte ###

a = ''.join(ascii)  #Crée une liste qui comporte les valeurs binaires du texte de l'utilisateur

for j in range(8):
    couleur_acc[j] = 2 * int(couleur_acc[j] // 2) + int(v[j])

for k in range(8 * u):
    couleur_acc[k + 8] = 2 * int(couleur_acc[k + 8] // 2) + int(a[k]) #Cache le texte dans l'image

## Création de la nouvelle image ###

couleur_modifiee = Image.new("L", (l,h))  # Creation d'une nouvelle image vide de memes dimensions que celle importée, mode "L" signifie en 8 bits pixels, en noir et blanc

couleur_modifiee .putdata(couleur_acc)  # Ajout dans la nouvelle image des teintes rouges modifiées qui contiennent le message de l'utilisateur

if taille[0] == red_sum:
    imgnew = Image.merge('RGB', (couleur_modifiee, g, b))  # Ajoute les bandes bleues et vertes de l'image de base et y ajoute la nouvelle teinte rouge qui contient le texte

if taille[0] == green_sum:
    imgnew = Image.merge('RGB', (r, couleur_modifiee, b))

if taille[0] == blue_sum:
    imgnew = Image.merge('RGB', (r, g, couleur_modifiee))

### Choix de l'emplacement de la nouvelle image ###

nom_repertoire = askdirectory(initialdir="/",title='Choix du répertoire') #demande le repertoire

print("Le répertoire est :",nom_repertoire) #Affiche le répertoire pris

imgnew.save("image_avec_message_codé.png") # Enregistre sous le nom choisit la nouvelle image, extension précisée et enregistre dans le dossier où se trouve le script en python

shutil.copy2("image_avec_message_codé.png", nom_repertoire) #fait une copie dans le répertoire que l'utilisateur a pris

os.remove("image_avec_message_codé.png") #supprime le fichier image modifiée dans le dossier où se trouve le script python