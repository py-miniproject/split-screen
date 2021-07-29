from tkinter import *

root1 = Tk()

btn1 = Button(root1,padx=10, pady=5, bg="green")
btn2 = Button(root1,padx=10, pady=5, bg="blue")
btn3 = Button(root1,padx=10, pady=5, bg="yellow")
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)



# root2 = Tk()
# root3 = Tk()
# root4 = Tk()


root1.geometry("120x30")
# root2.geometry("")
# root3.geometry("")
# root4.geometry("")


root1.mainloop()
# root2.mainloop()
# root3.mainloop()
# root4.mainloop()


