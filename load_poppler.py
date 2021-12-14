import os
import sys
from load_variables import get_program_destination

def load_poppler():
    program_destination = get_program_destination()
    if sys.platform == "win32":
        poppler_path = os.pathsep + (program_destination + r"app\modules\poppler\Library\bin")

        #os.environ["PATH"] += poppler_path
        #os.environ["PATH"] += os.pathsep + (program_destination + r"app\modules\poppler\Library\bin")

        #add poppler as an environment variable in the virtual environment

        os.environ["POPPLER_LIBRARY"] = (program_destination + r"app\modules\poppler\Library\bin")



        if poppler_path not in os.environ['PATH']:
            #os.environ['PATH'] += poppler_path
            print("poppler added to path")