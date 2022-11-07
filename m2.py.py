# importing the required libraries  
import tkinter 
from tkinter import messagebox  
import eval7, pprint
from eval7 import equity
    
var = ""  
A = 0  
operator = ""  
  

def button_Ac_is_Clicked():
    global var
    var = var + "Ac" + " "
    the_data.set(var) 

def button_As_is_Clicked():
    global var
    var = var + "As" + " "
    the_data.set(var) 

def button_Ah_is_Clicked():
    global var
    var = var + "Ah" + " "
    the_data.set(var) 

def button_Ad_is_Clicked():
    global var
    var = var + "Ad" + " "
    the_data.set(var) 

#----------
def button_2c_is_Clicked():
    global var
    var = var + "2c" + " "
    the_data.set(var) 

def button_2s_is_Clicked():
    global var
    var = var + "2s" + " "
    the_data.set(var) 

def button_2h_is_Clicked():
    global var
    var = var + "2h" + " "
    the_data.set(var) 

def button_2d_is_Clicked():
    global var
    var = var + "2d" + " "
    the_data.set(var) 


#-------

def button_3c_is_Clicked():
    global var
    var = var + "3c" + " "
    the_data.set(var) 

def button_3s_is_Clicked():
    global var
    var = var + "3s" + " "
    the_data.set(var) 

def button_3h_is_Clicked():
    global var
    var = var + "3h" + " "
    the_data.set(var) 

def button_3d_is_Clicked():
    global var
    var = var + "3d" + " "
    the_data.set(var) 

#-------------
def button_4c_is_Clicked():
    global var
    var = var + "4c" + " "
    the_data.set(var) 

def button_4s_is_Clicked():
    global var
    var = var + "4s" + " "
    the_data.set(var) 

def button_4h_is_Clicked():
    global var
    var = var + "4h" + " "
    the_data.set(var) 

def button_4d_is_Clicked():
    global var
    var = var + "4d" + " "
    the_data.set(var) 

#---------------

def button_5c_is_Clicked():
    global var
    var = var + "5c" + " "
    the_data.set(var) 

def button_5s_is_Clicked():
    global var
    var = var + "5s" + " "
    the_data.set(var) 

def button_5h_is_Clicked():
    global var
    var = var + "5h" + " "
    the_data.set(var) 

def button_5d_is_Clicked():
    global var
    var = var + "5d" + " "
    the_data.set(var) 

#----------------

def button_6c_is_Clicked():
    global var
    var = var + "6c" + " "
    the_data.set(var) 

def button_6s_is_Clicked():
    global var
    var = var + "6s" + " "
    the_data.set(var) 

def button_6h_is_Clicked():
    global var
    var = var + "6h" + " "
    the_data.set(var) 

def button_6d_is_Clicked():
    global var
    var = var + "6d" + " "
    the_data.set(var) 

#----------------------
  
def button_7c_is_Clicked():
    global var
    var = var + "7c" + " "
    the_data.set(var) 

def button_7s_is_Clicked():
    global var
    var = var + "7s" + " "
    the_data.set(var) 

def button_7h_is_Clicked():
    global var
    var = var + "7h" + " "
    the_data.set(var) 

def button_7d_is_Clicked():
    global var
    var = var + "7d" + " "
    the_data.set(var) 

#--------------

def button_8c_is_Clicked():
    global var
    var = var + "8c" + " "
    the_data.set(var) 

def button_8s_is_Clicked():
    global var
    var = var + "8s" + " "
    the_data.set(var) 

def button_8h_is_Clicked():
    global var
    var = var + "8h" + " "
    the_data.set(var) 

def button_8d_is_Clicked():
    global var
    var = var + "8d" + " "
    the_data.set(var) 

#---------

def button_9c_is_Clicked():
    global var
    var = var + "9c" + " "
    the_data.set(var) 

def button_9s_is_Clicked():
    global var
    var = var + "9s" + " "
    the_data.set(var) 

def button_9h_is_Clicked():
    global var
    var = var + "9h" + " "
    the_data.set(var) 

def button_9d_is_Clicked():
    global var
    var = var + "9d" + " "
    the_data.set(var) 
#------------------

def button_Tc_is_Clicked():
    global var
    var = var + "Tc" + " "
    the_data.set(var) 

