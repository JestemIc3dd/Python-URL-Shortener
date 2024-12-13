import customtkinter as gui
import pyshorteners as pys
import pyperclip as clip

def shorten_url():
    url = entry.get()
    if url:
        try:
            shortener = pys.Shortener()
            short_url = shortener.tinyurl.short(url)
            result_label.configure(text=f'Skrócony link: {short_url}')
            clip.copy(short_url)
        except Exception as e:
            result_label.configure(text=f'Wystąpił błąd: {str(e)}')

app = gui.CTk()
app.geometry("400x200")
app.title("URL Shortener")

gui.set_appearance_mode("System")
label = gui.CTkLabel(app, text="Podaj URL do skrócenia:")
label.pack(pady=10)

entry = gui.CTkEntry(app, width=300)
entry.pack(pady=5)

shorten_button = gui.CTkButton(app, text="Skróć link", command=shorten_url)
shorten_button.pack(pady=10)

result_label = gui.CTkLabel(app, text="")
result_label.pack(pady=20)

app.mainloop()
