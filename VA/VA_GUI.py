import tkinter as tk 
import tkinter.messagebox as messagebox 
import random

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


    def overlaps(self, other):
        sum_radii_squared = (self.radius + other.radius) ##avoids root in distance 
        dist_between_centers_squared = (self.x_coordinate - other.x_coordinate)**2 +  (self.y_coordinate - other.y_coordinate)**2

        if self.alive == False or other.alive == False:
            overlap = False
            print('dead') #test 2 
            return overlap


        if dist_between_centers_squared < sum_radii_squared:
            overlap = True
            print('overlap!') #test 2
        else:
            overlap = False
            print('no overlap') #test 2

        return overlap 


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
        create_balls()
    except InputError as ie:
        messagebox.showerror('Invalid input', str(ie))

#create balls and put them on the canvas! 
balls = []
#canvas.create_oval(x0, y0, x1, y1, fill=...
def create_balls():
    for _ in range (parameters['antal']):
        ball = Ball()
        balls.append(ball)
        ball.canvas_item_id = canvas_arena.create_oval(ball.x_coordinate - ball.radius, ball.y_coordinate - ball.radius, ball.x_coordinate + ball.radius, ball.y_coordinate + ball.radius, fill = ball.color)
        #print(ball.canvas_item_id)

##create buttons 

btn_initiera = tk.Button(
    text = 'Initiera',
    bg = 'white',
    fg = 'black',
    master= frame_controlpanel, 
    command = initiera
    )
btn_initiera.pack(fill = tk.X)


## starta

def starta():
    ## call initiera function, add command = starta to start btn
    pass

btn_starta = tk.Button(
    text='Starta',
    bg = 'white',
    fg = 'black',
    master= frame_controlpanel, 
    command = starta 
    )
btn_starta.pack(fill = tk.X)


## rensa

def rensa():
    balls.clear()
    canvas_arena.delete('all')
    #print(balls)


btn_rensa = tk.Button(
    text='Rensa',
    bg = 'white',
    fg = 'black',
    master= frame_controlpanel, 
    command = rensa 
    )
btn_rensa.pack(fill = tk.X)

#avsluta

def avsluta():
    pass 


btn_avsluta = tk.Button(
    text='Avsluta',
    bg = 'white',
    fg = 'Red',
    master= frame_controlpanel, 
    command = avsluta
    )
btn_avsluta.pack(fill = tk.X)


window.mainloop() #runs an unbroken loop for tinker, i.e. no new prompt appears in terminal

### tests ###

def test_bounce(): #test __init__ and move aswell
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

def test_overlaps():
    ball1 = Ball()
    ball2 = Ball()
    ball3 = Ball()
    for i in range (0, 100):
        ball1.move()
        ball1.bounce_wall(size_arena_x, size_arena_y)
        ball1.overlaps(ball2)
        ball1.overlaps(ball3)

        ball2.move()
        ball2.bounce_wall(size_arena_x, size_arena_y)
        ball2.overlaps(ball1)
        ball2.overlaps(ball3)
                
        
        ball3.move()
        ball3.bounce_wall(size_arena_x, size_arena_y)
        ball3.overlaps(ball2)
        ball3.overlaps(ball1)

#test_overlaps()

