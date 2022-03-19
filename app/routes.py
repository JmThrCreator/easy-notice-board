from app import app
from flask import render_template, redirect, request, url_for
from notice_board_functions import find_folders, load_folders, load_items, get_source_folder, get_items
from load_variables import get_program_destination, get_source_folder, get_navigation_setting

program_destination = get_program_destination()
source_folder = get_source_folder()
navigation_setting = get_navigation_setting()

# redirects to the home page
@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect(url_for("home"))

# shows all the folders in the source folder
@app.route("/home", methods=["GET", "POST"])
def home():

    # removes folders that don't exist in the source from app/static
    # loads folders from the source into app/static
    load_folders(program_destination, source_folder)

    # gets all the foldernames from app/static
    folders = find_folders()

    # open folder
    if request.method == "POST":
        for folder in folders:
            if folder in request.form: 

                # prepares variables to load the folder page
                filepath_source = source_folder+"/"+folder+"/"
                filepath_destination = "app/static/"+folder+"/"

                # converts pdf files to jpg and loads them into app/static
                load_items(filepath_source, filepath_destination)

                return render_template("/folder.html", thumbnail_list=get_items(filepath_destination, "filter", "page--1"), folder=folder, navigation_setting = navigation_setting)

    return render_template("/home.html", folder_list = folders)

# shows all the files in the folder
@app.route("/folder", methods=["GET", "POST"])
def folder():

    # return to home page
    if "home_button" in request.form:
        return render_template("/home.html", title="Home", folder_list = find_folders())

    filepath = next(iter(request.form.to_dict()))
    filepath_dict = filepath.split("/")
    indicator = filepath_dict[0]

    # sort buttons
    try:
        indicator = indicator[0:11]
        source_folder = filepath_dict[0][12:]
    except IndexError:
        indicator = ""
    
    if indicator in ["name_button", "date_button"]:
        folder_filepath = "app/static/"+source_folder+"/"
        if indicator == "date_button":
            sort_by = "date"
        else:
            sort_by = "name"
        return render_template("/folder.html", thumbnail_list=get_items(folder_filepath, "filter", "page--1", sort_by=sort_by), folder=source_folder, navigation_setting = navigation_setting)
    
    # open file
    source_folder = filepath_dict[0]
    pages = filepath_dict[len(filepath_dict)-1]
    pages_length = len(pages)
    source_dir = "app/static/"+filepath[:-pages_length]
    pages_name = pages.replace("page--1.jpg", "")
    return render_template("/display_page.html", thumbnail_list=get_items(source_dir, "filter", pages_name, "large"), folder=source_folder)

@app.route("/display_page", methods=["GET", "POST"])
def display_page():

    # return to folder page
    source_folder = next(iter(request.form.to_dict()))
    folder_filepath = "app/static/"+source_folder+"/"
    return render_template("/folder.html", thumbnail_list=get_items(folder_filepath, "filter", "page--1"), folder = source_folder, navigation_setting = navigation_setting)



