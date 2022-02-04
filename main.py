import subprocess
from load_variables import get_program_destination

program_destination = get_program_destination()
program_destination = program_destination.split("app")[0]
program_destination = f"{program_destination}run.bat"
print(program_destination)

subprocess.call([program_destination])
