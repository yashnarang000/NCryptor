import sys
import NCryptor.ncryptor as nc
import tkinter as tk
from main import codewords
from PIL import Image, ImageTk
import pyperclip as pc

ncrypt = nc.NCrypt(codewords, "[^a-zA-Z0-9. /:_%&]", "0")

default_bg = "#1e1e1e"

root = tk.Tk()
root.title("NCryptor")
root.configure(bg=default_bg)
root.state("zoomed")
# root.attributes("-fullscreen", True)

width = 1600
height = 800

root.geometry(f"{width}x{height}")

ncryptor_1 = nc.NCrypt(codewords, "[^a-zA-Z0-9. /:_%&]", "0")


frame1 = tk.Frame(root, height=200, width=1600, bg=default_bg)
frame1.pack(fill="x", side=tk.TOP, anchor="n")

frame2 = tk.Frame(bg=default_bg, height=600, width=1600)
frame2.pack(fill = "x", side=tk.BOTTOM, anchor="s")

# title = Image.open("title1.png")
# title = title.resize((600, 225),Image.Resampling.LANCZOS)
# title = ImageTk.PhotoImage(image=title)
# tk.Label(frame1,image=title,borderwidth=0, bg=default_bg).place(x=500, y=1)

tk.Label(frame1,text="</NCryptor>",borderwidth=0, bg=default_bg, font=["garamond", "100", "underline bold"], fg="#c1f5f5").place(x=400, y=1)


# tk.Label(frame2, text="MAIN MENU", font=["rockwell", "32", "underline"], bg=default_bg, fg="white").place(x=10, y=80)

canvas1 = tk.Canvas(width=600, height=400, bg="#283dfa", highlightthickness="0")
canvas1.place(x=100, y=250)
canvas2 = tk.Canvas(width=600, height=400, bg="#283dfa", highlightthickness="0")
canvas2.place(x=800, y=250)

# tk.Label(frame2,text="509035", borderwidth=0, bg=default_bg, font=["rockwell", "70"], fg="white").place(x=100,y=200)

canvas1.create_text(300,65, text="ENCRYPT TEXT", font=["agency fb", "100", "underline"], fill="#c1c1c1")
canvas1.create_text(80,200, text="ABC", font=["bahnshcrift", "50"], fill="white")
canvas1.create_text(450,200, text="509035", font=["terminal", "50"], fill="lime")

arrow = Image.open("arrow1.png")
arrow = arrow.resize((70, 70), Image.Resampling.LANCZOS)
arrow = ImageTk.PhotoImage(image=arrow)

canvas1.create_image(225, 200, image=arrow)

canvas2.create_text(300,65, text="DECRYPT TEXT", font=["agency fb", "100", "underline"], fill="#c1c1c1")
canvas2.create_text(520,200, text="ABC", font=["bahnshcrift", "50"], fill="white")
canvas2.create_text(150,200, text="509035", font=["terminal", "50"], fill="lime")

canvas2.create_image(380, 200, image=arrow)

def bg_red1(event): 
    canvas1.configure(bg="#fa2828")

def bg_red2(event): 
    canvas2.configure(bg="#fa2828")

def bg_blue1(event):
    canvas1.configure(bg="#283dfa")

def bg_blue2(event):
    canvas2.configure(bg="#283dfa")

canvas1.bind("<Enter>", bg_red1)
canvas1.bind("<Leave>", bg_blue1)

canvas2.bind("<Enter>", bg_red2)
canvas2.bind("<Leave>", bg_blue2)

quit0 = tk.Label(frame2, text="Press F1 to Quit or F11 to enter Full Screen", bg=default_bg, fg="white", font=["","10"])
quit0.pack(side=tk.BOTTOM, anchor="sw")

def encrypt(text):
    code = ncrypt.encrypt(text)
    k=0
    hidden=""
    while k<len(code):
        hidden += "*"
        k+=1
    
    hidden_code = tk.Label(text=f"Your Code :\n{hidden}", bg=default_bg, fg="white", font = ["terminal", "25"], wraplength="1400", justify=tk.LEFT)
    hidden_code.place(y=500, x=100)
    copy = tk.Button(text="Copy", font=["terminal", "15"], bg=default_bg, fg="white", command=lambda: pc.copy(code))
    copy.place(x=390, y=502)

