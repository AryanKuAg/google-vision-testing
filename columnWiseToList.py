

from typing import final


def columnWiseToList(rawData):
    finalColumnSeperatedList = []

    # taking data tracker
    takeData = True

    for index, element in enumerate(rawData):

        finalColumnSeperatedList.append(
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ])
        splitted = element.split()

        # Initial date of contact and ledger number
        if len(splitted[0]) < 10:

            finalColumnSeperatedList[index][0].append(splitted[0])
        elif len(splitted[0]) < 14:  # 12-Apr-114103

            finalColumnSeperatedList[index][0].append(
                splitted[0][0:len(splitted[0]) - 4])
            finalColumnSeperatedList[index][1].append(
                splitted[0][len(splitted[0]) - 4:])
