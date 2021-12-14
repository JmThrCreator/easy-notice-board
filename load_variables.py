import os
import sys
import configparser

def get_config():    
    config = configparser.ConfigParser()
    config.read("config.ini")
    return(config)

def get_source_folder():
    config = get_config()
    source_folder = config.get("SOURCE FILE LOCATION", "SOURCE")
    return source_folder

def get_navigation_setting():
    config = get_config()

    boolean_string_map = {"True":True, "False":False}
    navigation_setting = boolean_string_map.get(config.get("SETTINGS", "NAVIGATION"))
    return navigation_setting

def get_program_destination():

    program_destination = os.path.abspath("load.py")
    if sys.platform == "win32":
        program_destination = program_destination.replace("\load.py", "")

    if sys.platform == "linux":
        program_destination = program_destination.replace("/load.py", "")
    
    return program_destination

    
