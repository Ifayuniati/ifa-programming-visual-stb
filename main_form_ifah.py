import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

#inisialisasi
window = tkinter.Tk()
window.configure(bg="purple")
icon_img = PhotoImage(file='D:\\tugasmasdeka\\asset\\libro.png')
window.iconphoto(False,icon_img)
window.geometry("400x300")
window.resizable(False,False)
window.title("Penjualan Buku")

#Header
header_label = ttk.Label(window, text="Pengisian Formulir",font=(16), background="purple", foreground="gray")
header_label.pack(pady=20)

#Variable dan function
JUDUL = tkinter.StringVar()
PENGARANG = tkinter.StringVar()
PENERBIT = tkinter.StringVar()
TAHUN = tkinter.StringVar()
HARGA = tkinter.StringVar()

#fungsi tombol
def tombol_click():
        if not JUDUL.get() or not PENGARANG.get() or not PENERBIT.get() or not TAHUN.get() or not HARGA.get():
            showinfo(title="Error!", message="Mohon lengkapi semua form!")
        else:
            pesan = f"Hallo {JUDUL.get()},kamu sudah terdaftar!"
            showinfo(title="selamat",message=pesan)

#frame input
input_frame = ttk.Frame(window)

#penempatan grid,pack,place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

#komponen judul 
judul_label = ttk.Label(input_frame,text="judul")
judul_label.pack(padx=10,fill="x",expand=True)
judul_entry = ttk.Entry(input_frame,textvariable=JUDUL)
judul_entry.pack(padx=10,fill="x",expand=True)
#komponen pengarang
pengarang_label = ttk.Label(input_frame,text="pengarang")
pengarang_label.pack(padx=10,fill="x",expand=True)
pengarang_entry = ttk.Entry(input_frame,textvariable=PENGARANG)
pengarang_entry.pack(padx=10,fill="x",expand=True)
#komponen penerbit
penerbit_label = ttk.Label(input_frame,text="penerbit")
penerbit_label.pack(padx=10,fill="x",expand=True)
penerbit_entry = ttk.Entry(input_frame,textvariable=PENERBIT)
penerbit_entry.pack(padx=10,fill="x",expand=True)
#komponen tahun
tahun_label = ttk.Label(input_frame,text="tahun")
tahun_label.pack(padx=10,fill="x",expand=True)
tahun_entry = ttk.Entry(input_frame,textvariable=TAHUN)
tahun_entry.pack(padx=10,fill="x",expand=True)
#komponen harga
harga_label = ttk.Label(input_frame,text="harga")
harga_label.pack(padx=10,fill="x",expand=True)
harga_entry = ttk.Entry(input_frame,textvariable=HARGA)
harga_entry.pack(padx=10,fill="x",expand=True)
#tombol
tombol_daftar = ttk.Button(input_frame,text="Daftar",command=tombol_click)
tombol_daftar.pack(fill="x",pady=10,expand=True)

window.mainloop()




