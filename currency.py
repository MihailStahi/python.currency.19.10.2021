

print("################")
print("SELECT INPUT CURRENCY")
print(" *EUR")
print(" *USD")
print(" *MDL")
print("################")
currency_in = input("chose: ")

money_in = float(input("money:"))


print("################")
print("SELECT OUTPUT CURRENCY")

if currency_in != "EUR" :
    print(" *EUR")

if currency_in != "USD" :
    print(" *USD")

if currency_in != "MDL" :
    print(" *MDL")



#print(" *USD")
#print(" *MDL")
print("################")

currency_out = input("chose: ")
eur_to_usd = 1.1
eur_to_mdl = 20.01
usd_to_mdl = 17.35
usd_to_eur = 0.9
mdl_to_usd = 0.049
mdl_to_eur = 0.057



if  currency_in == "EUR" and currency_out == "USD" :
    money_out = money_in * eur_to_usd
if  currency_in == "USD" and currency_out == "EUR" : 
    money_out = money_in / eur_to_usd
if  currency_in == "MDL" and currency_out == "USD" :
    money_out = money_in * mdl_to_usd
if  currency_in == "MDL" and currency_out == "EUR" : 
    money_out = money_in * mdl_to_eur
if  currency_in == "EUR" and currency_out == "MDL" :
    money_out = money_in * eur_to_mdl
if  currency_in == "USD" and currency_out == "MDL" : 
    money_out = money_in * usd_to_mdl





money_out = round(money_out, 2)
print(money_out)




#money_usd = input("ENTER YOUR MONEY: ") #usd
#money_usd = float(money_usd)
#usd_2_eur = 0.9 #1 usd = 0.9 EUR

#money_eur = money_usd * usd_2_eur
#print("YOUR MONEY IN EURO: " , money_eur)