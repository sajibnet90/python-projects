from tkinter import *
def click():
    enterted_text=textentry.get()#collect text from textentry box
    output.delete(0.0,END) # clear the box from first line first charecter to end
    try:
        word_def= my_dictionary[enterted_text]
    except:
        word_def= "Sorry definition not found. Try another"
    output.insert(END,word_def)
### main:
window=Tk()
window.title("My glossary")
window.geometry('640x700')
## My photo attach
photo1= PhotoImage(file="img.png")
Label (window, image=photo1,bg='#336699',border=0).grid(row=0,column=0, sticky=W)
## create label
Label (window,text="Check Glossaries",fg="white",bg="#336699",font="none 20 bold italic",width=46).grid(row=1,column=0, sticky=W)
##Text box entry
textentry = Entry(window, width=20,bg="white",fg="black")
textentry.grid(row=3,column=0, sticky=W)

## Add button
Button(window, text= "submit",command=click).grid(row=4,column=0, sticky=W)

##another lebel


## create Text box
output= Text(window,width=25,height=10,wrap=WORD,bg="white",fg="black")
output.grid(row=5,column=0,sticky=W)

Label (window,text="Thank you",fg="white",bg="black",font="none 12 bold italic",width=21).grid(row=6,column=0, sticky=W)
## dictionary creating

my_dictionary= {
    'bug': 'Piece of code that causes problems',
    'mouse': 'A device for better controlling',
    'python': 'A programming language'
}

window.mainloop() #event handler