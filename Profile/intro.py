import random

def introduction():
    name = ["Gábor", "Gabe", "Gabriel", "NRG"]
    name_set = random.choice(name)
    return f"Hi, 👋 I’m {name_set}"