from moviepy.editor import VideoFileClip
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from os.path import abspath,splitext

win=Tk()
win.title("Extract sound from video file")
ww = 579
wh = 200
sw = win.winfo_screenwidth()
sh = win.winfo_screenheight()
cx = sw // 2
cy = sh // 2
wl = int(cx - ww / 2)
wt = int(cy - wh / 2)-110
win.geometry(f"{ww}x{wh}+{wl}+{wt}")
win.resizable(False, False)
win.configure(background="#212121")

def browse():
    types = (('All video types', '*.mkv;*.mp4;*.avi;*.wmv;*.wmp;*.wm;*.asf;*.mpg;*.mpeg;*.mpe;*.m1v;*.m2v;*.mpv2;*.mp2v;*.dat;*.ts;*.tp;*.tpr;*.trp;*.vob;*.ifo;*.ogm;*.ogv;*.m4v;*.m4p;*.m4b;*.3gp;*.3gpp;*.3g2;*.3gp2;*.rm;*.ram;*.rmvb;*.rpm;*.flv;*.swf;*.mov;*.qt;*.amr;*.nsv;*.dpg;*.m2t;*.m2ts;*.mts;*.k3g;*.dvr-ms;*.skm;*.evo;*.nsr;*.amv;*.webm;*.divx')
    ,('All files','*.*'))
    file = askopenfile(mode='r',filetypes=types)
    if file:
        ent.delete(0,END)
        filepath = abspath(file.name)       
        ent.insert(END,filepath)

def clear():
    l.config(text="")
def extract(): 
    path = ent.get() 
    if path == '':
        l.config(text="Insert the file path !",foreground="red")
        l.after(2500,clear)
        return
    exc = splitext(path)
    typ = ['.mp3','.m4a','.flac','.ogg','.wav','.wma','.mpa','.mp2','.m1a','.m2a','.aac','.mka','.ra','.ape','.mpc','.mod','.ac3','.dts','.wv','.tak']
    if exc[1] in typ:
        l.config(text="This is a sound file :/",foreground="red")
        l.after(3000,clear)
        return
    try:        
        clip = VideoFileClip(path)
        
        clip.audio.write_audiofile(exc[0] + ".mp3")
        l.config(text="Extracted ✅",foreground="green")
        l.after(7000,clear)
    except OSError:
        l.config(text="Enter a video path !",foreground="red")
        l.after(3000,clear)
    except KeyError:
        l.config(text="This is a sound file :/",foreground="red")
        l.after(3000,clear)
        
    except Exception:
        l.config(text="An error occurred, try again",foreground="red")
         

Label(win,text="Enter the video file path for extract sound",font="bahnschrift 20",bg="#212121",fg="green").place(x=36,y=20)

Label(win,text="Path :",bg="#212121",fg="white",font="bahnschrift 11").place(x=56,y=77)

ent = ttk.Entry(win,width=60)
ent.place(x=100,y=80)

ttk.Button(win,text="Browse",command=browse,style = 'W.TButton').place(x=470,y=78)

Button(win,text="Extract",command=extract,width=9,font="bahnschrift 15",border=10,foreground="white",bg="green",activebackground='#212121').place(x=230,y=130)

l = Label(win,bg="#212121",font="bahnschrift 10")
l.place(x=380,y=145)

mainloop()