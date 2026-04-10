import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "1f484a52393666e1d1de9183064f7531"

def get_weather():
    city = entry.get()
    
    if city == "":
        messagebox.showwarning("Warning", "Enter city name!")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message"))
            return

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        result = f"City: {city}\nTemperature: {temp}°C\nFeels Like: {feels_like}°C\nCondition: {weather}\nHumidity: {humidity}%"
        
        result_label.config(text=result)

    except:
        messagebox.showerror("Error", "Failed to fetch data!")

# GUI Window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="#2c3e50")

# Title
title = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white")
title.pack(pady=10)

# Entry
entry = tk.Entry(root, width=25, font=("Arial", 12))
entry.pack(pady=10)

# Button
btn = tk.Button(root, text="Get Weather", command=get_weather, bg="#27ae60", fg="white")
btn.pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#2c3e50", fg="white", justify="left")
result_label.pack(pady=20)

# Run app
root.mainloop()