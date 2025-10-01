try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        f =fajl.read()
        n=4/0
        print(n)
        print(f) 
except Exception as ex:
    print(f"halihóóó! hiba oka! {ex}")
except FileNotFoundError:
    print(" Hiba a fájl  megnyitsa közben")
except ZeroDivisionError:
    print("Ne ossz 0-val")
  
print("itt a program vége")