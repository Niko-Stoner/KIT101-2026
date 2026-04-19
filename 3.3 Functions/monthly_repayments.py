

##aoijsadoijasd 
#the quick brown fox jumps over the lazy dog



___author___ = "Niko Stoner"

import math





def calc_monthly_payment(principal: int, rate: float,  duration: int) -> float:
    months: int = duration * 12
    rate = rate/100
    monthly_rate: float = rate/12
    p1: float = monthly_rate*principal
    p2: float = 1 + monthly_rate
    p3: float = p2 ** -months
    p4: float = 1 - p3
    amount: float = p1/p4
    ##print (p1) 
    ##print (p2)
    ##print (p3)
    ##print (p4)
    ##print (amount)
    return(amount)
   ## print(f"Monthly payment: ${amount:.2f}")

def main():
    print("Loan Repayment/Month")
    print()
    print(f"Monthly repayment 1: ${calc_monthly_payment(826000, 6.25, 20):.2f}")
    print(f"Monthly relayment 2: ${calc_monthly_payment(648000, 5.87, 30):.2f}")
    print()
    principal: int = int(input("Input principal ($): ")) 
    rate: float = float(input("Input annual interest rate (%): "))
    duration: int = int(input("Input loan duration (years): "))
    print()
    print("Calculating...")
    months: int = duration * 12
    print(f"Monthly repayment: ${calc_monthly_payment(principal, rate, duration):.2f}")

    
if __name__ == "__main__":
    main() 