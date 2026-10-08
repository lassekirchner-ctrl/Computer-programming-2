import tkinter as tk 
import tkinter.messagebox as messagebox 

###create error class
class InputError(Exception):
    pass



# create window 

window = tk.Tk()

### creating main frame : i.e. battle arena:
canvas_arena = tk.Canvas(master = window, height = 400, width= 500, bg = 'light blue')
canvas_arena.pack(fill = tk.Y, side = tk.LEFT, expand= True)

frame_controlpanel = tk.Frame(master = window,  height = 400, width= 200, bg = 'white')
frame_controlpanel.pack(fill = tk.Y, side = tk.RIGHT)


#create entries 

lbl_antal = tk.Label(master = frame_controlpanel, text = 'Antal:')
lbl_antal.pack()

ent_antal = tk.Entry(master = frame_controlpanel)
ent_antal.pack(fill = tk.X)
ent_antal.insert(0, '10')


lbl_hastighet = tk.Label(master = frame_controlpanel, text = 'Hastighet:')
lbl_hastighet.pack()

ent_hastighet = tk.Entry(master = frame_controlpanel)
ent_hastighet.pack(fill = tk.X)
ent_hastighet.insert(0, '10')

def helper_read_inputs(entry):
    ### checks if inputs are valid
    entry_str = entry.get()
    
    try:    
        entry_int = int(entry_str)
    except:
        raise InputError ('Input cannot be a word or letter, must be a positive integer')
    if entry_int <= 0:
        raise InputError ("Input must be a positive integer!")
    
    return entry_int

def read_inputs():
    antal = helper_read_inputs(ent_antal)
    hastighet = helper_read_inputs(ent_hastighet)
    return antal, hastighet

    
## create helper function for initiera
parameters = {} #antal, hastighet
def initiera():
    try:
        antal, hastighet = read_inputs()
        parameters['antal'] = antal
        parameters['hastighet'] = hastighet
        #temprary test:
        #print(antal, hastighet)
    except InputError as ie:
        messagebox.showerror('Invalid input', str(ie))

   


##create buttons 

btn_initiera = tk.Button(
    text = 'Initiera',
    bg = 'white',
    fg = 'black',
    master= frame_controlpanel, 
    command = initiera
    )
btn_initiera.pack(fill = tk.X)


btn_starta = tk.Button(
    text='Starta',
    bg = 'white',
    fg = 'black',
    master= frame_controlpanel, 
    )
btn_starta.pack(fill = tk.X)

btn_rensa = tk.Button(
    text='Rensa',
    bg = 'white',
    fg = 'black',
    master= frame_controlpanel, 
    )
btn_rensa.pack(fill = tk.X)

btn_avsluta = tk.Button(
    text='Avsluta',
    bg = 'white',
    fg = 'Red',
    master= frame_controlpanel, 
    )
btn_avsluta.pack(fill = tk.X)


 


window.mainloop() #runs an unbroken loop for tinker, i.e. no new prompt appears in terminal
