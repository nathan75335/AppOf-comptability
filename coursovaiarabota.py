
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from matplotlib import pyplot as plt

#creation of a window
root  = Tk()
#putting a title in our window
root.title("курсовая работа студента мусоко каленга натан итп-21")
#setting the width and the heigth
root.geometry("1250x600+50+20")
#setting min and max size
root.minsize(width =1250 , height=600 )
root.maxsize(width =1400 , height=1080)
#setting a backgroung color
root.config(background= "cyan")

#writting the information about the courswork in a other function 
def information_coursovaia():
    window = Tk()
    window.title("ИНФОРМАЦИЯ О КУРСОВОЙ РАБОТЕ")
    window.geometry("1250x600+50+20")
    window.config(background="cyan")
    label_1 = Label (window ,text= "курсовая работа",pady=10,font  = "times 20 bold",background="cyan").pack()
    label_2 = Label(window , text ="\tМинистерство образования Республики Беларусь\nУчреждение образования\n«ГОМЕЛЬСКИЙ ГОСУДАРСТВЕННЫЙ ТЕХНИЧЕСКИЙ УНИВЕРСИТЕТимени П.О.Сухого»\nФакультет автоматизированных и информационных систем\Кафедра «Информационные технологии»\n\
    ЗАДАНИЕ\nпо курсовому проектированию\n\
    студенту гр. ИТП-21 Мусоко Каленга Натан\n\
    1. Тема курсовой работы: Автоматизация учета стоимости выпущенной продукции по кварталам.\n\
    2. Сроки сдачи студентом законченной работы – 23.12.2021.\n\
    3. Исходные данные к курсовой работе\n"+
    "В текстовом файле находится таблица, содержащая сведения о стоимости выпущенной продукции по кварталам и состоящая из шести граф: Наименование предприятия;\n Наименование изделия; Квартал I; Квартал II; Квартал III; Квартал IV.\n В последних четырех графах указана стоимость выпущенной продукции (тыс. р.) в соответствующем квартале.\n Известно, что одно и то же изделие может выпускаться разными предприятиями и каждое предприятие может выпускать несколько видов изделий.\n"+
    "Pазработайте алгоритм и программу вычисления выпуска продукции в денежном выражении каждым предприятием за год по всем изделиям с указанием номера квартала с минимальным и максимальным объемом.\n Результаты расчета запишите в новый текстовый файл, содержащий таблицу из четырех граф: Наименование предприятия; Годовой объем выпуска продукции, тыс. р.;\n Номер квартала с минимальным объемом; Номер квартала с максимальным объемом.\n"+
    "Программа должна обеспечить построение диаграммы зависимости Годового объема выпуска продукции, тыс. р. от Наименования предприятия.",background="cyan" , font = "times 12 bold").pack()
    
    
#information about the student that did the courswork
def information_student():
    window = Tk()
    window.title("ИНФОРМАЦИЯ О КУРСОВОЙ РАБОТЕ")
    window.geometry("1250x600+50+20")
    window.config(background="cyan")
    label_1 = Label (window ,text= "МУСОКО КАЛЕНГА НАТАН",pady=10,font  = "times 20 bold",background="cyan").pack()
    label_2  = Label(window , text = "СТУДЕНТ ИТП -21\nBorn in Kinshasa the 01/10/2001.\n Has studied in GSMA for 11 year .After My gradiation i went to belarus to continue my studies",font ="times 15 bold",background="cyan").pack()
  
