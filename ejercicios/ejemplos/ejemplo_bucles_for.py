lista = ["manzana", "pera", "kiwi" , "limón", "fresa"]
for fruta in lista:
    print(fruta)
    
print("___________________\n")

for letter in "Hoja":
    print(letter)

prices = [100, 250, 75, 500, 150]
discounted_prices = []
discounted_rate = 0.20

for price in prices:
    discounted = price * (1- discounted_rate)
    discounted_prices.append(discounted)
    print(f"Precio original: ${price} Con descuento: ${discounted} ")
    
print(f"Lista de descuento {discounted_prices}")
print(f"Lista de normal {prices}")
