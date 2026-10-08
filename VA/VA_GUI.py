import tkinter as tk 


window = tk.Tk()
button_initiera = tk.Button(
    text = 'Antal:',
    bg = 'white',
    fg = 'black',
    )
button_initiera.pack()

button_hastighet = tk.Button(
    text='Hastighet:',
    bg = 'white',
    fg = 'black',
    )
button_hastighet.pack()

button_starta = tk.Button(
    text='Starta',
    bg = 'white',
    fg = 'black',
    )
button_starta.pack()

button_rensa = tk.Button(
    text='Rensa',
    bg = 'white',
    fg = 'black',
    )
button_rensa.pack()

button_avsluta = tk.Button(
    text='Avsluta',
    bg = 'white',
    fg = 'Red',
    )
button_avsluta.pack()




window.mainloop() #runs an unbroken loop for tinker, i.e. no new prompt appears in terminal
