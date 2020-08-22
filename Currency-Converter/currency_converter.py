from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
p = CurrencyCodes()

curr1 = 'INR'
curr2 = 'USD'

print(p.get_symbol(curr1))  # to get currency symbol using code
print(p.get_currency_name(curr1))  # to get currency name using currency code
print(p.get_currency_code_from_symbol('₹'))  # to get currency name using symbol

print(c.get_rates(curr1))  # get all other currency status in respect to stated currency code here*
print(c.get_rate(curr2, curr1))  # get rates respect to currency codes
print(c.convert(curr2, curr1, 20))  # convert currency inr to usd
