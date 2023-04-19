#Les Bibliotheque a importer
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
import sqlite3
conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestion_prof"
)

import tkinter as tk
import sqlite3


def selectionner():
    try:
        # Récupérer la ligne sélectionnée
        curItem = table.focus()
        values = table.item(curItem)['values']

        # Afficher les valeurs dans les champs de texte correspondants
        txtnom.delete(0, END)
        txtnom.insert(END, values[0])

        txtprenom.delete(0, END)
        txtprenom.insert(END, values[1])

        valeurSexe.set(values[2])

        comboFiliere.delete(0, END)
        comboFiliere.insert(END, values[3])

        comboModule.delete(0, END)
        comboModule.insert(END, values[4])

        txtmatiere.delete(0, END)
        txtmatiere.insert(END, values[5])

    except Exception as e:
        print(e)
        messagebox.showwarning("Erreur", f"Erreur lors de la sélection des données: {e}")
        maBase.rollback()
        maBase.close()

        # retour
        maBase.rollback()
        maBase.close()



# Création de l'interface graphique et des boutons associés

def Ajouter():
    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    filiere = comboFiliere.get()
    module = comboModule.get()
    matiere  = txtmatiere.get()


    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_prof")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO professeursmatieres (nom, prenom, sexe, filiere, module, matiere) VALUES (%s, %s,%s, %s, %s, %s) "
        val = (nom,prenom, sexe, filiere, module, matiere)
        meConnect.execute(sql, val)
        maBase.commit()
        derniernom = meConnect.lastrowid
        messagebox.showinfo("information", "Professeur ajouté")
        root.destroy()
        call(["python", "page2.py"])

    except Exception as e:
        print(e)
        messagebox.showwarning("Erreur", f"Erreur lors de l'ajout des données: {e}")
        maBase.rollback()
        maBase.close()

#retour
        maBase.rollback()
        maBase.close()


def clear_widgets(txtnom, txtprenom, valeurSexe, comboFiliere, comboModule, txtmatiere):
    pass

def RemplirChamps():
    # Récupérer la ligne sélectionnée
    curItem = table.focus()
    row = table.item(curItem)['values']

def Modifier():
    print('nom')
    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    filiere  = comboFiliere.get()
    module = comboModule.get()
    matiere  = txtmatiere.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_prof")
    meConnect = maBase.cursor()

    try:

    # Modifier la ligne de la table
        meConnect.execute("UPDATE professeursmatieres SET nom=%s, prenom=%s, sexe=%s, filiere=%s, module=%s, matiere=%s WHERE nom=%s", (nom, prenom, sexe, filiere, module, matiere, nom))
        maBase.commit()

        messagebox.showinfo("information", "Modification effectuée")
        root.destroy()
        call(["python", "page2.py"])


    except Exception as e:
        print(e)

        #retour
        maBase.rollback()
        maBase.close()

def Supprimer():
    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_prof")
    meConnect = maBase.cursor()

    try:
        # Récupérer la ligne sélectionnée
        curItem = table.focus()
        values = table.item(curItem)['values']

        # Supprimer la ligne de la table
        meConnect.execute("DELETE FROM professeursmatieres WHERE nom=%s", (values[0],))
        maBase.commit()

        messagebox.showinfo("information", "Professeur supprimé")
        root.destroy()
        call(["python", "page2.py"])

    except Exception as e:
        print(e)

        # retour
        maBase.rollback()
        maBase.close()



#Ma fenetre
root  = Tk()

root.title("Acceuil")
root.geometry("1280x700+0+0")
root.resizable(False, False)
root.configure(background="#000066")


#Ajouter le titre
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                 , text = "GESTION PEDAGOGIQUE", font = ("Sans Serif", 25), background = "#091821", fg="#FFFAFA")
lbltitre.place(x = 0, y = 0, width = 1350, height=100)

#Detail des professeurs


