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

		""" Criar Menu """

		lb_menu = Label(frameTitulo, text="Menu")
		lb_menu.pack(side=LEFT, padx=5, pady=5)		
		lb_tool = Label(frameTitulo, text="Ferramentas")
		lb_tool.pack(side=LEFT, padx=5, pady=5)
		lb_arq= Label(frameTitulo, text="Arquivos")
		lb_arq.pack(side=LEFT, padx=5, pady=5)
		lb_opcao = Label(frameTitulo, text="Opcoes")
		lb_opcao.pack(side=LEFT, padx=5, pady=5)
		lb_preferencia = Label(frameTitulo, text="Preferencias")
		lb_preferencia.pack(side=LEFT, padx=5, pady=5)

		frameCad = Frame(self)
		frameCad.pack(fill=X)

		""" Etiquetas """
		lb_nome = Label(frameCad, text="Nome do cliente:")
		lb_nome.pack(side=LEFT, padx=5, pady=5)
		en_nome = Entry(frameCad)
		en_nome.pack(fill=X, padx=5, expand=True)

		frameCad2 = Frame(self)
		frameCad2.pack(fill=X)

		lb_placa = Label(frameCad2, text="Placa do carro:")
		en_placa = Entry(frameCad2)
		lb_placa.pack(side=LEFT, padx=5, pady=5)
		en_placa.pack(fill=X, padx=5, expand=True)

		frameCad3 = Frame(self)
		frameCad3.pack(fill=X)

		lb_modelo = Label(frameCad3, text="Modelo do carro:")
		en_modelo = Entry(frameCad3)
		lb_modelo.pack(side=LEFT, padx=5, pady=5)
		en_modelo.pack(fill=X, padx=5, expand=True)

		frameCad4 = Frame(self)
		frameCad4.pack(fill=X)

		lb_fabri = Label(frameCad4, text="Fabricante: ")
		en_fabri = Entry(frameCad4)
		lb_fabri.pack(side=LEFT, padx=5, pady=5)
		en_fabri.pack(fill=X, padx=5, expand=True)

def main():

	root = Tk()
	root.geometry("400x200")
	app = Caixa(root)
	root.mainloop()

if __name__ == '__main__':
	main()