import tkinter as tk, customtkinter as ctk, random, csv, numpy as np

word = ''
morsecodelist = []
morseword = 0
inputlist = []
shiftvalue = 0
dashdotlist = []
squarelist = []
row = 0
space = -20
inputspace = 0

letters_dict = {
    'a': '12',
    'b': '2111',
    'c': '2121',
    'd': '211',
    'e': '1',
    'f': '1121',
    'g': '221',
    'h': '1111',
    'i': '11',
    'j': '1222',
    'k': '212',
    'l': '1211',
    'm': '22',
    'n': '21',
    'o': '222',
    'p': '1221',
    'q': '2212',
    'r': '121',
    's': '111',
    't': '2',
    'u': '112',
    'v': '1112',
    'w': '122',
    'x': '2112',
    'y': '2122',
    'z': '2211'
}


def getmorse(word):
    global morseword
    for i in range(5):
        letter = (word[0][i]).lower()
        morsecodelist.append(letters_dict[letter])
    morseword = int(''.join(morsecodelist))
    print(morseword)
    print(morsecodelist)


def getword():
    global word
    with (open('5LetterWordSheet.csv', 'r')) as f:
        reader = csv.reader(f)
        rows = list(reader)
        word = rows[np.random.randint(1, 488)]
        print(word)
        getmorse(word)

getword()

lettervalue = len(morsecodelist[0])

class createdash():
    global dashdotlist, row
    def __init__(self):
        self.dash = main_canvas.create_rectangle(40 + (shiftvalue * 80) + (inputspace * 20) + space, 60 + (row * 80), 90 + (shiftvalue * 80) + (inputspace * 20) + space, 70 + (row * 80), fill= 'white')
        dashdotlist.append(self.dash)

class createdot():
    global dashdotlist, row
    def __init__(self):
        self.dot = main_canvas.create_oval(55 + (shiftvalue * 80) + (inputspace * 20) + space, 55 + (row * 80), 75 + (shiftvalue * 80) + (inputspace * 20) + space, 75 + (row * 80), fill= 'white')
        dashdotlist.append(self.dot)

def deletesymbol():
    global dashdotlist
    main_canvas.delete(dashdotlist[-1])
    dashdotlist.pop(-1)


def dot_command():
    global shiftvalue, morsecodelist, inputspace, lettervalue
    if len(inputlist) <= (len(str(morseword)) - 1):
        inputlist.append(1)
        createdot()
        shiftvalue += 1
        if shiftvalue >= lettervalue:
            if inputspace < 4:
                inputspace += 1
                lettervalue += (len(morsecodelist[inputspace]))

def dash_command():
    global shiftvalue, morsecodelist, inputspace, lettervalue
    if len(inputlist) <= (len(str(morseword)) - 1):
        inputlist.append(2)
        createdash()
        shiftvalue += 1
        if shiftvalue >= lettervalue:
            if inputspace < 4:
                inputspace += 1
                lettervalue += (len(morsecodelist[inputspace]))

def backspace():
    global shiftvalue, inputspace, lettervalue, morsecodelist
    if (len(inputlist) > 0):
        inputlist.pop(-1)
        deletesymbol()
        if shiftvalue == (lettervalue - (len(morsecodelist[inputspace]))):
            lettervalue -= (len(morsecodelist[inputspace]))
            inputspace -= 1
        shiftvalue -= 1

def submit():
    global dashdotlist, row, shiftvalue, lettervalue, inputspace
    lettervalue2 = 0
    if (len(inputlist) == (len(str(morseword)))):
        for i in range(5):
            if (''.join([str(x) for x in(inputlist[lettervalue2 : len(morsecodelist[i]) + lettervalue2])])) == morsecodelist[i]:
                for x in range(lettervalue2, (len(morsecodelist[i])) + lettervalue2):
                    main_canvas.itemconfigure(squarelist[(6 * x) + row], outline= 'green', fill= 'green')
            elif (''.join([str(x) for x in(inputlist[lettervalue2 : len(morsecodelist[i]) + lettervalue2])])) in morsecodelist:
                for x in range(lettervalue2, (len(morsecodelist[i])) + lettervalue2):
                    main_canvas.itemconfigure(squarelist[(6 * x) + row], outline= 'yellow', fill= 'yellow')
            else:
                for x in range(lettervalue2, (len(morsecodelist[i])) + lettervalue2):
                    main_canvas.itemconfigure(squarelist[(6 * x) + row], outline= 'gray20', fill= 'gray20')

            lettervalue2 += (len(morsecodelist[i])) # do this for any scenario

        if (int(''.join([str(i) for i in inputlist]))) == morseword:
            (print('You Win!'))
            submit_button.destroy()
            dot_button.destroy()
            dash_button.destroy()
            backspace_button.destroy()
            winttext = ctk.CTkLabel(master= app, height= 500, width= 200, text= ''.join(word), font= ctk.CTkFont(family= 'Arial', size= 100))
            winttext.pack(pady= 0, padx= 20)

        dashdotlist.clear()
        inputlist.clear()
        row += 1
        shiftvalue = 0
        lettervalue = len(morsecodelist[0])
        inputspace = 0
            


#---------------------------------------------------------------------------------------

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('1000x750')
app.title('Morsel')

main_canvas = ctk.CTkCanvas(master= app, width= (80 * len(str(morseword))) + 250, height= 520, bg = 'gray10', highlightthickness= 0)
main_canvas.pack(pady= 50, padx= 50, expand= True)


characternum = 0

for i in range(5):
    space += 20
    for y in range(len(morsecodelist[i])):
        characternum += 1
        for x in range(6):
            new_rect = main_canvas.create_rectangle(30 + (80 * characternum) + space, 30 + (80 * x), 100 + (80 * characternum) + space, 100 + (80 * x), outline= 'gray20', width= 3)
            squarelist.append(new_rect)


button_frame = ctk.CTkFrame(master= app, width= 500, height= 80, bg_color= 'gray10', fg_color= 'gray10')
button_frame.pack(pady= (0, 75), padx= 50)

dot_button = ctk.CTkButton(master= button_frame, width = 70, height = 70, fg_color= 'gray20', text= '•', font= ctk.CTkFont(family= "Helvetica", size= 45), command= dot_command)
dot_button.configure()
dot_button.pack(side= ctk.LEFT, pady= 10, padx= 10, expand = False)
backspace_button = ctk.CTkButton(master= button_frame, width = 100, height = 70, fg_color= 'gray20', text= 'Backspace', command= backspace)
backspace_button.configure()
backspace_button.pack(side= ctk.RIGHT, pady= 10, padx= (75, 0), expand = False)
dash_button = ctk.CTkButton(master= button_frame, width = 70, height= 70, fg_color= 'gray20', text= '—', font= ctk.CTkFont(family= "Helvetica", size= 45), command= dash_command)
dash_button.configure()
dash_button.pack(side= ctk.RIGHT, pady= 10, padx= 0)

submit_button = ctk.CTkButton(master= app, width= 100, height= 70, fg_color= 'gray20', text= 'Submit', command= submit)
submit_button.pack(pady= (10, 30), padx= 20)

app.mainloop()