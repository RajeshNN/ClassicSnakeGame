from msvcrt import kbhit, getch
import tkinter as tk
from arena import arena, Snake_tkinter
import argparse

parser = argparse.ArgumentParser(description = 'The Classical Snake Game')
parser.add_argument("-v", "--verbose", help="executes the CLI version, omitting it executes the tkinter GUI version",
                    action="store_true")

def play_in_CLI():
    n1 = True
    while(n1):
        a = arena()
        while(not a.terminate):
            a.display()
            a = a.update()
        print("\n\t\t\t\tGAME OVER!!!")
        n2=True
        while(n2):
            print('\nWanna play another round?(Y/N):')
            c = getch()
            if c in [b'Y', b'y']:
                n2 = False
            elif c in [b'N', b'n']:
                n2 = False
                n1 = False
            else:
                print('\nWrong Input!')

args = parser.parse_args()
if args.verbose:
    play_in_CLI()
else:
    app = Snake_tkinter()
    tk.mainloop()
    
