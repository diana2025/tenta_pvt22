import requests

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1


# HELP_STRING = """
# Ange ett år och fält
# Exempelvis 1965 fysik
# """

HELP_STRING = """
1) Ange ett år och fält 
Exempelvis 1965 fysik
Q) Quit
H) Hjälp
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


# calculation money for each prize
#  variables: money:total money
#             prize_cnt : awarded person's count
def calcMoneyForEachPrize(money: float, prize_cnt: float) -> float:
    average_money = money / prize_cnt
    res = round(average_money, 3)
    return res


# check if the field is correct
def checkfield(field: str) -> bool:
    if field not in cat:
        return False
    else:
        return True


# def get prizers from year and field
def getInforamationFromServer(year: int, field: str):
    params = {"nobelPrizeYear": year, "nobelPrizeCategory": cat[field]}
    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=params).json()
    return res


# print the result
def printResult(peng: float, idagpeng: float, prize_cnt: int):
    print("*" * 30)
    money_for_thattime = calcMoneyForEachPrize(peng, prize_cnt)
    result1 = f'{money_for_thattime:.3f}'
    print(f"The money of the time for each prizer is {result1}")

    money_for_now = calcMoneyForEachPrize(idagpeng, prize_cnt)
    result2 = f'{money_for_now:.3f}'
    print(f"The Today's value for each prizer is {result2}")


# print for year and field
def printOneFieldForYear(year: int, field: str):
    res = getInforamationFromServer(int(year), field)

    for p in res["nobelPrizes"]:
        print("----------------------------")
        peng = p["prizeAmount"]
        idagpeng = p["prizeAmountAdjusted"]
        print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")
        prize_cnt = 0

        for m in p["laureates"]:
            print("----------------------------")
            if "knownName" in m:
                print(m['knownName']['en'])
            print(m['motivation']['en'])
            andel = m['portion']
            prize_cnt += 1
        printResult(peng, idagpeng, prize_cnt)


# print all informations for year
def printAllInformationsForYear(year: int):
    for item in cat:
        print("*" * 30)
        print(f"Field is {item}")
        res = getInforamationFromServer(int(year), item)

        for p in res["nobelPrizes"]:
            print("----------------------------")
            peng = p["prizeAmount"]
            idagpeng = p["prizeAmountAdjusted"]
            print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")
            print(f"{p['categoryFullName']['se']} prissumma {idagpeng} SEK")
            prize_cnt = 0

            for m in p["laureates"]:
                print("----------------------------")
                if "knownName" in m:
                    print(m['knownName']['en'])
                print(m['motivation']['en'])
                andel = m['portion']
                prize_cnt += 1

            printResult(peng, idagpeng, prize_cnt)


def main():
    print(HELP_STRING)

    while True:
        menu_choice = input("\nMake a choice? \n(You can enter 1,2,h(H) or q(Q)) \n").upper().strip()
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
            field = ""
            year = ""
            aaa = input(">")
            str_list = aaa.split()
            flag = "All"
            if (len(str_list) == 1):
                flag = "All"
                year = str_list[0]
            else:
                flag = "OneField"
                year = str_list[0]
                field = str_list[1]

            if flag == "OneField" and not checkfield(field):
                print("You should print correct field.\n You can find the fields select 2")
            else:
                if (flag == "OneField"):
                    printOneFieldForYear(int(year), field)
                else:
                    printAllInformationsForYear(int(year))

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