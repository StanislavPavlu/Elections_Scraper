# Třetí projekt Engeto Python Akademie - Elections Scraper
----------------------------------------------------------------
## Popis projektu:
Projekt má za úkol extrahovat (scrapovat) vybraná data z webů s výsledky parlamentních voleb v roce 2017.
Program Elections_Scraper.py scrapuje data z jakéhokoliv územního celku a následně je ukládá v požadovaném rozsahu a struktuře do souboru csv.
Výjimka: program není určen pro scrapování územního celku Zahraničí, který má jinou vnitřní strukturu, než všechny ostatní územní celky.
Seznam všech územních celků s možností prokliknutí na další vnitřní struktury (seznam obcí, detail obcí) se nachází zde:
https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

## Použité knihovny:
- Seznam použitých knihoven je uveden v souboru requirements.txt
  
- Knihovny se nainstalují s použitím následujícího příkazu:

       pip install -r requirements.txt

- Instalace knihoven by měla být optimálně provedena do virtuálního prostředí vytvořeného speciálně pro tento projekt.

## Spouštění programu:

- Program Elections_Scraper.py se spouští z příkazové řádky s pomocí dvou povinných systémových argumentů.

- Obecná struktura příkazu pro spuštění:

       python <nazev_souboru.py> <www_odkaz_uzemniho_celku> <název_souboru_csv>

## Rozbor příkazu pro spouštění:

- python - program spouštíme v Pythonu

- Nultý argument - defaultní - název spouštěného python souboru

       např: Elections_Scraper.py

- První argument - povinně zadávaný - www odkaz rozkliknutého vybraného územního celku

       např: územní celek Benešov:

       https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101

- Druhý argument - povinně zadávaný - název souboru csv pro uložení scrapovaných dat

       např: vysledky_benesov.csv

## Běh programu:
Po spuštění program vypisuje jednotlivé řádky souboru csv ve formě slovníků se scrapovanými daty. Každý slovník (řádek vznikajícího souboru csv) představuje data jedné obce vybraného územního celku. Klíče slovníku tvoří záhlaví souboru csv. Po dokončení scrapování program vypíše oznámení, že výsledky jsou připraveny v souboru csv. Vzniklý soubor csv je pak možné otevřít např. v Excelu, kde lze také scrapovaná data prostřednictvím průvodce importovat do graficky přehledného souboru xlsx (Data -> Načíst a transformovat data -> z Text/CSV).

## Ukázka:

V programu Elections_Scraper.py, na konci kódu, jsou v zakomentované formě uvedeny následující dva příklady celého příkazového řádku se všemi argumenty:

- Územní celek Praha:

       python Elections_Scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100' 'vysledky_praha.csv'

- Územní celek Praha-západ:

       python Elections_Scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2110' 'vysledky_praha_zapad.csv'

## Výstup programu na terminálu:

:

![Poslední řádek souboru csv ve formě slovníku + závěrečné oznámení o připraveném souboru csv](URL)

     


