#For Reading and Exporting texts from Files
with open("Currencydata.txt") as f:
    lines = f.readlines()

#Using Dictionary For Calling Amount As Value From Currency as Key
currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

#For User input and taking out value in INR
amount = int(input("Enter the amount:\n"))
print("Enter the name of currency you want to convert this amount this amount to? Available options are:\n ")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values\n")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")