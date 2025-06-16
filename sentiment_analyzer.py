from textblob import TextBlob
import tkinter as tk
from tkinter import messagebox

def analyze_and_show():
    review = entry.get("1.0", tk.END).strip()
    if review == "":
        messagebox.showwarning("Warning", "Please enter a review.")
        return

    blob = TextBlob(review)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive 😊"
    elif polarity < -0.1:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"

    result_label.config(text=f"Sentiment: {sentiment}")

    with open("review_log.txt", "a") as file:
        file.write(f"Review: {review}\nSentiment: {sentiment}\n---\n")

# GUI Setup
root = tk.Tk()
root.title("Movie Review Sentiment Analyzer")
root.geometry("400x300")

tk.Label(root, text="Enter Review:", font=("Arial", 12)).pack(pady=5)
entry = tk.Text(root, height=5, width=40)
entry.pack(pady=5)

tk.Button(root, text="Analyze", command=analyze_and_show).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
