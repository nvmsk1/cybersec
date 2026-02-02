namefile = logfile.txt
try: 
    with open(namefile, "r", encoding="utf-8") as f:
        for riga in f:
            print(riga, end="")
except FileNotFoundError as e:
    print(f"[!] errore: {e}")
