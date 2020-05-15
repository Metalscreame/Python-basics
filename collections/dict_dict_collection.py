from collections import defaultdict

tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
# Works fine


some_dict = {}
try:

    some_dict['colours']['favourite'] = "yellow"
except KeyError:
    print("nope, error")
