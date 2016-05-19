#!/usr/bin/env python
import Tkinter
import tkFont
import parser

class Aplication(Tkinter.Frame):
	def __init__(self, master, **options):
		Tkinter.Frame.__init__(self, master, options)
		self.configure(bg="#f9f9f9")
		self.grid()
        

		self.font = tkFont.Font(family="Ubuntu", size=19)

		self.makeWidgets()

	def makeWidgets(self):
		self.display = Tkinter.Label(
			self,
			font=self.font,
			anchor="w",
			bg="#f9f9f9",
			textvariable=textDisplay
			)	
		self.display.grid(column=0, row=0, columnspan=5, sticky="we")

		buttons = [
			'7', '8', '9', '(', ')',
			'4', '5', '6', ' * ', ' / ',
			'1', '2', '3', ' +', ' -',
			'0', '.', '<-', '=' 
		]

		varColumn = -1
		varRow = 1

		for button in buttons:
			varColumn += 1

			self.gButton = MyButton(
				self,
				value=button,
				font=self.font,
				width=3,
				text=button.replace(' ', ''),
				bg="#ababab",
				highlightbackground="#545454",
				relief="flat",
				activebackground="#353535",
				activeforeground="#E02672"

			)

			if button == '<-':
				self.gButton.configure(command=self.gButton.delDisplay)

			elif button == '=':
				self.gButton.configure(command=self.gButton.calDisplay)
				self.gButton.grid(column=varColumn, row=varRow, columnspan=2, sticky="we")

			else:
				self.gButton.configure(command=self.gButton.addDisplay)

			self.gButton.grid(column=varColumn, row=varRow)

			if varColumn == 4:
				varColumn = -1
				varRow += 1

class MyButton(Tkinter.Button):
	def __init__(self, master, value=None, **options):
		Tkinter.Button.__init__(self, master, options)

		self.value = value
	
	def addDisplay(self):
		global secuencia

		guiCalculadora.display.config(fg="#E02672")
		secuencia += self.value

		textDisplay.set(secuencia.replace(' ', ''))

	def delDisplay(self):
		global secuencia

		if not secuencia == "":

			borrar = secuencia.split()[-1][-1]

			if borrar == '*' or borrar == '/':
				secuencia = secuencia[0:-3]
			elif borrar == '+' or borrar == '-':
				secuencia = secuencia[0:-2]
			else:
				secuencia = secuencia[0:-1]

			textDisplay.set(secuencia.replace(' ', ""))
		else:
			textDisplay.set(secuencia.replace(' ', ''))	

	def calDisplay(self):
		global secuencia

		guiCalculadora.display.config(fg="#268DEA")

		resultado = parser.resuelve(secuencia)
		textDisplay.set(resultado)

		secuencia = ""

root = Tkinter.Tk()
root.resizable(0, 0)
root.title("Calculator")

textDisplay = Tkinter.StringVar()
secuencia = ""

guiCalculadora = Aplication(root)

root.mainloop()
