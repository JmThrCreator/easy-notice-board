from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, request
from notice_board_functions import find_folders, load_folders, load_items, get_source_folder, get_items, get_size, convert_docx
from load_variables import get_program_destination, get_source_folder, get_navigation_setting

program_destination = get_program_destination()
source_folder = get_source_folder()
navigation_setting = get_navigation_setting()


@app.route("/", methods=['GET', 'POST'])
def index():
    print("index")
    form = LoginForm()
    return render_template("/login.html", title="Sign In", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate() and request.method == "POST":
        flash("Login requested for email {}".format(form.email.data))
        return redirect("/home")
    return render_template("/login.html", title="Sign In", form=form)

@app.route("/home", methods=["GET", "POST"])
def home():

    # loads all folders from the source folder
    
    load_folders(program_destination, source_folder)

    folders = find_folders()

    for folder in folders:
        if folder in request.form:
            filepath_source = source_folder+"/"+folder+"/"
            filepath_destination = "static/"+folder+"/"
            convert_docx(filepath_source, program_destination)
            load_items(filepath_source, filepath_destination)
            return render_template("/folder.html", thumbnail_list=get_items(filepath_destination, "filter", "page--1"), folder=folder, navigation_setting = navigation_setting)


    return render_template("/home.html", folder_list = find_folders())

@app.route("/folder", methods=["GET", "POST"])
def folder():

    if "home" in request.form:
        return render_template("/home.html", folder_list = find_folders())
    
    filepath = next(iter(request.form.to_dict()))
    filepath_dict = filepath.split("/")
    indicator = filepath_dict[0]

    try:
        indicator = indicator[0:5]
    except IndexError:
        indicator = ""


    if indicator == "reset":

        source_folder = get_source_folder()

        folder = filepath_dict[0]
        folder = folder.replace("reset", "")
        filepath_source = source_folder+"/"+folder+"/"
        filepath_destination = "static/"+folder+"/"

        convert_docx(filepath_source, program_destination)
        load_items(filepath_source, filepath_destination)
        
        return render_template("/folder.html", thumbnail_list=get_items(filepath_destination, "filter", "page--1"), folder = folder, navigation_setting = navigation_setting)
    else:

        source_folder = filepath_dict[0]
        pages = filepath_dict[len(filepath_dict)-1]
        pages_length = len(pages)
        source_dir = "static/"+filepath[:-pages_length]
        pages_name = pages.replace("page--1.jpg", "")

        return render_template("/display_page.html", thumbnail_list=get_items(source_dir, "filter", pages_name, "large"), folder=source_folder)

@app.route("/display_page", methods=["GET", "POST"])
def display_page():

    source_folder = next(iter(request.form.to_dict()))
    folder_filepath = "static/"+source_folder+"/"
    return render_template("/folder.html", thumbnail_list=get_items(folder_filepath, "filter", "page--1"), folder = source_folder, navigation_setting = navigation_setting)



