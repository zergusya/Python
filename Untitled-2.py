from tkinter import *
import random
import time
 
def button_clicked():
    
    inpt_get = inpt.get()
    num = [random.randint(0, 100) for i in range(0, int(inpt_get))]
    for index, elem in enumerate(num):
        obj =  Label(window, text = elem)
        obj.grid(column=index + 3, row=2)
 
window = Tk()
window.title("Графический интрефейс")
window.geometry('200x100')
 
inpt = Entry(window, width = 5)
inpt.grid(column=2, row=1)
 
lbl = Button(window, text="Старт", command=button_clicked)
lbl.grid(column=1, row=1)
window.mainloop()

# from tkinter import *
# import random
# import time

# window = Tk()
# window.title("Графический интрефейс")
# window.geometry('200x100')

# def button_clicked():
    
#     inpt_get = inpt.get()
#     num = [random.randint(0, 100) for i in range(0, int(inpt_get))]

    

#     # n1.configure(text=num[1])
#     # n2.configure(text=num[2])
    
    
# inpt = Entry(window, width = 5)
# inpt.grid(column=2, row=1)

# lbl = Button(window, text="Старт", command=button_clicked)
# lbl.grid(column=1, row=1)

# n1 = Label(window, text="")
# n2 = Label(window, text="")



# n1.grid(column=3, row=2)
# n2.grid(column=4, row=2)


# window.mainloop()
















# from watchdog.observers import Observer
# import os 
# import time
# from watchdog.events import FileSystemEventHandler

# class Handler(FileSystemEventHandler):
#     def on_modified(self, event):
#         for filename in os.listdir(folder_track):
#             file = folder_track + "/" + filename
#             new_path = folder_dest + "/" + filename
#             os.rename(file, new_path)


# folder_track = '\test1'
# folder_dest = '\test2'

# handle = Handler()
# observer = Observer()
# observer.schedule(handle, folder_track, recursive=True)


# try: 
#     while(true):
#         time.sleep(10)
# except KeyboardInterrupt:
#     observer.stop()

# observer.join()