import pymonad

from pymonad import curry
@curry
def systolic_bp(bmi, age, gender_male, treatment):
    return (
            68.15+0.58*bmi+0.65*age+0.94*gender_male+6.44*treatment
    )


treated = systolic_bp(25,60,0)
print(treated(0))
print(treated(1))

@curry
def add(x, y):
    return x + y

@curry
def mul(x, y):
    return x * y

comp = add(7) * mul(2)        # 'mul(2)' is evaluated first, and it's result passed to 'add(7)'
print(comp(4))                        # returns 15

# Composition order matters!
comp = mul(2) * add(7)
print(comp(4))           
