import os
def enter_data():
    first_name=input("Введите имя: ")
    second_name=input("Введите фамилию: ")
    midle_name = input("Введите отчество: ")
    phone_number= input("Введите номер телефона: ")
    contact = {'first_name': first_name,'second_name': second_name,'midle_name':midle_name,'phone_number':phone_number}
    return contact

def pars_record(str):
    str=str.split(";")
    contact = {'first_name': str[0],'second_name': str[1],'midle_name':str[2],'phone_number':str[3]}
    return contact

def add_rec(list):
    contact=enter_data()
    list.append(contact)
    return list
    
def save_ph(file_name,list,):
    temp_list=open_ph(file_name)
    with open(file_name, 'a', encoding='utf-8') as file:
      for i in range(len(list)):
        contact=list[i]
        if temp_list.count(contact)==0:
            for value in contact.values():
                value=value+";"
                file.write(value)
            file.write('\n')
        
def open_ph(file_name,list=[]):
    try:     
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                list.append(pars_record(line))
        return list
    except:
        print(f"файла {file_name} не существует!")
        input("press enter to cont")
        return

def view_ph(list):
    if list==None or len(list)==0:
        print("список пустой")
        return
    
    title = ["id","Имя", "Фамилия", "Отчество", "Телефон"]
    print("\t\t".join(title))
    print("|=================================================================================|")
    for i in range(len(list)):
        str=""
        for (k,v) in list[i].items():
            str+=f"{v}\t\t"
        print(f"{i}\t\t{str}")

def del_rec(list):
    view_ph(list)
    record_for_del=int(input("Номер какой записи удалить? : "))
    list.remove(list[record_for_del])
    view_ph(list)
    return list
    
def copy_ph(list):
    if not list:
        print("список пустой")
        input("press enter to cont")
        return
    view_ph(list)
    list_for_copy=[]
    record_for_copy=int(input("Номер какой записи копировать? : "))
    # print(list[record_for_copy])
    list_for_copy.append(list[record_for_copy])
    file_name_for_save=input("Имя файла для записи? : ")
    # print(f"create {file_name_for_save} for records {list_for_copy}") 
    with open(file_name_for_save, 'a', encoding='utf-8') as file:
      for i in range(len(list_for_copy)):
        contact=list_for_copy[i]
        for value in contact.values():
            value=value+";"
            file.write(value)
        file.write('\n')

def exit_ph(isStop):
    isStop=True
    print('end')
    return isStop
def show_ui():
    # for windows
    if os.name == 'nt':
        os.system('cls')
     # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')
    print(f"1 загрузить данные\n2 посмотреть данные\n3 добавить запись\n4 удалить запись\n5 сохранить данные\n6 копировать данные\n0 выход")

isStop=False
list=[]
pb_file_name='phonebook_my.txt'
while not isStop:
    show_ui()
    number=input('Ожидаю ввод ==> ')
    if number=='0':
        isStop=exit_ph(isStop)
    if number=='1':
        list=open_ph(pb_file_name,list)
    if number=='2':
        view_ph(list)
        input("press enter to cont")
    if number=='3':
        list=add_rec(list)
    if number=='4':
        list=del_rec(list)
    if number=='5':
        save_ph(pb_file_name,list)
    if number=='6':
        copy_ph(list)
