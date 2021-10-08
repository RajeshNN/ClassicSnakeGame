from msvcrt import kbhit, getch
import tkinter as tk
import utils
from snake import snake
from food import food
from score import score

class arena:
    def __init__(self):
        self.s = snake()
        self.f = food()
        self.scoring = score()
        self.terminate = 0
        self.removed_tail = None

    def update(self):
        if not self.s.body_chewed:
            if kbhit():
                x = getch()
                if self.s.head_dir == b'w' or self.s.head_dir == b's':
                    if x in [b'a', b'd']:
                        self.s.head_dir = x
                elif self.s.head_dir == b'a' or self.s.head_dir == b'd':
                    if x in [b'w', b's']:
                        self.s.head_dir = x
            if self.s.head.node==[self.f.p, self.f.q]:
                self.s.length += 1
                self.s.eaten = 1
                self.scoring.scores[-1] += 10
                self.f=food()
            self.removed_tail = self.s.move_snake()
            self.s.eaten = 0
            return self
        else:
            self.terminate = 1
            return self

    def edit_head_dir(self, key):
        if self.s.head_dir in [b'w', 'w', 's'] and key.char in ['a', 'd']:
            self.s.head_dir = key.char
        if self.s.head_dir in ['a', 'd'] and key.char in ['w', 's']:
            self.s.head_dir = key.char

    def display(self):
        utils.clearscreen()
        for i in range(32):
            for j in range(82):
                if i==31:
                    print('-', end='')
                    continue
                if j==81:
                    print('|', end='')
                    continue
                try:
                    if self.s.snake_coor_dict[str(i)+','+str(j)]:
                        print('*', end='')
                except:
                    if self.f.p==i and self.f.q==j:
                        print('ò', end='')
                    else:
                        print(' ', end='')
            print()
        print('\t\tSCORE: ', self.scoring.scores[-1], '\t\tHIGH SCORE: ', max(self.scoring.scores))

class Snake_tkinter:
    def __init__(self):
        self.w = tk.Tk(className='Classic Snake Game')
        self.c = tk.Canvas(self.w, height=310, width=810, bg='SpringGreen', highlightbackground='black')
        self.c.grid(columnspan = 1, rowspan = 1, sticky = 'n')
        self.title = self.c.create_text(420, 150, text = 'Classic Snake Game!', fill = 'Blue', font=('Helvetica 50 bold'))
        self.c2 = tk.Canvas(self.w, height=40, width=810, bg='SpringGreen', highlightbackground='black')
        self.c2.grid(rowspan=1, columnspan=6, sticky = 's')
        self.s1 = tk.Label(self.c2, text = 'SCORE:', bg='SpringGreen', font=('Helvetica 15 bold'))
        self.s2 = tk.Label(self.c2, text = 0, bg='SpringGreen', font=('Helvetica 15 bold'))
        self.s3 = tk.Label(self.c2, text = 'HIGH SCORE', bg='SpringGreen', font=('Helvetica 15 bold'))
        self.s4 = tk.Label(self.c2, text = 0, bg='SpringGreen', font=('Helvetica 15 bold'))
        self.s1.grid(row = 0, column = 0, ipadx = 20)
        self.s2.grid(row = 0, column = 1, ipadx = 20)
        self.s3.grid(row = 0, column = 2, ipadx = 20)
        self.s4.grid(row = 0, column = 3, ipadx = 20)
        self.btn1 = tk.Button(self.c2, bg = 'SpringGreen2', text = 'Stop', font=('Helvetica 10 bold'), width = 10, height = 1, command = lambda: self.stop_game())
        self.btn1.grid(row = 0, column = 4, ipadx = 10)
        self.btn2 = tk.Button(self.c2, bg = 'SpringGreen2', text = 'New Game', font=('Helvetica 10 bold'), width = 10, height = 1, command = lambda: self.new_game())
        self.btn2.grid(row = 0, column = 5, ipadx = 10)
        self.var = {}
        self.food = self.c.create_oval(0,0,1,1)
        self.cancel = True
        self.after_id = 0
        self.GO = 0
    def game_instance(self, a):
        if(not self.cancel):
            self.w.bind('<Key>', lambda i : a.edit_head_dir(i))
            buffer = a.s.length
            a.update()
            # move the snake
            temp = str(a.s.head.node[0])+','+str(a.s.head.node[1])
            self.var[temp] = self.c.create_rectangle(a.s.snake_coor_dict[temp][1]*10, a.s.snake_coor_dict[temp][0]*10, a.s.snake_coor_dict[temp][1]*10+10, a.s.snake_coor_dict[temp][0]*10+10, fill='blue', outline='blue')
            
            if buffer<a.s.length:  # if snake eats food
                self.s2.configure(text = a.scoring.scores[-1])
                self.s4.configure(text = max(a.scoring.scores))
                self.c.delete(self.food)
                self.food = self.c.create_oval(a.f.q*10, a.f.p*10, a.f.q*10 + 10, a.f.p*10 + 10, fill='red')
            else:  # if snake does not eat food
                self.c.delete(self.var[str(a.removed_tail[0])+','+str(a.removed_tail[1])])
            if a.terminate:
                self.cancel = True
                #self.var.clear()
            self.after_id = self.w.after(30, lambda: self.game_instance(a))
        else:
            self.w.after_cancel(self.after_id)
            self.GO = self.c.create_text(400, 170, text = 'GAME OVER!!!', font=('Helvetica 25 bold'))

    def run(self, a):
        
        # initialize food on canvas
        self.food = self.c.create_oval(a.f.q*10, a.f.p*10, a.f.q*10 + 10, a.f.p*10 + 10, fill='red')

        # initialize snake on canvas
        for i in a.s.snake_coor_dict:
            self.var[i] = self.c.create_rectangle(a.s.snake_coor_dict[i][1]*10, a.s.snake_coor_dict[i][0]*10, a.s.snake_coor_dict[i][1]*10+10, a.s.snake_coor_dict[i][0]*10+10, fill='blue', outline='blue')

    def new_game(self):
        self.cancel = False
        self.var.clear()
        self.c.delete('all')
        self.after_id = 0
        # initialize arena
        a = arena()
        self.s2.configure(text = a.scoring.scores[-1])
        self.run(a)
        self.game_instance(a)

    def stop_game(self):
        self.cancel = True
        self.var.clear()
