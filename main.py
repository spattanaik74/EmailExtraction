from tkinter import *
from tkinter import ttk, filedialog
from tkinter.scrolledtext import ScrolledText
import os
import pandas as pd
import scraper


def openFolder():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=window, initialdir=currdir, title='Pleas select')
    if len(tempdir) > 0:
        text.configure(state='normal')
        text.insert(END, f'file added' + '\n')
        text.insert(END, f'PATH: {tempdir}' + '\n')
        text.configure(state='disable')
    df = pd.read_csv(f'{tempdir}')
    return df.to_string()


window=Tk()
Framebig = Frame(window)
p1 = PhotoImage(file='./logo/email.png')
window.iconphoto(False, p1)

window.title('E.Xtraction')
window.geometry("500x200")
window.minsize(500, 200)
window.maxsize(500, 200)



pb = ttk.Progressbar(window, orient='horizontal', length='480')

pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

text = ScrolledText(window, width=58, height=6.3)
text.configure(state='disabled')
text.place(x= 10, y=80)

def startcommand():
    s = scraper.Scrapper("https://www.nichi.com/contact-us/")
    save = s.scrapping()
    for i in save:
        text.configure(state='normal')
        text.insert(END, f'website {i}........ scraped' + '\n')
        text.configure(state='disable')


start_button = ttk.Button(window, text="start", command=startcommand)
stop_button = ttk.Button(window, text="stop")
pause_button = ttk.Button(window, text="pause")
upload_button = ttk.Button(window, text="upload", command= openFolder)
export_button = ttk.Button(window, text="export")

start_button.place(x=10, y= 50)
stop_button.place(x= 90, y=50)
pause_button.place(x=170, y=50)
upload_button.place(x=335, y=50)
export_button.place(x=415, y=50)

# text = ScrolledText(window, width=58, height=6.3)
# text.configure(state='disabled')
# text.place(x= 10, y=80)

# for i in range(1, 100):
#     text.insert(END, f"website {i} ........completed " + '\n')



# scroll = Scrollbar(window, orient=VERTICAL, command=text.yview)
# text.config(yscrollcommand=scroll.set)
# scroll.grid(column=1, row=0, sticky='NS')



window.mainloop()