def button_Ts_is_Clicked():
    global var
    var = var + "Ts" + " "
    the_data.set(var) 

def button_Th_is_Clicked():
    global var
    var = var + "Th" + " "
    the_data.set(var) 

def button_Td_is_Clicked():
    global var
    var = var + "Td" + " "
    the_data.set(var) 
#-----------------------------
def button_Jc_is_Clicked():
    global var
    var = var + "Jc" + " "
    the_data.set(var) 

def button_Js_is_Clicked():
    global var
    var = var + "Js" + " "
    the_data.set(var) 

def button_Jh_is_Clicked():
    global var
    var = var + "Jh" + " "
    the_data.set(var) 

def button_Jd_is_Clicked():
    global var
    var = var + "Jd" + " "
    the_data.set(var) 

#---------------

def button_Qc_is_Clicked():
    global var
    var = var + "Qc" + " "
    the_data.set(var) 

def button_Qs_is_Clicked():
    global var
    var = var + "Qs" + " "
    the_data.set(var) 

def button_Qh_is_Clicked():
    global var
    var = var + "Qh" + " "
    the_data.set(var) 

def button_Qd_is_Clicked():
    global var
    var = var + "Qd" + " "
    the_data.set(var) 

#-----------------

def button_Kc_is_Clicked():
    global var
    var = var + "Kc" + " "
    the_data.set(var) 

def button_Ks_is_Clicked():
    global var
    var = var + "Ks" + " "
    the_data.set(var) 

def button_Kh_is_Clicked():
    global var
    var = var + "Kh" + " "
    the_data.set(var) 

def button_Kd_is_Clicked():
    global var
    var = var + "Kd" + " "
    the_data.set(var) 

#-------------------
def button_C_is_Clicked():  
    global A  
    global var  
    global operator  
    var = ""  
  
    the_data.set(var)  

def res():  
    global var  
    my_tuple = tuple(var.split())
    hand = [eval7.Card(s) for s in my_tuple]
    eval7.evaluate(hand)
    print(eval7.handtype(eval7.evaluate(hand)))
    x = tuple(eval7.handtype(eval7.evaluate(hand)))
    the_data.set(tuple(x))
    var = str(x)
    # messagebox.showinfo("Result", x)

guiWindow = tkinter.Tk()  
guiWindow.geometry("900x500+1000+500")  

guiWindow.resizable(0, 0)  

guiWindow.title("Poker Equity Calculator")  
  

the_data = StringVar()  
guiLabel = Label(  
    guiWindow,  
    text = "Label",  
    anchor = SE,  
    font = ("Cambria Math", 20),  
    textvariable = the_data,  
    background = "#ffffff",  
    fg = "#000000"  
)  

guiLabel.pack(expand = True, fill = "both")  
  
  
frameOne = Frame(guiWindow, bg = "#000000")  
frameOne.pack(expand = True, fill = "both") 
  

frameTwo = Frame(guiWindow, bg = "#000000")  
frameTwo.pack(expand = True, fill = "both")  
  

frameThree = Frame(guiWindow, bg = "#000000")  
frameThree.pack(expand = True, fill = "both")  
  

frameFour = Frame(guiWindow, bg = "#000000")  
frameFour.pack(expand = True, fill = "both")  
  

buttonAc = Button(
    frameOne,  
    text = "Ac",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Ac_is_Clicked  
)
buttonAc.pack(side = LEFT, expand = True, fill = "both")

buttonAs = Button(
    frameOne,  
    text = "As",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_As_is_Clicked  
)
buttonAs.pack(side = LEFT, expand = True, fill = "both")

buttonAh = Button(
    frameOne,  
    text = "Ah",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Ah_is_Clicked  
)
buttonAh.pack(side = LEFT, expand = True, fill = "both")

buttonAd = Button(
    frameOne,  
    text = "Ad",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Ad_is_Clicked  
)
buttonAd.pack(side = LEFT, expand = True, fill = "both")


#-------------

button2c = Button(
    frameOne,  
    text = "2c",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_2c_is_Clicked  
)
button2c.pack(side = LEFT, expand = True, fill = "both")

button2s = Button(
    frameOne,  
    text = "2s",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_2s_is_Clicked  
)
button2s.pack(side = LEFT, expand = True, fill = "both")

