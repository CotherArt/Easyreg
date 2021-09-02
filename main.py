from tkinter import *

# root = None
# dn_entry = None
# imei_entry = None
# model_entry = None
# problem_entry = None
# proc_entry = None
# resultentryBox = None
# copybutton = None
porta_visible = False

def deletereg():
    resultentryBox.delete(0, 'end')

def copyCallBack(): # Boton de copiar
    deletereg() 
    
    tx = ''

    if dn_entry.get() != '':
        tx += 'dn:' + dn_entry.get()
    if imei_entry.get() != '':
        tx += '//imei:' + imei_entry.get()
    if model_entry.get() != '':
        tx += '//modelo:' + model_entry.get()
    if problem_entry.get() != '':
        tx += '//' + problem_entry.get()
    if proc_entry.get() != '':
        tx += '//' + proc_entry.get()
    tx += '//' + empleadoentryBox.get() + '//' + extensionentryBox.get() 
    
    resultentryBox.insert(0,tx)
    print(tx)

    root.clipboard_clear()
    root.clipboard_append(tx) 

def portCallBack():
    # global porta_visible
    # if porta_visible:
    #     porta_frame.pack_forget()
    # else:
    #     porta_frame.pack()
    # porta_visible = not porta_visible
    proc_entry.insert(0,'Se genera la solicitud de portabilidad para el numero: ' + dn_entry.get() + ' nip:' + nip_entry.get())
    
    

root = Tk() #Create the base window
root.geometry("450x400")    # Sets the size of the base window
root.title("EasyReg by CotherArt")

frame = Frame(root) # Puts the frame into the windod
frame.pack()    # Displays the frame
    
dn_frame = Frame(root, bd=4)
dn_frame.pack(fill=X)
imei_frame = Frame(root, bd=4)
imei_frame.pack(fill=X)
model_frame  = Frame(root, bd=4)
model_frame.pack(fill=X)
problem_frame = Frame(root, bd=4)
problem_frame.pack(fill=X)
proce_frame = Frame(root, bd=4)
proce_frame.pack(fill=X)
porta_frame = Frame(root, bd=4)
porta_frame.pack()
dn_porta_frame = Frame(porta_frame)
dn_porta_frame.pack()
nip_porta_frame = Frame(porta_frame)
nip_porta_frame.pack()

copyframe = Frame(root, bd=4)
copyframe.pack(fill=X)
emp_frame = Frame(root, bd=4)
emp_frame.pack()
exten_frame = Frame(root, bd=4)
exten_frame.pack()
other_frame = Frame(root, bd=4)
other_frame.pack()

# DN row ---
dn_lbl = Label(dn_frame, text='DN:').pack(side=LEFT)
dn_entry = Entry(dn_frame, width=30)
dn_entry.pack(side=RIGHT)

# IMEI row ---
imei_lbl = Label(imei_frame, text='IMEI:').pack(side=LEFT)
imei_entry = Entry(imei_frame, width=30)
imei_entry.pack(side=RIGHT)

# MODEL row ---
model_lbl = Label(model_frame, text='Modelo:').pack(side=LEFT)
model_entry = Entry(model_frame, width=30)
model_entry.pack(side=RIGHT)

# PROBLEM row ---
prob_lbl = Label(problem_frame, text='Problema:').pack(side=LEFT)
llamadas_btn = Button(problem_frame, text='Llamadas', command=lambda: problem_entry.insert(0,'Cte no tiene servicio de llamadas')).pack(side=LEFT)
problem_entry = Entry(problem_frame, width=100)
problem_entry.pack(side=RIGHT, expand=True)

# PROCEDIMIENTO row --
proc_lbl = Label(proce_frame, text='PROCEDIMIENTO:').pack(side=LEFT)
conf_btn = Button(proce_frame, text='Config', command=lambda: proc_entry.insert(0,'Se activan los datos, el roaming, se configura APN, modo de red, se fuerza el operador de red')).pack(side=LEFT)
segniv_btn = Button(proce_frame, text='2do nivel', command=lambda: proc_entry.insert(0,'Se activan los datos, el roaming, se configura APN, modo de red, se fuerza el operador de red//Se genera reporte de 2do nivel')).pack(side=LEFT)
porta_btn = Button(proce_frame, text='Portabilidad', command=portCallBack).pack(side=LEFT)
proc_entry = Entry(proce_frame, width=100)
proc_entry.pack(side=RIGHT, expand=True)

# Portabilidad row ---
dn_port_lbl = Label(dn_porta_frame, text='dn a portar:').pack(side=LEFT)
dn_port_entry = Entry(dn_porta_frame, width=10)
dn_port_entry.pack(side=RIGHT)

nip_port_lbl = Label(nip_porta_frame, text='nip:').pack(side=LEFT)
nip_entry = Entry(nip_porta_frame, width=10)
nip_entry.pack(side=RIGHT)

# COPY row ---
copybutton = Button(copyframe, text='Copiar', command=copyCallBack)
copybutton.pack(side=TOP)
regi_lbl = Label(copyframe, text='--Registro--').pack()
resultentryBox = Entry(copyframe, width=200)
resultentryBox.pack(side=TOP, pady=5)

empleadolabel = Label(emp_frame, text='# Empleado:')
empleadolabel.pack(side=LEFT)
empleadoentryBox = Entry(emp_frame)
empleadoentryBox.pack(side=RIGHT)

extensionlabel = Label(exten_frame, text='# Extension:')
extensionlabel.pack(side=LEFT)
extensionentryBox = Entry(exten_frame)
extensionentryBox.pack(side=RIGHT)

# Other frame ---------------------------------------
Equiv_btn = Button(other_frame, text='Equivocada', command=lambda: proc_entry.insert(0, 'Cte llama por problemas de cableo  internet//Se le proporciona el numero de atecion a clilentes'))
Equiv_btn.pack()
root.mainloop()
