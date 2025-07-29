import os
import subprocess
from tkinter import filedialog, messagebox, Tk

def openPyFile():
    return filedialog.askopenfilename(
        title = "Select a Python file",
        filetypes=[("Python file", "*.py")]
    )

def openIcon():
    return filedialog.askopenfilename(
        title = "Select an Icon (.ico)",
        filetypes=[("Icon", "*.ico")]
    )

def build(scriptPath, onefile=True, noconsole=False, icon=None):
    pyExportFolder = os.path.dirname(os.path.abspath(scriptPath)) + "/export"

    dist_path = os.path.join(pyExportFolder, "exe")
    build_path = os.path.join(pyExportFolder, "build")
    spec_path = pyExportFolder

    command = ["pyinstaller"]

    if onefile:
        command.append("--onefile")
    if noconsole:
        command.append("--noconsole")
    if icon:
        command.append(f"--icon={icon}")

    command += [
        f"--distpath={dist_path}",
        f"--workpath={build_path}",
        f"--specpath={spec_path}"
    ]

    command.append(scriptPath)
    return command

def inputHelper(msg):
    print(msg)
    print("Press enter to continue")
    input()

def main():
    root = Tk()
    root.withdraw()

    print("Hi there!")
    inputHelper("First, you have to select your python file!")
    scriptPath = openPyFile()

    if not scriptPath:
        inputHelper("Uh, okay I guess, bye!")
        return

    inputHelper("Thanks!, now you have to set some compile options!")

    oneFile = messagebox.askyesno("Compile Option", "Compile everything in one file?\nIf yes, the exe will have everything needed inside it")
    noConsole = messagebox.askyesno("Compile Option", "Hide console?\nIf your .py is all literal console, NO!")
    useIcon = messagebox.askyesno("Compile Option", "Add an icon image? (.ico file)")
    icon = openIcon() if useIcon else None

    print("Great!, almost done!")
    print("Press enter to compile all the stuff!!!")
    input()

    command = build(scriptPath, oneFile, noConsole, icon)

    messagebox.showinfo("Compiling...", f"Executing:\n{' '.join(command)}")

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Done!", "Created executable in the folder exe!")

        print("\nThanks for using me!!!, have a good day ;D")
        print("Press Enter to finish!")
        input()
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Error while compiling! :c")

if __name__ == "__main__":
    main()
