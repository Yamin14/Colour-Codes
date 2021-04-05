import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import *
import random

class Game(Widget):
	def __init__(self, **kwargs):
		super(Game, self).__init__(**kwargs)
		
		#colours
		self.colours = []
		self.blacklisted = []
		self.choices = [0, 0.5, 1]
		
		for i in range(24):
			r = self.choices[random.randint(0, 2)]
			g = self.choices[random.randint(0, 2)]
			b = self.choices[random.randint(0, 2)]
			while (r==g and g==b) or ((r, g, b, 1) in self.blacklisted):
				r = self.choices[random.randint(0, 2)]
				g = self.choices[random.randint(0, 2)]
				b = self.choices[random.randint(0, 2)]
				
			self.blacklisted.append((r, g, b, 1))
			self.colours.append((r, g, b, 1))
			
		#layout
		x, y= 0, 0
		self.rex = []
		with self.canvas:
			for i in range(24):
				Color(rgba=self.colours[i])
				self.rex.append(Rectangle(size=(240, 160), pos=(x, y)))
				x += 240
			
				if x == 720:
					x = 0
					y += 160
				
				if y == 640:
					y += 160
					
		#center label
		with self.canvas:
			Color(rgba=(1, 1, 1, 0.7))
			Rectangle(size=(720, 160), pos=(0, 640))
			
		self.code = Label(text="(r, g, b)", color=(0, 0, 0, 1), pos=(0, 640), size=(720, 160), font_size=70)
		self.add_widget(self.code)

	def on_touch_down(self, touch):
		#checking the colour and displaying the colour code
		x, y = touch.pos[0], touch.pos[1]
		
		for i in range(24):
			if x >= self.rex[i].pos[0] and x <= self.rex[i].pos[0]+240 and y >= self.rex[i].pos[1] and y <= self.rex[i].pos[1]+160:
				self.code.color = self.colours[i]
				r = self.colours[i][0]/1*255
				g = self.colours[i][1]/1*255
				b = self.colours[i][2]/1*255
				
				if int(r) == r:
					r = int(r)
				if int(g) == g:
					g = int(g)
				if int(b) == b:
					b = int(b)
				
				self.code.text = f"({r}, {g}, {b})"
	
class MyApp(App):
	def build(self):
		return Game()
		
if __name__ == "__main__":
	MyApp().run()
	
