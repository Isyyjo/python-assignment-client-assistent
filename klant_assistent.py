"""
CODE KICKSTART — KlantAssistent (WerkZeker Nederland)
-----------------------------------------------------

Context: 
Dit project is onderdeel van de training Code Kickstart.
Je bouwt een eenvoudige Python applicatie die gegevens van burgers/aanvragers verwerkt
en op basis daarvan één advieslabel genereert.

De tool is beslisondersteunend: het advies is een intern signaal voor de medewerker.
De tool voert geen acties uit, kent geen rechten toe en neemt geen echte besluiten.

Doel:
- Oefenen met Python fundamentals (variables, types, if/elif/else, loops)
- Denken in iteraties
- Vertalen van pseudocode naar Python
- Structureren met dicts/lists en functies (parameters + return)

Spelregels:
- Werk stap voor stap
- Test elke iteratie
- Houd de code leesbaar
- Werk toe naar een werkende terminal-applicatie
"""

print("OUTPUT HELLO")

#global variables
klanten = []


def verzamel_klant():
    klantgegevens = {}
    print("Hallo, nieuwe klant!")
    print("Wij hebben een aantal gegevens van u nodig.")

    print("Wat is uw naam?")
    naam = input()

    print("Wat is uw leeftijd?")
    leeftijd = input()
    while not leeftijd.isdigit():
        print("ERROR: voer een geldige leeftijd in")
        leeftijd = input()

    print("Wat is uw bestedingslimiet per maand (in euro's)?")
    besteding = input()

    print("Wat is uw klanttype: nieuw, bestaand of premium?")
    klanttype = input()
    while klanttype not in ["nieuw", "bestaand", "premium"]:
        print(" ERROR: niet bestaand klanttype")
        klanttype = input()

    klantgegevens["naam"] = naam
    klantgegevens["leeftijd"] = leeftijd
    klantgegevens["besteding"] = besteding
    klantgegevens["klanttype"] = klanttype

    klanten.append(klantgegevens)

def print_klanten():
    for klant in klanten:
        print("-----------")
        print(f"Naam: {klant["naam"]}")
        print(f"Leeftijd: {klant["leeftijd"]}")
        print(f"Bestedingsruimte: {klant["besteding"]}")
        print(f"Klanttype: {klant["klanttype"]}")
        print("-----------")

verzamel_klant()
print_klanten()

def genereer_advies(klant):
    """
    Ontvangt één klant (dictionary) en retourneert één advieslabel (string).

    Advieslabels (exact deze strings gebruiken):
    - 'AOW-check en extra begeleiding'
    - 'Check aanvullende regelingen / samenloop'
    - 'Intensievere begeleiding (complex dossier)'
    - 'Standaard dienstverlening'

    Regels + prioriteit (hoog -> laag):
    1) Klanttype == 'premium' -> 'Intensievere begeleiding (complex dossier)'
    2) Leeftijd >= 67         -> 'AOW-check en extra begeleiding'
    3) Besteding > 100        -> 'Check aanvullende regelingen / samenloop'
    4) Anders                 -> 'Standaard dienstverlening'

    Denkstappen:
    1. Lees waarden uit de dictionary
    2. Gebruik if / elif / else in de juiste volgorde (prioriteit)
    3. Return één advieslabel
    """
    # TODO: implementeer deze functie
    pass


def samenvatting(klanten):
    """
    Print een samenvatting van alle klanten en adviezen.

    Verwachting (minimaal):
    - Print het aantal klanten
    - Print per advieslabel hoe vaak deze voorkomt

    Denkstappen:
    1. Loop over de lijst met klanten
    2. Bepaal per klant het advies (gebruik genereer_advies)
    3. Tel de adviezen (bijv. met een dict)
    4. Print het overzicht netjes
    """
    # TODO: implementeer deze functie
    pass


def main():
    """
    Hoofdprogramma van de applicatie.

    Programmaflow (pseudocode):
    1. Print startbericht
    2. Vraag hoeveel klanten worden ingevoerd (moet int zijn)
    3. Maak een lege lijst voor klanten
    4. Gebruik een loop om klanten te verzamelen (verzamel_klant)
    5. Print per klant het advieslabel (genereer_advies)
    6. Toon een samenvatting (samenvatting)
    """
    print("KlantAssistent gestart (WerkZeker Nederland)")

    # TODO: implementeer de hoofdlogica
    pass


if __name__ == "__main__":
    main()
