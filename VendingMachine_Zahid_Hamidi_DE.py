####################################################################
# CashNotes Class (Child Class)

class CashNote:


    def __init__(self,AmountBalance):
        self.AmountBalance = AmountBalance

    def Note_10 (self,AmountBalance):                                   # AmountBalance = 19

        CountNote_10 = int(self.AmountBalance / 10)                    # CountNote_10 = 1

        cash10_count = 5000 - CountNote_10                             # counts cash note left in machine
        if cash10_count <= 10:
            print("Machine not available")

        Remainder = self.AmountBalance - 10*CountNote_10                # Remainder = 9

        print("RM 10: ", CountNote_10)

        return Remainder



    def Note_5 (self,AmountBalance):

        CountNote_5 = int(self.AmountBalance / 5)

        cash5_count = 5000 - CountNote_5                                # counts cash note left in machine
        if cash5_count <= 10:
            print("Machine not available")

        Remainder = self.AmountBalance - 5*CountNote_5

        print("RM 5: ", CountNote_5)

        return Remainder


    def Note_1 (self,AmountBalance):

        CountNote_1 = int(self.AmountBalance / 1)
        cash1_count = 7000 - CountNote_1                                # counts cash note left in machine
        if cash1_count <= 10:
            print("Machine not available")

        return CountNote_1



    def Coin_50 (self,CoinBalance):

        self.CoinBalance = CoinBalance

        CountCoin_50 = int(self.CoinBalance / 50)
        coin50_count = 3000 - CountCoin_50                                # counts coins left in machine
        if coin50_count <= 30:
            print("Machine not available")

        Remainder = self.CoinBalance - 50*CountCoin_50

        print("50 cents: ", CountCoin_50)

        return Remainder



    def Coin_20 (self,CoinBalance):

        self.CoinBalance = CoinBalance

        CountCoin_20 = int(self.CoinBalance / 20)
        coin20_count = 3000 - CountCoin_20                               # counts coins left in machine
        if coin20_count <= 30:
            print("Machine not available")

        Remainder = self.CoinBalance - 20*CountCoin_20

        print("20 cents: ", CountCoin_20)

        return Remainder



    def Coin_10 (self,CoinBalance):

        self.CoinBalance = CoinBalance

        CountCoin_10 = int(self.CoinBalance / 10)
        coin10_count = 3000 - CountCoin_10                               # counts coins left in machine
        if coin10_count <= 30:
            print("Machine not available")

        Remainder = self.CoinBalance - 10*CountCoin_10

        print("10 cents: ", CountCoin_10)

        return Remainder




####################################################################
# NextBalance Class

class NextBalance:


    def __init__(self,AmountBalance):
        self.AmountBalance = AmountBalance

    def balance_10(self,Remainder):                                        # Reminder = 9
        self.Remainder = Remainder

        if self.Remainder % 5 != 0:
            CountNote_5 = int(self.Remainder / 5)                         # CountNote_5 = 1
            print("RM 5: ", CountNote_5)
            Remainder = self.Remainder - 5 * CountNote_5                  # Remainder = 4

            return Remainder


        else:

            return Remainder


    def balance_5(self,Remainder):
        self.Remainder = Remainder

        CountNote_1 = int(self.Remainder / 1 )                       # CountNote_1 = 4
        print("RM 1: ", CountNote_1)




    def balanceCoin_50(self,Remainder):                             # Remainder = 30
        self.Remainder = Remainder

        if int(self.Remainder % 50 != 0) or (self.Remainder == 30) or (self.Remainder == 40):                                    # 50 cents scenario

            if  self.Remainder % 20 == 0 :
                CountCoin_20 = int(self.Remainder / 20)
                print("20 cent: ", CountCoin_20)
                Remainder = self.Remainder - 20 * CountCoin_20

                return Remainder

            elif self.Remainder == 30:

                CountCoin_20 = int(self.Remainder / 20)
                print("20 cent: ", CountCoin_20)
                Remainder = self.Remainder - 20 * CountCoin_20

                return Remainder


            else:

                pass

        else:
            pass



    def balanceCoin_20(self,Remainder):
        self.Remainder = Remainder

        if (self.Remainder % 20 != 0) or (self.Remainder == 10):                # case Reminder == 10

            if self.Remainder % 10 == 0:
                CountCoin_10 = int(self.Remainder / 10)
                print("10 cent: ", CountCoin_10)
                Remainder = self.Remainder - 10 * CountCoin_10

                return Remainder

            elif self.Remainder == 10:
                CountCoin_10 = int(self.Remainder / 10)
                print("10 cent: ", CountCoin_10)
                Remainder = self.Remainder - 10 * CountCoin_10

                return Remainder


            else:
                return Remainder

        else:
            pass


    def balanceCoin_10(self,Remainder):
        self.Remainder = Remainder
        CountCoin_10 = int(self.Remainder / 10)
        print("10 cent: ", CountCoin_10)
        return Remainder


