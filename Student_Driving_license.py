from tkinter import *
root = Tk()
root.title("Student Driving License")
root.geometry("400x400")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

label_id = Label(root, text = ["1982719839"])
label_name = Label(root, text = ["Astha Mistry"])
label_dob = Label(root, text = ["09 December 2008"])
label_pin = Label(root, text = ["123456"])
label_address = Label(root, text = ["Hogwarts, Scotland"])
label_vehicle_type = Label(root, text = ["Two Wheeler"])



def student_driving_lisence:
    label_id = 1982719839
    print(type(label_id))
    label_name = "Astha Mistry"
    print(type(label_name))
    label_dob = "09 December 2008"
    print(type(label_id))
    label_pin = "123456"
    print(type(label_pin))
    label_address = "Hogwarts, Scotland"
    print(type(label_address))
    label_vehicle_type = "Two Wheeler"
    print(type(label_vehicle_type))
    
    label_id['text'] = "1982719839"
    label_name['text'] = "Astha Mistry"
    label_dob['text'] = "09 December 2008"
    label_address['text'] = "Hogwarts, Scotland"
    label_vehicle_type["text"] = "Two Wheeler"
    
    button1 = Button(root, text = "Show My Driving Lisence", command = attribute)


button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

root.mainloop()



