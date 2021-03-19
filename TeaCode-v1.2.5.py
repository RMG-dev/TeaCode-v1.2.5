from tkinter import *
from tkinter.filedialog import *
import tkinter.scrolledtext as tkst
import tkinter as tk
import time
import webbrowser
import os
import pathlib

fenetre = Tk()
fenetre.title("Tea Code (FrontEnd) v1.2.5")
fenetre.geometry("1730x820")
fenetre.configure(bg='grey')

def OpenUrl():
    webbrowser.open_new("https://discord.io/CofeeAndTea")
    return


def importer1():
    filepath = askopenfilename(title="Ouvrir votre fichier en python !",filetypes=[('python files','.html')])
    global FileName1
    FileName1 = str(filepath)
    pyFile = open(FileName1,"r")
    T.insert(tk.END, pyFile.read())
    pyFile.close()
    return

def importer2():
    filepath = askopenfilename(title="Ouvrir votre fichier en python !",filetypes=[('python files','.css')])
    global FileName2
    FileName2 = str(filepath)
    pyFile = open(FileName2,"r")
    T2.insert(tk.END, pyFile.read())
    pyFile.close()
    return

def importer3():
    filepath = askopenfilename(title="Ouvrir votre fichier en python !",filetypes=[('python files','.js')])
    global FileName3
    FileName3 = str(filepath)
    pyFile = open(FileName3,"r")
    T3.insert(tk.END, pyFile.read())
    pyFile.close()
    return

def save():
    pyFile = open(FileName1, "w")
    input1 = T.get("1.0","end-1c")
    pyFile.write(input1)
    pyFile.close()
    pyFilex = open(FileName2, "w")
    input2 = T2.get("1.0","end-1c")
    pyFilex.write(input2)
    pyFilex.close()
    pyFilexx = open(FileName3, "w")
    input3 = T3.get("1.0","end-1c")
    pyFilexx.write(input3)
    pyFilexx.close()
    return

def savex1(event):
    pyFile = open(FileName1, "w")
    input1 = T.get("1.0","end-1c")
    pyFile.write(input1)
    pyFile.close()
    pyFilex = open(FileName2, "w")
    input2 = T2.get("1.0","end-1c")
    pyFilex.write(input2)
    pyFilex.close()
    pyFilexx = open(FileName3, "w")
    input3 = T3.get("1.0","end-1c")
    pyFilexx.write(input3)
    pyFilexx.close()
    return

def htmlx1():
    T.insert(tk.END, """<!DOCTYPE html>
<html>
<head>
    <title>Default.</title>
</head>
<body>
    <p>Test.</p>
</body>
</html>
    """)
    return

def cssx1():
    T2.insert(tk.END, """body {
    font-color: blue;
}

p {
    size: 50px;
}
    """)
    return

def jsx1():
    return


def alert():
    return

def run():
    path = pathlib.Path.cwd() / "run"
    path.mkdir(parents=True, exist_ok=True)
    filerun1 = open(path / "index.html", "w")
    filerun2 = open(path / "main.css", "w")
    filerun3 = open(path / "script.js", "w")
    inputx1 = T.get("1.0","end-1c")
    inputx2 = T2.get("1.0","end-1c")
    inputx3 = T3.get("1.0","end-1c")
    filerun1.write(inputx1)
    filerun2.write(inputx2)
    filerun3.write(inputx3)
    filerun1.close()
    filerun2.close()
    filerun3.close()
    webbrowser.open_new(path / "index.html")
    return

def runx1(event):
    path = pathlib.Path.cwd() / "run"
    path.mkdir(parents=True, exist_ok=True)
    filerun1 = open(path / "index.html", "w")
    filerun2 = open(path / "main.css", "w")
    filerun3 = open(path / "script.js", "w")
    inputx1 = T.get("1.0","end-1c")
    inputx2 = T2.get("1.0","end-1c")
    inputx3 = T3.get("1.0","end-1c")
    filerun1.write(inputx1)
    filerun2.write(inputx2)
    filerun3.write(inputx3)
    filerun1.close()
    filerun2.close()
    filerun3.close()
    webbrowser.open_new(path / "index.html")
    return

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Importer Html", command=importer1)
menu1.add_command(label="Importer Css", command=importer2)
menu1.add_command(label="Importer JS", command=importer3)
menu1.add_command(label="Save", command=save)
menu1.add_command(label="Run", command=run)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Template html.", command=htmlx1)
menu2.add_command(label="Template css.", command=cssx1)
menu2.add_command(label="Template JS.", command=jsx1)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Discord", command=OpenUrl)
menubar.add_cascade(label="Aide", menu=menu3)

T = tk.Text(fenetre, height=40, width=50, relief="solid", borderwidth=4)
T2 = tk.Text(fenetre, height=40, width=50, relief="solid", borderwidth=4)
T3 = tk.Text(fenetre, height=40, width=50, relief="solid", borderwidth=4)
T.pack(padx=5, pady=2, side=tk.LEFT)
T2.pack(padx=5, pady=2, side=tk.LEFT)
T3.pack(padx=5, pady=2, side=tk.LEFT)
T.insert(tk.END, "Ici html.")
T.configure(bg='yellow')
T2.insert(tk.END, "Ici css.")
T2.configure(bg='yellow')
T3.insert(tk.END, "Ici js.")
T3.configure(bg='yellow')
fenetre.config(menu=menubar)

fenetre.bind("<Control-r>", runx1)
fenetre.bind("<Control-s>", savex1)

fenetre.mainloop()
