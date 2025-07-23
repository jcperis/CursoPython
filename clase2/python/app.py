import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from data_io import (
    importar_json,
    exportar_json,
    importar_pickle,
    exportar_pickle
)


class DiccionarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Lista de Diccionarios")
        self.lista_diccionarios = []

        # Frame para la lista visual
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.frame_lista, selectmode=tk.EXTENDED, font=("Courier", 10))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scroll = tk.Scrollbar(self.frame_lista, command=self.listbox.yview)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scroll.set)

        # Botones
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(fill=tk.X)

        botones = [
            ("Importar JSON", self.de_json),
            ("Importar Pickle", self.de_pickle),
            ("Exportar JSON", self.a_json),
            ("Exportar Pickle", self.a_pickle()),
            ("Nueva lista", self.nueva_lista),
            ("Añadir", self.anadir_diccionario),
            ("Eliminar", self.eliminar_seleccionados)
        ]

        for texto, comando in botones:
            tk.Button(self.frame_botones, text=texto, command=comando).pack(side=tk.LEFT, padx=5, pady=5)


    def actualizar_vista(self):
        self.listbox.delete(0, tk.END)
        for d in self.lista_diccionarios:
            self.listbox.insert(tk.END, str(d))

    def de_json(self):
        path = filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
        if path:
            try:
                datos = importar_json(path)
                if isinstance(datos, list):
                    self.lista_diccionarios = datos
                    self.actualizar_vista()
                else:
                    messagebox.showerror("Error", "El archivo no contiene una lista de diccionarios.")
            except Exception as e:
                messagebox.showerror("Error al importar JSON", str(e))

    def de_pickle(self):
        path = filedialog.askopenfilename(filetypes=[("Pickle", "*.pkl")])
        if path:
            try:
                datos = importar_pickle(path)
                if isinstance(datos, list):
                    self.lista_diccionarios = datos
                    self.actualizar_vista()
                else:
                    messagebox.showerror("Error", "El archivo no contiene una lista de diccionarios.")
            except Exception as e:
                messagebox.showerror("Error al importar Pickle", str(e))

    def a_json(self):
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")])
        if path:
            try:
                exportar_json(path, self.lista_diccionarios)
                messagebox.showinfo("Éxito", "Exportado correctamente a JSON.")
            except Exception as e:
                messagebox.showerror("Error al exportar JSON", str(e))

    def a_pickle(self):
        path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle", "*.pkl")])
        if path:
            try:
                exportar_pickle(path, self.lista_diccionarios)
                messagebox.showinfo("Éxito", "Exportado correctamente a Pickle.")
            except Exception as e:
                messagebox.showerror("Error al exportar Pickle", str(e))

    def nueva_lista(self):
        if messagebox.askyesno("Confirmar", "¿Deseas borrar la lista actual?"):
            self.lista_diccionarios = []
            self.actualizar_vista()

    def anadir_diccionario(self):
        entrada = simpledialog.askstring("Añadir diccionario", "Introduce el diccionario como clave=valor separados por coma (ej: nombre=Juan,edad=30):")
        if entrada:
            try:
                diccionario = dict(pair.strip().split('=') for pair in entrada.split(','))
                self.lista_diccionarios.append(diccionario)
                self.actualizar_vista()
            except Exception as e:
                messagebox.showerror("Error de formato", "Formato incorrecto. Usa clave=valor, separados por coma.")

    def eliminar_seleccionados(self):
        seleccion = list(self.listbox.curselection())
        if not seleccion:
            return
        for i in reversed(seleccion):
            del self.lista_diccionarios[i]
        self.actualizar_vista()



if __name__ == "__main__":
    root = tk.Tk()
    app = DiccionarioApp(root)
    root.mainloop()
