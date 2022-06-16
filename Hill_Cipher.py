#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import tkinter as tk
from tkinter.constants import CENTER
import tkinter.messagebox
import webbrowser


# In[2]:


def encryption(m, a):
    
    temp = np.empty(3)
    l = len(m)
    ldiv = int(l/3)
    if l % 3 != 0:
        ldiv = ldiv + 1
    cipher_num = np.empty(ldiv*3)
    for i in range(ldiv):
        n = i*3
        if l % 3 == 1 and i == ldiv-1:
            if m[n] == ' ':
                temp[0] = 26
            elif m[n] == ',':
                temp[0] = 27
            elif m[n] == '.':
                temp[0] = 28
            else:
                temp[0] = ord(m[n])-ord('a')
            temp[1] = 26
            temp[2] = 26
            temp = a.dot(temp)
            cipher_num[n] = temp[0]%29
            cipher_num[n+1] = temp[1]%29
            cipher_num[n+2] = temp[2]%29
        elif l % 3 == 2 and i == ldiv-1:
            if m[n] == ' ':
                temp[0] = 26
            elif m[n] == ',':
                temp[0] = 27
            elif m[n] == '.':
                temp[0] = 28
            else:
                temp[0] = ord(m[n])-ord('a')
            if m[n+1] == ' ':
                temp[1] = 26
            elif m[n+1] == ',':
                temp[1] = 27
            elif m[n+1] == '.':
                temp[1] = 28
            else:
                temp[1] = ord(m[n+1])-ord('a')
            temp[2] = 26
            temp = a.dot(temp)
            cipher_num[n] = temp[0]%29
            cipher_num[n+1] = temp[1]%29
            cipher_num[n+2] = temp[2]%29
        else:
            if m[n] == ' ':
                temp[0] = 26
            elif m[n] == ',':
                temp[0] = 27
            elif m[n] == '.':
                temp[0] = 28
            else:
                temp[0] = ord(m[n])-ord('a')
            if m[n+1] == ' ':
                temp[1] = 26
            elif m[n+1] == ',':
                temp[1] = 27
            elif m[n+1] == '.':
                temp[1] = 28
            else:
                temp[1] = ord(m[n+1])-ord('a')
            if m[n+2] == ' ':
                temp[2] = 26
            elif m[n+2] == ',':
                temp[2] = 27
            elif m[n+2] == '.':
                temp[2] = 28
            else:
                temp[2] = ord(m[n+2])-ord('a')
            temp = a.dot(temp)
            cipher_num[n] = temp[0]%29
            cipher_num[n+1] = temp[1]%29
            cipher_num[n+2] = temp[2]%29
    cipher = []
    for i in range(ldiv*3):
        if cipher_num[i] == 26:
            cipher.append(' ')
        elif cipher_num[i] == 27:
            cipher.append(',')
        elif cipher_num[i] == 28:
            cipher.append('.')
        else:
            cipher.append(chr(int(cipher_num[i])+ord('a')))
    s = ''
    s = s.join(cipher)
    return s


# In[3]:


def decryption(s, a):
    b =  np.linalg.inv(a)
    b = b*np.linalg.det(a)
    b = b % 29
    b = np.around(b)
    deta = int(round(np.linalg.det(a) % 29))
    k = 0
    for i in range(29):
        if (i * deta) % 29 == 1:
            k = i
            break
    b = k * b
    temp2 = np.empty(3)
    l2 = len(s)
    ans_num = np.empty(l2)
    b = b % 29
    for i in range(int(l2/3)):
        n = i * 3
        if s[n] == ' ':
            temp2[0] = 26
        elif s[n] == ',':
            temp2[0] = 27
        elif s[n] == '.':
            temp2[0] = 28
        else:
            temp2[0] = ord(s[n])-ord('a')
        if s[n+1] == ' ':
            temp2[1] = 26
        elif s[n+1] == ',':
            temp2[1] = 27
        elif s[n+1] == '.':
            temp2[1] = 28
        else:
            temp2[1] = ord(s[n+1])-ord('a')
        if s[n+2] == ' ':
            temp2[2] = 26
        elif s[n+2] == ',':
            temp2[2] = 27
        elif s[n+2] == '.':
            temp2[2] = 28
        else:
            temp2[2] = ord(s[n+2])-ord('a')
        temp2 = b.dot(temp2)
        ans_num[n] = round(temp2[0]%29)
        ans_num[n+1] = round(temp2[1]%29)
        ans_num[n+2] = round(temp2[2]%29)
    ans = []
    for i in range(l2):
        if ans_num[i] == 26:
            ans.append(' ')
        elif ans_num[i] == 27:
            ans.append(',')
        elif ans_num[i] == 28:
            ans.append('.')
        else:
            ans.append(chr(int(ans_num[i])+ord('a')))
    s2 = ''
    s2 = s2.join(ans)
    return s2


# In[6]:


txt = 'i'

