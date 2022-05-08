# Easy Notice Board

A program that allows you to easily create a notice board display for PDF files.

![Index Page](https://drive.google.com/file/d/1gCPeYpp3i0oOxDAfLt7wzI1uCs2Wk3H2/view?usp=sharing)

![Folder Page](https://drive.google.com/file/d/1aBAdjxN9-Glc79ZLR-4kr0oMJirQU-PC/view?usp=sharing)

![File Page](https://drive.google.com/file/d/1nH01ySUyexmr8jozyOM31Vq2umqhbufG/view?usp=sharing)

## How to use

Begin by running the "run.py" file. The first time it's run, it will request that you select the source folder. This folder should contain your folder directories with PDF files within them. You can find an example of one in the "examples" folder. Your source folder can be synced to your perfered cloud storage service for remote access if needed. The source folder location can then be changed any time in the config file. The notice board should then open in your default browser.

## Configuration

Once it's been set, if you need to change the filepath to your source folder, open the config.ini file and enter it after "SOURCE = ".

By changing the value "NAVIGATION" in the config file to "False", it removes the back button after a folder is selected. This is to prevent users from going back from the folder page.

All the assets can be edited to create a look to your liking; you will find them in static/assets.

If the icons look small or big and vertically uncentered, this can be solved by adjusting the zoom setting on your browser.

## Compatibility

Tested for Windows 10 and 11.
