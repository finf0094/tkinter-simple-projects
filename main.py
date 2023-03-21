import time
import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()


def first_task():
    problem = "5 + 3 * 2 = "
    answer = 5 + 3 * 2
    messagebox.showinfo("Math Problem", f"{problem}{answer}")


def second_task():
    second_window = tk.Toplevel(root)
    second_window.title("Математический есеп")

    operation_label = tk.Label(second_window, text="Математикалық операцияны енгізіңіз (+, -, *, /):")
    operation_entry = tk.Entry(second_window)
    num1_label = tk.Label(second_window, text="Бірінші сан:")
    num1_entry = tk.Entry(second_window)
    num2_label = tk.Label(second_window, text="Екінші сан:")
    num2_entry = tk.Entry(second_window)


    def calculate():
        math_operation = operation_entry.get()
        num1 = int(num1_entry.get())
        num2 = int(num2_entry.get())
        if math_operation == '+':
            result = num1 + num2
        elif math_operation == '-':
            result = num1 - num2
        elif math_operation == '*':
            result = num1 * num2
        elif math_operation == '/':
            result = num1 / num2

        messagebox.showinfo("Math Result", f"{num1} {math_operation} {num2} = {result}")

        second_window.destroy()

    def third_task():

        third_window = tk.Toplevel(root)
        third_window.title("Сандарды болжау ойыны")

        number_to_guess = random.randint(1, 100)

        def guess_number():

            guess = int(guess_entry.get())

            if guess == number_to_guess:
                messagebox.showinfo("Сандарды болжау ойыны», «Құттықтаймыз! Сіз санды таптың!")
                third_window.destroy()
            elif guess < number_to_guess:
                messagebox.showinfo("Сандарды болжау ойыны», «Сіздің болжамыңыз тым төмен. Қайтадан байқап көріңіз.")
            else:
                messagebox.showinfo("Сандарды болжау ойыны», «Сіздің болжамыңыз тым жоғары. Қайтадан байқап көріңіз.")


        guess_label = tk.Label(third_window, text="1 мен 100 арасындағы санды тап:")
        guess_entry = tk.Entry(third_window)


        guess_button = tk.Button(third_window, text="Болжам", command=guess_number)


        guess_label.pack()
        guess_entry.pack()
        guess_button.pack()

    calculate_button = tk.Button(second_window, text="Есептеу", command=calculate)


    operation_label.pack()
    operation_entry.pack()
    num1_label.pack()
    num1_entry.pack()
    num2_label.pack()
    num2_entry.pack()
    calculate_button.pack()





def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = "".join(random.sample(characters, length))
    messagebox.showinfo("Құпия сөз жасалды", f"Құпия сөзіңіз: {password}")



def third_task():

    third_frame = tk.Frame(root)
    third_frame.pack(fill=tk.BOTH, expand=True)

    number_to_guess = random.randint(1, 100)

    def guess_number():
        nonlocal number_to_guess
        guess = int(guess_entry.get())

        if guess == number_to_guess:
            messagebox.showinfo("Сіз санды таптыңыз!")
            switch_to_main_menu()
        elif guess < number_to_guess:
            messagebox.showinfo("Сіздің саңыныз кішкентай.")
        else:
            messagebox.showinfo("Сіздің саныңых үлкен.")

        guess_entry.delete(0, tk.END)

    guess_label = tk.Label(third_frame, text="1 ден 100 ге дейін санды енгізіңіз:")
    guess_entry = tk.Entry(third_frame)
    guess_button = tk.Button(third_frame, text="Есептеу", command=guess_number)

    guess_label.pack(pady=10)
    guess_entry.pack(pady=10)
    guess_button.pack(pady=10)

    def switch_to_main_menu():
        third_frame.destroy()


    back_button = tk.Button(third_frame, text="Артка", command=switch_to_main_menu)
    back_button.pack(side=tk.BOTTOM, pady=20)

def five_task():
    def convert():
        try:
            celsius = float(celsius_entry.get())
            fahrenheit = celsius * 9 / 5 + 32
            kelvin = celsius + 273.15
            fahrenheit_label.config(text=f"Фаренгейттегі температура: {fahrenheit:.1f}")
            kelvin_label.config(text=f"Кельвиндегі температура: {kelvin:.2f}")
        except ValueError:
            fahrenheit_label.config(text="кате жаздыныз!")
            kelvin_label.config(text="")

    window = tk.Tk()
    window.title("Температура түрлендіргіші")

    celsius_label = tk.Label(window, text="Температураны Цельсий градусымен енгізіңіз:")
    celsius_label.grid(column=0, row=0)

    celsius_entry = tk.Entry(window)
    celsius_entry.grid(column=1, row=0)

    convert_button = tk.Button(window, text="Трансформация", command=convert)
    convert_button.grid(column=2, row=0)

    fahrenheit_label = tk.Label(window, text="")
    fahrenheit_label.grid(column=0, row=1)

    kelvin_label = tk.Label(window, text="")
    kelvin_label.grid(column=0, row=2)


