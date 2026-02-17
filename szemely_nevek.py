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
        with open(fajlnev,"r",encoding="utf-8") as nevek:
            
            lista = []
            
            for sor in nevek:
                lista.append(sor.strip())
            
            return lista
        
        
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
    pass


# ============================================================================
# 3. FÜGGVÉNY: CSALÁDNEVEK GYAKORISÁGA
# ============================================================================

def csaladnevek_gyakorisaga(nevek):
    """
    Feladat: Számold meg, melyik családnév hányszor szerepel!
    
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
    pass


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
    pass



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
    nevek_listaja = nevek_betoltese("szemely_nevek.txt")
    
    
    
    
    

    
    # =====================================================
    # 2. Keresztnevek gyűjtése
    # =====================================================
    # TODO: Hívd meg a keresztenevek_gyujtese() függvényt
    # és írasd ki az eredményt
    
    
    # =====================================================
    # 3. Családnevek gyakorisága
    # =====================================================
    # TODO: Hívd meg a csaladnevek_gyakorisaga() függvényt
    # és írasd ki az eredményt    
  
    
    # =====================================================
    # 6. Nevek megfordítása
    # =====================================================
    # TODO: Hívd meg a nevek_megforditasa() függvényt
    # és írasd ki az eredményt
    
    

    
    print("\n" + "=" * 60)
    print("PROGRAM VÉGE")
    print("=" * 60)


# ============================================================================
# PROGRAM INDÍTÁSA
# ============================================================================

if __name__ == "__main__":
    main()