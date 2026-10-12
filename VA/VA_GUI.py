'''
Student: Lars Kirchner
Mail: lasse.kirchner@gmail.com
TA:
Date: 12/10/2026
'''

import tkinter as tk 
import tkinter.messagebox as messagebox 
import random
from math import pi

###create error class
class InputError(Exception):
    pass


## create class ball
class Ball():

    def __init__(self):
        self.alive = True ##used for eat 

        self.color = 'red'
        self.canvas_item_id = None 

        self.radius = random.randint(5, 20)


        ##note: fart can be negative if we move up in the window! 
        self.fart_x = random.randint(-10, 10) #notera fart ej samma som hastighet! 
        self.fart_y = random.randint(-10, 10) #notera fart ej samma som hastighet! 

        while self.fart_x == 0 and  self.fart_y == 0: ##prevents balls from having x = 0 and y = 0 
            self.fart_x = random.randint(-10, 10)
            self.fart_y = random.randint(-10, 10)

        self.x_coordinate = random.randint(0 + self.radius , size_arena_x - self.radius) #starting positions
        self.y_coordinate = random.randint(0 + self.radius, size_arena_y - self.radius) #starting positions


    def move(self):
        self.x_coordinate += self.fart_x
        self.y_coordinate += self.fart_y
        #print(self.x_coordinate, self.y_coordinate) ##test


    def bounce_wall(self, size_arena_x, size_arena_y):
        ## right wall:
        if self.radius + self.x_coordinate >= size_arena_x:  
            self.fart_x = - self.fart_x #invert fart
            self.x_coordinate = size_arena_x - self.radius #prevents balls from being "outside" the arena
            #print('BOUNCE right')

        #left wall
        elif self.x_coordinate - self.radius <= 0 :
            self.fart_x = - self.fart_x #invert fart 
            self.x_coordinate = self.radius #prevents balls from being "outside" the arena
            #print('BOUNCE left')


        ##bottom wall
        if self.radius + self.y_coordinate >= size_arena_y:
            self.fart_y = - self.fart_y #invert fart
            self.y_coordinate = size_arena_y - self.radius #prevents balls from being "outside" the arena
            #print('BOUNCE bottom')
        ##top wall
        elif self.y_coordinate - self.radius <= 0:
            self.fart_y = - self.fart_y #invert fart
            self.y_coordinate = self.radius #prevents balls from being "outside" the arena
            #print('BOUNCE top')

    def bounding_box(self): #gets coords for the bounding box of the circle 
        x_0 = self.x_coordinate - self.radius #top left
        y_0 = self.y_coordinate - self.radius #top left
        x_1 = self.x_coordinate + self.radius #bottom right
        y_1 = self.y_coordinate + self.radius #bottom right
        return x_0, y_0, x_1, y_1


    def overlaps(self, other):
        sum_radii_squared = (self.radius + other.radius)**2 ##avoids root in distance 
        dist_between_centers_squared = (self.x_coordinate - other.x_coordinate)**2 +  (self.y_coordinate - other.y_coordinate)**2

        if self.alive == False or other.alive == False:
            overlap = False
            #print('dead') #test 2 
            return overlap


        if dist_between_centers_squared < sum_radii_squared:
            overlap = True
            #print('overlap!') #test 2
        else:
            overlap = False
            #print('no overlap') #test 2

        return overlap 


    def eat(self, other):
        if self.radius > other.radius:
            #taking int makes radii comaprison easier! 
            self.radius += int(other.radius / (pi)) ##keeps balls a little smaller
            other.alive = False 
            other.radius = 0 

        elif self.radius == other.radius: #handles edge case 
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
ent_antal.insert(0, '10') #default value for antal


lbl_hastighet = tk.Label(master = frame_controlpanel, text = 'Hastighet:')
lbl_hastighet.pack()

ent_hastighet = tk.Entry(master = frame_controlpanel)
ent_hastighet.pack(fill = tk.X)
ent_hastighet.insert(0, '100') #default value for speed

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

    
## create command function for btn initiera
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
        x_0, y_0, x_1, y_1 = ball.bounding_box()
        ball.canvas_item_id = canvas_arena.create_oval(x_0, y_0, x_1, y_1, fill = ball.color)
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


## functions needed to start simulation:


def move_all():
    for ball in balls:
        ball.move()
        ball.bounce_wall(size_arena_x, size_arena_y)

def handle_collisions_old():
    tail = 0
    head = 1
    for _ in range(1, len(balls)):
        ball_tail = balls[tail]
        ball_head = balls[head]
        if ball_head.alive == True and ball_tail.alive == True:
            tail += 1
            head += 1 
            if Ball.overlaps(ball_head, ball_tail) == True:
                Ball.eat(ball_head, ball_tail)
        else:
            tail += 1
            head += 1

def handle_collisions(): #takes care of eating 
    for outer in range(0, len(balls)):
        ball_outer = balls[outer]
        for inner in range (outer, len(balls)): 
            ball_inner = balls[inner]
            if ball_outer.alive == True and ball_inner.alive == True:
                if Ball.overlaps(ball_outer, ball_inner) == True:
                    Ball.eat(ball_outer, ball_inner)
    


def remove_dead():
    balls_copy = balls.copy() ##copy list so that we dont need new globale variable
    balls.clear() #clear og balls 
    for ball in balls_copy:
        if ball.alive == False:
            canvas_arena.delete(ball.canvas_item_id) #remove from arena 
        else:
            balls.append(ball) ##add survivors to cleared balls 
    

def reanimate():
    for ball in balls:
        canvas_arena.coords(ball.canvas_item_id, *ball.bounding_box())
        canvas_arena.itemconfigure(ball.canvas_item_id, fill = ball.color)
    ##ful jävla funktion, är i stort sätt:
    #canvas.coord(cikel, *bounding box), alltså uppdateras bara koordinaterna av cirkel
  

loop_id = None ###behövs för tick och starta
def tick():
    #run the four steps, if len >1, schedule a new tick, else stop
    move_all()
    handle_collisions()
    remove_dead()
    reanimate()
    if len(balls) > 1:
        ### note! taking 1 / hastighet causes the speed to behave intuetivly
        #i.e. higher vlaues => faster 
        #take the int of that value to fint window.after specification
        ## 1000 is an arbitraty factor to make the input numbers resonable
        loop_id = window.after(int( 1000 * (1 / parameters['hastighet'])), tick)
        #function has the form: window.after(delay_ms, function)
    else:
        loop_id = None 
        messagebox.showinfo('Simulation information', 'Simulation Finished!')

    

def starta():
    #nothing to run if len(balls) = 0
    #dont start second sim if sim already underway
    #otherwise: start the first tick
    if len(balls) == 0:
        messagebox.showinfo('Error!', 'Nothing to simulate! Enter values and/or initiate a simulation!')
    else:
        if loop_id == None:
            tick()
        else:
            messagebox.showinfo('Error!', 'Cannot start a simulation while a current one is ongoing.')



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

def avsluta():
    messagebox.showinfo('Simulation information', 'Avslutar simultionen')
    window.destroy()


btn_avsluta = tk.Button(
    text='Avsluta',
    bg = 'white',
    fg = 'Red',
    master= frame_controlpanel, 
    command = avsluta
    )
btn_avsluta.pack(fill = tk.X)



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


window.mainloop() #runs an unbroken loop for tinker, i.e. no new prompt appears in terminal
