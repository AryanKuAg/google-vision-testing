
import re
from typing import final


def columnWiseToList(rawData):
    finalColumnSeperatedList = []

    # Date pattern
    pattern1 = re.compile("\d\d-\w\w\w-\d\d")  # 33-Mar-43
    pattern2 = re.compile("\d-\w\w\w-\d\d")  # 5-Jul-34
    pattern3 = re.compile("\d-\w\w\w\d")  # 6-Mar6
    pattern4 = re.compile("\d-\w\w\w-\d")  # 4-mar-3
    pattern5 = re.compile("\d\w\w\w-\d")  # 6mar-3
    pattern6 = re.compile("-\w\w\w-\d")  # -Dec-06
    pattern7 = re.compile("\d\d-\w\w\w- \d\d")  # 10-May- 12
    pattern8 = re.compile("\d\d\w\w\w-\d\d")  # 24Aug-07
    pattern9 = re.compile("\d-\w\w-\d")  # 4-Ap-0?
    pattern10 = re.compile("\d\d-\w\w\w-\d")  # 13-Apr-0?
    # pattern11 = re.compile("\w\w\w-\d\d")  # May-84

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
        #################################################################

        # This is for the name or customer name

        folioNumberIndex = element.index(
            finalColumnSeperatedList[index][2][0])
        # This is just initial data if we don't able to find it okay...)_)
        nameLastIndex = element.index(
            finalColumnSeperatedList[index][2][0]) + 10
        for yoyo in range(folioNumberIndex, folioNumberIndex + 30):
            if '-' in element[yoyo]:
                nameLastIndex = yoyo - 2
                break

        #print('name', str(element[folioNumberIndex + 6:nameLastIndex]).strip())
        finalColumnSeperatedList[index][3].append(
            str(element[folioNumberIndex + 6:nameLastIndex]).strip())

    print(finalColumnSeperatedList)
