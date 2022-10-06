"""
It's better if you have several specific interfaces as 
opposed to one general purpose interface
"""

#This shows the result after using the principle

from abc import ABC, abstractmethod 

class Order:
    
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"
    
    def set_status(self, status: str):
        self.status = status
    
    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
    
class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass
    
    
class PaymentProcessor_SMS(PaymentProcessor):
    
    @abstractmethod
    def auth_sms(self, code):
        pass
    
    
class DebitPaymentProcessor(PaymentProcessor_SMS):
    
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False
        
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
    
    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized!")
         
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status("paid")
        
        
class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code
        
    def pay(self, order): 
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status("paid")
            
            
class PaypalPaymentProcessor(PaymentProcessor_SMS):
    
    def __init__(self, email_addresss):
        self.email_addresss = email_addresss
        self.verified = False
        
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
            
    def pay(self, order): 
        if not self.verified:
            raise Exception("Not authorized!")
        
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_addresss}")
        order.set_status("paid")    
      
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = DebitPaymentProcessor("2349875")
processor.auth_sms(465839)
processor.pay(order)