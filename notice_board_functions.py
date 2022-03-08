import os
import PIL
import shutil
import re
from pdf2image import convert_from_path
from docx2pdf import convert
from load_variables import get_source_folder, get_program_destination

source_folder = get_source_folder()
program_destination = get_program_destination()
poppler_path = program_destination+r"\modules\poppler\Library\bin"


def load_folders(program_destination, source_folder):

    # removes all folders that don't exist in the source

    for folder in os.listdir(program_destination+"/static"):
        if folder not in os.listdir(source_folder) and folder != "assets" and folder != "load.js":
            shutil.rmtree(program_destination+"/static/"+folder)

    # loads all folders from the source

    for folder in os.listdir(source_folder):
        if os.path.isdir(source_folder+"/"+folder):
            filepath = program_destination+"/static/"+folder
            if not os.path.exists(filepath):
                os.mkdir(filepath)


def find_folders():

    # returns all folders in the static folder

    folders = []
    for filename in sorted(os.listdir("app/static/")):
        if os.path.isdir("app/static/"+filename) and filename != "assets":
            folders.append(filename)

    return folders


def convert_docx(directory):

    # searches through the source folder and converts docx files to pdf

    for filename in os.listdir(directory):
        
        if filename.endswith(".docx"):

            file_source = (directory+filename)
            file_destination = (directory+filename).replace(".docx",".pdf")

            if os.path.isfile(file_destination):
                pass
            else:
                convert(file_source, file_destination)
    
        else:
            continue


def load_items(source_dir, destination_dir):

    # converts every pdf in the source folder to a jpg and places them in the destination folder

    for filename in os.listdir(source_dir):

        if filename.endswith(".pdf"):
            # sets string names

            file_source = (source_dir+filename)
            file_destination = (destination_dir+filename).replace(".pdf"," page--1.jpg")
            file = convert_from_path(file_source, poppler_path=poppler_path)

            count = 1
         
            for page in file:
                if os.path.isfile(file_destination):
                    pass
                else:
                    page.save(file_destination)
                current_page = ("page--"+str(count)+".jpg")
                next_page = ("page--"+str(count+1)+".jpg")
                file_destination = file_destination.replace(current_page, next_page)
                count += 1
                    

        else:
            continue
    

    #removes files that aren't in the source

    for filename in os.listdir(destination_dir):

        pdf_filename = destination_dir+filename
        pdf_filename = pdf_filename.split(" page--", 1)
        pdf_filename = pdf_filename[0] + ".pdf"
        pdf_filename = pdf_filename.split("/", 3)
        pdf_filename = pdf_filename[3]

        

        if pdf_filename not in os.listdir(source_dir):
            os.remove(destination_dir+filename)
            print("removed: "+pdf_filename)


def get_size(source_dir, filename):

    # returns the image size of a file

    image = PIL.Image.open(source_dir+filename)
    width, height = image.size

    if width > height:
        return (320.32, 226.5)
    elif width < height:
        return (226.5, 320.32)
    else:
        print("image error: size not A4 ratio")
        return (0, 0)


def get_items(source_dir, option, filter = "", option_2 = "small", sort_by = "date"):

    # returns a list of files from the source folder, including its size and name

    return_list = []

    for filename in os.listdir(source_dir):

        if filename.endswith(".jpg"):
            file_size = get_size(source_dir, filename)

            if option_2 == "large":
                file_size = list(file_size)
                file_size[0] = file_size[0]*3
                file_size[1] = file_size[1]*3

            # uses '--' as an indicator for the page number
            name = filename.split("--", 1)[0]
            name = name.replace("page", "")

            string_filter = r"\b"+filter+r"\b"

            if option == "all":
                file = source_dir.replace("app/static/", "") +filename
                return_list.append([file, file_size[0], file_size[1], name])

            elif option == "filter" and re.search(string_filter, filename.replace(source_dir, "")):
                file = source_dir.replace("app/static/", "") +filename
                return_list.append([file, file_size[0], file_size[1], name])

    # sorts files by date

    if option_2 == "small":
        if sort_by == "date":
            return_list = sort_by_date(return_list)
        elif sort_by == "name":
            return_list = sort_by_order(return_list)
    elif option_2 == "large":
        return_list = sort_by_order(return_list)

    return return_list


def sort_by_date(list):  

    # sorts the list of files by date

    return sorted(list, reverse=True, key=lambda x: os.path.getctime((source_folder+"/"+x[0]).replace(" page--1.jpg", ".pdf")))


def sort_by_order(list):

    # sorts the list of files by order

    return sorted(list, reverse=False, key=lambda x: int(x[0].split("page--")[1].replace(".jpg", "")))
