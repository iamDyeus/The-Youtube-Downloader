from logging import exception
from pathlib import Path
from tkinter import  Tk, Canvas, Entry, Text, Button, PhotoImage,filedialog,END,ttk,messagebox
import os
from pytube import *




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def select_output_path():
    global output_path

    output_path = filedialog.askdirectory()
    path_entry.delete(0, END)
    path_entry.insert(0, output_path)

def downloader():
    if file_name.get() == "":
        messagebox.showerror("Error", "File Name is Required!")
    elif url_entry.get() == "":
        messagebox.showerror("Error", "Please Enter the URL First!")
    
    elif path_entry.get() == "":
        messagebox.showerror("Error", "Please Select the Output Path!")
    elif download_format.get() == "":
        messagebox.showerror("Error", "Download Format is Required !")
    else:
        start_download()

def start_download():
    # Object creation using YouTube
    try:
        yt = YouTube(str(url_entry.get()))
    except:
        messagebox.showerror(exception, "Something went wrong, try again later.") 
        window.destroy()

    if download_format.get() == "MP4":
        # Filters out all the files with 'mp4' extension 
        video = yt.streams.get_highest_resolution()
        out=video.download(path_entry.get())
        os.rename(out, path_entry.get() +'/'+ file_name.get() + '.mp4')
    elif download_format.get() == "MP3":
        video = yt.streams.filter(only_audio=True).first()
        out = video.download(path_entry.get())
        # Editing the extension
        base = out[:len(out)-4]
        os.rename(out, path_entry.get() +'/' + file_name.get() + '.mp3')

    messagebox.showinfo("Download Completed", "Your Download is Successfully Completed.")
    url_entry.delete(0, END)
    file_name.delete(0, END)



window = Tk()
window.geometry("862x462")
window.configure(bg = "#FFFFFF")
logo = PhotoImage(file=ASSETS_PATH / "icon_image2.png")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Youtube Downloader")




canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 462,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))  #LEFT SIDE BACKGROUND
image_1 = canvas.create_image(
    213.0,
    231.0,
    image=image_image_1
)

canvas.create_text(
    37.0,
    112.0,
    anchor="nw",
    text="YOUTUBE",
    fill="#FFFFFF",
    font=("RobotoCondensed Regular", 48 * -1)
)

canvas.create_text(
    37.0,
    162.0,
    anchor="nw",
    text="DOWNLOADER",
    fill="#FFFFFF",
    font=("RobotoCondensed Regular", 48 * -1)
)

canvas.create_text(
    37.0,
    60.0,
    anchor="nw",
    text="THE",
    fill="#FFFFFF",
    font=("RobotoCondensed Regular", 48 * -1)
)


#/////////////////////////  FORMAT BOX /////////////////////////////////////////////
entry_image_1 = PhotoImage(                         
    file=relative_to_assets("entry_format.png"))
entry_bg_1 = canvas.create_image(
    778.0,
    308.0,
    #image=entry_image_1
)
download_format = ttk.Combobox(
    values=["MP4", "MP3"],
    state="readonly"
)

download_format.place(
    x=731.0,
    y=285.0,
    width=94.0,
    height=46.0
)
canvas.create_text(
    742.0,
    256.0,
    anchor="nw",
    text="Format",
    fill="#363535",
    font=("Inter Bold", 22 * -1)
)
#-------------------------------------------------------------------- /FORMAT BOX)




#//////////////////    URL BOX    ///////////////////////////////////////////////
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_url.png"))
entry_bg_2 = canvas.create_image(
    643.5,
    217.0,
    image=entry_image_2
)
url_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
url_entry.place(
    x=472.0,
    y=194.0,
    width=343.0,
    height=46.0
)
canvas.create_text(
    465.0,
    162.0,
    anchor="nw",
    text="Video URL",
    fill="#363535",
    font=("Inter Bold", 22 * -1)
)
#---------------------------------------------------------------------- /URL BOX)




#////////////////////////  OUTPUT BOX ////////////////////////////////
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    582.0,
    308.0,
    image=entry_image_3
)
path_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
path_entry.place(
    x=472.0,
    y=285.0,
    width=220.0,
    height=46.0
)

canvas.create_text(
    465.0,
    256.0,
    anchor="nw",
    text="Output Path",
    fill="#363535",
    font=("Inter Bold", 22 * -1)
)
#-------------------------------------------------------- /OUTPUT BOX)




#^^^^^^^^^^^^^^^^  OUTPUT BUTTON ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
button_image_1 = PhotoImage(
    file=relative_to_assets("button_output.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=select_output_path,
    relief="flat"
)
button_1.place(
    x=660.0,
    y=290.0,
    width=38.0,
    height=38.0
)
#----------------------------------------------------  /OUTPUT BUTTON)




#////////////////  VIDEO NAME BOX //////////////////////////////////
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    643.5,
    116.0,
    image=entry_image_4
)
file_name = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
file_name.place(
    x=472.0,
    y=93.0,
    width=343.0,
    height=46.0
)
canvas.create_text(
    465.0,
    61.0,
    anchor="nw",
    text="Video Name",
    fill="#363535",
    font=("Inter Bold", 22 * -1)
)
#------------------------------------------------------ /VIDEO NAME)



#^^^^^^^^^^^^^^^^^^^^^ DOWNLOAD BUTTON ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
button_image_2 = PhotoImage(
    file=relative_to_assets("button_download.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=downloader,
    relief="flat"
)
button_2.place(
    x=549.0,
    y=363.0,
    width=178.0,
    height=64.0
)
#--------------------------------------------------- /Download button)

canvas.create_text(
    37.0,
    383.0,
    anchor="nw",
    text="Favourite Youtube Videos!",
    fill="#FFFFFF",
    font=("Inter Regular", 22 * -1)
)

canvas.create_text(
    37.0,
    358.0,
    anchor="nw",
    text="An Easy way to Download your ",
    fill="#FFFFFF",
    font=("Inter Regular", 22 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png")) #that line below the TITLE 
image_2 = canvas.create_image(
    121.0,
    232.0,
    image=image_image_2
)


window.resizable(False, False)
window.mainloop()
