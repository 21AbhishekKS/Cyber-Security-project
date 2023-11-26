

import cv2
import os
import string
import tkinter as tk
from tkinter import filedialog
from tkinter import Button

  #Secret Messages



def openfile():

    filepath = filedialog.askopenfilename()
    file = open(filepath,'r')

    img = cv2.imread(filepath,cv2.CAP_PROP_XI_COLOR_FILTER_ARRAY)   # read image in array

    msg = input("Enter secert message")
    password = input("Enter password")

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i  # dictionary  Maps each character to its ASCII code value.
        c[i] = chr(i)  # dictionary  Maps each ASCII code value to its corresponding character.

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n,m,z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3  # 3 because

    cv2.imwrite("Encryptedmsg.jpg", img)

    os.system("start Encryptedmsg.jpg")

    message = ""

    n = 0
    m = 0
    z = 0

    pas = input("Enter passcode for Decryption")

    if password == pas:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decryption message", message)
    else:
        print("Not valid key")



window = tk.Tk()

window.title("Stegno")
window.geometry("500x300")


label = tk.Label(text="choose a cover image",font=('Cooper Black',20),)
label.pack(padx=50,pady=50)

btn1 = tk.Button(window,text="choose",font=('Times New Roman',10),command= openfile,background="#007bff")
btn1.pack(padx=50,pady=30)
window.mainloop()











