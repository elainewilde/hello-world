#Elaine Wilde 1671617

import csv

#defining the functions and classes below for each csv file for a framework upon being imported.
def Strtodate(datestring):
    datestringlist = datestring.split("/")
    datelist = []
    for i in datestringlist:
        datelist.append(int(i))
    return datelist
def dateCompare(today, compare):  # filters if compare is older than today, returns True if needs to be serviced
    todayday = today[1]
    todaymonth = today[0]
    todayyear = today[2]
    compday = compare[1]
    compmonth = compare[0]
    compyear = compare[2]
    if compyear < todayyear: return True
    if compyear > todayyear: return False
    if compyear == todayyear:
        if compmonth < todaymonth: return True
        if compmonth > todaymonth: return False
        if compmonth == todaymonth:
            if compday < todayday: return True
            if compday > todayday: return False
            if compday == todayday: return False


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

#for the FullInventory.csv
class InventoryFull:
    def __init__(self, id, type, device, price, servicedate, status=None):
        self.ID = id
        self.brand = type
        self.types = device
        self.costs = price
        self.dated = servicedate
        self.note = status

    def __repr__(self,): return repr(self.ID + " " + self.brand + " " + self.types + " " + self.costs + " " + self.dated + " " + self.note)

#for the LaptopInventory.csv
class InventoryLaptop:
    def __init__(self, id, type, cost, dateserviced, status=None):
        self.ID = id
        self.brand = type
        self.price = cost
        self.dates = dateserviced
        self.notes = status

    def __repr__(self,): return repr(self.ID + " " + self.brand + " " + self.price + " " + self.dates + " " + self.notes)

#for the PastServiceDateInventory.csv
class PastServiceDate:
    def __init__(self, id, manufacturer, item, cost, dateserviced, status=None):
        self.ID = id
        self.manufacturer_type = manufacturer
        self.type = item
        self.price = cost
        self.service_date = dateserviced
        self.damaged = status

    def __repr__(self,): return repr(self.ID + " " + self.manufacturer_type + " " + self.type + " " + self.price + " " + self.service_date + " " + self.damaged)

#for the DamagedInventory.csv
class InventoryDamaged:
    def __init__(self, id, manufacturer, item, cost, dateserviced, status=None):
        self.ID = id
        self.manufacturer_type = manufacturer
        self.type = item
        self.price = cost
        self.service_date = dateserviced
        self.damaged = status


    def __repr__(self,): return repr(self.ID + " " + self.manufacturer_type + " " + self.item + " " + self.cost + " " + self.dateserviced + " ")

#The above are all the defined classes for the imported frameworks of the csv files.
#Below this is the code manipulating the frameworks into the lists that are displayed
#The data is stored into empty lists and then further manipulated by code to display the required output below.

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

    #id, MANUFACTURER, TYPE, PRICE, DATE, DAMAGE0
    dataframe=[]
    for i in range(len(man_rows)):
        row=[man_rows[i][0],man_rows[i][1],man_rows[i][2],price_rows[i][1],service_rows[i][1],man_rows[i][3]]
        dataframe.append(row)


#######################################################################################
                        ##Interactive Inventory Query Capability
#######################################################################################
input_info = ''
while input_info != 'q':
    input_info = input("Enter the item you would like (please ensure brand and type match the item--case sensitive) ('q' to quit): ")
    #manufacturer_type = input_info.split()
    #input_info = input()
    if input_info == 'q':
        print("Thank you for using the Interactive Inventory Query Program!")
        break
    qwer=input_info.split()
    print(qwer)

    #accepted_words=["Apple","computer", "phone"]
    brands={}
    types={}
    for i in dataframe:
        #print(i[1],i[2])
        brands[i[1]]='1'
        types[i[2]]='1'
    print(brands)
    print(types)
    accepted_words=[]
    for i in brands:
        accepted_words.append(i)
    for i in types:
        accepted_words.append(i)

    print(accepted_words)


    clean_input=[]
    for input_word in qwer: #goes through the input values
        for accepted_word in accepted_words: #goes through the stored values in the list
            if input_word == accepted_word: #actively compares both values and appends if in list
                clean_input.append(input_word)


    brandcount=0
    typecount=0
    brand_of_item=""
    type_of_item=""
    for i in clean_input:
        for brand in brands:
            if i == brand:
                brandcount+=1
                brand_of_item=i

    for i in clean_input:
        for type in types:
            if i == type:
                typecount+=1
                type_of_item=i
    print(brandcount,typecount)

    # if entry is incorrect---confirms that an item in dataframe matches brand and type
    if brandcount !=1 or typecount !=1:
        print("No such item in inventory")
        continue

    print("Your item is:", type_of_item)

    today ="5/11/2021"
    # get that item from dataframe
    index=-1
    row=[]
    for ind, i in enumerate(dataframe):
        if brand_of_item == i[1] and type_of_item== i[2] and i[5] != 'damaged' and dateCompare(today,i[4]):
            index = ind
            row=i

    print('here',row)
    price_of_item = row[3]

    print("you may, also, consider:")
    nu_ind=''
    for ind, j in enumerate(dataframe):
        if type_of_item == j[2] and j[5] != 'damaged' and dateCompare(today, j[4]) and j[3] < price_of_item:
            print(j)
            nu_ind=ind
    if nu_ind == '':
        print("There are no items from a competing brand for less that are undamaged and not past service date")



























#######################################################################################


