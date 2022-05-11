# Easy Notice Board

A program that allows you to easily create a notice board display for PDF files.

<img src="http://drive.google.com/uc?export=view&id=1gCPeYpp3i0oOxDAfLt7wzI1uCs2Wk3H2" width="50%">

<img src="http://drive.google.com/uc?export=view&id=1aBAdjxN9-Glc79ZLR-4kr0oMJirQU-PC" width="50%">

<img src="http://drive.google.com/uc?export=view&id=1nH01ySUyexmr8jozyOM31Vq2umqhbufG" width="50%">

## Setup

Create a virtual environment and install the dependencies using the following commands:

```
python3 -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## How to use

Begin by running the "run.py" file. The first time it's run, it will request that you select the source folder. This folder should contain your folder directories with PDF files within them. You can find an example of one in the "examples" folder. Your source folder can be synced to your perfered cloud storage service for remote access if needed. The source folder location can then be changed any time in the config file. The notice board should then open in your default browser.

## Configuration

Once it's been set, if you need to change the filepath to your source folder, open the config.ini file and enter it after "SOURCE = ".

By changing the value "NAVIGATION" in the config file to "False", it removes the back button after a folder is selected. This is to prevent users from going back from the folder page.

All the assets can be edited to create a look to your liking; you will find them in static/assets.

If the icons look small or big and vertically uncentered, this can be solved by adjusting the zoom setting on your browser.
