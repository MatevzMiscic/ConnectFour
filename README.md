# Štiri v vrsto

## Zagon
Povprečen uporabnik naj za uporabo programa zažene `spletni_vmesnik.py`.  
Heker lahko nameto tega zažene tekstovni vmesnik, to je `interface.py`.

## Uporaba

### Spletni vmesnik
Spletni vmesnik je zelo preprost. Na vstopni strani so nastavitve. Uporabnik si lahko izbere velikost igralnega polja (višino in širino) in 
koliko žetonov v vrsti mora igralec doseči za zmago. Poleg tega se lahko odloči, kdo upravlja katerega od igralcev, to je lahko človek ali računalnik.
Vsaj eden od obeh igralcev mora biti človek. Po vsaki spremembi nastavitev je potrebno pritisniti gumb ***"Apply"***, sicer se nastavitve ne bodo shranile.
Ko je uporabnik zadovoljen z nastavitvami, lahko pritisne gumb ***"Play"***, da se igra začne.  
Med igro je v levem zgornjem kotu napis, ki obvešča o tem, kdo je na potezi oziroma kdo je zmagal, če je igre že konec.
Pod tem so gumbi, s katerimi se lahko uporabnik vrne na začetno stran, začne novo igro ali pa razveljavi zadnjo potezo.
Pod gumbi je še rezutat, ki pove koliko iger je zmagal kateri igralec.  
**Igralec naredi potezo tako, da pritisne na žeton nad stolpcem, v katerega želi odigrati svojo potezo.**

### Tekstovni vmesnik
V osnovnem meniju lahko uporabnik izbira med opcijami ***"igraj"***, ***"nastavitve"*** in ***"izhod"***. 
V nastavitvah lahko nastavi iste stvari kot pri spletnem vmesniku, edina razlika je, da lahko tu oba igralca upravlja računalnik.  
**Med igro lahko igralec odigra potezo tako, da vpiše številko stolpca v katerega, želi spustiti žeton.** 
Stolpci so označeni po vrsti od leve proti desni s števili od 1 naprej.

## Pravila igre štiri v vrsto
Igralca izmenjujoče mečeta žetone v polje velikosti 7 x 6. Prvi igralec ima žetone rdeče barve, drugi pa žetone rumene barve. 
Tisti, ki prvi doseže štiri zaporedne žetone v isti vrstici, stolpcu ali na isti diagonali, je zmagal.
Če to ne uspe nikomur in je zasedeno celotno polje, je izenačeno.