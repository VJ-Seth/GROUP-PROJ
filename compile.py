import os
import sys

def main():
    start_prompt = input("""By running this script, you wish to convert this game into an exceutable.
                                You must have pygame and pyinstaller installed for this process.
                                Do you meet this requirements? (yes or no): """)
    
    if start_prompt == "no":
        sys.exit()

    print("Compiling. Please Wait")
    os.popen("pyinstaller main.py --onefile --noconsole")
    print("""
        WAIT 5 seconds and then continue.Compilation Complete. Move the assets folder into the dist folder and run the application
    """)


if __name__ == "__main__":
    main()