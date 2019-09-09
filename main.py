import sys
# for Python2
from Tkinter import *
import ttk
import tkMessageBox
import tkFileDialog as filedialog
import ConfigParser as configparser
import tkFont

class Window(Frame):
	server = ""
	protocol = ""
	cmd_list = ["help"]
	cmd_list_max_size = 5

	# Define settings upon initialization. Here you can specify
	def __init__(self, master=None):
		# parameters that you want to send through the Frame class.
		Frame.__init__(self, master)

		#reference to the master widget, which is the tk window
		self.master = master
		
		frame1= Frame(master)
		frame2= Frame(master)
		frame3= Frame(master)
		frame4= Frame(master)
		frame1.pack();
		frame2.pack(fill=BOTH);
		frame3.pack(fill=BOTH, expand=1);
		frame4.pack(fill=BOTH, side=BOTTOM);

		self.init_menu(frame1)
		self.init_label(frame2)
		self.init_textbox_output(frame3)
		self.init_combobox_cmd(frame4)

	def init_menu(self, frame):

		# changing the title of our master widget
		self.master.title("UR Tool")
		
		# creating a menu instance
		menu = Menu(self.master)
		self.master.config(menu=menu)
		
		# create the file object
		file = Menu(menu, tearoff=0)
		file.add_command(label="Open config file", command=self.file_open)
		file.add_command(label="Exit", command=self.client_exit)
		
		# create the file object
		help = Menu(menu, tearoff=0)
		help.add_command(label="About", command=self.show_about)
		
		#added "file" to our menu
		menu.add_cascade(label="File", menu=file)
		#added "help" to our menu
		menu.add_cascade(label="Help", menu=help)
		
	def init_label(self, frame):
		self.label_cmd = Label(frame, text="Command: ", fg='navy')
		self.label_cmd.pack(side=LEFT)

	def init_textbox_output(self, frame):
		
		self.textbox_output = Text(frame)
		
		scroll = Scrollbar(frame, command=self.textbox_output.yview, orient=VERTICAL )
		scroll.pack(side=RIGHT, fill=BOTH)
		
		self.textbox_output.configure(yscrollcommand=scroll.set)
		self.textbox_output.pack(side=LEFT,fill=BOTH, expand=1, padx=2)
	
	def init_combobox_cmd(self, frame):
		self.cmd = StringVar()
		self.combobox_cmd = ttk.Combobox(frame, textvariable=self.cmd, values=self.cmd_list)
		self.combobox_cmd.focus_set()
		self.combobox_cmd.current(0)
		self.combobox_cmd.pack(side=LEFT, fill=X, expand=1, padx=2)
		
		button_Submit=Button(frame, text="Submit", command=self.click_submit)
		button_Submit.pack(side=RIGHT, padx=2)
		
		self.master.bind('<Return>', self.click_submit)
		
	def client_exit(self):
		exit()

	def file_open(self):
		self.filename = filedialog.askopenfilename(initialdir = ".",title = "Select file", filetypes=( ("Config file", "*.ini*"),("All types", "*.*")))
    
		if self.filename != "":
			# read config file
			config = configparser.ConfigParser()
			config.read(self.filename)
    	
			self.server = config.get("GENERAL", "SERVER")
			self.protocol = config.get("GENERAL", "PROTOCOL")
			
			# Python 3		
			#self.server = config["GENERAL"]["SERVER"]
			#self.protocol = config["GENERAL"]["PROTOCOL"]
			
			self.master.title("UR Tool - " + self.server + " (" + self.protocol + ")")

	def show_about(self):
		tkMessageBox.showinfo("About", "Version: 1.0.0\n")
		
	def click_submit(self, *args):
		if (self.server == ""):
			tkMessageBox.showerror("Error", "Please load the config file first.\n\nHint: \nFile > Open config file")
		else:
			command = self.cmd.get()
			self.label_cmd.config(text="Command: " + command)
			self.add_to_cmd_list(command, self.combobox_cmd)
			
			# set text in the textbox
			self.textbox_output.insert(INSERT, command + "...")

	def add_to_cmd_list(self, command, combobox):
		list_size = len(self.cmd_list)
		
		
		if not(self.cmd_list.count(command)):
			if (list_size == self.cmd_list_max_size):
				# remove the 1st command
				self.cmd_list.pop(0)

			self.cmd_list.append(command)
			combobox.config(values=self.cmd_list)
			
# -------------------------------------------------------- #
# main program                                             #
# -------------------------------------------------------- #
platform = sys.platform
root = Tk()

bigfont = tkFont.Font(family="Helvetica",size=11)
root.option_add("*Font", bigfont)

if platform == "win32":
	root.iconbitmap("favicon.ico")

app = Window(root)
root.mainloop() 
