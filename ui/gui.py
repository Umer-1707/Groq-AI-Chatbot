import tkinter as tk
from tkinter import scrolledtext
import threading
from PIL import Image, ImageTk

from core.chatbot import process_query
from voice.speech_to_text import recognize_speech
from voice.text_to_speech import speak_text


# 🎨 COLOR PALETTE
C1 = "#081F26"
C2 = "#002626"
C3 = "#103232"
C4 = "#225857"
C5 = "#6EB5B0"
C6 = "#D4F7DC"

last_response = ""


# =========================
# 🚀 MAIN APP
# =========================
def chatbot_gui():
    root = tk.Tk()
    root.title("AI Chatbot")
    root.geometry("900x650")
    root.configure(bg=C1)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    load_home(root)

    root.mainloop()


# =========================
# 🏠 HOME SCREEN (FULL BG IMAGE)
# =========================
def load_home(root):
    frame = tk.Frame(root, bg=C1)
    frame.grid(sticky="nsew")

    # 🎨 Canvas for background
    canvas = tk.Canvas(frame, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    original_img = Image.open("assets/title.png")

    # 🚀 Start Button
    def go_to_chat():
        frame.destroy()
        load_chat(root)

    start_btn = tk.Button(
        root,
        text="Start Chat",
        command=go_to_chat,
        font=("Segoe UI", 14, "bold"),
        fg="white",
        bg=C3,
        activebackground=C3,
        bd=0,
        padx=210,
        pady=15
    )

    def resize_bg(event):
        canvas.delete("all")

        # resize image to full screen
        resized = original_img.resize((event.width, event.height))
        bg_img = ImageTk.PhotoImage(resized)

        canvas.bg_img = bg_img
        canvas.create_image(0, 0, image=bg_img, anchor="nw")

        # place button in lower blank area
        canvas.create_window(
            event.width // 2,
            int(event.height * 0.87),   # 👈 adjust if needed
            window=start_btn
        )

    canvas.bind("<Configure>", resize_bg)


# =========================
# 💬 CHAT SCREEN
# =========================
def load_chat(root):
    global last_response

    frame = tk.Frame(root, bg=C1)
    frame.grid(sticky="nsew")

    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    # 🧠 Scrollable Canvas
    canvas = tk.Canvas(frame, bg=C3, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=C3)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")
    scrollbar.grid(row=0, column=3, sticky="ns")

    # 📥 Input
    input_box = tk.Entry(frame, bg="white", fg=C1, font=("Segoe UI", 12), bd=0)
    input_box.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

    frame.columnconfigure(0, weight=1)

    # 🎨 Bubble function
    def add_message(text, sender="bot"):
        bubble_frame = tk.Frame(scrollable_frame, bg=C3)

        if sender == "user":
            bubble_frame.pack(fill="both", expand=True)

            bubble = tk.Label(
                bubble_frame,
                text=text,
                bg=C5,
                fg="black",
                font=("Segoe UI", 11),
                wraplength=400,
                justify="left",
                padx=12,
                pady=8,
                bd=0,
                relief="flat",
                highlightthickness=0
            )

            bubble.pack(anchor="e", padx=(835,10), pady=5)
        else:
            bubble = tk.Label(
                bubble_frame,
                text=text,
                bg=C6,
                fg="black",
                font=("Segoe UI", 11),
                wraplength=400,
                justify="left",
                padx=12,
                pady=8,
                bd=0,
                relief="ridge"
            )
            bubble.pack(anchor="w", padx=15, pady=5)

        bubble_frame.pack(fill="both", expand=True)
        bubble.config(highlightthickness=0)
        canvas.update_idletasks()
        canvas.yview_moveto(1.0)

    # 🚀 Send
    def send_query():
        user_query = input_box.get()
        if not user_query:
            return

        add_message(user_query, "user")
        input_box.delete(0, tk.END)

        add_message("Typing...", "bot")

        def task():
            global last_response
            response = process_query(user_query)

            # remove "Typing..."
            for widget in scrollable_frame.winfo_children():
                if isinstance(widget, tk.Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, tk.Label) and child.cget("text") == "Typing...":
                            widget.destroy()

            add_message(response, "bot")
            last_response = response

        threading.Thread(target=task).start()

    send_btn = tk.Button(
        frame,
        text="Send",
        command=send_query,
        bg=C4,
        fg="white",
        font=("Segoe UI", 11, "bold"),
        bd=0,
        padx=15
    )
    send_btn.grid(row=1, column=1, padx=5)

    # 🎤 Voice
    def voice_query():
        add_message("Listening...", "bot")

        def task():
            global last_response
            query = recognize_speech()

            if not query:
                add_message("Could not understand.", "bot")
                return

            add_message(query, "user")
            add_message("Typing...", "bot")

            response = process_query(query)

            add_message(response, "bot")
            last_response = response

        threading.Thread(target=task).start()

    voice_btn = tk.Button(
        frame,
        text="Voice",
        command=voice_query,
        bg=C3,
        fg="white",
        font=("Segoe UI", 11, "bold"),
        bd=0,
        padx=15
    )
    voice_btn.grid(row=2, column=0, pady=5)

    # 🔊 Speak
    def speak():
        if last_response:
            speak_text(last_response)

    speak_btn = tk.Button(
        frame,
        text="Speak",
        command=speak,
        bg=C5,
        fg="black",
        font=("Segoe UI", 11, "bold"),
        bd=0,
        padx=15
    )
    speak_btn.grid(row=2, column=1)

    root.bind("<Return>", lambda e: send_query())