def six_task():
    import tkinter as tk

    def fibonacci(n):

        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

    def display_fibonacci():
        try:
            n = int(input_field.get())
            result = fibonacci(n)
            output_text.config(state='normal')
            output_text.delete('1.0', tk.END)
            for num in result:
                output_text.insert(tk.END, str(num) + '\n')
            output_text.config(state='disabled')
        except ValueError:
            output_text.config(state='normal')
            output_text.delete('1.0', tk.END)
            output_text.insert(tk.END, "сан жазыныз!")
            output_text.config(state='disabled')


    root = tk.Tk()
    root.title("Фибоначчи саны")


    input_label = tk.Label(root, text="сан жазыныз n:")
    input_label.pack()
    input_field = tk.Entry(root)
    input_field.pack()

    display_button = tk.Button(root, text="Фибоначчи сандарын корсету", command=display_fibonacci)
    display_button.pack()

    output_text = tk.Text(root, state='disabled', width=30, height=10)
    output_text.pack()

    root.mainloop()

def seven_task():
    quotes = {
        "мотивация": [
            'Cіздің болашағыңыз көп нәрсеге байланысты, бірақ ең алдымен өзіңізге',
             'Егер сіз бір нәрсені өзгерткіңіз келсе, әрекетті бастаңыз және басқалардан өзгерістерді күтпеңіз',
             'Жетістікке мойымайтындар келеді',
             'Шағын адамдар тобы әлемді өзгерте алатынына ешқашан күмәнданбаңыз. Шындығында, бұл әрқашан болған»'
        ],
        "жетістік": [
            'Егер сіз ең жақсы болуға ұмтылмасаңыз, онда сіз қазірдің өзінде бас тартасыз',
             'Жетістік белгісі – қол жеткізгеніңіз емес, оған жету жолында жеңгеніңіз',
             'Табыс – соңғы нүкте емес, егер біз алға ұмтылғымыз келсе, ол өмір бойы жалғасады',
             'Жетістіктің ең жақсы дәлелі - сіздің еңбегіңіз'
        ],
    }

    def get_random_quote(category):
        return random.choice(quotes[category])

    def update_quote():
        category = var.get()
        quote = get_random_quote(category)
        quote_label.config(text=quote)

    root = tk.Tk()
    root.title("Кездейсоқ дәйексөздер")

    tk.Label(root, text="Санатты таңдаңыз:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

    var = tk.StringVar(value="мотивация")
    tk.OptionMenu(root, var, *quotes.keys()).grid(row=0, column=1, padx=10, pady=10, sticky="w")

    quote_label = tk.Label(root, text="")
    quote_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    tk.Button(root, text="Дәйексөзді жаңарту", command=update_quote).grid(row=2, column=0)

def eight_task():

    def update_time():
        current_time = time.strftime("%H:%M:%S %p")
        time_label.config(text=current_time)


    root = tk.Tk()
    root.title("Текущее время")


    time_label = tk.Label(root, font=("Helvetica", 24), text="")
    time_label.pack(pady=10)

    update_button = tk.Button(root, text="Жаңарту уақытты", command=update_time)
    update_button.pack()


    update_time()


    root.mainloop()

def nine_task():
    def update_population(event):
        country = country_var.get()
        population = country_population.get(country, "Неизвестно")
        population_label.config(text=f"Население {country}: {population} млн.")


    root = tk.Tk()
    root.title("Страны и население")


    countries = ["Россия", "США", "Китай", "Индия", "Япония"]
    country_var = tk.StringVar(value=countries[0])
    country_dropdown = tk.OptionMenu(root, country_var, *countries, command=update_population)
    country_dropdown.pack(padx=10, pady=10)

    country_population = {
        "Россия": 144.5,
        "США": 328.2,
        "Китай": 1393.8,
        "Индия": 1366.4,
        "Япония": 126.2,
    }
    population_label = tk.Label(root, text="Выберите страну для просмотра населения")
    population_label.pack(padx=10, pady=10)

    root.mainloop()


def teen_task():
    root = tk.Tk()
    root.title("Список задач")

    tasks = []

    def add_task():
        task = entry_task.get()
        if task != "":
            tasks.append(task)
            list_tasks.delete(0, tk.END)
            for task in tasks:
                list_tasks.insert(tk.END, task)
            entry_task.delete(0, tk.END)

    def delete_task():
        selected_tasks = list_tasks.curselection()
        for task in selected_tasks:
            del tasks[task]
        list_tasks.delete(0, tk.END)
        for task in tasks:
            list_tasks.insert(tk.END, task)

    label_task = tk.Label(root, text="Задача:")
    label_task.pack()

    entry_task = tk.Entry(root)
    entry_task.pack()

    button_add_task = tk.Button(root, text="Добавить задачу", command=add_task)
    button_add_task.pack()

    button_delete_task = tk.Button(root, text="Удалить задачу", command=delete_task)
    button_delete_task.pack()

    list_tasks = tk.Listbox(root)
    list_tasks.pack()

    root.mainloop()

menu_bar = tk.Menu(root)

img = Image.open("erko.png")
photo = ImageTk.PhotoImage(img)
label = tk.Label(root, image=photo)
label.pack()

math_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Math", menu=math_menu)


math_menu.add_command(label="Тапсырма 1", command=first_task)

math_menu.add_command(label="Тапсырма 2", command=second_task)

math_menu.add_command(label="Тапсырма 3", command=third_task)

math_menu.add_command(label="Тапсырма 4", command=lambda: generate_password(8))

math_menu.add_command(label="Тапсырма 5", command=five_task)

math_menu.add_command(label="Тапсырма 6", command=six_task)

math_menu.add_command(label="Тапсырма 7", command=seven_task)

math_menu.add_command(label="Тапсырма 8", command=eight_task)

math_menu.add_command(label="Тапсырма 9", command=nine_task)

math_menu.add_command(label="Тапсырма 10", command=teen_task)
root.config(menu=menu_bar)

root.mainloop()
