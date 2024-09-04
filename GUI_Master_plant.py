
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModelp 
import sqlite3
#import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Crop Disease and Pest Identification System")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('ff.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#
lbl = tk.Label(root, text="Crop Disease & Pest Identification System", font=('times', 35,' bold '), height=1, width=32,bg="#7a3b2e",fg="white")
lbl.place(x=300, y=20)


frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=350, bd=5, font=('times', 14, ' bold '),bg="grey")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=10, y=90)

    
    
###########################################################################
def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= CNNModelp.main()
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    print(msg)

import functools
import operator


def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def test_model_proc(fn):
    from keras.models import load_model
    #from keras.optimizers import Adam

#    global fn
    
    IMAGE_SIZE = 64
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
        # Model Architecture and Compilation
       
        model = load_model('Plant_model.h5')
            
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        plant=np.argmax(prediction)
        print(plant)
        
        
        
        if plant == 0:
            Cd="Disease:Apple___Apple_scab  \n Pest= Venturia inaequalis. \n Fertilizer= Use Fertilome Liquid Systemic Fungicide,\n Immunox, Systemic Infuse, and liquid Copper.\n  Six or more sprays are recommended at 7-10 day intervals. \n If it rains within 6 hours of spraying, you should re-spray. "
        elif plant == 8:
            Cd="Disease:Apple___Black_rot \n Pest =xanthomonas campestris. \n Fertilizer = apply copper bactericides at a 7-10 day \n schedule as soon as disease is detected"
        elif plant == 9:
            Cd="Disease:Apple___Cedar_apple_rust \n Pest=gymnosporangium juniperi-virginianae. \n Fertilizer = Sulfur Plant Fungicide. Serenade Garden. \n Liquid Copper Spray. \n Orchard Spray."
        elif plant == 10:
            Cd="Apple___healthy"
        elif plant == 11:
            Cd="Disease:Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot \n Pest=Cercospora zeae-maydis.\n Fertilizer = products containing chlorothalonil, \n mancozeb, propiconazole, \n or copper-based compounds "
        elif plant == 12:
            Cd="Disease:Corn_(maize)___Common_rust \n Pest=Puccinia sorghi.\n Fertilizer= Products containing mancozeb,\n  pyraclostrobin, pyraclostrobin + metconazole, \n pyraclostrobin + fluxapyroxad, azoxystrobin + propiconazole,\n trifloxystrobin + prothioconazole can be \n used to control the disease"

        elif plant == 13:
            Cd="Corn_(maize)___healthy"
        elif plant == 14:
            Cd="Disease:Corn_(maize)___Northern_Leaf_Blight \n Pest=Bipolaris zeicola.\n Fertilizer=Spray 2.5g Mancozeb 75 WP or \n 1 ml Hexaconazole 5 EC or \n  per liter of water immediately after appearance of \n the disease symptoms. \n Repeat the same after 15 days which helps \n to manage Curvularia leaf spot also."
        elif plant == 15:
            Cd="Disease:Grape___Black_rot \n Pest=Guignardia bidwellii.\n Fertilizer=Mancozeb, and Ziram are all \n highly effective against black rot"
        elif plant == 1:
            Cd="Disease:Grape___Esca_(Black_Measles) \n Pest= Phaeoacremonium aleophilum.\n Fertilizer= glyphosate, Acephate, Deet, \n Propoxur, Metaldehyde, Boric Acid"
        elif plant == 2:
            Cd="Grape___healthy"
        elif plant == 3:
            Cd=" Disease:Grape___Leaf_blight_(Isariopsis_Leaf_Spot), \n Pest=Pseudocercospora vitis.\n Fertilizer= Spray 2.5g Mancozeb 75 WP or \n 1 ml Hexaconazole 5 EC or \n  1 ml combiproduct fungicide \n Azoxystrobin 18.2% + Difenconazole 11.4% per liter of water \n immediately after appearance of the disease symptoms.\n Repeat the same after 15 days \n which helps to manage Curvularia leaf spot also."  
        elif plant == 4:
            Cd="Disease:Peach___Bacterial_spot \n Pest=Xanthomonas arboricola pv. pruni.\n Fertilizer= Maintain adequate fertility, \n especially nitrogen in the field and \n apply copper bactericides at a 7-10 day \n schedule as soon as disease is detected."
        elif plant == 5:
            Cd="Peach___healthy"
        elif plant == 6:
            Cd="Strawberry___healthy"
        elif plant == 7:
            Cd="Disease:Strawberry___Leaf_scorch, \n Pest=Diplocarpon earliana .\n Fertilizer=There is no cure for bacterial leaf scorch,\n  and trees will continue to decline \n  over a period of several years"
            
            
        A=Cd
        return A

############################################################
def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=60,height=13, font=("bold", 18), bg='bisque2', fg='black')
    result_label.place(x=300, y=400)

###############################################################################


def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        #X1="Selected Image is {0}".format(X)
        x2=format(X)+"\n  "
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ x2 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
#############################################################################
    
def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='E:/Incource Ravina work/All code/100% code Plant Leaf Disease 2/Plant Leaf Disease', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName


#        img = Image.open(imgpath).convert("L")
    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
#        img = img / 255.0
#        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)


    x1 = int(img.shape[0])
    y1 = int(img.shape[1])



    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=300, y=100)
  
#############################################################################    

def convert_grey():
    global fn    
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
    #result_label1.place(x=300, y=400)
    img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=580, y=100)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=100)
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250, font=("bold", 25), bg='bisque2', fg='black')
    #result_label1.place(x=300, y=400)


#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(frame_alpr, text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="green",fg="white")
button1.place(x=10, y=40)

button2 = tk.Button(frame_alpr, text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="green",fg="white")
button2.place(x=10, y=100)

# button3 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=12, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button3.place(x=10, y=150)
#
button4 = tk.Button(frame_alpr, text="CNN_Prediction", command=test_model,width=15, height=1,bg="green",fg="white", font=('times', 15, ' bold '))
button4.place(x=10, y=160)
#
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=450, y=20)


exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="Red",fg="white")
exit.place(x=10, y=220)



root.mainloop()