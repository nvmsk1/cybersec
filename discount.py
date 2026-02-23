def discount(prices, isPet):
    pets = sum(isPet)
    altri = sum(prices[i] for i in range(len(prices)) if not isPet[i])
    n_altri = len(prices) - pets

    if pets >= 1 and n_altri >= 5:
        return altri * 0.20
    return 0.0


prices = []
isPet = []

while True:
    p = float(input("Prezzo (-1 per finire): "))
    if p == -1:
        break
    t = input("Animale? (Y/N): ").upper()
    prices.append(p)
    isPet.append(t == "Y")

sconto = discount(prices, isPet)

print("Sconto:", round(sconto, 2), "euro")
print("Numero totale articoli:", len(prices))
