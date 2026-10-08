import tkinter as tk


#demo exc 1 create tinker window
def demo_tinker_1():
    window = tk.Tk()

    ### basic ###
    '''greeting = tk.Label(text="Python rocks!")
    greeting.pack()'''

    ###more advanced ###
    '''  label = tk.Label(
        text="Hello, Tkinter",
        foreground="white",  # Set the text color to white
        background="black"  # Set the background color to black
    )

    label.pack()'''

    ## hex version
    label = tk.Label(text="Hello, Tkinter", background="#34A2FE")
    label.pack()

    # can also be shortened to:
    #label = tk.Label(text="Hello, Tkinter", fg="white", bg="black")

    window.mainloop() #runs an unbroken loop for tinker, i.e. no new prompt appears in terminal

#demo_tinker_1()

def demo_tk_2():
    window = tk.Tk()
    label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
    ) 
    label.pack()
    window.mainloop()  

#demo_tk_2()

def tk_3(): #button example
    window = tk.Tk()
    label = tk.Label (text= 'Hello bro!')
    label.pack()
    button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    )
    button.pack()
    window.mainloop()

#tk_3()

def tk_4():
    window = tk.Tk()
    label = tk.Label (text= 'Hello bro!')
    label.pack()
    entry = tk.Entry(fg="yellow", bg="blue", width=50)
    entry.pack()
    window.mainloop()

#tk_4()

def tk_5():
    window = tk.Tk()
    label = tk.Label(text="Name")
    entry = tk.Entry()
    name = entry.get()
    label.pack()
    entry.pack()
    window.mainloop()
    

#tk_5()


def tk_6_text():
    window = tk.Tk()
    text_box = tk.Text()
    text_box.pack()
    window.mainloop()

#tk_6_text()

str = 'hej'
print(int(str))