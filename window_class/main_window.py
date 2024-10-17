import tkinter as tk
import tkinter.messagebox as messagebox

from game_function.create_massive import create_massive, mines_around


class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Сапер')
        self.geometry('400x400')
        self.grid_game = None
        self.massive_game = None
        self.n = 12
        self.massive_button = None

        self.create_game = tk.Button(self, text='Новая игра', command=self.create_game)
        self.create_game.pack(padx=10, pady=10)

    def create_game(self):
        if self.grid_game is None:
            self.grid_game = tk.Frame(self)
        else:
            self.grid_game.destroy()
            self.grid_game = tk.Frame(self)
        self.grid_game.pack(padx=10, pady=10)
        self.n = 12
        self.massive_game = create_massive(self.n)
        self.massive_button = []
        for i in range(10):
            new_row = []
            for j in range(10):
                button = tk.Button(self.grid_game, text='', width=2, height=1)
                button.around_mine = mines_around(i, j, self.massive_game)
                button.status = self.massive_game[i][j]
                button.i = i
                button.j = j
                button.bind('<Button-1>', lambda e, b=button: self.open_cell(e, b))
                button.bind('<Button-3>', lambda e: e.widget.configure(text='M'))
                button.grid(row=i, column=j)
                new_row.append(button)
            self.massive_button.append(new_row)

    def open_cell(self, event: tk.Event, button: tk.Button):

        if button.status == 1:
            button.status = 'disabled'
            button['text'] = '*'
            button.configure(state='disabled')
            button.unbind('<Button-1>')
            button.unbind('<Button-3>')
            messagebox.showinfo('Сапер', 'Вы проиграли')
            for i in self.massive_button:
                for b in i:
                    b.configure(text=f'{b.around_mine if b.status == 0 else '*'}')
                    b.configure(state='disabled')
                    b.unbind('<Button-1>')
                    b.unbind('<Button-3>')

        elif button.around_mine == 0:
            button['text'] = '0'
            button.configure(state='disabled')
            button.unbind('<Button-1>')
            button.unbind('<Button-3>')
            i = button.i
            j = button.j
            for i_ in range(i - 1, i + 2):
                for j_ in range(j - 1, j + 2):
                    if 0 <= i_ < 10 and 0 <= j_ < 10 and (i_ != i or j_ != j):
                        if (self.massive_button[i_][j_].around_mine == 0
                                and self.massive_button[i_][j_]['state'] == 'normal'):
                            self.open_cell(event, self.massive_button[i_][j_])
                        if self.massive_button[i_][j_].around_mine != 0:
                            self.open_cell(event, self.massive_button[i_][j_])

        elif button.around_mine != 0:
            button['text'] = button.around_mine
            button.configure(state='disabled')
            button.unbind('<Button-1>')
            button.unbind('<Button-3>')

        sum_normal = 0
        for i in self.massive_button:
            for b in i:
                if b['state'] == 'normal':
                    sum_normal += 1

        if sum_normal <= self.n:
            messagebox.showinfo('Сапер', 'Вы выиграли')
            for i in self.massive_button:
                for b in i:
                    b.configure(text=f'{b.around_mine if b.status == 0  else '*'}')
                    b.configure(state='disabled')
                    b.unbind('<Button-1>')
                    b.unbind('<Button-3>')



    def notice_cell(self, event: tk.Event):
        b: tk.Button = event.widget
        if b['text'] != '0':
            b.configure(text='M')
        else:
            b.configure(text='')
