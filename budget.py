def calcBills():
    myBills = {'Electric': 120.00, 'Rent': 1200.00, 'Water_sewer': 60.00, 'Car insurance': 75.00, 'Phone': 65.00}
    total =  0
    for i in myBills:
        total += myBills[i]
    owed = 'The total owed is: ${}'.format(total)
    return owed
