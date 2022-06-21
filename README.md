# Simplified Minesweeper (Zjednodušená verzia hry "Hľadanie Mín")

* Hru zapnite cez dokument main.py

* Pravidla hry:
  - Hráč zadá veľkosť hracej plochy (program ho nepustí ďalej kým nesplní podmienku size >= 5)
  - Hráč ma na výber z dvoch akcií - odhaliť políčko alebo označiť/odznačiť políčko ako mínu (program ho nepustí ďalej kým nezadá buď **'u'** (uncover) alebo **'m'** (mark) )
  - Hra vždy vyzve hráča, aby zadal súradnice políčka, ktoré chce odhaliť alebo označiť/odznačiť (ak hráč zadá neplatné súradnice hra ho na to upozorní)
  - Ak hráč odhalí všetky políčka s číslami vyhráva hru
  - Ak hráč odhalí políčko s mínou prehráva hru a odhalí sa mu celá hracia plocha
  - Ak hráč odhalí políčko s číslom 0 odhalia sa všetky susedné políčka (ak je susedné políčko opäť 0 hráč musí jej susedné políčka odhaliť sám alebo zadať súradnice tohto políčka v ďalšom kroku)
