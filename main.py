import Tkinter as tk
import utils

root=tk.Tk()
root.title("My First Tk GUI")
root.resizable(0,0)
#root.geometry("400x400")

label_cmd=tk.Label(root, text="Command: <input in following text box>")
label_info=tk.Label(root, text="<Target>")

label_log_display=tk.Label(root, text="Log: ")
label_server=tk.Label(root, text="Server: ")
label_protocol=tk.Label(root, text="Protocol: ")

textbox_cmd = tk.Text(root,height=1)
textbox_server = tk.Text(root,height=1, width="20")
textbox_output = tk.Text(root,height=20)

scrollbar=tk.Scrollbar(root, command=textbox_output.yview, orient=tk.VERTICAL)
scrollbar.config(command=textbox_output.yview)
textbox_output.configure(yscrollcommand=scrollbar.set)

protocol = tk.StringVar()
radio_ssh = tk.Radiobutton(root, text="SSH", variable=protocol, value="SSH", command=utils.sel(label_info, textbox_server, protocol))
radio_com = tk.Radiobutton(root, text="COM", variable=protocol, value="COM", command=utils.sel(label_info, textbox_server, protocol))
radio_ssh.select();

button_Submit=tk.Button(root, text="Submit", command=lambda: utils.clickOK(label_cmd, label_info, textbox_cmd, textbox_server, protocol))

label_server.grid(row=1,column=0, sticky=tk.W)
textbox_server.grid(row=2,column=0,sticky=tk.W)
label_protocol.grid(row=3,column=0, sticky=tk.W)
radio_ssh.grid(row=4,column=0, sticky=tk.W)
radio_com.grid(row=5,column=0, sticky=tk.W)
label_log_display.grid(row=6,column=0,sticky=tk.W)
textbox_output.grid(row=7,column=0)
scrollbar.grid(row=7,column=1,sticky=tk.N+tk.S+tk.W)

label_cmd.grid(row=8,column=0,sticky=tk.W)
textbox_cmd.grid(row=10,column=0)
button_Submit.grid(row=10,column=1)
label_info.grid(row=9,column=0,sticky=tk.W)

root.mainloop()