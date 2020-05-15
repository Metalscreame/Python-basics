ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
try:
    ages['Michael']
except KeyError:
    print("dict error")