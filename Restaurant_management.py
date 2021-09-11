from tkinter import*
import sys

def restaurant():
	root = Tk()
	root.geometry("1160x520")
	root.resizable(width=NO,height=NO)
	root.title("RESTAURANT SYSTEM")
	root.configure(bg="white")

	def Enter_button_click():
		global bill, custor_name, phone_no_
		bill = Label(second_frame,text=bill_entry.get(),fg="black", bg ="#F0F0F0",font ="serief 9 bold")
		bill.grid(row=1,column=0,sticky="W",padx=55)

		custor_name = Label(second_frame,text= (name_entry.get()).upper(),fg="black", bg ="#F0F0F0",font ="serief 9 bold")
		custor_name.grid(row=2,column=0,sticky="W",padx=120)

		phone_no_= Label(second_frame,text=phone_entry.get(),fg="black", bg ="#F0F0F0",font ="Roboto 9 bold")
		phone_no_.grid(row=3,column=0,sticky="W",padx=75)


	def Total_cosmetic():
		list1 = bath_soap_entry.get()
		list2 = face_cream_entry.get()
		list3 = face_wash_entry.get()
		list4 = hair_style_entry.get()
		list5 = body_lotion_entry.get()
		sum_cosmetic = str(((int(list1)*240) + (int(list2)*200)+ (int(list3)*220) + (int(list4)*150) + (int(list5)*230)))+".00"
		total_cosmetic_entry.insert(0,sum_cosmetic)

	def Total_grocery():
		list6 = rice_entry.get()
		list7 = food_oil_entry.get()
		list8 = egg_entry.get()
		list9 = wheat_entry.get()
		list10 = sugar_entry.get()
		sum_grocery = str(((int(list6)*600) + (int(list7)*300)+ (int(list8)*70) + (int(list9)*200) + (int(list10)*150)))+".00"
		total_grocery_entry.insert(0,sum_grocery)

	def Total_drink():
		list11 = sprite_entry.get()
		list12 = monster_entry.get()
		list13 = fanta_entry.get()
		list14 = maltina_entry.get()
		list15 = coke_entry.get()
		sum_drink = str(((int(list11)*100) + (int(list12)*100)+ (int(list13)*100) + (int(list14)*200) + (int(list15)*120)))+".00"
		total_drink_entry.insert(0,sum_drink)

	def Total_other():
		list16 = maza_entry.get()
		list17 = semovita_entry.get()
		list18 = indomie_entry.get()
		list19 = beans_entry.get()
		list20 = biscuit_entry.get()
		sum_other = str(((int(list16)*100) + (int(list17)*600)+ (int(list18)*300) + (int(list19)*1200) + (int(list20)*50)))+".00"
		total_other_entry.insert(0,sum_other)

	def All_entry_clear():
		delete_all = [bath_soap_entry.delete(0,END),face_wash_entry.delete(0,END),face_cream_entry.delete(0,END),
		hair_style_entry.delete(0,END),body_lotion_entry.delete(0,END),rice_entry.delete(0,END),food_oil_entry.delete(0,END),
		egg_entry.delete(0,END),wheat_entry.delete(0,END),sugar_entry.delete(0,END),sprite_entry.delete(0,END),
		monster_entry.delete(0,END),fanta_entry.delete(0,END),maltina_entry.delete(0,END),coke_entry.delete(0,END),
		maza_entry.delete(0,END),semovita_entry.delete(0,END),indomie_entry.delete(0,END),beans_entry.delete(0,END),
		biscuit_entry.delete(0,END),name_entry.delete(0,END),phone_entry.delete(0,END),bill_entry.delete(0,END)]
		for dele in range(0,23):
			delete_all[dele]
		
	def all_total_clear():
		total_cosmetic_entry.delete(0,END)
		total_grocery_entry.delete(0,END)
		total_drink_entry.delete(0,END)
		total_other_entry.delete(0,END)

	def all_tax_clear():
		cosmetic_tax_entry.delete(0,END)
		Grocery_tax_entry.delete(0,END)
		other_tax_entry.delete(0,END)
		drink_tax_entry.delete(0,END)

	def Total_tax():
		list1 = bath_soap_entry.get()
		list2 = face_cream_entry.get()
		list3 = face_wash_entry.get()
		list4 = hair_style_entry.get()
		list5 = body_lotion_entry.get()
		sum_cosmetic = str(((int(list1)*0.34) + (int(list2)*0.34)+ (int(list3)*0.34) + (int(list4)*0.34) + (int(list5)*0.34)))
		cosmetic_tax_entry.insert(0,sum_cosmetic)

		list6 = rice_entry.get()
		list7 = food_oil_entry.get()
		list8 = egg_entry.get()
		list9 = wheat_entry.get()
		list10 = sugar_entry.get()
		sum_grocery = str(((int(list6)*0.34) + (int(list7)*0.34)+ (int(list8)*0.34) + (int(list9)*0.34) + (int(list10)*0.34)))
		Grocery_tax_entry.insert(0,sum_grocery)

		list11 = sprite_entry.get()
		list12 = monster_entry.get()
		list13 = fanta_entry.get()
		list14 = maltina_entry.get()
		list15 = coke_entry.get()
		sum_drink = (int(list11)*0.34) + (int(list12)*0.34)+ (int(list13)*0.34) + (int(list14)*0.34) + (int(list15)*0.34)
		other_tax_entry.insert(0,sum_drink)

		list16 = maza_entry.get()
		list17 = semovita_entry.get()
		list18 = indomie_entry.get()
		list19 = beans_entry.get()
		list20 = biscuit_entry.get()
		sum_other = str(((int(list16)*0.34) + (int(list17)*0.34)+ (int(list18)*0.34) + (int(list19)*0.34) + (int(list20)*0.34)))
		drink_tax_entry.insert(0,sum_other)

	def del_frame_label():
		global bill, custor_name, phone_no_
		bill.configure(text="")
		custor_name.configure(text="")
		phone_no_.configure(text="")
			
	def Total_button_click():
		Total_cosmetic()
		Total_grocery()
		Total_drink()
		Total_other()
		Total_tax()
		
	def Clear_button_click():
		All_entry_clear()
		all_total_clear()
		all_tax_clear()
		del_frame_label()
		

	labe1 = Label(root, text="Billing Software",bd=4,bg="#003151",
					fg="white",relief=GROOVE,width=115,font=("aria" ,13, "bold"),justify=CENTER)
	labe1.place(x=0,y=0)

	frame1 = Frame(root,width=1160,height=55,bg="#003151",bd=6,relief=GROOVE)
	frame1.place(x=0,y=32)

	Custormer_detail = Label(root,text="Custormer Details",fg="#FFBF00",font="Serif 8 bold",bg="#003151")
	Custormer_detail.place(x=6,y=30)

	name_labe = Label(frame1,text="Custormer Name",fg="white", bg ="#003151",font="Serif 10 bold")
	name_labe.place(x=6,y=13)
	name_entry = Entry(frame1,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold")
	name_entry.place(x=120,y=13)

	phone_labe = Label(frame1,text="Phone No",fg="white", bg ="#003151",font="Serif 10 bold")
	phone_labe.place(x=280,y=13)
	phone_entry = Entry(frame1,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold")
	phone_entry.place(x=360,y=13)

	bill_labe = Label(frame1,text="Bill No",fg="white", bg ="#003151",font="Serif 10 bold")
	bill_labe.place(x=530,y=13)
	bill_entry = Entry(frame1,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold")
	bill_entry.place(x=590,y=13)

	enter_button = Button(frame1,text="Enter",padx=12,pady=2,relief=GROOVE,bd=3,bg="#003151",fg="white",font="Roboto 10 bold",command=Enter_button_click)
	enter_button.place(x=800,y=8)

	frame2 = Frame(root,width=1160,height=300,bg="#003151",relief=GROOVE)
	frame2.place(x=0,y=90)

	sub_frame1 = Frame(frame2,width=200,height=300,bg="#003151",bd=6,relief=GROOVE)
	sub_frame1.place(x=0,y=0)

	cosmetic_label = Label(root,text="Cosmetics",fg="#FFBF00",font="Serif 8 bold",bg="#003151")
	cosmetic_label.place(x=6,y=90)

	bath_soap_label = Label(sub_frame1,text="Bath Soap",fg="white", bg ="#003151",font="Serif 8 bold")
	bath_soap_label.place(x=0,y=30)
	face_cream_label = Label(sub_frame1,text="Face Cream",fg="white", bg ="#003151",font="Serif 8 bold")
	face_cream_label.place(x=0,y=90)
	face_wash_label = Label(sub_frame1,text="Face Wash",fg="white", bg ="#003151",font="Serif 8 bold")
	face_wash_label.place(x=0,y=140)
	hair_style_label = Label(sub_frame1,text="Hair Spray",fg="white", bg ="#003151",font="Serif 8 bold")
	hair_style_label.place(x=0,y=190)
	body_lotion_label = Label(sub_frame1,text="Body Lotion",fg="white", bg ="#003151",font="Serif 8 bold")
	body_lotion_label.place(x=0,y=240)

	bath_soap_entry = Entry(sub_frame1,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	bath_soap_entry.place(x=77,y=30)
	face_cream_entry = Entry(sub_frame1,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	face_cream_entry.place(x=77,y=90)
	face_wash_entry = Entry(sub_frame1,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	face_wash_entry.place(x=77,y=140)
	hair_style_entry = Entry(sub_frame1,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	hair_style_entry.place(x=77,y=190)
	body_lotion_entry = Entry(sub_frame1,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	body_lotion_entry.place(x=77,y=240)

	sub_frame2 = Frame(frame2,width=200,height=300,bg="#003151",bd=6,relief=GROOVE)
	sub_frame2.place(x=200,y=0)

	Grocery_label = Label(root,text="Grocery",fg="#FFBF00",font="Serif 8 bold",bg="#003151")
	Grocery_label.place(x=200,y=90)

	rice_label = Label(sub_frame2,text="Rice",fg="white", bg ="#003151",font="Serif 8 bold")
	rice_label.place(x=10,y=30)
	food_oil_label = Label(sub_frame2,text="Food Oil",fg="white", bg ="#003151",font="Serif 8 bold")
	food_oil_label.place(x=10,y=90)
	egg_label = Label(sub_frame2,text="Egg",fg="white", bg ="#003151",font="Serif 8 bold")
	egg_label.place(x=10,y=140)
	wheat_label = Label(sub_frame2,text="Wheat",fg="white", bg ="#003151",font="Serif 8 bold")
	wheat_label.place(x=10,y=190)
	sugar_label = Label(sub_frame2,text="Sugar",fg="white", bg ="#003151",font="Serif 8 bold")
	sugar_label.place(x=10,y=240)

	rice_entry = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	rice_entry.place(x=77,y=30)
	food_oil_entry = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	food_oil_entry.place(x=77,y=90)
	egg_entry = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	egg_entry.place(x=77,y=140)
	wheat_entry = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	wheat_entry.place(x=77,y=190)
	sugar_entry = Entry(sub_frame2,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	sugar_entry.place(x=77,y=240)

	sub_frame3 = Frame(frame2,width=200,height=300,bg="#003151",bd=6,relief=GROOVE)
	sub_frame3.place(x=400,y=0)

	Other_label = Label(root,text="Drinks",fg="#FFBF00",font="Serif 8 bold",bg="#003151")
	Other_label.place(x=400,y=90)

	sprite_label = Label(sub_frame3,text="Sprite",fg="white", bg ="#003151",font="Serif 8 bold")
	sprite_label.place(x=10,y=30)
	monster_label = Label(sub_frame3,text="Monster",fg="white", bg ="#003151",font="Serif 8 bold")
	monster_label.place(x=10,y=90)
	fanta_label = Label(sub_frame3,text="Fanta",fg="white", bg ="#003151",font="Serif 8 bold")
	fanta_label.place(x=10,y=140)
	maltina_label = Label(sub_frame3,text="Maltina",fg="white", bg ="#003151",font="Serif 8 bold")
	maltina_label.place(x=10,y=190)
	coke_label = Label(sub_frame3,text="Coke",fg="white", bg ="#003151",font="Serif 8 bold")
	coke_label.place(x=10,y=240)

	sprite_entry = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	sprite_entry.place(x=77,y=30)
	monster_entry = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	monster_entry.place(x=77,y=90)
	fanta_entry = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	fanta_entry.place(x=77,y=140)
	maltina_entry = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	maltina_entry.place(x=77,y=190)
	coke_entry = Entry(sub_frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	coke_entry.place(x=77,y=240)


	sub_frame4 = Frame(frame2,width=200,height=300,bg="#003151",bd=6,relief=GROOVE)
	sub_frame4.place(x=600,y=0)
	Other_label = Label(root,text="Others",fg="#FFBF00",font="Serif 8 bold",bg="#003151")
	Other_label.place(x=600,y=90)

	maza_label = Label(sub_frame4,text="Maza",fg="white", bg ="#003151",font="Serif 8 bold")
	maza_label.place(x=10,y=30)
	semovita_label = Label(sub_frame4,text="Semovita",fg="white", bg ="#003151",font="Serif 8 bold")
	semovita_label.place(x=10,y=90)
	indomie_label = Label(sub_frame4,text="Indomie",fg="white", bg ="#003151",font="Serif 8 bold")
	indomie_label.place(x=10,y=140)
	beans_label = Label(sub_frame4,text="Beans",fg="white", bg ="#003151",font="Serif 8 bold")
	beans_label.place(x=10,y=190)
	biscuit_label = Label(sub_frame4,text="Biscuit",fg="white", bg ="#003151",font="Serif 8 bold")
	biscuit_label.place(x=10,y=240)

	maza_entry = Entry(sub_frame4,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	maza_entry.place(x=77,y=30)
	semovita_entry = Entry(sub_frame4,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	semovita_entry.place(x=77,y=90)
	indomie_entry = Entry(sub_frame4,bd=4,bg="White",relief = GROOVE,font = "Roboto 10 bold",width = 14)
	indomie_entry.place(x=77,y=140)
	beans_entry = Entry(sub_frame4,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	beans_entry.place(x=77,y=190)
	biscuit_entry = Entry(sub_frame4,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	biscuit_entry.place(x=77,y=240)

	sub_frame5 = Frame(frame2,bg="white",bd=6,relief=GROOVE)
	sub_frame5.place(x=800,y=0,width=360,height=300)

	my_canvas = Canvas(sub_frame5)
	second_frame = Frame(my_canvas)

	bill_area = Label(sub_frame5,text="Bill Area",bg="white",font="Roboto 14 bold",bd=4,relief=GROOVE,width=30)
	bill_area.pack(side=TOP)

	my_scrollbar = Scrollbar(sub_frame5,orient = VERTICAL,command=my_canvas.yview)
	my_canvas.configure(yscrollcommand=my_scrollbar.set)
	my_scrollbar.pack(side=RIGHT,fill="y")
	my_canvas.pack(side=LEFT)
	my_canvas.create_window((0,0),window=second_frame,anchor="nw")
	second_frame.bind("<Configure>",lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

	welcome = Label(second_frame,text="Welcome Heaman's Retailer",fg="#003151", bg ="#F0F0F0",font ="Roboto 11 bold")
	welcome.grid(row=0,column=0,sticky="W",padx=70)

	def display_pro_info():
		bill_no_label = Label(second_frame,text="Bill No: ",fg="black", bg ="#F0F0F0",font ="Roboto 10 bold")
		bill_no_label.grid(row=1,column=0,sticky="W")

		cost_name = Label(second_frame,text="Custormer Name: ",fg="black", bg ="#F0F0F0",font ="Roboto 10 bold")
		cost_name.grid(row=2,column=0,sticky="W")
		phone_no = Label(second_frame,text="Phone No: ",fg="black", bg ="#F0F0F0",font ="Roboto 10 bold")
		phone_no.grid(row=3,column=0,sticky="W")
		line_style1 = Label(second_frame,text="-----"*13,fg="black",bg="#F0F0F0",font ="Roboto 12 bold")
		line_style1.grid(row=4,column=0,sticky="W")

		product_label =  Label(second_frame,text="Product",fg="black",bg="#F0F0F0",font ="Roboto 10 bold")
		product_label.grid(row=5,column=0,sticky="W")

		number_label =  Label(second_frame,text="NO",fg="black",bg="#F0F0F0",font ="Roboto 10 bold")
		number_label.grid(row=5,column=0,sticky="W",padx=80)

		price_label =  Label(second_frame,text="Price",fg="black",bg="#F0F0F0",font ="Roboto 10 bold")
		price_label.grid(row=5,column=0,padx=126,sticky="W")

		b_num_label =  Label(second_frame,text="B No",fg="black",bg="#F0F0F0",font ="Roboto 10 bold")
		b_num_label.grid(row=5,column=0,padx=185,sticky="W")

		cost_label =  Label(second_frame,text="B Cost",fg="black",bg="#F0F0F0",font ="Roboto 10 bold")
		cost_label.grid(row=5,column=0,padx=250,sticky="W")

		line_style2 = Label(second_frame,text="-----"*13,fg="black",bg="#F0F0F0",font ="Roboto 12 bold")
		line_style2.grid(row=6,column=0,sticky="W")

		list_item = ["Bath Soap","Face Cream","Face Wash","Hair Style",
					"Body Lotion","Rice","Food Oil","Egg","Wheat","Sugar",
				"Sprite","Monster","Fanta","Maltina","Coke","Maza",
				"Semovita","Indomie","Beans","Biscuit"]
		price_list = [240,200,220,150,230,600,300,70,200,150,100,100,100,200,120,100,600,300,1200,50]


		for n in range(0,20):
				e1 = Label(second_frame,text=list_item[n],font="Roboto 9 bold")
				e1.grid(row=7+n,column=0,sticky="W")
				e2 = Label(second_frame,text=1,font="Roboto 10 bold")
				e2.grid(row=7+n,column=0,sticky="W",padx=85)
				e3 =Label(second_frame,text=price_list[n],font="Roboto 9 bold")
				e3.grid(row=7+n,column=0,sticky="W",padx=130)

	
	def Generate_bill():
		
		global e4,e5,total_b_no,total_cost
		
		b_no = [int(bath_soap_entry.get()) ,int(face_cream_entry.get()),int(face_wash_entry.get()),
				int(hair_style_entry.get()), int(body_lotion_entry.get()),int(rice_entry.get()),
				int(food_oil_entry.get()),int(egg_entry.get()),int(wheat_entry.get()),int(sugar_entry.get()),
				int(sprite_entry.get()),int(monster_entry.get()),int(fanta_entry.get()),int(maltina_entry.get()),
				int(coke_entry.get()),int(maza_entry.get()),int(semovita_entry.get()),int(indomie_entry.get()),
				int(beans_entry.get()),int(biscuit_entry.get())]

		b_cost = [int(bath_soap_entry.get())*240 ,int(face_cream_entry.get())*200,int(face_wash_entry.get())*220,
				int(hair_style_entry.get())*150, int(body_lotion_entry.get())*230,int(rice_entry.get())*600,
				int(food_oil_entry.get())*300,int(egg_entry.get())*70,int(wheat_entry.get())*200,int(sugar_entry.get())*150,
				int(sprite_entry.get())*100,int(monster_entry.get())*100,int(fanta_entry.get())*100,int(maltina_entry.get())*200,
				int(coke_entry.get())*120,int(maza_entry.get())*100,int(semovita_entry.get())*600,int(indomie_entry.get())*300,
				int(beans_entry.get())*1200,int(biscuit_entry.get())*50]
			
		for pro in range(0,20):
			global e4,e5,values1,values2

			values1 = StringVar(value=b_no[pro])
			values2 = StringVar(value=b_cost[pro])

			e4 = Label(second_frame,font="Roboto 9 bold",textvariable=values1)			
			e4.grid(row=7+pro,column=0,sticky="W",padx=200)

			e5 = Label(second_frame,font="Roboto 9 bold",textvariable=values2)
			e5.grid(row=7+pro,column=0,sticky="W",padx=260)

		line_style3 = Label(second_frame,text="-----"*13,fg="black",bg="#F0F0F0",font ="Roboto 12 bold")
		line_style3.grid(row=27,column=0,sticky="W")

		total_b_no = Label(second_frame,text=f"ITEM NO : {sum(b_no)}",font="Roboto 7 bold")
		total_b_no.grid(row=28,column=0,sticky="W",padx=169)

		total_cost = Label(second_frame,text=f"TOTAL COST: {sum(b_cost)}",font="Roboto 7 bold")
		total_cost.grid(row=28,column=0,sticky="W",padx=235)

		

	line_style4 = Label(second_frame,text="-----"*13,fg="black",bg="#F0F0F0",font ="Roboto 12 bold")
	line_style4.grid(row=29,column=0,sticky="W")
			
	frame3 = Frame(root,width=1160,height=130,bg="#003151",relief=GROOVE,bd=4)
	frame3.place(x=0,y=391)

	total_cosmetic_label = Label(frame3,text="Total Cosmetics",fg="white", bg ="#003151",font="Serif 8 bold")
	total_cosmetic_label.place(x=10,y=10)

	total_grocery_label = Label(frame3,text="Total Grocery",fg="white", bg ="#003151",font="Serif 8 bold")
	total_grocery_label.place(x=10,y=35)

	total_drink_label = Label(frame3,text="Total Drink",fg="white", bg ="#003151",font="Serif 8 bold")
	total_drink_label.place(x=10,y=65)

	total_other_label = Label(frame3,text="Total Other",fg="white", bg ="#003151",font="Serif 8 bold")
	total_other_label.place(x=10,y=95)

	total_cosmetic_entry = Entry(frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	total_cosmetic_entry.place(x=115,y=10)

	total_grocery_entry = Entry(frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	total_grocery_entry.place(x=115,y=38)

	total_drink_entry = Entry(frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	total_drink_entry.place(x=115,y=66)

	total_other_entry = Entry(frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	total_other_entry.place(x=115,y=94)

	cosmetic_tax_label = Label(frame3,text="Cosmetics Tax",fg="white", bg ="#003151",font="Serif 8 bold")
	cosmetic_tax_label.place(x=240,y=10)

	Grocery_tax_label = Label(frame3,text="Grocery Tax",fg="white", bg ="#003151",font="Serif 8 bold")
	Grocery_tax_label.place(x=240,y=35)

	other_tax_label = Label(frame3,text="Other Tax",fg="white", bg ="#003151",font="Serif 8 bold")
	other_tax_label.place(x=248,y=65)

	other_tax_label = Label(frame3,text="Other Tax",fg="white", bg ="#003151",font="Serif 8 bold")
	other_tax_label.place(x=248,y=95)

	cosmetic_tax_entry = Entry(frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	cosmetic_tax_entry.place(x=343,y=10)
	Grocery_tax_entry = Entry(frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	Grocery_tax_entry.place(x=343,y=38)
	other_tax_entry = Entry(frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	other_tax_entry.place(x=343,y=66)
	drink_tax_entry = Entry(frame3,bd=4,bg="White",relief=GROOVE,font= "Roboto 10 bold",width=14)
	drink_tax_entry.place(x=343,y=94)

	total_button = Button(frame3,text="Total",padx=16,pady=2,relief=GROOVE,bd=3,bg="#003151",fg="white",font="Roboto 10 bold",command=Total_button_click)
	total_button.place(x=500,y=50)

	Gene_bill_button = Button(frame3,text="Generate Bill",padx=15,pady=2,relief=GROOVE,bd=3,bg="#003151",fg="white",font="Roboto 10 bold",command=Generate_bill)
	Gene_bill_button.place(x=600,y=50)

	clear_button = Button(frame3,text="Clear",padx=15,pady=2,relief=GROOVE,bd=3,bg="#003151",fg="white",font="Roboto 10 bold",command=Clear_button_click)
	clear_button.place(x=750,y=50)

	exit_button = Button(frame3,text="Exit",padx=15,pady=2,relief=GROOVE,bd=3,bg="#003151",fg="white",font="Roboto 10 bold",command = root.quit)
	exit_button.place(x=850,y=50)

	Custormer_detail = Label(root,text="Custormer Details",fg="#FFBF00",font="Serif 8 bold",bg="#003151")
	Custormer_detail.place(x=6,y=30)

	Custormer_detail = Label(root,text="Custormer Details",fg="#FFBF00",font="Serif 8 bold",bg="#003151")
	Custormer_detail.place(x=6,y=30)
	Custormer_detail = Label(root,text="Custormer Details",fg="#FFBF00",font="Serif 8 bold",bg="#003151")
	Custormer_detail.place(x=6,y=30)

	display_pro_info()
	root.mainloop()
restaurant()




