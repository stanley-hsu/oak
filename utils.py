import Tkinter as tk
import tkMessageBox

def clickOK(label_cmd, label_info, input_cmd, input_server, radio_protocol):
  command = input_cmd.get("1.0", "end-1c")
  server = input_server.get("1.0", "end-1c")
  if (server == ""):
    tkMessageBox.showerror(title='Error', message='You have to input server.')
  elif (command==""):
    tkMessageBox.showerror(title='Error', message='You have to input command.')
  else:
    protocol = radio_protocol.get()
    label_cmd.configure(text="Command: " + command)
    label_info.configure(text="Send to " + server + " via " + protocol)
