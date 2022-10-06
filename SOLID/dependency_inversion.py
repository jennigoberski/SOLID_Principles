"""
We want our classes to depend on abstractions and not on 
concrete subclasses
"""

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
    

class Authorizer(ABC):
    
    def is_authorized(self) -> bool:
        return self.authorized


class SMSAuth(Authorizer):
    authorized = False
    
    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.set_authorized(True)
        
    def is_authorized(self) -> bool:
        return self.authorized
    
    def set_authorized(self, authorized: bool):
        self.authorized = authorized


class NotARobot(Authorizer):
    authorized = False
    
    def not_a_robot(self):
        print("Are you a robot? Naaaa...")
        self.set_authorized(True)
        
    def is_authorized(self) -> bool:
        return self.authorized
    
    def set_authorized(self, authorized: bool):
        self.authorized = authorized    
        
        
class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass
    
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer
    
    def pay(self, order):
        if not self.authorizer.is_authorized:
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
            
            
class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer
        
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
            
    def pay(self, order): 
        if not self.authorizer.is_authorized:
            raise Exception("Not authorized!")
        
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.set_status("paid")    
      
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = NotARobot()
processor = DebitPaymentProcessor("2349875", authorizer)
authorizer.not_a_robot()
processor.pay(order)