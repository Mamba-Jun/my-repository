class BankAccount:
    bank_name = '中国银行'
    rate = 0.035
    def __init__(self,account_number,owner,balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    def save(self,money):
        self.balance = self.balance+money
        return f'存款成功，当前余额{self.balance}'
    def withdrawr(self,money):
        if money <= self.balance:
            self.balance = self.balance-money
            return f'取钱成功，当前余额{self.balance}'
        else:
            return f'余额不足'
        
bankaccount1 = BankAccount('12345','leo',100)
print(bankaccount1.save(10))
print(bankaccount1.withdrawr(120))