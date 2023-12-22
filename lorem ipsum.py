import random

slabiky = [
   "su", "lenc", "lé", "to", "ro", "hy", "pí", "seň", "ká", "vav",
    "vo", "ad", "klíč", "fí", "lam", "cy", "kal", "ti", "si", "ka",
    "ryc", "lík", "brý", "le", "plá", "ž", "lé", "ladt", "o",
    "ja", "ko", "bl", "stů", "l", "ští", "šte", "hra", "čka", "š",
    "ka", "lo", "hra", "čka", "ko", "c", "ka", "řu", "že", "klo",
    "bouk", "ví", "o", "ry", "ba", "š", "tíš", "dům", "po",
    "čta", "čí", "klo", "bou", "ví", "tr", "po", "dha", "ká",
    "kyar", "t", "hu", "bda", "š", "ka", "lo", "kha","či",
    "tě", "mi", "li", "ní", "ký", "ší", "di", "ní", "ra", "ma"
]
#generace proměnných
min_pocet_slabik = int(input("min počet slabik ve slově: "))
max_pocet_slabik = int(input("max počet slabik ve slově: "))
slov_ve_vete = int(input("kolik slov ve větě? "))
pocet_slov = int(input("Zadej kolik slov potrebujes:"))
# definuji hlavní kod pro pozdější jednodušší použití
def generace_slova():
    nahodne_slovo = ''
    #řeší chybu uživatele, když se splní podmínka, kod pokračuje 
    if min_pocet_slabik < max_pocet_slabik:
        pocet_slabik_dva = random.randint(min_pocet_slabik, max_pocet_slabik)
    else:
        print("Error, max počet slabik je menší nebo stejný, jak min počet slabik.")
            
    #tvoří slovo, zároveň přidává tečku na zvolenou délku věty. 
    for a in range(pocet_slabik_dva):  
        nahodne_slovo += random.choice(slabiky)

    if (i + 1) % slov_ve_vete == 0:
         return nahodne_slovo + "."
    else :
         return nahodne_slovo 
 #seznam pro dokončené věty   
dokoncene_vety_seznam = []  
#počet slov
for i in range(pocet_slov):
     
    dokoncene_vety_seznam.append(generace_slova())
#přidává mezeru mezi slova
vysledek = ' '.join(dokoncene_vety_seznam)
print(vysledek)