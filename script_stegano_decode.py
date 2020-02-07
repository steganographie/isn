from PIL import Image #Depuis le module PIL, importer image, permet d'effectuer des actions sur des images

im = Image.open("image_avec_message_codé.png") #Enregistre l'image sous la variable

r,g,b=im.split()

### MODIFICATION DU CODE POUR DETECTER LA BANDE DE COULEUR QUI A CHANGE ###

red = list(r.getdata())  # Créée une liste contenant toutes les intensitées de la bande rouge
green = list(g.getdata())
blue = list(b.getdata())

red_sum = sum(red) #Somme des intensités des rouges
green_sum =sum(green)
blue_sum = sum(blue)


#### FONCTION QUI DETERMINE LES COULEURS DOMINANTE MAIS EXISTE PLUS SIMPLE AVEC LA LISTE EN-DESSOUS ####
#if blue_sum > green_sum and red_sum :
    #print("Couleur dominante : Bleu")

#if green_sum > red_sum and blue_sum:
    #print("Couleur dominante : Vert")

#if red_sum > blue_sum and green_sum :
    #print("Couleur dominante : Rouge")
#### FIN ####

taille=[red_sum, green_sum, blue_sum] #Liste contenant les valeurs des intensitées des 3 couleurs

### CHOIX A FAIRE JOUER SUR LA COULEUR LA + ou - PRESENTE ? POUR L'INSTANT, LA - PRESENTE ###
taille.sort() #tri dans l'ordre croissant, on joue sur la couleur la moins présente (taille[0])
#taille.sort(reverse=False) tri dans l'ordre décroissant pour jouer sur la couleur la plus présente (taille[0])
### FIN ###

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

p=[str(x%2) for x in couleur_acc[0:8]]

q="".join(p)

q=int(q,2)

n=[str(x%2) for x in couleur_acc[8:8*(q+1)]]

b = "".join(n)

message=""

for k in range(0,q):
    l=b[8*k:8*k+8]
    message=message+chr(int(l,2))
print (message)

