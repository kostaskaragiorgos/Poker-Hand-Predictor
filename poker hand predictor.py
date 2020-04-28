"""
Poker Hand Predictor
"""
from tkinter import Tk, Menu, Button, StringVar, OptionMenu, LEFT, RIGHT
from tkinter import messagebox as msg
import numpy as np
import pickle
def helpmenu():
    """ help menu funciton """
def aboutmenu():
    """ about menu function """
class PokerHandPredictor():
    """ Clipboard Saver Class"""
    def __init__(self, master):
        self.master = master
        self.master.title("Poker Hand Predictor")
        self.master.geometry("250x190")
        self.master.resizable(False, False)
        self.model= pickle.load( open('poker_hand_n_n.sav', "rb"))
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Predict")
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        suit_of_card1 = list(["Hearts", "Spades", "Diamonds", "Clubs"])
        self.suitc1 = StringVar(master)
        self.suitc1.set(suit_of_card1[0])
        self.suitofcard1menu = OptionMenu(self.master, self.suitc1, *suit_of_card1)
        self.suitofcard1menu.grid(row=0, column=0)
        rank_of_card1 = list(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
        self.rankc1 = StringVar(master)
        self.rankc1.set(rank_of_card1[0])
        self.rankofcard1menu = OptionMenu(self.master, self.rankc1, *rank_of_card1)
        self.rankofcard1menu.grid(row=0, column=1)
        suit_of_card2 = list(["Hearts", "Spades", "Diamonds", "Clubs"])
        self.suitc2 = StringVar(master)
        self.suitc2.set(suit_of_card2[0])
        self.suitofcard2menu = OptionMenu(self.master, self.suitc2, *suit_of_card2)
        self.suitofcard2menu.grid(row=1, column=0)
        rank_of_card2 = list(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
        self.rankc2 = StringVar(master)
        self.rankc2.set(rank_of_card2[0])
        self.rankofcard2menu = OptionMenu(self.master, self.rankc2, *rank_of_card2)
        self.rankofcard2menu.grid(row=1, column=1)
        suit_of_card3 = list(["Hearts", "Spades", "Diamonds", "Clubs"])
        self.suitc3 = StringVar(master)
        self.suitc3.set(suit_of_card3[0])
        self.suitofcard3menu = OptionMenu(self.master, self.suitc3, *suit_of_card3)
        self.suitofcard3menu.grid(row=2, column=0)
        rank_of_card3 = list(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
        self.rankc3 = StringVar(master)
        self.rankc3.set(rank_of_card3[0])
        self.rankofcard3menu = OptionMenu(self.master, self.rankc3, *rank_of_card3)
        self.rankofcard3menu.grid(row=2, column=1)
        suit_of_card4 = list(["Hearts", "Spades", "Diamonds", "Clubs"])
        self.suitc4 = StringVar(master)
        self.suitc4.set(suit_of_card4[0])
        self.suitofcard4menu = OptionMenu(self.master, self.suitc4, *suit_of_card4)
        self.suitofcard4menu.grid(row=3, column=0)
        rank_of_card4 = list(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
        self.rankc4 = StringVar(master)
        self.rankc4.set(rank_of_card4[0])
        self.rankofcard4menu = OptionMenu(self.master, self.rankc4, *rank_of_card4)
        self.rankofcard4menu.grid(row=3, column=1)
        suit_of_card5 = list(["Hearts", "Spades", "Diamonds", "Clubs"])
        self.suitc5 = StringVar(master)
        self.suitc5.set(suit_of_card5[0])
        self.suitofcard5menu = OptionMenu(self.master, self.suitc5, *suit_of_card5)
        self.suitofcard5menu.grid(row=4, column=0)
        rank_of_card5 = list(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
        self.rankc5 = StringVar(master)
        self.rankc5.set(rank_of_card5[0])
        self.rankofcard5menu = OptionMenu(self.master, self.rankc5, *rank_of_card5)
        self.rankofcard5menu.grid(row=4, column=1)
        self.pbutton = Button(self.master, text="Predict", command=self.prediction)
        self.pbutton.grid(row=5, column=5)
    def input_val(self):
        input= [self.suitc1.get(), self.rankc1.get(), self.suitc2.get(), self.rankc2.get(), self.suitc3.get(), self.rankc3.get(), self.suitc4.get(), self.rankc4.get(), self.suitc5.get(), self.rankc5.get()]
        return input
        
    def prediction(self):
        inputs = self.input_val()
        for i in range(len(inputs)):
            if inputs[i] == "Hearts":
                inputs[i] = int(1)
            elif inputs[i] == "Spades":
                inputs[i] = int(2)
            elif inputs[i] == "Diamonds":
                inputs[i] = int(3)
            elif inputs[i] == "Clubs":
                inputs[i] = int(4)
            elif inputs[i] == "J":
                inputs[i] = 11
            elif inputs[i] == "Q":
                inputs[i] = 12
            elif inputs[i] == "K":
                inputs[i] = 13
        for i in range(0, len(inputs)): 
            inputs[i] = int(inputs[i]) 
        print(inputs)
        hands = ("NO HAND", "ONE PAIR", "TWO PAIRS", "THREE OF A KIND", "STRAIGHT", "FLUSH","FOOL HOUSE", "FOUR OF A KIND", "STRAIGHT FLUSH", "ROYAL FLUSH")
        msg.showinfo("PREDICTION",str(hands[np.argmax(self.model.predict(np.array([inputs]).reshape(1, -1)))]))

    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function """
    root = Tk()
    PokerHandPredictor(root)
    root.mainloop()
if __name__ == '__main__':
    main()