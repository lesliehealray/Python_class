# Cost of a meal
meal = 44.50
tax = .0675
tip = 0.15

#reassigning a variable
meal = meal + meal * tax
print meal

#Assign the variable total
total = meal + meal * tip
print total

# A very simple function

def tip_amount(total_bill, tax):
    rate_service = raw_input("Rate your service as excellent, good, or poor >> ")
    tax = tax / 100
    total_without_tax = total_bill - tax
    if rate_service == "excellent":
      tip = 1.20 * total_without_tax
      return "Please pay %s tip" %tip
    if rate_service == "good":
      tip = 1.15 * total_without_tax
      return "Please pay %s tip" %tip
    if rate_service == "poor":
      tip = 0
      return "Don't pay a thing and find a manager!" 

#calling a function    
print tip_amount(50.46, 6.8)