button2h = Button(
    frameOne,  
    text = "2h",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_2h_is_Clicked  
)
button2h.pack(side = LEFT, expand = True, fill = "both")

button2d = Button(
    frameOne,  
    text = "2d",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_2d_is_Clicked  
)
button2d.pack(side = LEFT, expand = True, fill = "both")

#-------------

button3c = Button(
    frameOne,  
    text = "3c",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_3c_is_Clicked  
)
button3c.pack(side = LEFT, expand = True, fill = "both")

button3s = Button(
    frameOne,  
    text = "3s",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_3s_is_Clicked  
)
button3s.pack(side = LEFT, expand = True, fill = "both")

button3h = Button(
    frameOne,  
    text = "3h",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_3h_is_Clicked  
)
button3h.pack(side = LEFT, expand = True, fill = "both")

button3d = Button(
    frameOne,  
    text = "3d",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_3d_is_Clicked  
)
button3d.pack(side = LEFT, expand = True, fill = "both")


#----------
button4c = Button(
    frameOne,  
    text = "4c",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_4c_is_Clicked  
)
button4c.pack(side = LEFT, expand = True, fill = "both")

button4s = Button(
    frameOne,  
    text = "4s",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_4s_is_Clicked  
)
button4s.pack(side = LEFT, expand = True, fill = "both")

button4h = Button(
    frameOne,  
    text = "4h",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_4h_is_Clicked  
)
button4h.pack(side = LEFT, expand = True, fill = "both")

button4d = Button(
    frameOne,  
    text = "4d",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_4d_is_Clicked  
)
button4d.pack(side = LEFT, expand = True, fill = "both")

#------------------

button5c = Button(
    frameTwo,  
    text = "5c",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_5c_is_Clicked  
)
button5c.pack(side = LEFT, expand = True, fill = "both")

button5s = Button(
    frameTwo,  
    text = "5s",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_5s_is_Clicked  
)
button5s.pack(side = LEFT, expand = True, fill = "both")

button5h = Button(
    frameTwo,  
    text = "5h",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_5h_is_Clicked  
)
button5h.pack(side = LEFT, expand = True, fill = "both")

button5d = Button(
    frameTwo,  
    text = "5d",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_5d_is_Clicked  
)
button5d.pack(side = LEFT, expand = True, fill = "both")

#--------------
button6c = Button(
    frameTwo,  
    text = "6c",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_6c_is_Clicked  
)
button6c.pack(side = LEFT, expand = True, fill = "both")

button6s = Button(
    frameTwo,  
    text = "6s",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_6s_is_Clicked  
)
button6s.pack(side = LEFT, expand = True, fill = "both")

button6h = Button(
    frameTwo,  
    text = "6h",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_6h_is_Clicked  
)
button6h.pack(side = LEFT, expand = True, fill = "both")

button6d = Button(
    frameTwo,  
    text = "6d",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_6d_is_Clicked  
)
button6d.pack(side = LEFT, expand = True, fill = "both")

#-------------
button7c = Button(
    frameTwo,  
    text = "7c",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_7c_is_Clicked  
)
button7c.pack(side = LEFT, expand = True, fill = "both")

button7s = Button(
    frameTwo,  
    text = "7s",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_7s_is_Clicked  
)
button7s.pack(side = LEFT, expand = True, fill = "both")

button7h = Button(
    frameTwo,  
    text = "7h",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_7h_is_Clicked  
)
button7h.pack(side = LEFT, expand = True, fill = "both")

button7d = Button(
    frameTwo,  
    text = "7d",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_7d_is_Clicked  
)
button7d.pack(side = LEFT, expand = True, fill = "both")

#----------------
button8c = Button(
    frameTwo,  
    text = "8c",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_8c_is_Clicked  
)
button8c.pack(side = LEFT, expand = True, fill = "both")

button8s = Button(
    frameTwo,  
    text = "8s",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_8s_is_Clicked  
)
button8s.pack(side = LEFT, expand = True, fill = "both")

button8h = Button(
    frameTwo,  
    text = "8h",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_8h_is_Clicked  
)
button8h.pack(side = LEFT, expand = True, fill = "both")

