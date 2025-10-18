import customtkinter as ctk
from tkinter import messagebox

# Tema & tampilan
ctk.set_appearance_mode("System")  # Bisa "Dark" atau "Light"
ctk.set_default_color_theme("blue")

# Window utama
app = ctk.CTk()
app.title("Penentu Bilangan Terbesar")
app.geometry("2048x1280")
app.resizable(False, False)

# Efek animasi fade-in
app.attributes('-alpha', 0.0)
def fade_in():
    alpha = app.attributes('-alpha')
    if alpha < 1:
        alpha += 0.04
        app.attributes('-alpha', alpha)
        app.after(30, fade_in)
fade_in()

# Fungsi utama
def cari_terbesar():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = float(entry_d.get())
        terbesar = max(a, b, c, d)

        # Animasi hasil (fade label)
        result_label.configure(text=f"Bilangan terbesar: {terbesar}")
        result_label.after(50, lambda: result_label.configure(text_color="green"))
    except ValueError:
        messagebox.showerror("Error", "Pastikan semua input adalah angka!")

# Frame card minimalis
card = ctk.CTkFrame(app, corner_radius=20, fg_color=("white", "#1E1E1E"))
card.pack(padx=30, pady=40, fill="both", expand=True)

# Judul di dalam card
title_label = ctk.CTkLabel(
    card, 
    text="💡 Penentu Bilangan Terbesar", 
    font=("Poppins", 18, "bold")
)
title_label.pack(pady=(25, 10))

subtitle = ctk.CTkLabel(
    card, 
    text="Masukkan empat bilangan untuk dibandingkan", 
    font=("Poppins", 12)
)
subtitle.pack(pady=(0, 20))

# Input box (Entry)
entry_a = ctk.CTkEntry(card, placeholder_text="Bilangan pertama")
entry_a.pack(pady=8, padx=40, ipady=5)

entry_b = ctk.CTkEntry(card, placeholder_text="Bilangan kedua")
entry_b.pack(pady=8, padx=40, ipady=5)

entry_c = ctk.CTkEntry(card, placeholder_text="Bilangan ketiga")
entry_c.pack(pady=8, padx=40, ipady=5)

entry_d = ctk.CTkEntry(card, placeholder_text="Bilangan keempat")
entry_d.pack(pady=8, padx=40, ipady=5)

# Tombol interaktif dengan hover animasi
button = ctk.CTkButton(
    card,
    text="Cari Bilangan Terbesar",
    font=("Poppins", 14, "bold"),
    corner_radius=12,
    fg_color="#0078D7",
    hover_color="#005A9E",
    height=40,
    command=cari_terbesar
)
button.pack(pady=(25, 15))

# Label hasil (animasi teks)
result_label = ctk.CTkLabel(card, text="", font=("Poppins", 14, "bold"))
result_label.pack(pady=10)

# Footer
footer = ctk.CTkLabel(app, text="By Arthur Adam Radhitya", font=("Poppins", 11))
footer.pack(side="bottom", pady=10)

# Jalankan aplikasi
app.mainloop()
