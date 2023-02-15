def tuitionComp(studInfo):

    if studInfo[0] == "BSIT":
        firstPayment = int(input("First Payment: "))
        balance = 12500 - firstPayment

        print(studInfo[1] + ", " + studInfo[3] + ", " + studInfo[2] + studInfo[4] + ". Balance: ", balance)

    elif studInfo[0] == "BSCS":
        firstPayment = int(input("First Payment: "))
        balance = 13500 - firstPayment

        print(studInfo[1] + ", " + studInfo[3] + ", " + studInfo[2] + studInfo[4] + ". Balance: ", balance)
   
    else:
        print("Invalid")
