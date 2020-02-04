from PIL import Image #Depuis le module PIL, importer image, permet d'effectuer des actions sur des images

im = Image.open("image_avec_message_codé.png") #Enregistre l'image sous la variable

### MODIFICATION DU CODE POUR DETECTER LA BANDE DE COULEUR QUI A CHANGE ###

r,g,b=im.split()

r=list(r.getdata())

p=[str(x%2) for x in r[0:8]]

q="".join(p)

q=int(q,2)

n=[str(x%2) for x in r[8:8*(q+1)]]

b="".join(n)

message=""

for k in range(0,q):
    l=b[8*k:8*k+8]
    message=message+chr(int(l,2))
print (message)