button8d = Button(
    frameTwo,  
    text = "8d",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_8d_is_Clicked  
)
button8d.pack(side = LEFT, expand = True, fill = "both")

#-----------------

button9c = Button(
    frameThree,  
    text = "9c",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_9c_is_Clicked  
)
button9c.pack(side = LEFT, expand = True, fill = "both")

button9s = Button(
    frameThree,   
    text = "9s",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_9s_is_Clicked  
)
button9s.pack(side = LEFT, expand = True, fill = "both")

button9h = Button(
    frameThree,   
    text = "9h",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_9h_is_Clicked  
)
button9h.pack(side = LEFT, expand = True, fill = "both")

button9d = Button(
    frameThree,  
    text = "9d",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_9d_is_Clicked  
)
button9d.pack(side = LEFT, expand = True, fill = "both")

#--------------------------

buttonTc = Button(
    frameThree,  
    text = "10c",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Tc_is_Clicked  
)
buttonTc.pack(side = LEFT, expand = True, fill = "both")

buttonTs = Button(
    frameThree,   
    text = "10s",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Ts_is_Clicked  
)
buttonTs.pack(side = LEFT, expand = True, fill = "both")

buttonTh = Button(
    frameThree,   
    text = "10h",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Th_is_Clicked  
)
buttonTh.pack(side = LEFT, expand = True, fill = "both")

buttonTd = Button(
    frameThree,  
    text = "10d",
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Td_is_Clicked  
)
buttonTd.pack(side = LEFT, expand = True, fill = "both")

#-----------------


buttonJc = Button(
    frameThree,  
    text = "Jc",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Jc_is_Clicked  
)
buttonJc.pack(side = LEFT, expand = True, fill = "both")

buttonJs = Button(
    frameThree,   
    text = "Js",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Js_is_Clicked  
)
buttonJs.pack(side = LEFT, expand = True, fill = "both")

buttonJh = Button(
    frameThree,   
    text = "Jh",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Jh_is_Clicked  
)
buttonJh.pack(side = LEFT, expand = True, fill = "both")

buttonJd = Button(
    frameThree,  
    text = "Jd",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Jd_is_Clicked  
)
buttonJd.pack(side = LEFT, expand = True, fill = "both")

#-------------------
buttonQc = Button(
    frameThree,  
    text = "Qc",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Qc_is_Clicked  
)
buttonQc.pack(side = LEFT, expand = True, fill = "both")

buttonQs = Button(
    frameThree,   
    text = "Qs",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Qs_is_Clicked  
)
buttonQs.pack(side = LEFT, expand = True, fill = "both")

buttonQh = Button(
    frameThree,   
    text = "Qh",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Qh_is_Clicked  
)
buttonQh.pack(side = LEFT, expand = True, fill = "both")

buttonQd = Button(
    frameThree,  
    text = "Qd",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Qd_is_Clicked  
)
buttonQd.pack(side = LEFT, expand = True, fill = "both")

#-----------------
buttonKc = Button(
    frameFour,  
    text = "Kc",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Kc_is_Clicked  
)
buttonKc.pack(side = LEFT, expand = True, fill = "both")

buttonKs = Button(
    frameFour,   
    text = "Ks",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Ks_is_Clicked  
)
buttonKs.pack(side = LEFT, expand = True, fill = "both")

buttonKh = Button(
    frameFour,   
    text = "Kh",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Kh_is_Clicked  
)
buttonKh.pack(side = LEFT, expand = True, fill = "both")

buttonKd = Button(
    frameFour,  
    text = "Kd",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Kd_is_Clicked  
)
buttonKd.pack(side = LEFT, expand = True, fill = "both")

buttonC = Button(  
    frameFour,  
    text = "Clear",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_C_is_Clicked  
)  
 
buttonC.pack(side = LEFT, expand = True, fill = "both")  
# buttonONE = Button(  
#     frameOne,  
#     text = "1",  
#     font = ("Cambria", 22),  
#     relief = GROOVE,  
#     border = 0,  
#     command = button_1_is_Clicked
# )  
  
# button 2  

  

buttonEQUAL = Button(  
    frameFour,  
    text = "=",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = res  
)  

buttonEQUAL.pack(side = LEFT, expand = True, fill = "both")  
  
# running the GUI  
guiWindow.mainloop()  