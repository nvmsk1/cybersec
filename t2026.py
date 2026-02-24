def calcola_tasse(reddito):
    tasse = 0

    if reddito <= 28000:
        tasse = reddito * 0.23
    elif reddito <= 50000:
        tasse = (28000 * 0.23) + ((reddito - 28000) * 0.35)
    else:
        tasse = (28000 * 0.23) + (22000 * 0.35) + ((reddito - 50000) * 0.43)

    return tasse


reddito = float(input("reddito lordo: "))

tasse = calcola_tasse(reddito)
reddito_netto = reddito - tasse

print("\n--- risultato ---")
print(f"reddito lordo: {reddito:.2f} €")
print(f"tasse da pagare: {tasse:.2f} €")
print(f"reddito netto: {reddito_netto:.2f} €")
