#Elaine Wilde 1671617

import csv

#defining the classes below for each csv file for a framework upon being imported.

#for the ManufacturerList.csv
class Manufacturer:
    def __init__(self,num,brand,device,status=None):
        self.number = num
        self.brands = brand
        self.type = device
        self.note = status

    def __repr__(self): return repr(self.number + " " + self.brands + " " + self.type + " " + self.note)

#for the Pricelist.csv
class ListPrice:
    def __init__(self,id,price):
        self.ID = id
        self.prices = price

    def __repr__(self): return repr(self.ID + " " + self.prices + " ")

#for the ServiceDatesList.csv
class DatesServiced:
    def __init__(self, id, servicedate):
        self.ID = id
        self.service_date = servicedate

    def __repr__(self,): return repr(self.ID + " " + self.service_date + " ")

#The above are all the defined classes for the imported frameworks of the csv files.
#Below this is the code manipulating the frameworks
#The data is stored into empty lists/dictionary and then further manipulated by code to display the required output below.

if __name__ == "__main__":
    #######################################################################################
                        ##READ DATA
    #######################################################################################
    filename = "ManufacturerList.csv"
    man_rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for slice in csvreader:
            man_rows.append(slice)

    ##BUBBLE SORT
    n =len(man_rows)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if int(man_rows[j][0])>int(man_rows[j+1][0]):
                man_rows[j],man_rows[j+1]=man_rows[j+1],man_rows[j]
    #The extra print statements # out were used for testing purposes.
    #print("Man Rows")
    # for i in man_rows:
        #print(i)#asdf1=Container("1167234","Apple","phone")
