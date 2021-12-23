

from typing import final


def columnWiseToList(rawData):
    finalColumnSeperatedList = []

    # taking data tracker
    takeData = True

    for index, element in enumerate(rawData):

        finalColumnSeperatedList.append(
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ])
        splitted = element.split()

        # Initial date of contact
        if len(splitted[0]) < 10:

            finalColumnSeperatedList[index][0].append(splitted[0])
        elif len(splitted[0]) < 14:  # 12-Apr-114103

            finalColumnSeperatedList[index][0].append(
                splitted[0][0:len(splitted[0]) - 4])
            finalColumnSeperatedList[index][1].append(
                splitted[0][len(splitted[0]) - 4:])

        # Ledger number
        if len(finalColumnSeperatedList[index][1]) == 0 and len(splitted[1]) < 6:
            finalColumnSeperatedList[index][1].append(
                splitted[1])

        # Folio Number
        if len(splitted[1]) == 6:
            finalColumnSeperatedList[index][2].append(
                splitted[1])
        elif len(splitted[2]) == 6:
            finalColumnSeperatedList[index][2].append(
                splitted[2])

        #################################################################
        ##########EVERYTHING IS WELL AND GOOD ABOVE######################

    print(finalColumnSeperatedList)
