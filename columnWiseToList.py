

def columnWiseToList(rawData):
    finalColumnSeperatedList = []

    # taking data tracker
    takeData = True

    for index,element in enumerate(rawData):
        tempEntryList  = []
        for i, e in enumerate(element):
            if takeData:
                tempEntryList.append(e)



        takeData = True
