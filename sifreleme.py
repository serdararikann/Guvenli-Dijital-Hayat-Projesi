import base64
import os
liste = []
files = []

for r, d, fa in os.walk('C:/Users/Serdar Arıkan/deneme'):
    for file in fa:
        files.append(os.path.join(r, file))
for f in files:
    dosyaOkuma = open(f, 'rb').read()
    dosyaEncode = base64.b64encode(dosyaOkuma).decode('UTF-8')
    os.remove(f)
    f=(os.path.splitext(f)[0]+'.txt')
    with open(f, "w") as file:
        file.write(str(dosyaEncode))
    with open(f, "r") as fa:
        liste = [i for i in fa.readlines() if i is not None or len(str(i).strip()) > 0]
    with open(f, "w") as fa:
        for x in liste:
            encoded = x.encode()
            sifreleyici = base64.b64encode(encoded)
            mesaj = sifreleyici.decode()
            x = x.replace(x, mesaj)
            fa.write(x)
    