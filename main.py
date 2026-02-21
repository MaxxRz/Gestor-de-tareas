
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

from add_window import AgregarTarea

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.windowAddEdit = None
        self.listaTabla = []
        
        
        # implementacion de funciones
        self.configurar_ventana()
        self.frame_filtros()
        self.frame_tabla()
    
    
    
    
    
    def configurar_ventana(self):
        self.geometry('800x400')
        self.title('Gestor de tareas')
        self.resizable(0,0)
        self.grid_columnconfigure(0, weight=1)
    
    
    def frame_filtros(self):
        filtrosFrame = ttk.Frame(self, padding=10)
        filtrosFrame.grid(row=0, column=0 ,padx=10, pady=10, sticky="nsew")
        filtrosFrame.grid_columnconfigure(4, weight=1)
        
        # contanido de la seccion filtros
        label_title = ttk.Label(filtrosFrame, text='Filtros', font=('', 10))
        
        opciones = ('Completado', 'En progreso', 'Cancelado')
        label_status = ttk.Label(filtrosFrame, text='Status:')
        self.entry_status = ttk.Combobox(filtrosFrame, state='readonly', values=opciones)
        
        label_prioridad = ttk.Label(filtrosFrame, text='Prioridad: ')
        self.entry_prioridad = ttk.Combobox(filtrosFrame, state='readonly', values=('Alta', 'Media', 'Baja'))
        
        btnLimpiar = ttk.Button(filtrosFrame, text='Limpiar Filtro', cursor='hand2', command=self.limpiarFiltro)
        btnBuscar = ttk.Button(filtrosFrame, text='Buscar', cursor='hand2', command=self.realizarFiltro)
        
        # implementacion
        label_title.grid(row=0, column=0)
        label_status.grid(row=1, column=0)
        self.entry_status.grid(row=1, column=1, padx=(0,20))
        label_prioridad.grid(row=1, column=2)
        self.entry_prioridad.grid(row=1, column=3, padx=(0,20))
        btnBuscar.grid(row=1, column=4, padx=(10, 0), sticky="W")
        btnLimpiar.grid(row=1, column=5, padx=(10, 0), sticky="E")
        
        
    def frame_tabla(self):
        tablaFrame = ttk.LabelFrame(self, padding=10)
        tablaFrame.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")
        tablaFrame.grid_columnconfigure(0, weight=1)
        
        # contanido de la seccion botones 
        btnFrame = ttk.Frame(tablaFrame)
        btnFrame.grid(row=0, column=1, sticky='W')
        
        btnAgregar = ttk.Button(btnFrame, text='Agregar tarea', cursor='hand2', command=self.window_agregar)
        btnEditar = ttk.Button(btnFrame, text='Editar tarea', cursor='hand2', command=self.editarValor)
        btnEliminar = ttk.Button(btnFrame, text='Eliminar tarea', cursor='hand2', command=self.eliminarValor)
        btnLimpiar = ttk.Button(btnFrame, text='Limpiar lista', cursor='hand2', command=self.eliminarLista)
        
        
        btnLimpiar.pack( side='right', padx=(10,0))
        btnEliminar.pack( side='right', padx=(10,0))
        btnEditar.pack( side='right', padx=(10,0))
        btnAgregar.pack( side='right', padx=(10,0))
        
        
        
        
        self.tabla = ttk.Treeview(tablaFrame, columns=('id', 'Titulo', 'Descripcion', 'Estatus', 'Prioridad', 'Fecha'), show='headings')
        # Cabezeras
        self.tabla.heading('id', text='id', anchor=tk.W)
        self.tabla.heading('Titulo', text='Titulo', anchor=tk.W)
        self.tabla.heading('Descripcion', text='Descripcion', anchor=tk.W)
        self.tabla.heading('Estatus', text='Estatus', anchor=tk.W)
        self.tabla.heading('Prioridad', text='Prioridad', anchor=tk.W)
        
        # Columnas
        self.tabla.column(0, width=50)
        self.tabla.column(1, width=150)
        self.tabla.column(2, width=380)
        self.tabla.column(3, width=100)
        self.tabla.column(4, width=100)
        
        
        self.tabla.grid(row=1, column=0, columnspan=2, pady=(10,0))




    # >>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<< #
    
    # >>>>>>>>>> Funciones de Opciones <<<<<<<<<<<< #
    
    # >>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<< #
    
    # validamos que no exista otra ventana 
    def window_agregar(self, item = None):
       
        if not self.tabla.selection():
            self.windowAddEdit = AgregarTarea(self)
        else:
            self.windowAddEdit = AgregarTarea(self, item)
    
    # esta funcion se ejecuta desde la ventana y obtiene los valores proporcionados
    def insertarValores(self, values):
        self.tabla.insert(parent='', index=tk.END, values=values)
        self.listaTabla.append(values)
    
    # funcion btn editar valor seleccionado
    def editarValor(self):
        selected_item = self.tabla.selection() # Obtiene la fila seleccionada
        item = self.tabla.item(selected_item)['values']
        
        # si no hay nada seleccionado cerramos el ciclo
        if not selected_item:
            return
        
        # ejecutamos la ventana para editar y le pasamos los valores que se pueden modificar
        self.window_agregar(item)
        
                
    # funcion que se ejutara en la ventana donde se edita para insertar valores modificados
    def guardarEditado(self, value):
        itemTrabajar = self.tabla.selection() # obtenemos el id del elemento que se modificara
        self.tabla.item(itemTrabajar, values=value)

        # realizamos la modificacion del elemento en el listado guardado
        for index, item in enumerate(self.listaTabla):
            if item[0] == value[0]:
                self.listaTabla[index] = value

  
    # funcion para eliminar un valor
    def eliminarValor(self):
        selected_item = self.tabla.selection() # Obtiene la fila seleccionada
        id_item = self.tabla.item(selected_item)['values'][0] # obtenemos el valor del id
        
        if selected_item:
            self.tabla.delete(selected_item) 

        # buscamos el elemento en el listado y lo eliminamos
        for index, item in enumerate(self.listaTabla):
            if item[0] == id_item:
                del self.listaTabla[index]
        
    
    # funcion para eliminar toda la lista
    def eliminarLista(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
            
            
        AgregarTarea.contador = 0 # modificamos el valor de clase de la ventana
        
        self.listaTabla = [] # reiniciamos la lista
        
    
    
    # >>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<< #
    
    # >>>>>>>>>>> Funciones de Filtro <<<<<<<<<<<<< #
    
    # >>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<< #
                
    def limpiarFiltro(self):
        self.entry_status.set('')
        self.entry_prioridad.set('')
        
        # eliminamos todos los valores de la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # mostramos los valores de la tabla original
        for item in self.listaTabla:
            self.tabla.insert(parent='', index=tk.END, values=item)


    def realizarFiltro(self):
        valorStatus = self.entry_status.get()
        valorPrioridad = self.entry_prioridad.get()
        
        if not valorStatus and not valorPrioridad:
            return
       
        listaMostrar = self.operacionesFiltrio(valorStatus, valorPrioridad)
        
        # eliminamos todos los valores de la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # mostramos los valores filtrados
        for item in listaMostrar:
            self.tabla.insert(parent='', index=tk.END, values=item)
        

    def operacionesFiltrio(self, status, prioridad):
        lista = []
        
        # si existen los dos elemenos, solamente buscara los que sean igual alos dos
        if status and prioridad:
            for idex, item in enumerate(self.listaTabla):
                if item[3] == status and item[4] == prioridad:
                    lista.append(item)
                    
            return lista
        
        # si solo buscamos por prioridad o status
        if status:
            for idex, item in enumerate(self.listaTabla):
                if item[3] == status:
                    lista.append(item)
                    
            return lista
        
        if prioridad:
            for idex, item in enumerate(self.listaTabla):
                if item[4] == prioridad:
                    lista.append(item)
                    
            return lista
        
                
        
        



if __name__ == '__main__':
    app = App()
    app.mainloop()
    