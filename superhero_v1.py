#Superhero name generator
#Steven Sturrock

'''
V0.0.1 - 17.06.25: Initial version, non-functional, layout complete
'''

from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self):
        #Create window
        self.master = Tk()
        self.master.title("Superhero Name Generator")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)       
        
        #Create container
        self.container = Frame(self.master)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)     
        
        #Main heading
        self.main_heading = Label(self.master, text="Hero name generator", fg="white", bg="purple", font="Raleway 15 bold")
        self.main_heading.grid(row=0, column=0, sticky="NSEW")
        
        #Adjective heading
        self.adj_heading = Label(self.master, text="Choose an adjective...", font="Raleway 12 bold")
        self.adj_heading.grid(row=1, column=0, sticky="NSEW")
        
        #Adjective options
        self.adj_var = StringVar()
        self.opt1 = ttk.Radiobutton(self.master, text="Happy", variable=self.adj_var)
        self.opt1.grid(row=2, column=0, sticky="NSEW", padx=30)
        self.opt2 = ttk.Radiobutton(self.master, text="Awesome", variable=self.adj_var)
        self.opt2.grid(row=3, column=0, sticky="NSEW", padx=30)
        self.opt3 = ttk.Radiobutton(self.master, text="Outgoing", variable=self.adj_var)
        self.opt3.grid(row=4, column=0, sticky="NSEW", padx=30)
        self.opt4 = ttk.Radiobutton(self.master, text="Funky", variable=self.adj_var)
        self.opt4.grid(row=5, column=0, sticky="NSEW", padx=30)
        
        #Colour
        self.col_heading = Label(self.master, text="Enter a colour", font="Raleway 12 bold")
        self.col_heading.grid(row=6, column=0, sticky="NSEW")
        self.cbox = Entry(self.master, justify=CENTER)
        self.cbox.grid(row=7, column=0, sticky="NSEW", padx=30, pady=10)
        
        #Animal
        self.col_heading = Label(self.master, text="Pick an animal", font="Raleway 12 bold")
        self.col_heading.grid(row=8, column=0, sticky="NSEW")  
        self.animals = ["Takahe", "Kereru", "Ruru", "Karearea"]
        self.chosen_animal = StringVar()
        self.chosen_animal.set("")
        self.animal_combobox = ttk.Combobox(self.master, textvariable=self.chosen_animal, state="readonly")
        self.animal_combobox['values'] = self.animals
        self.animal_combobox.grid(row=9, column=0, sticky="NSEW", padx=30, pady=10)
        
        #Go command
        self.go_button = Button(self.master, text="GO!", font="Raleway 12 bold")
        self.go_button.grid(row=10, column=0, sticky="NSEW", padx=50, pady=10)
        
        #Output
        self.output = Label(self.master, text="Press 'GO!' to generate your superhero name!", font="Raleway 10 bold", fg="purple")
        self.output.grid(row=11, column=0, sticky="NSEW", padx=20, pady=10)
        
    def run(self):
        self.master.mainloop()        
        
                
        
app = GUI()
app.run()