
print("="*20)

customerNames= ['jane Smith', 'Iason Jordan', 'David Morgan',]
customerPins = ['1234','5489','4587','1849','4756']
customerBalances = [10000, 20000,40000,10000,60000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0
 
while True:
    print("===============================")
    print(" ----welcome to Times Bank---- ")
    print("***********************")
    print("=<< 1. Open a new account    >>=")
    print("=<< 2. Withdraw Money        >>=")
    print("=<< 3. Deposit Money         >>=")
    print("<<  4. Check Customers & Balance  >>=")
    print("<<  5. Exit/Quit      >>=")
    print("***************************")
    choiceNumber = input("select your choice number fro the above menu:")
    if choiceNumber == "1":
        print("choice number 1 is selected by the customer")
        NOC = eval(input("number of customers : "))

        i = i + NOC

        if i > 5:
            print("/n")
            print("customer registration exceed reached")
            i=i - NOC
        else: 

            while counter_1 <= i:
                name = input("input fullname : ")
                customerNames.append(name)
                pin = str(input("please input a pin of your choice :"))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("please input a value to deposit to start an account :"))
                balance = balance + deposition
                customerBalances.append(balance)
                print("/nName=", end=" ")
                print(customerNames[counter_1])
                print("pin=", end=" ")
                print(customerPins[counter_2])
                print("Balance=", end=" ")
                print(customerBalances[counter_2], end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("/nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("your balance is added to customer system")
                print("---New account created successfully !---")
                print("/n")
                print("your name is available onthe customer list now :")
                print(customerNames)
                print("/n")
                print("Note! Please remember the Name and Pin")
                print("===========================")

        mainMenu = input("please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "2":
        j = 0
        print("choice number 2 is selected by the customer")
        while j < 1:
            k = -1
            name=input("please input name :")
            pin = input("please input pin :")
            
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        
                    
                
                        print("your current Balance :", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/RS\n")
                        balance= (customerBalances[k])

                        withdrawal = eval(input("Input value to WithDrawl :"))
                        
                        
                        if withdrawal > balance:
                            deposition = eval(input("please Deposit a higher value because your balance mentioned above is not enough : "))
                            balance = balance + deposition
                            print("your current balance:", end=" ")
                            print(balance, end=" ")
                            print("-/RS\n")
                            balance = balance - withdrawal
                            print("-/n")
                            print("------withdrawal successfully----")
                            customerBalances[k]= balance
                            print("your New Balance:", balance, end=" " )
                            print("-/RS\n\n")
                        else: 

                            balance = balance - withdrawal
                            print("\n")
                            print("-----withdrawal successsfully----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/RS\n\n")
            if j < 1:
                print("your name and pin does not match!\n")
                break

                                
                            
        mainMenu = input("please enter a key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "3":
        print("choice number 3 is selected by the customer")
        n = 0
        while n < 1:
            k = -1
            name=input("please input name:")
            pin= input("please input pin :")
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        print("Your current Balance: ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        depositon= eval(input("enter the value you e=want to deposit :"))
                        balance = balance + deposition 
                        customerBalances[k] = balance
                        print("/n")
                        print("-----deposition successful!-----")
                        print("your New Balance:", balance, end=" ")
                        print("-/RS\n\n")
            if n < 1:
                print("your name and pin does not match!\n")
                break
    
        mainMenu = input("please enter a key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "4":
        print("choice number 4 is selected by the customer")
        k = 0
        print("customer name list and balances mentioned below: ")
        print("/n")
        while k <= len(customerNames) - 1:
            print("->.customer =", customerNames[k])
            print("->.balance =", customerBalances[k],end=" ")
            print("-/RS")
            
            print("/n")
            k = k + 1
        mainMenu = input("please enter a key to go back to main menu to perform another function or exit ...")
    elif choiceNumber =="5":
        print("choice number 5 is selected by the customer")
        print("thank you for using our banking system!")
        print("/n")
        print("come again")
        print("BYE BYE")
        break
    else:
        print("invalid option selected by the customer")
        print("please try again!")
        mainMenu = input("please enter a key to go back to main menu to perform another function or exit ...")


                     





                           

















    




    


     
 