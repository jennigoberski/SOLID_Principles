"""
We want to write code that's open for extension, so we can
extend the preexisting code with new functionalities, but
close for modification, which means we shouldn't need to modify 
the existing code in order to add new functionalities
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
    
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass
    
class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code): 
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status("paid")
        
class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code): 
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status("paid")
            
class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code): 
        print("Processing paypal payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status("paid")    
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = DebitPaymentProcessor()
processor.pay(order, "037846")