def cambia0(num):
    if isinstance(num, int):
        return cambia0Aux(num, 0)
    else:
        return

def cambia0Aux(num, exp):
    if num == 0:
        return 0
    elif num % 10 == 0:
        return 1 * 10 ** exp + cambia0Aux(num//10, exp + 1)
    else:
        return num%10*10**exp + cambia0Aux(num//10, exp + 1)
    #Prueba git

print("Hola")