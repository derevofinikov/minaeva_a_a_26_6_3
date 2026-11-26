import tkinter as tk
from tkinter import messagebox

# стартовые данные
balance = 1000
history = []

def update_ui():
    balance_label.config(text=f"Баланс: {balance} руб.")
    history_listbox.delete(0, tk.END)
    for item in reversed(history):
        history_listbox.insert(tk.END, item)

def add_history(text):
    global history
    history.append(text)
    if len(history) > 10:
        history.pop(0)
    update_ui()

def check_amount(amount_str):
    # проверка ввода: число ли это и больше ли нуля
    try:
        amount = float(amount_str)
        if amount <= 0:
            return None
        return amount
    except ValueError:
        return None

def deposit():
    global balance
    amount = check_amount(entry.get())
    if amount is None:
        messagebox.showerror("Ошибка", "Введи нормальную сумму больше нуля")
        return
    
    balance += amount
    add_history(f"Пополнение: +{amount}")
    entry.delete(0, tk.END)

def withdraw():
    global balance
    amount = check_amount(entry.get())
    if amount is None:
        messagebox.showerror("Ошибка", "Введи нормальную сумму больше нуля")
        return
        
    if amount > balance:
        messagebox.showerror("Ошибка", "Недостаточно средств")
        return
        
    balance -= amount
    add_history(f"Снятие: -{amount}")
    entry.delete(0, tk.END)

def transfer():
    global balance
    amount = check_amount(entry.get())
    if amount is None:
        messagebox.showerror("Ошибка", "Введи нормальную сумму больше нуля")
        return
        
    if amount > balance:
        messagebox.showerror("Ошибка", "Недостаточно средств")
        return
        
    balance -= amount
    add_history(f"Перевод: -{amount}")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Банкомат")
root.geometry("350x450")

balance_label = tk.Label(root, text="Баланс: 1000 руб.", font=("Arial", 14, "bold"))
balance_label.pack(pady=10)

tk.Label(root, text="Сумма:").pack()
entry = tk.Entry(root, width=20, font=("Arial", 12))
entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_deposit = tk.Button(btn_frame, text="Пополнить", width=12, command=deposit)
btn_deposit.grid(row=0, column=0, padx=5, pady=5)

btn_withdraw = tk.Button(btn_frame, text="Снять", width=12, command=withdraw)
btn_withdraw.grid(row=0, column=1, padx=5, pady=5)

btn_transfer = tk.Button(btn_frame, text="Перевести", width=12, command=transfer)
btn_transfer.grid(row=1, column=0, columnspan=2, pady=5)

tk.Label(root, text="История операций:").pack(pady=5)
history_listbox = tk.Listbox(root, width=40, height=8)
history_listbox.pack(pady=5)

root.mainloop()
