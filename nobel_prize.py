import requests

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

# Tip: use the page below to see what data we get back and how the api works
# we only use /nobelPrizes
# Documentation, help and tools for testing the api can be found here: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1


# HELP_STRING = """
# Ange ett år och fält
# Exempelvis 1965 fysik
# """

HELP_STRING = """
1) Write a year and field 
Example 1965 physics
2) If you are not sure for the fields, select this
Q) quit
H) help
"""

cat = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}

# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# TODO 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med till apiet och vi får då alla priser det året
"--------------------------------------"


# TODO 10p the program should give a helpful output instead of a crash if the user enters the wrong input
# TODO 15p if the user does not specify a field such as physics or chemistry, then that parameter should not be sent to the api and we will then receive all the prizes for that year


def main():
    print(HELP_STRING)

    while True:
        menu_choice = input("Make a choice? \n(You can enter 1,2,h(H) or q(Q)) ").upper().strip()
        # TODO 5p Skriv bara ut hjälptexten en gång när programmet startar inte efter varje gång användaren matat in en fråga
        #      Förbättra hjälputskriften så att användaren vet vilka fält, exempelvis kemi som finns att välja på

        # TODO 5p Gör så att det finns ett sätt att avsluta programmet, om användaren skriver Q så skall programmet stängas av
        #      Beskriv i hjälptexten hur man avslutar programmet
        # TODO 5p Gör så att hjälptexten skrivs ut om användaren skriver h eller H
        "---------------------------------------"

        # TODO 5p Only print the help text once when the program does not start after each time the user enters a question
        # Improve the help printout so that the user knows which fields, for example chemistry, are available to choose from

        # TODO 5p Make sure there is a way to terminate the program, if the user types Q the program should be shut down
        # Describe in the help text how to end the program
        # TODO 5p Make the help text printed if the user types h or H

        if menu_choice == '1':
            aaa = input(">")
            a, b = aaa.split()

            if b not in cat:
                print("You should print correct field.\n You can find the fields select 2")
            else:
                c = cat[b]
                c = {"nobelPrizeYear": int(a), "nobelPrizeCategory": c}

                res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=c).json()
                # TODO 5p  Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------

                # TODO 20p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
                #   Skriv ut med tre decimalers precision. exempel 534515.123
                #   Skapa en funktion som hanterar uträkningen av prispengar och skapa minst ett enhetestest för den funktionen
                #   Tips, titta på variabeln andel
                # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde

                for p in res["nobelPrizes"]:
                    peng = p["prizeAmount"]
                    idagpeng = p["prizeAmountAdjusted"]
                    print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")

                    for m in p["laureates"]:
                        print(m['knownName']['en'])
                        print(m['motivation']['en'])
                        andel = m['portion']
        if menu_choice == '2':
            print("Here, you can see the fields")
            for item in cat:
                print(item)
            continue
        if menu_choice.upper() == 'H':
            print(HELP_STRING)
            continue

        if menu_choice.upper() == 'Q':
            print("Good bye and have a nice day!")
            return


if __name__ == '__main__':
    main()