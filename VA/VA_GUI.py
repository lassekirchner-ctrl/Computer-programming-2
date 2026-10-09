import tkinter as tk 
import tkinter.messagebox as messagebox 
import random


# create window 

window = tk.Tk()

size_arena_x = 500 ##global variables
size_arena_y = 400 ##global variables

### creating main frame : i.e. battle arena:
canvas_arena = tk.Canvas(master = window, height = size_arena_y, width=size_arena_x, bg = 'light blue')
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



###create error class
class InputError(Exception):
    pass


## create class ball

class Ball():

    def __init__(self):
        self.alive = True ##used for eat 

        self.color = 'red'
        self.canvas_item_id = None 

        self.radius = random.randint(5, 30)

        self.fart_x = random.randint(-10, 10)
        self.fart_y = random.randint(-10, 10)

        while self.fart_x == 0 and  self.fart_y == 0: ##prevents balls from having x = 0 and y = 0 
            self.fart_x = random.randint(-10, 10)
            self.fart_y = random.randint(-10, 10)

        self.x_coordinate = random.randint(0 + self.radius , size_arena_x - self.radius)
        self.y_coordinate = random.randint(0 + self.radius, size_arena_y - self.radius)


    def move(self):
        self.x_coordinate += self.fart_x
        self.y_coordinate += self.fart_y
        #print(self.x_coordinate, self.y_coordinate) ##test


    def bounce_wall(self, size_arena_x, size_arena_y):
        ## right wall:
        if self.radius + self.x_coordinate >= size_arena_x:  
            self.fart_x = - self.fart_x
            self.x_coordinate = size_arena_x - self.radius
            #print('BOUNCE right')

        #left wall
        elif self.x_coordinate - self.radius <= 0 :
            self.fart_x = - self.fart_x
            self.x_coordinate = self.radius
            #print('BOUNCE left')


        ##bottom wall
        if self.radius + self.y_coordinate >= size_arena_y:
            self.fart_y = - self.fart_y
            self.y_coordinate = size_arena_y - self.radius
            #print('BOUNCE bottom')
        ##top wall
        elif self.y_coordinate - self.radius <= 0:
            self.fart_y = - self.fart_y
            self.y_coordinate = self.radius
            #print('BOUNCE top')



    def eat(self, other):
        if self.radius > other.radius:
            #taking int makes radii comaprison easier! 
            self.radius += int(other.radius / 2) ##keeps balls a little smaller
            other.alive = False 
            other.radius = 0 

        elif self.radius == other.radius:
            pass #no ball shoudl win! 
        
        else:
             #taking int makes radii comaprison easier! 
            other.radius += int(self.radius / 2) ##keeps balls a little smaller
            self.radius = 0     
            self.alive = False   

        return self.alive, other.alive 


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

### tests ###

def test_bounce():
    ball1 = Ball()
    ball2 = Ball()
    ball3 = Ball()
    for i in range (0, 1000):
        ball1.move()
        ball1.bounce_wall(size_arena_x, size_arena_y)

        ball2.move()
        ball2.bounce_wall(size_arena_x, size_arena_y)

        
        ball3.move()
        ball3.bounce_wall(size_arena_x, size_arena_y)

#to get test bounce to work, remove hashtags in bounce with msg! 

#test_bounce()