#asdf2=Container("2390112","Dell","laptop")
    # manufacturer = []
    # for ind, i in enumerate(rows):
    #     manufacturer.append(Manufacturer(rows[ind][0],rows[ind][1],rows[ind][2],rows[ind][3]))

    #print(manufacturer[0])

    filename = "PriceList.csv"
    price_rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for slice in csvreader:
            price_rows.append(slice)

    ##BUBBLE SORT
    n =len(price_rows)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if int(price_rows[j][0])>int(price_rows[j+1][0]):
                price_rows[j],price_rows[j+1]=price_rows[j+1],price_rows[j]
    # print("Price_Rows")
    # for i in price_rows:
    #     print(i)

    # priceslisted = []
    # for ind, i in enumerate(rows):
    #     priceslisted.append(ListPrice(rows[ind][0],rows[ind][1]))

    filename = "ServiceDatesList.csv"
    service_rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for slice in csvreader:
            service_rows.append(slice)
    ##BUBBLE SORT
    n =len(service_rows)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if int(service_rows[j][0])>int(service_rows[j+1][0]):
                service_rows[j],service_rows[j+1]=service_rows[j+1],service_rows[j]
    # print("Price_Rows")
    # for i in service_rows:
    #     print(i)
    # service_dates = []
    # for ind, i in enumerate(rows):
    #     service_dates.append(DatesServiced(rows[ind][0],rows[ind][1]))

    #id, MANUFACTURER, TYPE PRICE, DATE, DAMAGE
    dataframe=[]
    for i in range(len(man_rows)):
        row=[man_rows[i][0],man_rows[i][1],man_rows[i][2],price_rows[i][1],service_rows[i][1],man_rows[i][3]]
        dataframe.append(row)
    # print(man_rows[i][0],man_rows[i][1],man_rows[i][2],price_rows[i][1],service_rows[i][1],man_rows[i][3])
    # print("0-000000000000000000000000000000000000000")
    # for i in dataframe:
    #     print(i)

    #######################################################################################
                            ## A FullInventory.csv
    #######################################################################################

    clone_frame1=[]
    for i in dataframe:
        if i[0]!=0: #filter.
            clone_frame1.append(i)
    full_frame=[]
    ##BUBBLE SORT
    n =len(clone_frame1)
    #print('Apple'>'Lenovo')
    for i in range(n-1):
        for j in range(0,n-i-1):
            if clone_frame1[j][1]>clone_frame1[j+1][1]: #sorted by attribute
                clone_frame1[j],clone_frame1[j+1]=clone_frame1[j+1],clone_frame1[j]
    #for i in clone_frame1:
        #print(i)
    with open('FullInventory.csv','w') as f:
        write = csv.writer(f)
        for i in clone_frame1:
            write.writerow(i)


    #######################################################################################
                            ## B Item Type List
    #######################################################################################

    types = {}

    for i in dataframe:
        types[i[2]] = 0
    # print(typeDict)
    numtypes = len(types)
    bertha = []
    for ind, i in enumerate(types):
        clone_frame = []
        for row in dataframe:
            if row[2] == i:
                clone_frame.append(row)
        bertha.append(clone_frame)
    # printFrame(bertha)

    # Bubble sort bertha
    for ind, sheet in enumerate(bertha):
        clone_frame1 = sheet
        n = len(clone_frame1)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if clone_frame1[j][0] > clone_frame1[j + 1][0]:  # sorted by attribute
                    clone_frame1[j], clone_frame1[j + 1] = clone_frame1[j + 1], clone_frame1[j]
        bertha[ind] = clone_frame1
    # printFrame(bertha)

    for ind, type in enumerate(types):
        Type = type.capitalize()
        # print(Type)
        full_name = Type + 'Inventory.csv'
        with open(full_name, 'w') as f:
            write = csv.writer(f)
            for i in bertha[ind]:
                write.writerow(i)
            f.close()


    #######################################################################################
                            ## C Past Service Date
    #######################################################################################

    def Strtodate(datestring):
        datestringlist = datestring.split("/")
        datelist = []
        for i in datestringlist:
            datelist.append(int(i))
        return datelist

    def printFrame(frame):
        for i in frame:
            print(i)

    def dateCompare(today,compare): #filters if compare is older than today, returns True if needs to be serviced
        todayday=today[1]
        todaymonth=today[0]
        todayyear=today[2]
        compday=compare[1]
        compmonth=compare[0]
        compyear=compare[2]
        if compyear<todayyear: return True
        if compyear>todayyear: return False
        if compyear==todayyear:
            if compmonth<todaymonth:return True
            if compmonth>todaymonth: return False
            if compmonth==todaymonth:
                if compday<todayday: return True
                if compday>todayday: return False
                if compday == todayday: return False

    clone_frame1 = []
    for i in dataframe:
        today=[4,11,2021]
        compare=Strtodate(i[4])
        if dateCompare(today,compare)==True:  # filter.
            # asdf = Strtodate(i[4])
            # i.append(asdf)
            clone_frame1.append(i)

    #BUBBLE SORT
    n = len(clone_frame1)
    for i in range(n - 1):
        for j in range(0,n-i-1):
            if dateCompare(Strtodate(clone_frame1[j][4]),Strtodate(clone_frame1[j+1][4])):#clone_frame1[j][1]>clone_frame1[j+1][1]: #sorted by attribute
                clone_frame1[j],clone_frame1[j+1]=clone_frame1[j+1],clone_frame1[j]
    #printFrame(dataframe)
    #print("--------------------------------")
    #printFrame(clone_frame1)
    # for i in clone_frame1:
    #     print(i)
    full_name = 'PastServiceDateInventory.csv'
    with open(full_name, 'w') as f:
        write = csv.writer(f)
        for i in clone_frame1:
            write.writerow(i)

    #######################################################################################
                            ## D Damaged Inventory
    #######################################################################################

    clone_frame1 = []
    for row in dataframe:
        if row[5] == "damaged":
            clone_frame1.append(row)# filter.
    #         clone_frame1.append(i)
    #print("---------------------------")
    #printFrame(clone_frame1)
    # ##BUBBLE SORT
    n = len(clone_frame1)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if int(clone_frame1[j][3])>int(clone_frame1[j+1][3]): #sorted by attribute
                clone_frame1[j], clone_frame1[j + 1] = clone_frame1[j + 1], clone_frame1[j]
    # for i in clone_frame1:
    #     print(i)
    full_name = 'DamagedInventory.csv'
    with open(full_name, 'w') as f:
        write = csv.writer(f)
        for i in clone_frame1:
            write.writerow(i)
