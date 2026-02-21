
import tkinter as tk
from tkinter import ttk

class AgregarTarea:
    contador = 0
    
    def __init__(self, parent, valoresEditar = None):
        # obtenemos el valor del padre para futuro uso
        self.parent = parent
        self.valoresEditar = valoresEditar
        
        # creamos la ventana nueva
        self.window = tk.Toplevel()
        self.window.title("Agregar Tarea")
        self.window.resizable(False, False)
        self.window.grab_set()
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        
        # creamos el frame donde estaran
        frame = ttk.Frame(self.window)
        frame.grid(row=0, column=0, sticky='nsew', padx=20, pady=(10, 20))
        
        # configuramos la columna del grid 
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=0)
        frame.columnconfigure(3, weight=1)
        frame.columnconfigure(4, weight=1)
        frame.columnconfigure(5, weight=1)
        
        # titulo y descripcion 
        titulo = ttk.Label(frame, text='Titulo: ')
        self.input_titulo = ttk.Entry(frame)
        
        # realizamos un encapsulamiento para la descripcion y poder manejarlo
        frame_description = ttk.Frame(frame)
        descripcion = ttk.Label(frame_description, text='Descripcion: ')
        self.input_descripcion = tk.Text(frame_description,  height = 2, width=60)
        
        # status y la prioridad
        status = ttk.Label(frame, text='Status:')
        self.input_status = ttk.Combobox(frame, state='readonly', values=('Completado', 'En progreso', 'Cancelado'))
        prioridad = ttk.Label(frame, text='Prioridad:')
        self.input_prioridad = ttk.Combobox(frame, state='readonly', values=('Alta', 'Media', 'Baja'))
        
        # btn de guardado final
        btn_guardar = ttk.Button(frame, text='Guardar', cursor='hand2', command=self.ejecutarGaurdado)
        
       
        
        
        
        
        # publicamos grid titulo y descripcion
        titulo.grid(row=0, column=0, sticky="W", pady=10)
        self.input_titulo.grid(row=0, column=1,sticky="WE")
        
        # publicamos el frame y el input de descripcion
        frame_description.grid(row=2, column=0, columnspan=5, sticky="W", pady=(0,10))
        descripcion.grid(row=0, column=0, sticky="W")
        self.input_descripcion.grid(row=1, column=0)
        
        # publicamos el estatus y la prioridad 
        status.grid(row=3, column=0, sticky="W")
        self.input_status.grid(row=3, column=1, sticky="W")
        prioridad.grid(row=3, column=2, sticky="W")
        self.input_prioridad.grid(row=3, column=3, sticky="W")
        
        # publicamos el btn
        btn_guardar.grid(row=3, column=4, sticky="E") 
        
        
        # si pasamos valores significa que editaremos asi que cambiamos el titulo
        # y ejecutamos la funcion para editar los valores cargandolos nuevamente 
        if valoresEditar:
            self.window.title("Editar Tarea")
            self.editar()

    
    # funcion que ejecutara al darle click al btn guardar
    def ejecutarGaurdado(self):
        
        # si no pasamos valores significa que es valor nuevo y se agrega como nuevo elemento
        if not self.valoresEditar:
            
            AgregarTarea.contador += 1
            
            valores = (AgregarTarea.contador,
                    self.input_titulo.get(),
                    self.input_descripcion.get("1.0", "end-1c"),
                    self.input_status.get(),
                    self.input_prioridad.get())
            
            self.parent.insertarValores(valores)
        
        # contrario significa que es valor a editar 
        else:
            valores = (self.valoresEditar[0],
                    self.input_titulo.get(),
                    self.input_descripcion.get("1.0", "end-1c"),
                    self.input_status.get(),
                    self.input_prioridad.get())
        
            self.parent.guardarEditado(valores)
            
        # destruimos la ventana
        self.window.destroy()


    def editar(self):
        self.input_titulo.insert(0, self.valoresEditar[1])
        self.input_descripcion.insert('1.0', self.valoresEditar[2])
        self.input_status.set(self.valoresEditar[3])
        self.input_prioridad.set(self.valoresEditar[4])
        



    