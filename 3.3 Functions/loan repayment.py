

##aoijsadoijasd 
#the quick brown fox jumps over the lazy dog



___author___ = "Niko Stoner"

import math


rate: float
principal: float
duration: int   
amount: float
months: int



def calc_monthly_payment(rate: float, principal: float, duration: int) -> float:
    months: int = duration * 12
    rate = rate/100
    monthly_rate: float = rate/12
    p1: float = monthly_rate*principal
    p2: float = 1 + monthly_rate
    p3: float = p2 ** -months
    p4: float = 1 - p3
    amount = p1/p4
    ##print (p1) 
    ##print (p2)
    ##print (p3)
    ##print (p4)
    ##print (amount)
    print(f"Mothly payment: ${amount:.2f}")

def main():
    
    calc_monthly_payment(6.25, 826000, 20)
    calc_monthly_payment(5.87, 648000, 30)
    rate: float = float(input("Input annual interest rate (%): "))
    principal: float = float(input("Input principal ($): ")) 
    duration: int = int(input("Input loan duration (years): "))
    months: int = duration * 12
    calc_monthly_payment(rate, principal, duration)
    
    
if __name__ == "__main__":
    main() 