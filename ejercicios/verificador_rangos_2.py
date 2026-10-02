print("Indica la temperatura del sistema")
temp = float(input("Temperatura? = "))
# if temp >= 18 and temp <=27:
#     print("La temperatura está OPTIMA")
if 18 <= temp <= 27 :
    print("La temperatura está OPTIMA")
elif temp < 18 :
    print("ALERTA FRÍO")
else:
    print("ALERTA CALOR")