# Start.py for install requirements and loading into project

from GUI import main_menu
from subprocess import run

if __name__ == "__main__":

    run(["pip", "install", "-r", "requirements.txt"])

    menu=main_menu(tuning_name="standard")

    try:
        menu.mainloop()
    except Exception as e:
        print(f"Error occurred: {e}")
