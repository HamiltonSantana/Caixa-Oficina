from tkinter import *

class Caixa(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.iniUI()

	def iniUI(self):
		self.parent.title("Caixa")
		self.pack(fill=BOTH, expand=True)

		frameTitulo = Frame(self)
		frameTitulo.pack(fill=X)

		"""  Criar Menu """
		menubar = Menu(frameTitulo)
		filMenu = Menu(menubar, tearoff=0)
		filMenu.add_command(label="Open")
		filMenu.add_command(label="Save")
		filMenu.add_separator()
		filMenu.add_command(label="Exit")
		menubar.add_cascade(label="File", menu=filMenu)
		""" Menu 2 """
		editMenu = Menu(menubar, tearoff=0)
		editMenu.add_command(label="Cut")
		editMenu.add_command(label="Copy")
		editMenu.add_command(label="Paste")
		menubar.add_cascade(label="Edit", menu=editMenu)
		""" Menu 3 """ 
		opMenu = Menu(menubar, tearoff=0)
		opMenu.add_command(label="Opcao")
		menubar.add_cascade(label="Option", menu=opMenu)
		
		prefMenu = Menu(menubar, tearoff=0)
		prefMenu.add_command(label="Configuraçoes")
		menubar.add_cascade(label="Preferencia", menu=prefMenu)

		helpMenu = Menu(menubar, tearoff=0)
		helpMenu.add_command(label="About")
		menubar.add_cascade(label="Help",menu=helpMenu)
				
		self.parent.config(menu=menubar)
		
		frameCad = Frame(self)
		frameCad.columnconfigure(0, weight=1)
		frameCad.pack(fill=X)
		
		""" Declara entradas """
		lb_nome = Label(frameCad, text="Nome do cliente:")
		lb_placa = Label(frameCad, text="Placa do carro:")
		lb_modelo = Label(frameCad, text="Modelo do carro:")
		lb_fabri = Label(frameCad, text="Fabricante: ")
		
		en_nome = Entry(frameCad)
		en_placa = Entry(frameCad)
		en_modelo = Entry(frameCad)
		en_fabri = Entry(frameCad)
		""" Packing entradas """
		lb_nome.grid(row=0, column=0, sticky=W)
		en_nome.grid(row=1, sticky=E+W)
		lb_placa.grid(row=2, column=0, sticky=W)
		en_placa.grid(row=3, sticky=E+W)
		lb_modelo.grid(row=4, column=0, sticky=W)
		en_modelo.grid(row=5, sticky=E+W)
		lb_fabri.grid(row=6, column=0, sticky=W)
		en_fabri.grid(row=7, sticky=E+W)	
		
def main():

	root = Tk()
	root.geometry("400x210")
	app = Caixa(root)
	root.mainloop()

if __name__ == '__main__':
	main()