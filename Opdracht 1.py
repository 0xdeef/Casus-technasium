lijstCijfers = [] #Dit is de lijst waar alle cijfers in staan. Deze is momenteel nog leeg, maar deze wordt gevuld door de gebruiker zodra ze cijfers opgeven voor desbetreffende vak.
vraagDoorgaan = "JA"

vraagVak = input("Voor welk vak wil je een cijfer invoeren? : ") # Hier vraag je de gebruiker voor welk vak ze het gemiddelde willen berekenen.

while vraagDoorgaan != "NEE": # Zolang start gelijk is aan True (start == True) gaat die alles wat hieronder staat herhalen totdat start =/= True oftewel start == False
    vraagCijfer = float(input(f"Welk cijfer heb je voor {vraagVak} behaald? : ")) # Hier vraag je de gebruiker welk cijfer ze voor dit vak hebben behaald. Omdat er float van tevoren staat zorgt dit ervoor dat het ingevoerde getal een comma getal kan zijn.
    vraagWeging = int(input("Wat is de weging van dit cijfer : "))
    if vraagCijfer < 1 or vraagCijfer > 10: # Dit kijkt als de waarde tussen 1 en 10 is. +
        print("De waarde moet tussen de 1 en 10 zijn") # Als bovenstaande uitspraak klopt (vraagCijfer < 1) print dan "ijfer moet minmaal een 1 zijn, probeer opnieuw"
    else: # Als bovenstaande uitspraak niet klopt doe dan dit 
        cijferWaarde = [vraagCijfer] * vraagWeging
        lijstCijfers.extend(cijferWaarde) # Met append die je de ingevoerde cijfers aan de lege lijst toevegen die we bovenaan hebben gedefineerd
        vraagDoorgaan = input(f"Wil je nog een cijfer invoeren voor {vraagVak} (Ja/Nee) : ").upper() # Hier vragen we als we nog een vak willen invoeren. Met .upper() zorg je ervoor dat alle ingevoerde waarde gelijk is en niet bv. ja, Ja, jA of JA. 
        if vraagDoorgaan == "NEE": # Als bovenstaande uitspraak gelijk is aan "NEE" doe dan het volgende 
            minimaalUitrekenen = input(f"Wil je nog invoeren hoeveel cijfers je nog moet ontvangen voor {vraagVak} om minimaal een voldoende te halen (Ja/Nee) : ").upper() # Hier vraag je de gebruiker als hij of zij willen berekenen wat ze minimaal moeten behalen voor de x aantal volgende toetsen.
            if minimaalUitrekenen == "JA": # Als bovenstaande waarde gelijk is aan "JA" voer dan onderstaande uit
                vraagAantalMinmaal = int(input(f"Hoeveel cijfer verwacht je nog voor {vraagVak} : ")) # Vraag de gebruiker hoeveel cijfers ze nog verwacht voor het vak

            
gemiddelde = sum(lijstCijfers) / len(lijstCijfers) # Hier word het gemiddelde berekend 
bestandsLocatie = input("Waar wil je het document opslaan? (Bv: C:\Program Files\Python) : ") #Hier word de gebruiker gevraagd voor de bestandlocatie bv. C:\Users\JohnDoe\Desktop
bestand = open(f"{bestandsLocatie}\cijfers-{vraagVak}.txt", "a") #Hier word een bestandgeopend op bovenstaande locatie met de naam van het vak.

if  minimaalUitrekenen == "NEE": # Als de gebruiker heeft gekozen voor niet het minimaal berekenen van aantal cijfers dan doe onderstaande instructies
    bestand.write(f"Voor {vraagVak} is je gemiddelde {round(gemiddelde, 1)}") #Open het bestand met schrijf rechten en schrijf het vak en wat het gemiddelde is voor dit vak. Rond dit af met 1 cijfer achter de comma.

if minimaalUitrekenen == "JA": # Als de gebruiker wel heeft gekozen voor het berekenen van minimaal cijfer voor x komende toetsen voer onderstaande instructies uit
    aantalcijfers = len(lijstCijfers) + vraagAantalMinmaal # Voeg het al ingvoerde aantal cijfers + verwachte aantal cijfers bij elkaar op om te weten hoeveel cijfers er intotaal zijn.
    aantalPunten = aantalcijfers * 5.5 # Vervolgens het aantal toetsen * 5.5
    rekenen = aantalPunten - sum(lijstCijfers) # Trek het aantal punten van al bekende cijfers af van het totaal minimaal aantal punten
    uitkomst = rekenen / vraagAantalMinmaal # Deel de resterende punten door het nog verwachte cijfers 
    if uitkomst > 10: # Als het minimale cijfer om een voldoende > 10 doe dan onderstaande instructie
        print("Helaas! Je moet hoger dan een 10 halen om gemiddeld een voldoende te hebben") # print "Helaas! Je moet hoger dan een 10 halen om gemiddeld een voldoende te hebben"
    else: # Als vraagMinimaal == True doe dan onderstaande instructie
            bestand.write(f"Voor {vraagVak} is je gemiddelde {round(gemiddelde, 1)}. Als je de komende {vraagAantalMinmaal} toetsen minimaal {round(uitkomst, 1)} behaald heb je een voldoende!") #Open het bestand met schrijf rechten en schrijf het vak en wat het gemiddelde is voor dit vak. Rond dit af met 1 cijfer achter de comma. En wat de gebruiker minimaal moeten halen voor de X aantal toetsen om minimaal een voldoende te scoren

bestand.close() # Sluit het bestand. 
    
print(f"De puntenlijst voor {vraagVak} staat in {bestandsLocatie}") #print waar het bestand is opgeslagen
