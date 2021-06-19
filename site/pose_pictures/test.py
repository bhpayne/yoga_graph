import os, re, Tkinter, ImageTk


def ls_rec(direc, filter_fun=lambda a: True):
    for (dirname, dirnames, fnames) in os.walk(direc):
        for fname in fnames:
            if filter_fun(fname):
                yield os.path.join(dirname, fname)


top = Tkinter.Tk()
image_label = Tkinter.Label(top)
text_label = Tkinter.Label(top, text="Below is an image")
images = ls_rec(os.getcwd(), lambda a: re.match(".*\\.jpg$", a))

imgL = []


def get_next_image(event=None):
    fname = images.next()
    print fname
    fhandle = open(fname)
    img = ImageTk.PhotoImage(file=fhandle)
    fhandle.close()
    imgL.append(img)
    image_label.config(image=img)


top.bind("<Return>", get_next_image)
image_label.pack(side="bottom")
text_label.pack(side="top")
get_next_image()
top.mainloop()