#function read data to read data from a file
data =[] #data of coming from the file
data_file_sorted =[]#data sorted by the sort_data method
def read_data():
    try : 
        file_name  = filedialog.askopenfilename()
    except:
        pass
    with open(file_name , encoding= 'utf-8') as file:
        file.readline()
        global data_file
        for line in file:
            try:
                line_stripped = line.strip("\n")
                data.append(line_stripped.split(';'))  
            except:
                messagebox.showinfo("ERROR","THE DATA HAVE NOT BEEN READ")
    messagebox.showinfo("SUCCESS","THE DATA HAS BEEN READ")
    window = Tk()
    window.title("ИНФОРМАЦИЯ О КУРСОВОЙ РАБОТЕ")
    window.geometry("1250x600+50+20")
    window.config(background="cyan")
    #creation of a canvas 
    frame_table_data = Canvas(window,height= 450 ,width = 1100,background="white" )
    frame_table_data.pack( pady=20)
    #creation of a treeview
    treeview = ttk.Treeview(frame_table_data,height = 20,show= 'headings' )
    #define the columns
    treeview['columns'] = (1,2,3,4,5,6)
    treeview.column(1,width=120)
    treeview.column(2,anchor= W,)
    treeview.column(3,anchor=W,)
    treeview.column(4,anchor= W,)
    treeview.column(5,anchor= W,)
    treeview.column(6,anchor= W,)
    #creating heading
    treeview.heading(1,text="Наименование предприятия",)
    treeview.heading(2,text="Намеинование изделия",anchor= W,)
    treeview.heading(3,text="Квартал I",anchor= W,)
    treeview.heading(4,text="Квартал II",anchor= W,)
    treeview.heading(5,text="Квартал III",anchor= W)
    treeview.heading(6,text="Квартал IV",anchor= W,)
    treeview.pack(side = TOP)
    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    
    # sorting method that sort element by name      
    # sorting method that sort element by name      
    def sort_data():
        for item in treeview.get_children():
            treeview.delete(item)
        count = 0
        name_of_enterprise = []
        for element in data:
            if element[0] not in name_of_enterprise :
                for data_element in data:
                    if element[0] == data_element[0]:
                        treeview.insert(parent='' ,iid= count  ,index= 'end', text="",values=(data_element[0],\
                                    data_element[1],data_element[2],data_element[3],data_element[4],data_element[5] ))
                        data_file_sorted.append(data_element)
                        name_of_enterprise.append(data_element[0])
                        count +=1
        
    #adding button
    frame_button  = Frame(window,height=40 , width= 40)
    frame_button.pack()
    button_add = Button(frame_button , text ="ОТСОРТИРОВАТЬ",font = "times 15 bold" , width =20 , height =3 ,background="#1dbf85",command = sort_data)
    button_add.pack()
    #printing data in the treeview
    count = 0 
    for element in data:
        treeview.insert(parent='' ,iid= count  ,index= 'end', text="",values=(element[0],\
                                 element[1],element[2],element[3],element[4],element[5] ))
        count += 1   
    
 #
year_production_data = []
def calculation():
    window = Tk()
    window.title("ИНФОРМАЦИЯ О КУРСОВОЙ РАБОТЕ")
    window.geometry("1250x600+50+20")
    window.config(background="cyan")
    #creation of a canvas 
    frame_table_data = Canvas(window,height= 450 ,width = 1100,background="white" )
    frame_table_data.pack( pady=20)
    #creation of a treeview
    treeview = ttk.Treeview(frame_table_data,height = 20,show= 'headings' )
    #define the columns
    treeview['columns'] = (1,2,3,4)
    treeview.column(1,width=120)
    treeview.column(2,anchor= W,)
    treeview.column(3,anchor=W,)
    treeview.column(4,anchor= W,)
    #creating heading
    treeview.heading(1,text="Наименование предприятия",)
    treeview.heading(2,text="Год-й обьем выпуска",anchor= W,)
    treeview.heading(3,text="Номер квартала с минобъемом",anchor= W,)
    treeview.heading(4,text="Номер квартала с максимальным объемом",anchor= W,)
    treeview.pack(side = TOP)
    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    
    #calculating the year production  
    
    name_of_enterprise =[]
    try:
        for element in data_file_sorted:
            if element[0] not in name_of_enterprise :
                data_revenue =[]
                summ_year_production = 0
                kvartal_1 = 0
                kvartal_2 = 0
                kvartal_3 = 0
                kvartal_4 = 0
                for data in data_file_sorted:
                    if data[0]== element[0] and data[0] not in name_of_enterprise:
                        summ_year_production += round(float(data[2])+float(data[3])+ float(data[4])+float(data[5]),2)
                        kvartal_1 += round(float(data[2]),2)
                        kvartal_2 +=round(float(data[3]),2)
                        kvartal_3 +=round(float(data[4]),2)
                        kvartal_4 +=round(float(data[5]),2)
                        # finding the maximum item
                max = ""
                if kvartal_1 > kvartal_2 and kvartal_1 > kvartal_3 and kvartal_1 >kvartal_4:
                    max = "квартал I"
                elif kvartal_2 >kvartal_1 and kvartal_2 >kvartal_3 and kvartal_2 >kvartal_4:
                    max = "квартал II"
                elif kvartal_3 > kvartal_1 and kvartal_3 >kvartal_2 and kvartal_3 >kvartal_4:
                    max = "квартал III"
                else:
                    max = "квартал IV" 
                #finding the minimum
                min = ""
                if kvartal_1 < kvartal_2 and kvartal_1 < kvartal_3 and kvartal_1 <kvartal_4:
                    min = "квартал I"
                elif kvartal_2 < kvartal_1 and kvartal_2 <kvartal_3 and kvartal_2 <kvartal_4:
                    min = "квартал II"
                elif kvartal_3 < kvartal_1 and kvartal_3 < kvartal_2 and kvartal_3 <kvartal_4:
                    min = "квартал III"
                else:
                    min = "квартал IV"
                data_revenue.append(element[0])
                name_of_enterprise.append(element[0])
                data_revenue.append(summ_year_production)
                data_revenue.append(min)
                data_revenue.append(max)
                year_production_data.append(data_revenue)
    except:
        messagebox.showinfo("ERROR","DATA ARE NOT ABLE TO BE READ")
    #printing the result
    count = 0
    for data in year_production_data:
        treeview.insert(parent='' ,iid= count  ,index= 'end', text="",values= (data[0],data[1],data[2],data[3]))
        count+=1
 
