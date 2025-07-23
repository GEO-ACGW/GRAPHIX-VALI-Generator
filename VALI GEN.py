import customtkinter as ctk
from tkinter import filedialog
import subprocess

ctk.set_appearance_mode("Dark")  # Options: "Dark", "Light", "System"
ctk.set_default_color_theme("green")  # Options: "blue", "dark-blue", "green"

app = ctk.CTk()
app.title("⚙️ Vali Loc Gen & Updater")
app.geometry("500x300")
app.resizable(False, False)  # Disable resizing

def generate_command():
    file_path = filedialog.askopenfilename(
        title="Select JSON File",
        filetypes=[("JSON Files", "*.json")]
    )
    if file_path:
        command = f'cmd /c start cmd /k vali generate --file "{file_path}"'
        subprocess.Popen(command, shell=True)

def update_command():
    command = 'cmd /c start cmd /k dotnet tool update -g vali'
    subprocess.Popen(command, shell=True)

header = ctk.CTkLabel(app, text="Graphix Vali Loc Generator & Updater", font=ctk.CTkFont(size=24, weight="bold"))
header.pack(pady=(30, 10))

subtext = ctk.CTkLabel(app, text="Easily generate locations or update Vali without code", font=ctk.CTkFont(size=14))
subtext.pack(pady=(0, 20))

button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=10)

generate_button = ctk.CTkButton(
    button_frame,
    text="📄 Generate from JSON",
    command=generate_command,
    font=ctk.CTkFont(size=16, weight="bold"),
    width=200,
    height=40,
    corner_radius=15,
)
generate_button.pack(pady=10)

update_button = ctk.CTkButton(
    button_frame,
    text="🔄 Update Vali Tool",
    command=update_command,
    font=ctk.CTkFont(size=16, weight="bold"),
    width=200,
    height=40,
    corner_radius=15,
)
update_button.pack(pady=10)

footer = ctk.CTkLabel(app, text="Credit to    ❤️SlashP & HAV3R", font=ctk.CTkFont(size=12), text_color="gray")
footer.pack(side="bottom", pady=10)


app.mainloop()
