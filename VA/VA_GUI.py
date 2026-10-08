import tkinter as tk 

###create error class
class Inputerror(Exception):
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

ent_antal = tk.Entry(
    bg = 'white',
    fg = 'black',
    master= frame_controlpanel, 
    )
ent_antal.pack(fill = tk.X)
antal_str = ent_antal.get()

try:
    antal_float = float(antal_str)
    try:
        antal_float > 0 == True
    except:
        raise Inputerror ('Input must be a positive string or float!')

except:
    raise Inputerror ('Input must be a positive string or float!')


lbl_hastighet = tk.Label(master = frame_controlpanel, text = 'Hastighet:')
lbl_hastighet.pack()


ent_hastighet = tk.Entry(
    bg = 'white',
    fg = 'black',
    master= frame_controlpanel, 
    )
ent_hastighet.pack(fill = tk.X)
hastighet = ent_hastighet.get()


def read_inputs():
    ##antal
    
    antal_str = ent_antal.get()

    try:
        antal_float = float(antal_str)
        try:
            antal_float > 0 == True
        except:
            raise Inputerror ('Input must be a positive string or float!')

    except:
        raise Inputerror ('Input must be a positive string or float!')

    ## hastighet
    
    hastighet_str = ent_hastighet.get()

    try:
        hastighet_float = float(hastighet_str)
        try:
            hastighet_float > 0 == True
        except:
            raise Inputerror ('Input must be a positive string or float!')

    except:
        raise Inputerror ('Input must be a positive string or float!')

    

##create buttons 

btn_initiera = tk.Button(
    text = 'Initiera',
    bg = 'white',
    fg = 'black',
    master= frame_controlpanel, 
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
