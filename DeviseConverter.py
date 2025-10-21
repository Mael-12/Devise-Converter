import tkinter as tk
import requests

devises = ["USD", "EUR", "GBP", "JPY", "CAD", "XOF", "INR"]

def convertir():
    try:
        montant = float(entry_montant.get())
        de = var_de.get()
        vers = var_vers.get()

        url = f"https://v6.exchangerate-api.com/v6/3acb23baad98a85451a39a7f/latest/{de}"
        r = requests.get(url).json()

        taux = r["conversion_rates"].get(vers)
        if taux:
            resultat = montant * taux
            label_resultat.config(text=f"{montant} {de} = {resultat:.2f} {vers}")
        else:
            label_resultat.config(text="Devise cible non trouvée.")
    except ValueError:
        label_resultat.config(text="Montant invalide.")
    except Exception as e:
        label_resultat.config(text=f"Erreur: {e}")

# Interface Tkinter
root = tk.Tk()
root.title("Convertisseur de devises")

tk.Label(root, text="Montant:").grid(row=0, column=0)
entry_montant = tk.Entry(root)
entry_montant.grid(row=0, column=1)

tk.Label(root, text="De:").grid(row=1, column=0)
var_de = tk.StringVar(value=devises[0])
tk.OptionMenu(root, var_de, *devises).grid(row=1, column=1)

tk.Label(root, text="Vers:").grid(row=2, column=0)
var_vers = tk.StringVar(value=devises[1])
tk.OptionMenu(root, var_vers, *devises).grid(row=2, column=1)

tk.Button(root, text="Convertir", command=convertir).grid(row=3, columnspan=2)
label_resultat = tk.Label(root, text="")
label_resultat.grid(row=4, columnspan=2)

root.mainloop()