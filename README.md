## How to use

Begin by setting your source folder in the config file. It should contain your folder directories with PDF and DOCX files within them. You can find an example of this in the examples folder. This source folder can be synced to your perfered cloud storage service for remote access if needed. You start the notice board by running the python virtual environment and running the flask app. This can be done by entering the following commands in cmd:

### Windows ###
```
cd [file location of easy-notice-board folder]
venv\Scripts\activate
(python -m) flask run
```

### Linux ###
```
cd [file location of easy-notice-board folder]
source venv/bin/activate
flask run
```

## Configuration

Open the config.ini file and change the filepath to your source folder. To test if it works, you can use the filepath for the folder named 'source' and change it later.

By changing the value 'NAVIGATION' in the config file to 'False', it removes the back button after a folder is selected. This is to prevent users from going back from the folder page.

All the assets can be edited to create a look to your liking; you will find them in static/assets.

If the icons look small or big and vertically uncentered, this can be solved by adjusting the zoom setting on your browser.

## Compatibility

Tested for Windows 10 and Ubuntu Linux; docx files can only be converted on windows systems with Microsoft Word installed.
Tested with python versions 3.8.8, 3.8.10, 3.9.5 and 3.9.7.
Tested for Chrome, Edge and Firefox.

## Issues

If you don't have Microsoft Word installed, the program will not be able to convert docx files and will throw an error if it tries to. You can find an adjusted python file in examples. Alternatively, you can make sure not to put docx files in the program.
