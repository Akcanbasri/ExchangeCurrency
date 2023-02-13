import os
from datetime import datetime

"""# istediğin dizine gitmeni sağlar
os.chdir("C:/Users/Lenova/Desktop")"""

"""# Konum belirtir
print(os.getcwd())"""

"""# bulunduğu yerin içinde bulunan dosyaları listeler
for i in os.listdir():
    print(i)"""

"""# tek dosya oluşturur bulunduğu konumda
os.mkdir("Deneme1")"""

"""# iç içe dosya oluşturur bulunduğu konumda
os.makedirs("Denem2/Deneme3")"""

"""# Deneme2 altında deneme3 ü siler
os.rmdir("Denem2/Deneme3")"""

"""#tekrar deneme3 oluşur
os.mkdir("Denem2/Deneme3")
"""

"""# Deneme1 silinir
os.rmdir("Deneme1")"""

"""# Al kloserleri siler
os.removedirs("Denem2/Deneme3")"""

"""# dosyanın ismini değiştirir.
os.rename("text.txt", "test2.txt")"""

"""# test2 nin bilgisayarda tutulan tüm bilgilerini verir
print(os.stat("test2.txt"))"""

"""# test2 nin bilgisayarda bulunan değişme saatini alır
print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))"""

"""# Girilen path içinde bulunan tüm .txt dosyaları görmemizi sağlıyor.
for klasor_yolu, klasor_ismi, dosya_ismi in os.walk("C:/Users/Lenova/Desktop"):
    for i in dosya_ismi:
        if i.endswith(".txt"):
            print(i)"""

mp4_list = list()
text_list = list()
pdf_list = list()

for klasor_yolu, klasör_ismi, dosya_ismi in os.walk("C:/Users/Lenova/Desktop"):
    for i in dosya_ismi:
        if i.endswith(".py"):
            with open("Python.txt", "w", encoding="utf-8") as file:
                file.write(i + "\n")

        elif i.endswith(".txt"):
            with open("Text.txt", "w", encoding="utf-8") as file:
                file.write(i + "\n")

        elif i.endswith(".pdf"):
            with open("Pdf.txt", "w", encoding="utf-8") as file:
                file.write(i + "\n")
