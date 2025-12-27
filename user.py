class User:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.accounts = []
        
    def verify_pin(self, entered_pin):
        return self.pin == entered_pin
    
    def add_account(self, account):
        self.accounts.append(account)