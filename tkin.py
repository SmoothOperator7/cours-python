import tkinter as tk
#print(tk.TkVersion)

def action_bouton():
    print("Le bouton à été cliqué")

fenetre = tk.Tk()
fenetre.title("Ma premiere interface graphique")

#etiquette= tk.Label(fenetre, text="Bravo tu as fais ta première interface graphique")
#etiquette.pack()
bouton = tk.Button(fenetre, text="Cliquez sur moi ! ", command=action_bouton)
bouton.pack()



fenetre.geometry("400x300")
fenetre.mainloop()