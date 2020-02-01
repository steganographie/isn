from PIL import Image  # Depuis le module PIL, importer image, permet d'effectuer des actions sur des images

img = Image.open("image.png")  # Enregistre l'image sous la variable

l, h = img.size  # Renvoie un tupple contenant (largeur,hauteur)

r, g, b = img.split()  # Renvoie un tupple,
# Crée 3 nouvelles images à partir de celle de base, contenant chacune des bandes originales dans l'ordre rouge, vert et bleu

#### CHOISIR QUELLE COULEUR AUGMENTER L'INTENSITE ####

red = list(r.getdata())  # Affiche toutes les valeurs de rouges présentes dans la bande rouge
green = list(g.getdata())
blue = list(b.getdata())

if blue > green and red :
    print("Dominante bleue dans l'image")

if green > red and blue:
    print("Dominante verte dans l'image")

if red > blue and green :  # Si le rouge domine
    print("Dominante rouge dans l'image")

taille=[red, green, blue]

taille.sort() #trie par ordre croissant

if taille[0]==red:
    couleur_acc=list(r.getdata())

if taille[0]==green:
    couleur_acc=list(g.getdata())

if taille[0]==blue:
    couleur_acc=list(b.getdata())

#### FIN ####

c = input("Entrez le texte qui sera encodé dans l'image : ")  # Demande le texte qui sera entré dans l'image

u = len(c)  # Renvoie la longeur de la chaine rentrée par l'utilisateur

v = bin(u)[2:].rjust(8, "0")  # On transforme en binaire, met un longeur de 8 bits ATTENTION PAS COMPRIS .rjust
# [2:] enleve les 2 premiers caractères qui sont 0b, dans Pyhton, pour dire que c'est un nombre binaire

ascii = [bin(ord(i))[2:].rjust(8, "0") for i in c]  # Convertit en binaire la valeur decimale de chaque lettre composant la message que veut coder l'utilisateur dans l'image

a = ''.join(ascii)  # crée liste qui prends la valeur des 8 bits en rouge

for j in range(8):
    couleur_acc[j] = 2 * int(couleur_acc[j] // 2) + int(v[j])  # PAS COMPRIS

# on code la chaine dans les pixels suivants PAS ENCORE COMPRS
for k in range(8 * u):
    couleur_acc[k + 8] = 2 * int(couleur_acc[k + 8] // 2) + int(a[k])

nr = Image.new("L", (l,h))  # Creation d'une nouvelle image vide de meme dimensions que celle importée, mode "L" signifie en 8bits pixels, en noir et blanc

nr.putdata(couleur_acc)  # Ajout dans la nouvelle image des teintes rouges modifiées qui contiennent

imgnew = Image.merge('RGB', (nr, g,b))  # Ajoute les bandes bleues et vertes de l'image de base et y ajoute la nouvelle teinte rouge qui contient le texte
# RGB =  3*8 bits pxiels, true colors

imgnew.save("image_avec_message_codé.png")  # Enregistre sous le nom choisit la nouvelle image, extension précisée
