import gi;gi.require_version('Gtk','3.0');from gi.repository import Gtk as gtk, GdkPixbuf, Gdk
from MenuBar import *
from Insetos import *

def Sol(self):
	self.Soly = gtk.Window()
	self.grid_result = gtk.Grid(column_spacing=6, row_spacing=6)
	self.Soly.add(self.grid_result)
	self.Button = []
		
	for c in range(len(self.label)):
		self.Button.append(gtk.Button())
	
	#Image0
	self.image0 = gtk.Image()
	pixbuf0 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto0.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image0.set_from_pixbuf(pixbuf0)
	
	#Image1
	self.image1 = gtk.Image()
	pixbuf1 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto1.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image1.set_from_pixbuf(pixbuf1)

	#image2
	self.image2= gtk.Image()
	pixbuf2 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto2.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image2.set_from_pixbuf(pixbuf2)
	
	#image3
	self.image3= gtk.Image()
	pixbuf3 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto3.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image3.set_from_pixbuf(pixbuf3)

	#image4
	self.image4= gtk.Image()
	pixbuf4 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto4.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image4.set_from_pixbuf(pixbuf4)

	#image5
	self.image5= gtk.Image()
	pixbuf5 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto5.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image5.set_from_pixbuf(pixbuf5)

	#image6
	self.image6= gtk.Image()
	pixbuf6 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto6.png', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image6.set_from_pixbuf(pixbuf6)

	#image7
	self.image7= gtk.Image()
	pixbuf7 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto7.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image7.set_from_pixbuf(pixbuf7)

	#image8
	self.image8= gtk.Image()
	pixbuf8 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto8.png', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image8.set_from_pixbuf(pixbuf8)

	#image9
	self.image9= gtk.Image()
	pixbuf9 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto9.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image9.set_from_pixbuf(pixbuf9)
	
	#Button0
	self.Button[0].add(self.image0)
	self.Button[0].set_size_request(100,100)
	self.Button[0].connect('clicked', lambda arg: Inseto0(self))
	#----------------------------------------
	#Button1
	self.Button[1].add(self.image1)
	self.Button[1].set_size_request(100,100)
	self.Button[1].connect('clicked', lambda arg: Inseto1(self))
	#----------------------------------------
	#Button2
	self.Button[2].add(self.image2)
	self.Button[2].set_size_request(100,100)
	self.Button[2].connect('clicked', lambda arg: Inseto2(self))
	#----------------------------------------

	#Button3
	self.Button[3].add(self.image3)
	self.Button[3].set_size_request(100,100)
	self.Button[3].connect('clicked', lambda arg: Inseto3(self))
	#----------------------------------------

	#Button4
	self.Button[4].add(self.image4)
	self.Button[4].set_size_request(100,100)
	self.Button[4].connect('clicked', lambda arg: Inseto4(self))
	#----------------------------------------

	#Button5
	self.Button[5].add(self.image5)
	self.Button[5].set_size_request(100,100)
	self.Button[5].connect('clicked', lambda arg: Inseto5(self))
	#----------------------------------------	

	#Button6
	self.Button[6].add(self.image6)
	self.Button[6].set_size_request(100,100)
	self.Button[6].connect('clicked', lambda arg: Inseto6(self))
	#----------------------------------------

	#Button7
	self.Button[7].add(self.image7)
	self.Button[7].set_size_request(100,100)
	self.Button[7].connect('clicked', lambda arg: Inseto7(self))
	#----------------------------------------	

	#Button8
	self.Button[8].add(self.image8)
	self.Button[8].set_size_request(100,100)
	self.Button[8].connect('clicked', lambda arg: Inseto8(self))
	#----------------------------------------

	#Button9
	self.Button[9].add(self.image9)
	self.Button[9].set_size_request(100,100)
	self.Button[9].connect('clicked', lambda arg: Inseto9(self))
	#----------------------------------------	
	return 0