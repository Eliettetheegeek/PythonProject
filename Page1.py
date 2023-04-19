# import
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from subprocess import call
import smtplib
import secrets
import hashlib


# Connexion
def Seconnecter():
    email = txtemail.get()
    mot_de_passe = txtmdp.get()
    if email == "" or mot_de_passe == "":
        messagebox.showerror("Saisir données")
        txtmdp.delete("0", "end")
        txtemail.delete("0", "end")
    elif email == "admingp@domain.com" and mot_de_passe == "1234":
        messagebox.showinfo("", "Hello Admin!!!")
        txtemail.delete("0", "end")
        txtmdp.delete("0", "end")
        root.destroy()
        # fermer la fenêtre de connexion
        call(["python", "page2.py"])
    else:
        try:
            cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='gestion_prof'
            )
            cursor = cnx.cursor()

            # Requête pour vérifier si l'utilisateur existe dans la base de données
            query = "SELECT * FROM professeurs WHERE email = %s AND mot_de_passe = %s"
            cursor.execute(query, (email, mot_de_passe))
            result = cursor.fetchone()

            if result is not None:
                # Utilisateur valide, vous pouvez maintenant accéder a votre pédagogie
                messagebox.showinfo("", "Bienvenu Teacher!!!")
                txtemail.delete("0", "end")
                txtmdp.delete("0", "end")
                root.destroy()
                # fermer la fenêtre de connexion
                call(["python", "page3.py"])
            else:
                # Utilisateur invalide, afficher un message d'erreur et ne pas rediriger vers la page3
                messagebox.showerror("", "Email ou mot de passe invalide")
                txtmdp.delete("0", "end")
                txtemail.delete("0", "end")
        except mysql.connector.Error as err:
            # En cas d'erreur de connexion à la base de données
            messagebox.showwarning("Erreur", f"Erreur de connexion à la base de données: {err}")
            txtmdp.delete("0", "end")
            txtemail.delete("0", "end")




# Ma fenetre
root = Tk()

root.title("Authentification")
root.geometry("400x300+450+200")
root.resizable(False, False)
root.configure(background="#F5F5DC")


#Ajouter le titre
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                  , text = "Connexion", font = ("Verona", 25), background = "#091821", foreground="white")
lbltitre.place(x = 0, y = 0, width = 400)

lblemail = Label (root, text="E-mail :", font=("Verona", 14),bg="#091821", fg="white")
lblemail.place(x = 5, y = 100,width = 150 )
txtemail = Entry(root,bd=4, font=("Arial", 13))
txtemail.place(x=150,y=100,width=200,height=30)

lblmdp = Label (root, text="Mot de Passe :", font=("Verona", 14),bg="#091821", fg="white")
lblmdp.place(x = 5, y = 150,width = 150 )
txtmdp = Entry(root,show="*",bd=4, font=("Arial", 13))
txtmdp.place(x=150,y=150,width=200,height=30)


#Bouton Connecter
btnconnexion = Button(root, text = "Connexion", font = ("Verona", 16),bg ="#db1414", fg = "white", command=Seconnecter)
btnconnexion.pack()
btnconnexion.place(x=200, y= 230, width=180)



# execution
root.mainloop()
