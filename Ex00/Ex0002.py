"Will it rain?"

def rain(where, num):

    "Should I dry my clothes?"

    if (where == "Outdoor" and num >= 240) or (where == "Indoor" and num >= 480):
        return "True"
    else:
        return "False"

print(rain(input(), float(input())))
