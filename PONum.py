#Automatically converts to and from PO number format.
print("Please unter a number to convert to or from WWWLLC PO format: ")
userConvert = input()

#input validation
if not userConvert.isnumeric():
    print("Invalid input")
    exit()
userConvert = int(userConvert)
if(userConvert >= 8675309):
    if ((userConvert - 8675309) % 42) != 0:
        print("This value is not a valid PO number")
        exit()
    outputConvert = int(((userConvert - 8675309) / 42) + 1)
    print("The PO number entered is " + str(outputConvert) + " in the series")
else:
    outputConvert = int(8675309 + (42 * (userConvert - 1)))
    print("The series number entered has " + str(outputConvert) + " as a PO number")
    
