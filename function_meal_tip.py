# A very simple function
def tip_amount(meal, tax):
    tax = tax / 100
    rate_service = raw_input("Rate your service as excellent, good, or poor: ")
    if rate_service == "excellent":
        tip = .20 * meal
        total = meal + meal * tax + tip
        return "Please pay %s " % total
    elif rate_service == "good":
        tip = .15 * meal
        total = meal + meal * tax + tip
        return "Please pay %s " % total
    elif rate_service == "poor":
        return "Don't pay a thing and find a manager!"

# calling a function
print tip_amount(50.46, 6.8)
