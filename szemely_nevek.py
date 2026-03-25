"""
NÉVKEZELŐ PROGRAM - FELADATOK
Készítsd el a függvényeket a névlista kezeléséhez!
"""

# ============================================================================
# 1. FÜGGVÉNY: NEVEK BETÖLTÉSE TXT-FÁJLBÓL
# ============================================================================

def nevek_betoltese(fajlnev):
    """
    Feladat: Töltsd be a neveket a megadott txt-fájlból!
    
    A fájl minden sorában egy név szerepel (pl. "András Kovács").
    Olvasd be a sorokat, és tárold őket egy listában.
    
    Paraméterek:
        fajlnev (str): A beolvasandó fájl neve
    
    Visszatérési érték:
        list: A neveket tartalmazó lista
    """
    # TODO: Implementáld a fájlbeolvasást
    try:
        with open(fajlnev, encoding="utf-8") as falj:
            
            nevek = falj.readlines()
            
            
            return nevek
        
        
    except IOError as nev:
        print(f"probléma van a falj megnitással {nev}")


# ============================================================================
# 2. FÜGGVÉNY: KERESZTNEVEK LISTÁZÁSA
# ============================================================================

def keresztenevek_gyujtese(nevek):
    """
    Feladat: Gyűjtsd ki az összes keresztnevet (az első keresztnevet)!
    
    Példa: ["András Kovács", "Anna Mária Szabó"] -> ["András", "Anna"]
    
    Paraméterek:
        nevek (list): A nevek listája
    
    Visszatérési érték:
        list: A keresztnevek listája
    """
    # TODO: Implementáld a függvényt
    keresztnev = []
    
    
    for nev in nevek:
        kn = nev.split(' ')[0]
        
        if kn not in keresztnev:
            keresztnev.append(kn)
    
    return keresztnev        


# ============================================================================
# 3. FÜGGVÉNY: leggyakoribb családnév
# ============================================================================

def csaladnevek_gyakorisaga(nevek):
    """
    Feladat: Számold meg, melyik a leggyakoribb családnév!
    
    Használj két listát: egyiket a családneveknek, másikat a darabszámoknak!
    
    Példa: ["András Kovács", "Anna Szabó", "Balázs Kovács"] 
            -> csaladnevek: [["Kovács", 2],
                             ["Szabó", 1]
                            ]
    
    Paraméterek:
        nevek (list): A nevek listája
    
    Visszatérési érték:
        tuple: (csaladnevek_listaja, darabszamok_listaja)
    """
    # TODO: Implementáld a függvényt
    csaladnev = []
    
    
    
    for nev in nevek:
        vn = nev.split()[-1]
        
        i = 0
        while i < len(csaladnev) and csaladnev[i][0] != vn:
            i += 1
        
        if i <len(csaladnev):
            csaladnev[i][1] += 1
        else:
            csaladnev.append([vn,1])
    
    """for csn in csaladnev:
        print(f"{csn[0]}: {csn[1]}")"""

    maxi = 0
    max_ertek = csaladnev[0][1]
    
    
    for i in range(1, len(csaladnev)):
        if max_ertek <  csaladnev[i][1]:
            maxi = i
            max_ertek = csaladnev[i][1]
            
    return  csaladnev[maxi][0]

# ============================================================================
# 6. FÜGGVÉNY: NEVEK MEGFORDÍTÁSA
# ============================================================================

def nevek_megforditasa(nevek):
    """
    Feladat: Cseréld meg a kereszt- és családnevek sorrendjét minden névben!
    
    Példák:
        "András Kovács" -> "Kovács András"
        "Anna Mária Szabó" -> "Szabó Anna Mária"
    
    Paraméterek:
        nevek (list): Az eredeti nevek listája
    
    Visszatérési érték:
        list: A megfordított nevek listája
    """
    # TODO: Implementáld a függvényt
    uj_nevek=[]
    for nev in nevek:
        nev_reszek = nev.split(' ')
        #Verzió 1:
        
        
        # seged = nev_reszek[0]
        # nev_reszek[0] = nev_reszek[-1]
        # nev_reszek[-1] = seged
        
        
        #Verzió 2:
        nev_reszek[0], nev_reszek[1] = nev_reszek[-1], nev_reszek[0]
        uj_nevek.append(" ".join(nev_reszek))
    
    
    return uj_nevek


# ============================================================================
# FŐPROGRAM - INNEN HÍVJUK MEG A FÜGGVÉNYEKET
# ============================================================================

def main():
    # Főprogram
    
    print("=" * 60)
    print("NÉVKEZELŐ PROGRAM - FÜGGVÉNYEK TESZTELÉSE")
    print("=" * 60)
    
    
    # =====================================================
    # 1. Nevek betöltése
    # =====================================================
    # TODO: Hívd meg a nevek_betoltese() függvényt a "nevek.txt" fájllal
    nev_lista = nevek_betoltese("Prog2025/szemely_nevek.txt")
    # print(nev_lista)
    
    
    
    

    
    # =====================================================
    # 2. Keresztnevek gyűjtése
    # =====================================================
    # TODO: Hívd meg a keresztenevek_gyujtese() függvényt
    # és írasd ki az eredményt
    keresztenevek_listaja =keresztenevek_gyujtese(nev_lista)
    #print(keresztenevek_listaja)
    
    # =====================================================
    # 3. Családnevek gyakorisága
    # =====================================================
    # TODO: Hívd meg a csaladnevek_gyakorisaga() függvényt
    # és írasd ki az eredményt    
    print(f"A leggyakoribb családnév:{csaladnevek_gyakorisaga(nev_lista)}")
    
    
    # =====================================================
    # 6. Nevek megfordítása
    # =====================================================
    # TODO: Hívd meg a nevek_megforditasa() függvényt
    # és írasd ki az eredményt
    lista = nevek_megforditasa(nev_lista)
    for le  in lista:
        print(le)
    

    
    print("\n" + "=" * 60)
    print("PROGRAM VÉGE")
    print("=" * 60)


# ============================================================================
# PROGRAM INDÍTÁSA
# ============================================================================

if __name__ == "__main__":
    main()