#writting the result in a text file       
def write_text_file():  
    try:
        file_name = filedialog.askopenfilename()
    except:
        messagebox.showinfo("ERROR","DID NOT OPEN THE FILE")
    with open(file_name , "w" , encoding="utf-8") as file:
        file.write("Наименование предприятия"+";"+"Год-й обьем выпуска"+";"+"Номер квартала с минобъемом"+";"+"Номер квартала с максимальным объемом"+"\n")
        for data in year_production_data:
            file.write(data[0]+";"+str(data[1])+";"+str(data[2])+";"+str(data[3])+"\n")
        file.close()
#printing the graphic in a window
def print_graphic():
    my_dictionary = {}
    for data in year_production_data:
        my_dictionary[year_production_data[0]]= year_production_data[1]
    plt.bar(my_dictionary.keys(),my_dictionary.values() , width = 0.9,color ="green")
    plt.title("График зависимости Годового объема выпуска продукции, тыс. р. от Наименования предприятия")
    plt.ylabel("Год-й обьем выпуска")
    plt.ylabel("Наименование предприятия")
    plt.show()
    
label  = Label (root ,text= "курсовая работа",pady=10,font  = "times 20 bold",background="cyan").pack()  
#button to see the information about the courswork
button_information = Button(root  , width=35 , height=2 , background="#1dbf85",text = "ИНФОРМАЦИЯ О КУРСОВОЙ РАБОТЕ",font  = "times 15 bold",borderwidth= 3,pady=10,command = information_coursovaia).pack(pady=10)
#button to see the information about the student
button_student = Button(root  , width=35, height=2 , background="#1dbf85",text = "ИНФОРМАЦИЯ О СТУДЬЕНТЕ",font  = "times 15 bold",borderwidth= 3,command  = information_student).pack(pady=10)
#button to see the information about the data that is going to be read from a file
button_data = Button(root  , width=35, height=2 , background="#1dbf85",text = "ПРОЧИТАТЬ ДАННЫЕ",font  = "times 15 bold",borderwidth= 3,command= read_data).pack(pady=10)
#button to show the year production
button_sort = Button(root  , width=35, height=2 , background="#1dbf85",text = "РАСЧЕТЫ",font  = "times 15 bold",borderwidth= 3,command = calculation).pack(pady=10)
#button to write data from the treeview to a file
button_write_file = Button(root  , width=35, height=2 , background="#1dbf85",text = "ЗАПЫСАТЬ ДАННЫЕ В ФАЙЛ",font  = "times 15 bold",borderwidth= 3,command = write_text_file).pack(pady=10)
#button to show the graphic 
button_show_graphic = Button(root  , width=35, height=2 , background="#1dbf85",text = "ПОКАЗАТЬ ГРАФИК",font  = "times 15 bold",borderwidth= 3,command = print_graphic).pack(pady=15)
mainloop()