####################################################################
# Purchase Class (Main Class)

class Purchase:

    def __init__(self,AmountBalance,CoinBalance):
        self.price = AmountBalance
        self.CoinBalance = CoinBalance

    def get_price(self):

        print("- Menu -\nCola : RM 2.00\nPepsi : RM 2.00\nGreen Tea : RM 1.50\nLatte: RM 4.00\nCappucino : RM 4.50\nMineral Water : RM 1.50")
        print("-" * 50)



class Sum(Purchase):                                                        # Inheritance Class (Child Class)

    def total(self,AmountBalance,CoinBalance):


        print(f"Your balance is RM {AmountBalance}.{CoinBalance} ")
        print("-" * 50)

###############################################################
# Main body program
print("-"*50)
print("This is a Vending Machine balance program. It will return the least amount of notes according to the balance set.")
print("-"*50)
print("Permitted notes are RM 10, RM 5 and RM 1")
print("Permitted coins are 50 cents, 20 cents and 10 cents")
print("Maximum cash inserted is RM 20 total")
print("-"*50)


AmountBalance = 17                                                       # Amount cash balance set
CoinBalance = 90                                                       # Amount coin balance set


if AmountBalance >= 0:

    Display = Sum(AmountBalance,CoinBalance)
    Display.get_price()                                             # Values inherit from base class get_price() function

    SumTotal = Sum(AmountBalance,CoinBalance)
    SumTotal.total(AmountBalance,CoinBalance)

else:
    pass


if AmountBalance >= 10:

    print("Your cash note balance: ")

    MyBalance = CashNote(AmountBalance)
    Remainder = MyBalance.Note_10(AmountBalance)            # Remainder returned from CashNote class (9)

    CashCount = NextBalance(Remainder)                      # Call NextBalance class
    Remainder = CashCount.balance_10(Remainder)             # Call balance_10 function in NextBalance class : Returned (3)

    CashCount = NextBalance(Remainder)                      # Call NextBalance class
    CashCount.balance_5(Remainder)



elif AmountBalance >=5:

    print("Your cash note balance: ")

    MyBalance = CashNote(AmountBalance)
    Remainder = MyBalance.Note_5(AmountBalance)

    CashCount = NextBalance(Remainder)
    CashCount.balance_5(Remainder)





elif AmountBalance >=1:

    print("Your cash note balance: ")

    MyBalance = CashNote(AmountBalance)
    Remainder = MyBalance.Note_1(AmountBalance)

    CashCount = NextBalance(Remainder)
    CashCount.balance_5(Remainder)



else:
    pass

####################################################################
# Coin balance part

if CoinBalance >= 50:

    print("-" * 50)
    print("Your coin balance: ")

    MyBalance = CashNote(CoinBalance)
    Remainder = MyBalance.Coin_50(CoinBalance)

    CashCount = NextBalance(Remainder)
    Remainder = CashCount.balanceCoin_50(Remainder)


    CashCount = NextBalance(Remainder)
    CashCount.balanceCoin_20(Remainder)


elif CoinBalance >= 20:

    print("-" * 50)
    print("Your coin balance: ")
    MyBalance = CashNote(CoinBalance)
    Remainder = MyBalance.Coin_20(CoinBalance)

    CashCount = NextBalance(Remainder)
    CashCount.balanceCoin_20(Remainder)


elif CoinBalance >= 10:

    print("-" * 50)
    print("Your coin balance: ")
    MyBalance = CashNote(CoinBalance)
    Remainder = MyBalance.Coin_10(CoinBalance)

else:
    pass



print("-"*50)
print("Thank you")
print("-"*50)


