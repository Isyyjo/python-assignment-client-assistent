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

#Lege klantenlijst
klanten = []

#Welkomstbericht
def welkom():
    print("")
    print("Welkom!")
    print("Hier kunt u klanten toevoegen en hun gegevens inzien")
    print("")

#Vraagt aantal klanten
def vraag_aantal_klanten():
    print("Hoe veel klanten wilt u toevoegen?")
    aantal_klanten = int(input())
    return aantal_klanten


#Verzamelt klantgegevens
def verzamel_klant():
    klant = {}
    print("")
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

    klant["naam"] = naam
    klant["leeftijd"] = int(leeftijd)
    klant["besteding"] = besteding
    klant["klanttype"] = klanttype

    klanten.append(klant)

#Print klanten in klantenlijst
def print_klanten():
    for klant in klanten:
        print("-----------")
        print(f"Naam: {klant["naam"]}")
        print(f"Leeftijd: {klant["leeftijd"]}")
        print(f"Bestedingsruimte: {klant["besteding"]}")
        print(f"Klanttype: {klant["klanttype"]}")
        print("-----------")

# Genereert advies voor klant op basis van klantgegevens
def genereer_advies(klant):
    if klant["klanttype"] == "premium":
        return "Intensievere begeleiding (complex dossier)"
    
    elif klant["leeftijd"] >= 67:
        return "AOW-check en extra begeleiding"
    
    elif int(klant["besteding"]) > 100:
        return "Check aanvullende regelingen / samenloop"
    
    else:
        return "Standaard dienstverlening"

#Genereert samenvatting 
def samenvatting(klanten):
    premium = []
    senior = []
    rich = []
    overig = []

    for klant in klanten:
        if genereer_advies(klant) == "Intensievere begeleiding (complex dossier)":
            premium.append(klant)
        elif genereer_advies(klant) == "AOW-check en extra begeleiding":
            senior.append(klant)
        elif genereer_advies(klant) == "Check aanvullende regelingen / samenloop":
            rich.append(klant)
        else:
            overig.append(klant)
    print("SAMENVATTING")
    print("----------")
    print(f"Premium klanten: {len(premium)}")
    print(f"Senior klanten: {len(senior)}")
    print(f"aanvullende klanten: {len(rich)}")
    print(f"Overige klanten: {len(overig)}")
    print("----------")


def main():
    #Welkomstbericht
    welkom()

    #Vraag aantal klanten
    aantal_klanten = vraag_aantal_klanten()

    #Verzamel klantgegevens
    while len(klanten) < aantal_klanten:   
        verzamel_klant()
    print("")

    #Print klantgegevens
    print_klanten()
    print("")

    #print advies voor klanten
    for klant in klanten:
        print(f"ADVIES: {genereer_advies(klant)}")
    print("")

    #toon samenvatting
    samenvatting(klanten)
    
    print("")
    print("KlantAssistent gestart (WerkZeker Nederland)")

if __name__ == "__main__":
    main()
