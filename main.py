from tkinter import *
 
# root = None
# dnentryBox = None
# imeientryBox = None
# modelentrybox = None
# problementryBox = None
# procedentryBox = None
# resultentryBox = None
# copybutton = None

def copyCallBack():
    tx = 'dn:' + dnentryBox.get() + '//imei:' + imeientryBox.get() + '//modelo:' + modelentrybox.get() + '//' + problementryBox.get() + procedentryBox.get() + resultentryBox.get() + '//' + empleadoentryBox.get() + '//' + extensionentryBox.get() 
    resultText.set('')
    resultText.set(tx)

    root.clipboard_clear()
    root.clipboard_append(tx) 


root = Tk() #Create the base window
root.geometry("400x200")    # Sets the size of the base window
root.title("EasyReg by CotherArt")

frame = Frame(root) # Puts the frame into the windod
frame.pack()    # Displays the frame
    
dnframe = Frame(root)
dnframe.pack()
imeiframe = Frame(root)
imeiframe.pack()
modelframe  = Frame(root)
modelframe.pack()
problemframe = Frame(root)
problemframe.pack()
procedframe = Frame(root)
procedframe.pack()
copyframe = Frame(root)
copyframe.pack()
empleadoframe = Frame(root)
empleadoframe.pack()
extesionframe = Frame(root)
extesionframe.pack()

# DN row ---
dnlabel = Label(dnframe, text='DN:')
dnlabel.pack(side=LEFT)
dnentryBox = Entry(dnframe)
dnentryBox.pack(side=RIGHT)
# IMEI row ---
imeilabel = Label(imeiframe, text='IMEI:')
imeilabel.pack(side=LEFT)
imeientryBox = Entry(imeiframe)
imeientryBox.pack(side=RIGHT)
# MODEL row ---
modellabel = Label(modelframe, text='MODELO:')
modellabel.pack(side=LEFT)
modelentrybox = Entry(modelframe)
modelentrybox.pack(side=RIGHT)
# PROBLEM row ---
problemlabel = Label(problemframe, text='PROBLEM:')
problemlabel.pack(side=LEFT)
problementryBox = Entry(problemframe)
problementryBox.pack(side=RIGHT)
# PROCEDIMIENTO row --
procedlabel = Label(procedframe, text='PROCEDIMIENTO:')
procedlabel.pack(side=LEFT)
procedentryBox = Entry(procedframe)
procedentryBox.pack(side=RIGHT)
# COPY row ---
resultText = StringVar()
copybutton = Button(copyframe, text='Copiar', command=copyCallBack)
copybutton.pack(side=TOP)
resultentryBox = Entry(copyframe, width=60, textvariable=resultText)
resultentryBox.pack(side=TOP)

empleadolabel = Label(empleadoframe, text='# Empleado:')
empleadolabel.pack(side=LEFT)
empleadoentryBox = Entry(empleadoframe)
empleadoentryBox.pack(side=RIGHT)

extensionlabel = Label(extesionframe, text='# Extension:')
extensionlabel.pack(side=LEFT)
extensionentryBox = Entry(extesionframe)
extensionentryBox.pack(side=RIGHT)

root.mainloop()