#Nom
lblnom = Label(root, text="NOM", font=("Arial", 18), bg="#091821", fg="white")
lblnom.place(x=10, y=200, width=150)
txtnom = Entry(root,bd=4, font=("Arial", 14))
txtnom.place(x=190,y=200,width=300)
#Prenom
lblprenom = Label(root, text="PRENOM", font=("Arial", 18), bg="#091821", fg="white")
lblprenom.place(x=10, y=250, width=150, )
txtprenom = Entry(root,bd=4, font=("Arial", 14))
txtprenom.place(x=190,y=250,width=300)

#sexe

valeurSexe = StringVar()
lblsexe = Label(root, text="SEXE", font=("Arial", 18), bg="#091821", fg="white")
lblsexe.place(x=10, y=300, width=150, )
lblSexeMasculin = Radiobutton(root, text="♂", value="M",variable=valeurSexe, indicatoron=0, font=("Arial", 14), bg="#091821", fg="#31cbff")
lblSexeMasculin.place(x=190, y=300, width=130)
txtSexeFeminin = Radiobutton(root,text="♀",value="F", variable=valeurSexe, indicatoron=0,font=("Arial", 14), bg="#091821", fg="#f70a8d")
txtSexeFeminin.place(x=360,y=300,width=100)

#filiere
lblFiliere = Label(root, text="FILIERE", font=("Arial", 18), bg="#091821", fg="white")
lblFiliere.place(x=10, y=400, width=150, )

comboFiliere = ttk.Combobox(root,font=("Arial", 14))
comboFiliere['values'] = ['DWWM','MCO','TSSR','SIO']
comboFiliere.place(x=190, y=400, width=130)

#Module
lblModule = Label(root, text="MODULE", font=("Arial", 18), bg="#091821", fg="white")
lblModule.place(x=10, y=450, width=150, )

comboModule = ttk.Combobox(root,font=("Arial", 14))
comboModule['values'] = ['Analyse','Cybersécurité','Langues appliquées','Mathématiques','Programmation']
comboModule.place(x=190, y=450, width=130)

#Matiere
lblmatiere = Label(root, text="MATIERE", font=("Arial", 18), bg="#091821", fg="white")
lblmatiere.place(x=10, y=500, width=150, )
txtmatiere = Entry(root,bd=4, font=("Arial", 14))
txtmatiere.place(x=190,y=500,width=300)


#Selectionner
btnSelectionner = tk.Button(text="Sélectionner", command=selectionner)
btnSelectionner.place(x=1190,y=600)
#Enregistrer
btnenregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "#53b24a", fg = "white", command=Ajouter)
btnenregistrer.place(x=10, y=620, width=200)

#modifier
btnmodifier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "#bdc03b", fg = "white", command=Modifier)
btnmodifier.place(x=260, y= 620, width=200)

#Supprimer
btnSupprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "#ff1200", fg = "white", command=Supprimer)
btnSupprimer.place(x=510, y= 620, width=200)


#Table
table = ttk.Treeview(root, columns = (1, 2, 3, 4, 5, 6), height = 5, show = "headings")
table.place(x = 510,y = 150, width = 790, height = 450)

#Entete
table.heading(1 , text = "NOM")
table.heading(2 , text = "PRENOM")
table.heading(3 , text = "SEXE")
table.heading(4 , text = "FILIERE")
table.heading(5 , text = "MODULE")
table.heading(6 , text = "MATIERE")


#definir les dimentions des colonnes
table.column(1,width = 120)
table.column(2,width = 120)
table.column(3,width = 120)
table.column(4,width = 120)
table.column(5,width = 120)
table.column(6,width = 120)



# afficher les informations de la table
maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_prof")
meConnect = maBase.cursor()
meConnect.execute("SELECT * from professeursmatieres")
for row in meConnect:
    table.insert('', END, value = row)
maBase.close()

#Execution
root.mainloop()