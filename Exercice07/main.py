def square(number):
    """ renvoie le carré du nombre"""
    if not isinstance(number, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    else:

        return number ** 2


print(square(2))
print(square(2.5))
print(square("dv"))