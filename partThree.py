def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(pounds):
    mealcost = float(pounds.strip('£'))
    print(mealcost)
    return(mealcost)                     

def percent_to_float(percent):
    chargefloat = float(percent.strip('%'))
    chargefloat2 = chargefloat/100
    print(chargefloat2)
    return(chargefloat2)              

main()
