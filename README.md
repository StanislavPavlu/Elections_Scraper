Třetí projekt Engeto Python Akademie - Elections Scraper
----------------------------------------------------------------
Popis projektu:
Projekt má za úkol extrahovat (scrapovat) vybraná data z webů s výsledky parlamentních voleb v roce 2017.
Program Elections_Scraper.py scrapuje data z jakéhokoliv územního celku a následně je ukládá v požadovaném rozsahu a struktuře do souboru csv.
Výjimka: program není určen pro scrapování územního celku Zahraničí, který má jinou vnitřní strukturu, než všechny ostatní územní celky.
Seznam všech územních celků s možností prokliknutí na další vnitřní struktury (seznam obcí, detail obcí) se nachází zde:
https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

Použité knihovny:
Seznam použitých knihoven je uveden v souboru requirements.txt.
Knihovny se nainstalují s použitím následujícího příkazu:
pip install -r requirements.txt
Instalace knihoven by měla být optimálně provedena do virtuálního prostředí vytvořeného speciálně pro tento projekt.

Spouštění programu:
Program Elections_Scraper.py se spouští z příkazové řádky s pomocí dvou povinných systémových argumentů.
Obecná struktura příkazu pro spuštění:
python <nazev_souboru.py> <www_odkaz_uzemniho_celku> <název_souboru_csv>
Rozbor příkazu pro spouštění:
python ...........  program spouštíme v Pythonu
0. argument: .....  defaultní - název spouštěného python souboru
                    např: Elections_Scraper.py
1. argument: .....  povinně zadávaný - www odkaz rozkliknutého vybraného územního celku
                    např: územní celek Benešov:
                    https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
2. argument: .....  povinně zadávaný - název souboru csv pro uložení scrapovaných dat
                    např: vysledky_benesov.csv

Běh programu:
Po spuštění program vypisuje jednotlivé řádky souboru csv ve formě slovníků se scrapovanými daty. Každý slovník (řádek vznikajícího souboru csv) představuje data jedné obce vybraného územního celku. Klíče slovníku tvoří záhlaví souboru csv. Po dokončení scrapování program vypíše oznámení, že výsledky jsou připraveny v souboru csv. Vzniklý soubor csv je pak možné otevřít např. v Excelu, kde lze také scrapovaná data prostřednictvím průvodce importovat do graficky přehledného souboru xlsx (Data -> Načíst a transformovat data -> z Text/CSV).

Ukázka:
V programu Elections_Scraper.py, na konci kódu, jsou v zakomentované formě uvedeny následující dva příklady celého příkazového řádku se všemi argumenty:
Územní celek Praha:
python Elections_Scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100' 'vysledky_praha.csv'
Územní celek Praha-západ:
python Elections_Scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2110' 'vysledky_praha_zapad.csv'

Výstup programu na terminálu - poslední řádek souboru csv ve formě slovníku + závěrečné oznámení o připraveném souboru csv:
======================================================================
{'Kód obce': '539899', 'Název obce': 'Praha-Zličín', 'Voliči v seznamu': '4 079', 'Vydané obálky': '2 826', 'Platné hlasy': '2 801', 'Občanská demokratická strana': '472', 'Řád národa - Vlastenecká unie': '1', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI': '0', 'Česká str.sociálně demokrat.': '111', 'Volte Pr.Blok www.cibulka.net': '2', 'Radostné Česko': '0', 'STAROSTOVÉ A NEZÁVISLÍ': '169', 'Komunistická str.Čech a Moravy': '125', 'Strana zelených': '33', 'ROZUMNÍ-stop migraci,diktát.EU': '15', 'Společ.proti výst.v Prok.údolí': '4', 'Strana svobodných občanů': '50', 'Blok proti islam.-Obran.domova': '2', 'Občanská demokratická aliance': '6', 'Česká pirátská strana': '490', 'OBČANÉ 2011-SPRAVEDL. PRO LIDI': '1', 'Unie H.A.V.E.L.': '0', 'Referendum o Evropské unii': '2', 'TOP 09': '347', 'ANO 2011': '623', 'Dobrá volba 2016': '1', 'SPR-Republ.str.Čsl. M.Sládka': '2', 'Křesť.demokr.unie-Čs.str.lid.': '131', 'Česká strana národně sociální': '0', 'REALISTÉ': '33', 'SPORTOVCI': '5', 'Dělnic.str.sociální spravedl.': '4', 'Svob.a př.dem.-T.Okamura (SPD)': '166', 'Strana Práv Občanů': '6'}
======================================================================
*** TABULKA "vysledky_praha.csv" JE PŘIPRAVENA ***
======================================================================



