cisla = list(range(10, 0, -1)) + list(range(4, 0, -1)) + [1]

vety = [
    "zelených láhví stojí na stole a jedna spadne",
    "zelené lahve stojí na stole a jedna spadne",
    "zelená láhev stojí na stole a jedna spadne"
]

for cislo in cisla:
    if cislo == 1:
        print(f"{cislo} {vety[2]}")
    elif cislo % 10 in [2, 3, 4]:
        print(f"{cislo} {vety[1]}")
    else:
        print(f"{cislo} {vety[0]}")

# range(start, stop, step) je vestavěná funkce v Pythonu, která generuje postupnost čísel od start (včetně) do stop (vyjma), s krokem step. V případě, že step není specifikováno, předpokládá se hodnota 1.

#V kódu, který jste poskytl, se používá range ke generování dvou oddělených postupností čísel a ty jsou následně spojeny pomocí operátoru +. Výsledkem je jeden seznam čísel obsahující prvky z obou postupností.

#Zde je konkrétní vysvětlení:

 #   Seznam čísel od 10 do 1 (včetně) se krokem -1:

  #  python

#list(range(10, 0, -1))

#Tato část kódu vytváří seznam čísel od 10 do 1 (včetně) s krokem -1, což znamená, že čísla se snižují o 1 s každým prvkem. Výsledkem je seznam [10, 9, 8, 7, 6, 5, 4, 3, 2, 1].

#Seznam čísel od 4 do 1 (včetně) se krokem -1:

#python

#list(range(4, 0, -1))

#Tato část kódu vytváří seznam čísel od 4 do 1 (včetně) s krokem -1. Výsledkem je seznam [4, 3, 2, 1].

#Spojení obou seznamů a přidání čísla 1:

#python

 #   cisla = list(range(10, 0, -1)) + list(range(4, 0, -1)) + [1]

  #  Tímto krokem jsou oba výše uvedené seznamy spojeny dohromady pomocí operátoru +. Poté je přidáno číslo 1 do vytvořeného seznamu. Výsledkem je jediný seznam, který obsahuje prvky z obou původních postupností a číslo 1 na konci: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 4, 3, 2, 1, 1].

