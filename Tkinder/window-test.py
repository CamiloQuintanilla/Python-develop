import tkinter

#create window tkinder
window = tkinter.Tk()

window.geometry("750x450")

#title
window.title("Test-tkinder")

#icon
window.iconbitmap("./Tkinder/image/images.ico")

#text
text = "jiji"
text_window = tkinter.Label(window,text=text)
text_window.pack()
#block
window.resizable(0,0)

#go window
window.mainloop()