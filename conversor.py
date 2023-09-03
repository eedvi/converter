dog_face = '''
 / \__                                
(    @\___                         
 /         O       Conversor de temperatura
/   (_____/                 
/_____/   U  
'''

print(dog_face)
temp = int(input("Ingrese la temperatura a convertir:"))
escala = input("Es Farenheit (F) o Celsius (C)?").upper()

if escala == "F":
    celcius = (temp - 32 )* 5 / 9
    print(celcius)
elif escala == "C":
    farenheit = (temp * 1.8000) +32
    print(farenheit)
else:
    print("Escala incorrecta o no incluida en la aplicación")
    