def encrypt_text(event):
    global quit0
    frame1.destroy()
    frame2.destroy()
    canvas1.destroy()
    canvas2.destroy()
    quit0.destroy()

    if root.attributes('-fullscreen') == False:
        quit0 = tk.Label(text="Press F1 to Quit or F11 to enter Full Screen", bg=default_bg, fg="white", font=["","10"])
    else:
        quit0 = tk.Label(text="Press F1 to Quit or F11 to leave Full Screen", bg=default_bg, fg="white", font=["","10"])
    quit0.pack(side=tk.BOTTOM, anchor="sw")
    tk.Label(text="Enter text to encrypt : ", font=["terminal", "25"], fg="white", bg=default_bg).place(y=100, x=500)
    
    text = tk.StringVar()

    tk.Entry(textvariable=text, font="arial 25", bg=default_bg, fg="white", insertbackground="white", width="30").place(x=500, y=150)
    tk.Button(text="E N C R Y P T", command=lambda: encrypt(text.get()), font=["ms serif", "20"], bg=default_bg, fg="white").place(x=650, y=250)
    root.bind('<Return>', lambda event: encrypt(text.get()))


def decrypt(code):
    text = ncrypt.decrypt(code)
    
    yourtext = tk.Label(text=f"Your Secret Text :", bg=default_bg, fg="white", font = ["terminal", "25"], wraplength="800", justify=tk.LEFT)
    textoutput = tk.Label(text=f"{text}", bg=default_bg, fg="white", font = ["terminal", "25"], wraplength="1400", justify=tk.LEFT)
    yourtext.place(y=500, x=100)
    textoutput.place(y=600, x=100)

def codevar(inputcode):
    code = inputcode.get()
    decrypt(code)

def pastecode():
    code = pc.paste()
    decrypt(code)

def decrypt_text(event):
    global quit0
    frame1.destroy()
    frame2.destroy()
    canvas1.destroy()
    canvas2.destroy()
    quit0.destroy()

    if root.attributes('-fullscreen') == False:
        quit0 = tk.Label(text="Press F1 to Quit or F11 to enter Full Screen", bg=default_bg, fg="white", font=["","10"])
    else:
        quit0 = tk.Label(text="Press F1 to Quit or F11 to leave Full Screen", bg=default_bg, fg="white", font=["","10"])
    quit0.pack(side=tk.BOTTOM, anchor="sw")
    tk.Label(text="Enter code to decrypt : ", font=["terminal", "25"], fg="white", bg=default_bg).place(y=100, x=100)
    
    inputcode = tk.StringVar()

    tk.Entry(textvariable=inputcode, font="arial 25", bg=default_bg, fg="white", insertbackground="white", width="30").place(x=100, y=150)

    tk.Label(text="OR", font = "terminal 100", bg=default_bg, fg="white").place(x=700, y=150)

    tk.Button(text="Paste Text", font="terminal 30", bg=default_bg, fg="white", command=pastecode).place(x=900, y=175)

    tk.Button(text="D E C R Y P T", command=lambda: codevar(inputcode), font=["ms serif", "20"], bg=default_bg, fg="white").place(x=250, y=250)

    root.bind('<Return>', lambda event: codevar(inputcode))

def fullscreen(event):
    global quit0
    if root.attributes("-fullscreen") == False:
        root.attributes("-fullscreen", True)
        quit0.destroy()
        if frame2.winfo_exists() == 1:
            quit0 = tk.Label(frame2, text="Press F1 to Quit or F11 to leave Full Screen", bg=default_bg, fg="white", font=["","10"])
            quit0.pack(side=tk.BOTTOM, anchor="sw")
        else:
            quit0 = tk.Label(text="Press F1 to Quit or F11 to leave Full Screen", bg=default_bg, fg="white", font=["","10"])
            quit0.pack(side=tk.BOTTOM, anchor="sw")

    else:
        root.attributes("-fullscreen", False)
        quit0.destroy()
        if frame2.winfo_exists() == 1:
            quit0 = tk.Label(frame2, text="Press F1 to Quit or F11 to enter Full Screen", bg=default_bg, fg="white", font=["","10"])
            quit0.pack(side=tk.BOTTOM, anchor="sw")
        else:
            quit0 = tk.Label(text="Press F1 to Quit or F11 to enter Full Screen", bg=default_bg, fg="white", font=["","10"])
            quit0.pack(side=tk.BOTTOM, anchor="sw")

quit_bind = root.bind('<F1>', sys.exit)
root.bind('<F11>', fullscreen)

canvas1.bind("<Button>", encrypt_text)
canvas2.bind("<Button>", decrypt_text)

# TODO : add scrollbar to decrypt and add a back button

root.mainloop()