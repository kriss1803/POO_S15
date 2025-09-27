import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x500")

        # Campo de entrada
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.add_task())

        # Botones
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        self.add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, width=80, height=30, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Permitir doble clic para completar
        self.task_listbox.bind("<Double-Button-1>", lambda event: self.complete_task())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)

            # Si ya está completada, no volver a marcar
            if task.startswith("✔ "):
                return

            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, f"✔ {task}")
        except IndexError:
            messagebox.showwarning("Sin selección", "Por favor selecciona una tarea.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Sin selección", "Por favor selecciona una tarea.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
