class ATM:
    def __init__(self,CardNo,PinNo,Balance):
        self.CardNo=CardNo
        self.PinNo=PinNo
        self.Balance=Balance

    def balanceEnquiry(self):
        print(self.Balance)

Person1=ATM(1432,8654,120345870)
Person1.balanceEnquiry()