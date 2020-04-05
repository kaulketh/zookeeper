# the list "meals" is already defined
# your code here
def get_kcal_per_day(m: list, key='kcal'):
    kcal = 0
    for i in m:
        kcal += i.get(key)
    return kcal


print(get_kcal_per_day(m=meals))