win = tk.Tk()
win.title('Hill Cipher')
win.geometry('720x480') #width x height


#label
lbl_1 = tk.Label(win, text='Text you want to encrypt/decrypt (Can only allowed  lower-case letters, spaces, comma and period) :', font=('Arial', 12))
lbl_2 = tk.Label(win, text='Key (Normally will be a 9 lower-case letter code) :', font=('Arial', 12))
lbl_3 = tk.Label(win, text='The text after encryption: ', font=('Arial', 15))

lbl_1.grid(column=0, row=0, padx=0, pady=10)
lbl_2.place(x=2,y=80)
lbl_3.place(x=2,y=300)

#text
text_1 = tk.Text(win, width = 96, height = 2)
text_2 = tk.Text(win, width = 15, height = 2)
text_3 = tk.Text(win, width = 50, height = 2)

text_1.grid(column = 0, row = 1)
text_2.place(x=350,y=80)
text_3.place(x=235,y=300)

def callback():
    webbrowser.open_new(r'https://youtu.be/dQw4w9WgXcQ')
    
def callback2():
    webbrowser.open_new(r'https://youtu.be/dMTy6C4UiQ4')

def copy():
    global txt
    win.clipboard_clear()
    win.clipboard_append(txt)

def key_trans(k):
    numk = np.empty(9)
    for i in range(9):
        if k[i] == ' ':
            numk[i] = 26
        elif k[i] == ',':
            numk[i] = 27
        elif k[i] == '.':
            numk[i] = 28
        else:
            numk[i] = ord(k[i])-ord('a')
    nkey = np.array([[numk[0],numk[1],numk[2]],[numk[3],numk[4],numk[5]],[numk[6],numk[7],numk[8]]]) 
    kdet = int(np.linalg.det(nkey))
    state = 0
    for i in numk:
        if i > 28 or i < 0:
            state = 1
    if kdet == 0 or state == 1:
        return 0, 0
    else:
        return 1, nkey
        

def Hill_Cipher_encryption():
    sentence = text_1.get("1.0","end")
    key = text_2.get("1.0","end")
    sentence_temp = '1'
    key_temp = '1'
    while sentence != sentence_temp:
        sentence_temp = sentence
        sentence = sentence.strip('\n')
        sentence = sentence.strip(' ')
    while key != key_temp:
        key_temp = key
        key = key.strip('\n')
        key = key.strip(' ')
        
    if len(key) == 9:
        state, arrkey = key_trans(key)
        if state == 1:
            cipher = encryption(sentence, arrkey)
            lbl_3.configure(text='The text after encryption: ')
            text_3.delete("1.0","end")
            text_3.insert('1.0', cipher)
            global txt
            txt = cipher
        else:
            msg = 'Sorry, the key which you have entered won\'t work in Hill Cipher'
            tkinter.messagebox.showinfo(title = 'Error', message = msg)
    else:
        msg = 'Sorry, the key has to have 9 letters.'
        tkinter.messagebox.showinfo(title = 'Error', message = msg) 

def Hill_Cipher_decryption():
    sentence = text_1.get("1.0","end")
    key = text_2.get("1.0","end")
    sentence_temp = '1'
    key_temp = '1'
    while sentence != sentence_temp:
        sentence_temp = sentence
        sentence = sentence.strip('\n')
        sentence = sentence.strip(' ')
    while key != key_temp:
        key_temp = key
        key = key.strip('\n')
        key = key.strip(' ')
    
    if len(key) == 9:
        state, arrkey = key_trans(key)
        if state == 1:
            cipher = decryption(sentence, arrkey)
            lbl_3.configure(text='The text after decryption: ')
            text_3.delete("1.0","end")
            text_3.insert('1.0', cipher)
            global txt
            txt = cipher


def ex_key():
    text_2.insert('1.0', 'lctfxzuhr')

#button
button_1 = tk.Button(win, text = 'Encryption', font=('Arial', 12), bg = 'white', fg = 'black', command = Hill_Cipher_encryption)
button_2 = tk.Button(win, text = 'Decryption', font=('Arial', 12), bg = 'white', fg = 'black', command = Hill_Cipher_decryption)
button_3 = tk.Button(win, text = 'Summon an example key', bg = 'white', fg = 'black', font=('Arial', 12), command = ex_key)
button_4 = tk.Button(win, text = 'Copy the text', bg = 'white', fg = 'black', font=('Arial', 12), command = copy)
button_5 = tk.Button(win, text = 'Simple tutorial of how this works.', bg = 'white', fg = 'black', font=('Arial', 12), command = callback)
button_6 = tk.Button(win, text = 'Bug report', bg = 'white', fg = 'black', font=('Arial', 12), command = callback2)

button_1.place(x=220,y=150)
button_2.place(x=400,y=150)
button_3.place(x=465,y=80)
button_4.place(x=600,y=300)
button_5.place(x=260,y=380)
button_6.place(x=330,y=420)

win.mainloop()


# In[ ]:





# In[ ]:




