from PIL import Image #Importation de Python Imaging Library
im = Image.open("image_avec_message_codé.png")
#UN COMMENTAIRE DE PLUS
r,g,b=im.split()
r=list(r.getdata())
#lecture de la longueur de la chaine
p=[str(x%2) for x in r[0:8]]
q="".join(p)
q=int(q,2)
#lecture du message
n=[str(x%2) for x in r[8:8*(q+1)]]

b="".join(n)
message=""

for k in range(0,q):
    l=b[8*k:8*k+8]
    message=message+chr(int(l,2))
print (message)
