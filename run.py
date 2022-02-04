import tkinter as tk
from tkinter import filedialog
from load_variables import get_source_folder
from configobj import ConfigObj

# allows user to find source folder
def request_source_folder():
    root = tk.Tk()
    root.withdraw()

 
    file_path = filedialog.askdirectory(title="Select the source folder")
    return(file_path)

# gets the source folder from config.ini
source_folder = get_source_folder()

# if there is no directory, it asks the user to select one
if source_folder == "":
    file_path = request_source_folder()

    config = ConfigObj("config.ini")
    config["SOURCE FILE LOCATION"]["SOURCE"] = file_path
    config.write()

