from PIL import Image #Importation de la librairie PIL, module qui permet de traiter des images.

im = Image.open("image.png") #Variable qui ouvre le fichier image.png

w,h=im.size #on récupère les dimensions de l'image

r,g,b=im.split() #On éclate l'image en trois (rouge vert bleu)

r=list(r.getdata()) #on transforme l'image en liste

c=input("Entrez le texte qui sera encodé dans l'image : ")

u=len(c) #on note la longueur de la chaine et on la transforme en binaire

v=bin(len(c))[2:].rjust(8,"0") #on transforme la chaine en une liste de 0 et de 1 

ascii=[bin(ord(x))[2:].rjust(8,"0") for x in c] #transformation de la liste en chaine

a=''.join(ascii) #on code la longueur de la liste dans les 8 premiers pixels rouges

for j in range(8):
    r[j]=2*int(r[j]//2)+int(v[j])

#on code la chaine dans les pixels suivants
for i in range(8*u):
    r[i+8]=2*int(r[i+8]//2)+int(a[i])

#on recrée l'image rouge 
nr = Image.new("L",(w,h))

nr.putdata(r) #fusion des trois nouvelles images

imgnew = Image.merge('RGB',(nr,g,b)) 
imgnew.save("image_avec_message_codé.png") 
