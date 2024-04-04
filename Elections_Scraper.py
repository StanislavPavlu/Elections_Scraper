# Identification:
"""
Elections Scraper.py: third project for Engeto Online Python Akademie
author: Stanislav Pavlů
email: standic@seznam.cz
discord: Standa P. (standa_40063)
"""

# Import modules:
import pprint
import sys
import requests
from bs4 import BeautifulSoup
import csv

def main() -> None:
    '''Main function of the program'''

def vyzobej_kody_obci(soup) -> list:
    '''User function to select all municipality codes'''
    kody_obci = soup.find_all("td", {"class": "cislo"})
    return [item.get_text() for item in kody_obci]
        
def vyzobej_nazvy_obci(soup) -> list:
    '''User function to select all municipality names'''
    nazvy_obci = soup.find_all("td", {"class": "overflow_name"})
    return [item.get_text() for item in nazvy_obci]
    
def vyzobej_odkazy_obci(soup) -> list:
    '''User function to select all municipality web links'''
    odkazy_obci = soup.find_all("td", {"class": "cislo", "headers": ["t1sb1", "t2sb1", "t3sb1"]})
    a_tags = [item.find("a") for item in odkazy_obci]
    return ["https://volby.cz/pls/ps2017nss/"+item["href"] for item in a_tags]
    
def vyzobej_odkazy_okresu() -> list:
    '''User function to select all district web links'''
    cr_url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    cr_odpoved = requests.get(cr_url)
    cr_soup = BeautifulSoup(cr_odpoved.text, "html.parser")
    headers = ["t1sa3", "t2sa3", "t3sa3", "t4sa3", "t5sa3", "t6sa3", "t7sa3", 
               "t8sa3", "t9sa3", "t10sa3", "t11sa3", "t12sa3", "t13sa3", "t14sa3"]
    odkazy_okresu = cr_soup.find_all("td", {"headers": headers})
    a_tags = [item.find("a") for item in odkazy_okresu]
    return ["https://volby.cz/pls/ps2017nss/"+item["href"] for item in a_tags]
    
def vyzobej_nazvy_stran(soup) -> list:
    '''User function to select names of all political parties'''
    nazvy_stran = soup.find_all("td", {"class": "overflow_name"})
    return [item.get_text() for item in nazvy_stran]
    
def vyzobej_hlasy_stran(soup) -> list:
    '''User function to select numbers of votes of all political parties'''
    hlasy_stran = soup.find_all("td", {"class": "cislo", "headers": ["t1sb3", "t2sb3"]})
    return [uprava_cisla(item) for item in hlasy_stran]
    
def uprava_cisla(tag) -> str:
    '''User function to replace non-breaking space ("\xa0") in mumbers with normal space (" ")'''
    return tag.get_text().replace("\xa0", " ")

obec_radek = dict()
hlavicka = True
cara, hvezdy = 70 * "=", 3 * "*"
odkazy_okresu_list = vyzobej_odkazy_okresu()

try:
    okres_url = sys.argv[1]
    okres_odpoved = requests.get(okres_url)
    okres_soup = BeautifulSoup(okres_odpoved.text, "html.parser")
    csv_soubor = open(sys.argv[2], mode = "w", encoding = "utf-8-sig", newline = "")
    
except IndexError:
    print(f'''{cara}\n{hvezdy} NESPRÁVNÝ POČET ARGUMENTŮ {hvezdy}
1. argument: zadejte webový odkaz vybrané územní úrovně.
2. argument: zadejte název souboru .csv pro scrapování dat.\n{cara}''')
    exit()

else:
    if not sys.argv[1] in odkazy_okresu_list or "ps36" in sys.argv[1]:
        print(f'''{cara}\n{hvezdy} NESPRÁVNĚ ZADANÝ PRVNÍ ARGUMENT {hvezdy}
Zadejte webový odkaz vybrané územní úrovně.\n{cara}''')
        exit()
    if not sys.argv[2].endswith(".csv"):
        print(f'''{cara}\n{hvezdy} NESPRÁVNĚ ZADANÝ DRUHÝ ARGUMENT {hvezdy}
Zadejte název souboru .csv pro scrapování dat.\n{cara}''')
        exit()

kody_obci_list = vyzobej_kody_obci(okres_soup)
nazvy_obci_list = vyzobej_nazvy_obci(okres_soup)
odkazy_obci_list = vyzobej_odkazy_obci(okres_soup)

for kod, nazev, odkaz in zip(kody_obci_list, nazvy_obci_list, odkazy_obci_list):
    
    obec_radek["Kód obce"] = kod
    obec_radek["Název obce"] = nazev
        
    obec_odpoved = requests.get(odkaz)
    obec_soup = BeautifulSoup(obec_odpoved.text, "html.parser")
    
    obec_radek["Voliči v seznamu"] = uprava_cisla(obec_soup.find("td", {"headers": "sa2"}))
    obec_radek["Vydané obálky"] = uprava_cisla(obec_soup.find("td", {"headers": "sa3"}))
    obec_radek["Platné hlasy"] = uprava_cisla(obec_soup.find("td", {"headers": "sa6"}))

    nazvy_stran_list = vyzobej_nazvy_stran(obec_soup)
    hlasy_stran_list = vyzobej_hlasy_stran(obec_soup)
        
    for strana, hlas in zip(nazvy_stran_list, hlasy_stran_list):
        obec_radek[strana] = hlas
     
    print(f"{obec_radek}\n{cara}")
    
    zapisovac = csv.DictWriter(csv_soubor, fieldnames = obec_radek.keys(), delimiter = ';')
    if hlavicka:
        zapisovac.writeheader()
        zapisovac.writerow(obec_radek)
        hlavicka = False
    else:
        zapisovac.writerow(obec_radek)
     
csv_soubor.close()
print(f"{hvezdy} TABULKA \"{sys.argv[2]}\" JE PŘIPRAVENA {hvezdy}\n{cara}")

if __name__ == '__main__':
    main()

# Ukázky spouštění s argumenty z příkazového řádku - územní okrsky Praha a Praha-západ:
# python Elections_Scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100' 'vysledky_praha.csv'
# python Elections_Scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2110' 'vysledky_praha_zapad.csv'

# print("Odkazy okresů list:")
# pprint.pprint(odkazy_okresu_list)
# print(len(odkazy_okresu_list))

# print("Kódy obcí list:")
# pprint.pprint(kody_obci_list)
# print(len(kody_obci_list))

# print("Názvy obcí list:")
# pprint.pprint(nazvy_obci_list)
# print(len(nazvy_obci_list))

# print("Odkazy obcí list:")
# pprint.pprint(odkazy_obci_list)
# print(len(odkazy_obci_list))

# print("Názvy stran list:")
# pprint.pprint(nazvy_stran_list)
# print(len(nazvy_stran_list))

# print("Hlasy stran list:")
# pprint.pprint(hlasy_stran_list)
# print(len(hlasy_stran_list))