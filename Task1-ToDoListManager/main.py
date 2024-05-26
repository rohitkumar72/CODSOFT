# TASK - 1
# A To-Do List application is a useful project that helps users manage and organize their tasks efficiently.
# This project aims to create a command-line or GUI-based application using Python, allowing users to create, update,
# and track their to-do lists.

from tkinter import *
import tkinter.messagebox as msg
import os
from termcolor import colored

class TodoApp(Tk):

    def __init__(self):
        super().__init__()
        # Centering the window when opened.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        print(colored(f"SCREEN WIDTH : {screen_width} x SCREEN HEIGHT : {screen_height}", "blue"))
        app_width = 1280
        app_height = 720
        print(colored(f"APP WIDTH : {app_width} x APP HEIGHT : {app_height}", "blue"))
        set_x = int((screen_width/2) - (app_width/2))
        set_y = int((screen_height/2) - (app_height/2))
        self.geometry(f'{app_width}x{app_height}+{set_x}+{set_y}')
        self.title("TodoList Manager")
        self.resizable(False, False)
        self.configure(bg="#f7f7f7")
        # Font sizes
        self.sizes = {'Small': ('Helvetica', 12), 'Medium': ('Helvetica', 16), 'Large': ('Helvetica', 22)}
        self.current_size = 'Medium'
        # Design
        self.create_app_heading()
        self.give_separation_line()
        self.item_input_frame = self.create_input_frame()
        self.item_entry_box = self.create_new_item_entry_box()
        self.create_add_button()
        self.list_display_frame = self.create_display_frame()
        self.todo_display_listbox = self.create_todo_list_box()
        self.listbox_scrollbar = self.add_listbox_scrollbar()
        self.show_scrollbar()
        self.operation_button_frame = self.create_operation_frame()
        self.load_images()
        self.create_buttons()
        self.size_option_menu()
        # Functions
        self.listbox_load()

    def create_app_heading(self):
        app_heading = Label(self, text="TODO-List Manager", font=('Arial', 27, 'bold'), pady=20, bg="#4CAF50", fg="#FFFFFF")
        app_heading.pack(fill=X)

    def give_separation_line(self):
        frame = Frame(self, bg="#0b227a", height=5)
        frame.pack(fill=X)

    def create_input_frame(self):
        frame = Frame(self, bg="#d3d3d3", height=100, padx=20, pady=20)
        frame.pack(fill=X)
        return frame

    def create_new_item_entry_box(self):
        entry = Entry(self.item_input_frame, width=50, borderwidth=0, font=self.sizes[self.current_size])
        entry.pack(side=LEFT)
        return entry

    def create_add_button(self):
        button = Button(self.item_input_frame, text="Add to list", width=18, borderwidth=0, font=('Helvetica', 14, 'bold'), bg="#2e5d72", fg="#ffffff", command=self.add_item)
        button.pack(side=LEFT)

    def create_display_frame(self):
        frame = Frame(self, width=200, height=700, bg="#f0f0f0", padx=20, pady=20)
        frame.pack(fill=BOTH)
        return frame

    def create_todo_list_box(self):
        listbox = Listbox(self.list_display_frame, width=78, height=20, font=self.sizes[self.current_size], bg="#dde1e3", fg="#0e0c49", selectbackground="#6016d9", activestyle=NONE, cursor="hand2")
        listbox.pack(side=LEFT, fill=BOTH)
        return listbox

    def add_listbox_scrollbar(self):
        scrollbar = Scrollbar(self.list_display_frame)
        scrollbar.pack(side=LEFT, fill=BOTH)
        return scrollbar

    def show_scrollbar(self):
        self.todo_display_listbox.config(yscrollcommand=self.listbox_scrollbar.set)
        self.listbox_scrollbar.config(command=self.todo_display_listbox.yview)

    def create_operation_frame(self):
        frame = Frame(self, bg="#d3d3d3")
        frame.pack(fill=BOTH)
        return frame

    def load_images(self):
        self.edit_img = PhotoImage(file='Images/edit.png')
        self.clear_img = PhotoImage(file='Images/clear.png')
        self.remove_img = PhotoImage(file='Images/remove.png')
        self.uncross_img = PhotoImage(file='Images/save.png')
        self.cross_img = PhotoImage(file='Images/cross.png')

    def create_buttons(self):
        buttons = [
            (self.edit_img, self.edit_task, LEFT),
            (self.cross_img, self.cross_item, RIGHT),
            (self.uncross_img, self.uncross_item, RIGHT),
            (self.remove_img, self.delete_crossed_item, RIGHT),
            (self.clear_img, self.clear_list, RIGHT)
        ]
        for img, cmd, side in buttons:
            button = Button(self.operation_button_frame, image=img, bd=0, bg="#d3d3d3", cursor="hand2", command=cmd)
            button.pack(side=side, pady=10, padx=10)

    def blank_line_handler(self):
        with open("todo.txt", "r") as tdf:
            lines = tdf.readlines()
        if any(line.strip() for line in lines):
            with open("todo.txt", "w") as new_tdf:
                for line in lines:
                    if line.strip():
                        new_tdf.write(line)

    def add_item(self):
        new_item = self.item_entry_box.get()
        if new_item:
            with open('todo.txt', "a") as tdf:
                tdf.write(f"{new_item}\n")
            self.listbox_load()
            self.item_entry_box.delete(0, END)
        else:
            msg.showwarning(title="WARNING", message="Cannot add an empty task.")

    def listbox_load(self):
        self.blank_line_handler()
        self.todo_display_listbox.delete(0, END)
        try:
            with open('todo.txt', "r") as tdf:
                for line in tdf:
                    self.todo_display_listbox.insert(END, line.strip())
        except Exception as e:
            print(colored(f"SORRY! EXCEPTION OCCURRED: {e}", "red"))
            with open('todo.txt', "w") as tdf:
                pass

    def cross_item(self):
        try:
            self.todo_display_listbox.itemconfig(self.todo_display_listbox.curselection(), fg="#b7b3bd")
            self.todo_display_listbox.selection_clear(0, END)
        except TclError:
            msg.showwarning(title="WARNING", message="Task list is empty or no task selected.")

    def uncross_item(self):
        try:
            self.todo_display_listbox.itemconfig(self.todo_display_listbox.curselection(), fg="#0e0c49")
            self.todo_display_listbox.selection_clear(0, END)
        except TclError:
            msg.showwarning(title="WARNING", message="Task list is empty or no task selected.")

    def save_edit_task(self, line_number, task):
        with open("todo.txt", "r") as tdf:
            lines = tdf.readlines()
        lines[line_number] = task + "\n"
        with open("todo.txt", "w") as tdf:
            tdf.writelines(lines)
        self.listbox_load()
        self.edit_task_popup_window.destroy()
        msg.showinfo(title="Edited", message=f"Successfully edited Task {line_number + 1}!")

    def popup_edit_task(self, item_number, editable_task):
        self.edit_task_popup_window = Toplevel(self)
        self.edit_task_popup_window.geometry("700x215")
        self.edit_task_popup_window.resizable(False, False)
        self.edit_task_popup_window.title(f"Edit task {item_number + 1}")
        Label(self.edit_task_popup_window, text=f"EDIT TASK:\n{editable_task}", fg="#1d3b64", font=self.sizes[self.current_size]).pack()
        task_entry = Entry(self.edit_task_popup_window, width=60, font=self.sizes[self.current_size], fg="#1d3b64")
        task_entry.insert(0, editable_task)
        task_entry.pack(pady=20)
        btn_frame = Frame(self.edit_task_popup_window, padx=20, pady=20)
        btn_frame.pack()
        Button(btn_frame, text="SAVE", width=13, bd=0, bg="#3c8bdf", fg="#ffffff", font=("Helvetica", 13, "bold"), command=lambda: self.save_edit_task(item_number, task_entry.get())).pack(side=LEFT, padx=(370, 10))
        Button(btn_frame, text="CANCEL", width=13, bd=0, bg="#3c8bdf", fg="#ffffff", font=("Helvetica", 13, "bold"), command=self.edit_task_popup_window.destroy).pack(side=LEFT)
        self.edit_task_popup_window.mainloop()

    def edit_task(self):
        try:
            selected_item = self.todo_display_listbox.curselection()
            if selected_item:
                line_number = selected_item[0]
                with open("todo.txt", "r") as tdf:
                    lines = tdf.readlines()
                self.popup_edit_task(line_number, lines[line_number].strip())
            else:
                msg.showwarning(title="WARNING", message="No task selected.")
        except Exception as e:
            msg.showwarning(title="WARNING", message=f"An error occurred: {e}")

    def delete_crossed_item(self):
        try:
            selected_item = self.todo_display_listbox.curselection()
            if selected_item:
                line_number = selected_item[0]
                with open("todo.txt", "r") as tdf:
                    lines = tdf.readlines()
                lines.pop(line_number)
                with open("todo.txt", "w") as tdf:
                    tdf.writelines(lines)
                self.listbox_load()
            else:
                msg.showwarning(title="WARNING", message="No task selected.")
        except Exception as e:
            msg.showwarning(title="WARNING", message=f"An error occurred: {e}")

    def clear_list(self):
        if msg.askyesno(title="CLEAR LIST", message="Do you want to delete all tasks?"):
            open('todo.txt', 'w').close()
            self.listbox_load()

    def size_option_menu(self):
        size_frame = Frame(self, bg="#d3d3d3", pady=10)
        size_frame.pack(fill=X)
        Label(size_frame, text="Adjust Size:", font=('Helvetica', 14), bg="#d3d3d3").pack(side=LEFT, padx=(20, 10))
        size_var = StringVar(self)
        size_var.set(self.current_size)
        size_menu = OptionMenu(size_frame, size_var, *self.sizes.keys(), command=self.adjust_size)
        size_menu.pack(side=LEFT)
        size_menu.config(width=10, font=('Helvetica', 12))

    def adjust_size(self, selected_size):
        self.current_size = selected_size
        self.item_entry_box.config(font=self.sizes[selected_size])
        self.todo_display_listbox.config(font=self.sizes[selected_size])
        for widget in self.edit_task_popup_window.winfo_children():
            if isinstance(widget, Entry) or isinstance(widget, Label):
                widget.config(font=self.sizes[selected_size])

if __name__ == "__main__":
    todo = TodoApp()
    todo.mainloop()
