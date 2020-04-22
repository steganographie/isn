import shutil
from tkinter.filedialog import *  # Depuis tkinter import tout le contenu de filedialog
from PIL import Image  # Depuis le module PIL, importer image, permet d'effectuer des actions sur des images
import os

### IMPORTER L'IMAGE VIA INTERFACE GRAPHIQUE ###

nom_image = askopenfilename(title=u"Ouvrir votre image",filetypes=[('images png','.png'),('image jpg','.jpg'),('images jpeg','.jpeg'),('images ppm','.ppm'),('images bmp','.bmp')])
#Permet de choisir son fichier via interface graphique et enregistre le chemin sous une variable

print("Le chemin du fichier image est :",nom_image) #Affiche le chemin de l'image , OPTIONNEL

img = Image.open(nom_image)

#img = Image.open("image.png")  # Enregistre l'image sous la variable nécessite de connaitre l'extension et le chemin de l'image
## Si on connait a coup sur le chemin de l'image
### FIN ###

l, h = img.size  # Renvoie un tupple contenant (largeur,hauteur)

r, g, b = img.split()  # Renvoie un tupple, Crée 3 nouvelles images à partir de celle de base, contenant chacune des bandes originales dans l'ordre rouge, vert et bleu

#### CHOISIR DE QUELLE COULEUR AUGMENTER L'INTENSITE ####

red = list(r.getdata())  # Créée une liste contenant toutes les intensitées de la bande rouge
green = list(g.getdata())
blue = list(b.getdata())

red_sum = sum(red) #Somme des intensités des rouges
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

#Passer par une somme n'est pas obligatoire mais a du sens car comment dit on qu'une liste et plus forte qu'une autre ? Alors que pour une somme, il faut juste comparer les résultats
#### FIN ####

c = input("Entrez le texte qui sera encodé dans l'image : ")  # Demande le texte qui sera entré dans l'image

u = len(c)  # Renvoie la longeur de la chaine rentrée par l'utilisateur

v = bin(u)[2:].rjust(8, "0")  # On transforme en binaire, met un longeur de 8 bits ATTENTION PAS COMPRIS .rjust
# [2:] enleve les 2 premiers caractères qui sont 0b, dans Python (pour dire que c'est un nombre binaire)

ascii = [bin(ord(i))[2:].rjust(8, "0") for i in c]  # Convertit en binaire la valeur decimale de chaque lettre composant la message que veut coder l'utilisateur dans l'image

### PARTIE COMPLIQUE ###

a = ''.join(ascii)  # crée liste qui prends la valeur des 8 bits en rouge

for j in range(8):
    couleur_acc[j] = 2 * int(couleur_acc[j] // 2) + int(v[j])  # PAS COMPRIS

for k in range(8 * u):
    couleur_acc[k + 8] = 2 * int(couleur_acc[k + 8] // 2) + int(a[k])

## FIN ###

couleur_modifiee = Image.new("L", (l,h))  # Creation d'une nouvelle image vide de meme dimensions que celle importée, mode "L" signifie en 8 bits pixels, en noir et blanc

couleur_modifiee .putdata(couleur_acc)  # Ajout dans la nouvelle image des teintes rouges modifiées qui contiennent

if taille[0] == red_sum:
    imgnew = Image.merge('RGB', (couleur_modifiee, g, b))  # Ajoute les bandes bleues et vertes de l'image de base et y ajoute la nouvelle teinte rouge qui contient le texte
# RGB =  3*8 bits pxiels, true colors

if taille[0] == green_sum:
    imgnew = Image.merge('RGB', (r, couleur_modifiee, b))

if taille[0] == blue_sum:
    imgnew = Image.merge('RGB', (r, g, couleur_modifiee))

### CHOISIR Où ENREGISTRER LA NOUVELLE IMAGE ###

nom_repertoire = askdirectory(initialdir="/",title='Choix du répertoire') #demande le repertoire

print("Le répertoire est :",nom_repertoire) #affiche le répertoire pris

imgnew.save("image_avec_message_codé.png") # Enregistre sous le nom choisit la nouvelle image, extension précisée et enregistre dans le dossier ou se trouve le script en python

shutil.copy2("image_avec_message_codé.png", nom_repertoire) #fait une copie dans le répertoire que l'utilisateur a pris

os.remove("image_avec_message_codé.png") #supprime le fichier image modifiée dans le dossier ou se trouve le script python

### FIN ###