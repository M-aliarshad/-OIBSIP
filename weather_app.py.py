from tkinter import *
from tkinter import ttk
import requests
import json

def data_get():
    city = city_name.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2477ab37b8b601bb70cb8eb8d22e51af"
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            w_label1.config(text=data["weather"][0]["main"])
            wb_label1.config(text=data["weather"][0]["description"])
            temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)) + " °C")
            per_label1.config(text=str(data["main"]["pressure"]) + " hPa")
        else:
            raise Exception(data["message"])
    except Exception as e:
        print(f"Error: {e}")
        w_label1.config(text="N/A")
        wb_label1.config(text="N/A")
        temp_label1.config(text="N/A")
        per_label1.config(text="N/A")

win = Tk()

win.title("Ali's Weather Hub")
win.config(bg="green")
win.geometry("500x600")

name_label = Label(win, text="Ali's Weather Hub", font=("Arial", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = cities = ["Mian Channu", "Multan", "Lahore", "Istanbul", "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat", "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Vadodara", "Firozabad", "Ludhiana", "Rajkot", "Agra", "Nashik", "Faridabad", "Patiala", "Meerut", "Kalyan-Dombivali", "Vasai-Virar", "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad", "Howrah", "Ranchi", "Ghaziabad", "Jabalpur", "Coimbatore", "Vijayawada", "Jodhpur", "Raipur", "Kota", "Guwahati", "Chandigarh", "Thiruvananthapuram", "Bhubaneswar", "Salem", "Warangal", "Mira-Bhayandar", "Thiruchirapalli", "Durgapur", "Asansol", "Bhiwandi", "Saharanpur", "Guntur", "Amravati", "Bikaner", "Noida", "Jamshedpur", "Bhilai Nagar", "Cuttack", "Firozpur", "Nanded-Waghala", "Rourkela", "Kollam", "Ajmer", "Akola", "Rajahmundry", "Kakinada", "Kurnool", "Tirunelveli", "Karnal", "Bathinda", "Jhansi", "Ulhasnagar", "Nellore", "Bijapur", "Kukatpally", "Bokaro Steel City", "Lakhisarai", "Panipat", "Dhule", "Panvel", "Muzaffarpur", "Ahmednagar", "Mathura", "Kollam", "Avadi", "Alwar", "Aligarh", "Vijayanagaram", "Jalandhar", "Tiruvottiyur", "Malegaon", "Gaya", "Jalgaon", "Kochi", "Muzaffarnagar", "Thrissur", "Siliguri", "Ratlam", "Moradabad", "Darbhanga", "Shahjahanpur", "Satna", "Bhagalpur", "Lakhisarai", "Sonipat", "Rewa", "Rohtak", "Shimla", "Haridwar", "Gorakhpur", "Yamuna Nagar", "Nizamabad", "Sambhal", "Jhansi", "Ichalkaranji", "Tiruppur", "Karnal", "Panipat", "Dhanbad", "Jammu", "Srinagar", "Rawalpindi", "Faisalabad", "Multan", "Gujranwala", "Peshawar", "Quetta", "Islamabad", "Bahawalpur", "Sialkot", "Gujrat", "Larkana", "Sheikhupura", "Sahiwal", "Okara", "Rahim Yar Khan", "Sargodha", "Sukkur", "Mirpur Khas", "Nawabshah", "Mardan", "Kasur", "Mingora", "Jhang", "Chiniot", "Gujranwala", "Dera Ghazi Khan", "Hafizabad", "Kohat", "Muridke", "Kamoke", "Mandi Bahauddin", "Khanewal", "Mandi Bahauddin", "Chakwal", "Attock", "Gujrat", "Jhelum", "Narowal", "Vehari", "Pakpattan", "Khushab", "Mianwali", "Bhakkar", "Layyah", "Muzaffargarh", "Rajanpur", "Lodhran", "Bahawalnagar", "Ghotki", "Sanghar", "Shikarpur", "Jacobabad", "Kandhkot", "Kashmore", "Qambar Shahdadkot", "Kanpur","New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington, D.C.", "Boston", "El Paso", "Detroit", "Nashville", "Oklahoma City", "Portland", "Las Vegas", "Milwaukee", "Baltimore", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Long Beach", "Kansas City", "Mesa", "Virginia Beach", "Atlanta", "Colorado Springs", "Omaha", "Raleigh", "Miami", "Cleveland", "Tulsa", "Oakland", "Minneapolis", "Wichita", "Arlington", "New Orleans", "Bakersfield", "Tampa", "Honolulu", "Anaheim", "Aurora", "Santa Ana", "St. Louis", "Riverside", "Corpus Christi", "Pittsburgh", "Lexington", "Anchorage", "Stockton", "Cincinnati", "St. Paul", "Toledo", "Greensboro", "Newark", "Plano", "Henderson", "Lincoln", "Orlando", "Chula Vista", "Irvine", "Fort Wayne", "Jersey City", "Durham", "Chula Vista", "Buffalo", "St. Petersburg", "Chandler", "Laredo", "Madison", "Gilbert", "Reno", "Norfolk", "Glendale", "Winston-Salem", "Hialeah", "Baton Rouge", "Richmond", "Boise", "Spokane", "Des Moines", "Montgomery", "Modesto", "Fayetteville", "Tacoma", "Oxnard", "Fontana", "Columbus"]

com = ttk.Combobox(win, values=list_name, font=("Arial", 20), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(win, text="Weather", font=("Arial", 20))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Arial", 20))
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="Description", font=("Arial", 17))
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(win, text="", font=("Arial", 17))
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Arial", 20))
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text="", font=("Arial", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

per_label = Label(win, text="Pressure", font=("Arial", 20))
per_label.place(x=25, y=470, height=50, width=210)
per_label1 = Label(win, text="", font=("Arial", 20))
per_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="search", font=("Arial", 20, "bold"), command=data_get)
done_button.place(y=190, height=40, width=115, x=175)

win.mainloop()