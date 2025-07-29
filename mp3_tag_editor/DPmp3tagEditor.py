import eyed3
import os
from tkinter import filedialog, messagebox, Tk

version = "1.0.0"

# hehehe
def inputHelper(msg):
    print(msg)
    print("Press enter to continue")
    input()

def titlePrint(title):
    clear()
    print("/*** " + title + " ***/")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def stfu():
    inputHelper("Uh, okay I guess, bye!")
    exit()

### Action Chits
def mp3Act(path, func, arg1):
    try:
        audiofile = eyed3.load(path)
        if audiofile is None:
            raise Exception("Failure while opening mp3 file")

        if audiofile.tag is None:
            audiofile.initTag(version = (2, 3, 0))

        func(audiofile, arg1)
        audiofile.tag.save(version =  (2, 3, 0))

    except Exception as e:
        messagebox.showerror("Error", f"Error:\n{str(e)}")

def actionHelper(act, arg1, _desc):
    for song in mp3_path:
        mp3Act(song, act, arg1)

    if isPlural == "0": 
        messagebox.showinfo("Done!", _desc + f" to: \n{os.path.basename(mp3_path[0])}")
    else: 
        messagebox.showinfo("Done!", _desc + f" to \n{len(mp3_path)} files!")

    print("Thanks for using me!\nWrite anything to reset everything\nJust press enter to select an option!")
    dummy = input()
    if (len(dummy) > 0): main()
    else: selectOption()

def getEveryDamnFile(parentFolder):
    _files = []
    for cur, subdirs, preFile in os.walk(parentFolder):
        for archivo in preFile:
            fullPath = os.path.join(cur, archivo)
            _files.append(fullPath)
    return _files

def mp3Cover(audiofile, imgPath):
    with open(imgPath, "rb") as img:
        mime = "image/jpeg" if imgPath.lower().endswith(".jpg") else "image/png"
        audiofile.tag.images.set(3, img.read(), mime, "Cover")

def mp3Album(audiofile:eyed3.core.AudioFile, name):
    audiofile.tag.album = name

def mp3Author(audiofile:eyed3.core.AudioFile, name):
    audiofile.tag.album_artist = name

isPlural = ""
option = ""
mp3_path = []

### Selection Chits
def main():
    global isPlural
    global option
    global mp3_path

    root = Tk()
    root.withdraw()

    isPlural = ""
    option = ""
    mp3_path = []

    titlePrint("Main")
    print("Welcome to 'DPs MP3 tag editor' (" + version +") pal!")
    print("With this, uh tool?, you can edit the image cover, the album name and the album artist!\n")

    selectPlural()
    selectFiles()

    selectOption()

def selectPlural():
    print("Enter 0 if you want to change only ONE mp3")
    print("Enter 1 if you want to change MORE THAN ONE mp3s!")
    print("Enter 2 if you want to select ONE FOLDER, and change every mp3 in it\n(including subfolders!)")
    global isPlural
    isPlural = input()

    while (isPlural not in ("0", "1", "2")):
        print("\nI SAID")
        print("ENTER 0 IF YOU WANT TO CHANGE ONE MP3")
        print("ENTER 1 IF YOU WANT TO CHANGE MORE THAN ONE MP3s")
        print("ENTER 2 IF YOU WANT TO SELECT ONE FOLDER, AND CHANGE EVERY MP3 IN IT\n(INCLUDING SUBFOLDERS!)")
        isPlural = input()

    inputHelper("\nGreat!")

def selectFiles():
    global isPlural
    global mp3_path

    if isPlural == "0":
        inputHelper("1. Open an mp3 file")
        mp3_path = [filedialog.askopenfilename(
            title = "Select an mp3 file",
            filetypes = [("MP3 file", "*.mp3")]
        )]
    elif isPlural == "2":
        inputHelper("1. Select a folder")
        mp3_path = getEveryDamnFile(filedialog.askdirectory(
            title = "Select a folder",
        ))
    else:
        inputHelper("1. Open some mp3 files")
        mp3_path = list(filedialog.askopenfilenames(
            title = "Select some mp3 files",
            filetypes = [("MP3 files", "*.mp3")]
        ))

    if not mp3_path: stfu()

def selectOption():
    global option
    option = ""
    options = ["[0] Album Cover",
               "[1] Album Name",
               "[2] Album Artist"]

    print("\nSelect the option you want to change!")
    print("\n".join(options))
    option = input()

    while (option not in [str(i) for i in range(len(options))]):
        print("\nMmMmMmMMm, I don't see that option there!")
        print("Try again!")
        option = input()

    match option:
        case "0":
            cover()
        case "1":
            album()
        case "2":
            author()

### Options chits
def cover():
    titlePrint("Album Cover")

    inputHelper("2. Open the cover image")
    img_path = filedialog.askopenfilename(
        title = "Select the cover image (png or jpg)",
        filetypes = [("Images", "*.jpg *.jpeg *.png")]
    )

    if not img_path: stfu()

    actionHelper(mp3Cover, img_path, "Cover added")

def album():
    titlePrint("Album Name")
    print("2. Write the album name")
    albumName = input()

    actionHelper(mp3Album, albumName, "Album added")

def author():
    titlePrint("Album Artist")
    print("2. Write the album artist")
    albumName = input()

    actionHelper(mp3Author, albumName, "Album artist added")

if __name__ == "__main__":
    main()

### Uhhh credits to Dipazio347! (mateo360p/DP)