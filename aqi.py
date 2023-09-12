import tkinter as tk
from tkinter import messagebox
import requests
import time

def get_aqi():
    update_datetime()  # Start updating the time and date
    city = city_entry.get()
    api_key = "1d7b51b70a72407988ab4c47ad53a69e" # Get your API key from Weatherbit
    url = f"https://api.weatherbit.io/v2.0/current/airquality?city={city}&key={api_key}"

    response = requests.get(url)
    aqi_data = response.json()
    if "error" in aqi_data :
        aqi_label.config(text=aqi_data["error"])
    else:
        aqi_text = f"\t\tCity: {city}\n"
        aqi_text += f"\n\t\tAQI: {aqi_data['data'][0]['aqi']}\n\n"
        aqi_text += ("         ( Some other pollutants data include )\n")
        aqi_text += f"\nPM2.5: {aqi_data['data'][0]['pm25']}"
        aqi_text += f"\tPM10: {aqi_data['data'][0]['pm10']}"
        aqi_text += f"\t\tCO: {aqi_data['data'][0]['co']}\n"
        aqi_text += f"SO2: {aqi_data['data'][0]['so2']}"
        aqi_text += f"\t\tNO2: {aqi_data['data'][0]['no2']}"
        aqi_text += f"\t\tO3: {aqi_data['data'][0]['o3']}"
        
        aqi_label.config(text=aqi_text)
        aqi_label.config(text=aqi_text)

        aqi_value = int(aqi_data['data'][0]['aqi'])
        if aqi_value <= 50:
            a = tk.Label(text="     GOOD             ", fg = "light GREEN", bg="#3a83e8",font=("arial", 13,"bold"))
            a.place(anchor="n", x =509, y = 255)
            
        elif aqi_value > 50 and aqi_value <= 100:
            b = tk.Label(text="SATISFACTORY", fg = "LIGHT GREEN",bg="#3a83e8", font=("arial", 12,"bold"))
            b.place(anchor="n", x =500, y = 255)
            
        elif aqi_value > 100 and aqi_value <= 200:
            c = tk.Label(text="   MODERATE   ", fg = "YELLOW", bg="#3a83e8",font=("arial", 12,"bold"))
            c.place(anchor="n", x =500, y = 255)
        elif aqi_value > 200 and aqi_value <= 300:
            d = tk.Label(text="    POOR    ", fg = "Orange", bg="#3a83e8",font=("arial", 12,"bold"))
            d.place(anchor="n", x =490, y = 255) 
        else:
            e = tk.Label(text="  VERY POOR ", fg = "red", bg="#3a83e8",font=("arial", 12,"bold"))
            e.place(anchor="n", x =500, y = 255)


# Dummy function to fetch water quality data based on location.
# Data taken from CENTRAL POLLUTION CONTROL BOARD GOVERNMENT ORGANIZATION
def fetch_water_quality_data(location):

    dummy_data = {
    'Jaipur': {
        'ph_level': 7.5,
        'Temp': 28.5,
        'Conduct': 1533,
        'BOD': None,  # Used None for Python's null value
        'FC': 1.4,
    },
    'Jodhpur': {
        'ph_level': 8.2,
        'Temp': 22.5,
        'Conduct': 503.5,
        'BOD': None,
        'FC': 5.5,
    },
    'Udaipur': {
        'ph_level': 7.45,
        'Temp': 26,
        'Conduct': 957.5,
        'BOD': None,
        'FC': 2.5,
    },
    'Kota': {
        'ph_level': 7.55,
        'Temp': 28,
        'Conduct': 1152.5,
        'BOD': None,
        'FC': 9,
    },
    'Ajmer': {
        'ph_level': 7.8,
        'Temp': 27,
        'Conduct': 1040,
        'BOD': None,
        'FC': 5.5,
    },
    'Alwar': {
        'ph_level': 7.35,
        'Temp': 28.5,
        'Conduct': 1294,
        'BOD': None,
        'FC': 3.5,
    },
    'Chandigarh': {
        'ph_level': 7,
        'Temp': 25.4,
        'Conduct': 846,
        'BOD': 1,
        'FC': 2,
    },
    'Haridwar': {  # Removed extra space at the end of the key
        'ph_level': 7.9,
        'Temp': 20,
        'Conduct': 640.5,
        'BOD': 1,
        'FC': 2,
    },
    'Dehradun': {
        'ph_level': 6.4,  # Corrected format from .6.4 to 6.4
        'Temp': 19,
        'Conduct': 199.5,
        'BOD': 1,
        'FC': 2,
    },
    'Varanasi': {
        'ph_level': 7.8,
        'Temp': 24.5,
        'Conduct': 552,
        'BOD': 1,
        'FC': 1,
    },
    'Allahabad': {
        'ph_level': 7.1,
        'Temp': 25.3,
        'Conduct': 1140,
        'BOD': 1,
        'FC': 2,
    },
    'Lucknow': {
        'ph_level': 7.75,
        'Temp': 26,
        'Conduct': 1172.5,
        'BOD': 1,
        'FC': 2,
    },
    'Patna': {
        'ph_level': 7.5,
        'Temp': 25.5,
        'Conduct': 463,
        'BOD': None,
        'FC': 2,
    },
    'Kolkata': {
        'ph_level': 7.6,
        'Temp': 30,
        'Conduct': 796,
        'BOD': 1,
        'FC': 2,
    },
    'Howrah': {
        'ph_level': 7.4,
        'Temp': 26,
        'Conduct': 404,
        'BOD': 1,
        'FC': 2,
    },
    'Guwahati': {  # Removed extra space at the end of the key
        'ph_level': 7.4,
        'Temp': 28,
        'Conduct': 405,
        'BOD': 2.4,
        'FC': 1,
    },
    'Bhopal': {
        'ph_level': 7.6,
        'Temp': 27,
        'Conduct': 816.5,
        'BOD': 1,
        'FC': 48,
    },
    'Indore': {
        'ph_level': 7.5,
        'Temp': 21,
        'Conduct': 2044,
        'BOD': 1,
        'FC': 2,
    },
    'Jabalpur': {  # Removed extra space at the end of the key
        'ph_level': 7.2,
        'Temp': 21.2,
        'Conduct': 282,
        'BOD': 1,
        'FC': 2,
    },
    'New Delhi': {
        'ph_level': 7.5,
        'Temp': 28.5,
        'Conduct': 1002,
        'BOD': 1,
        'FC': 2,
    },
    'Vishakhapatnam': {
        'pH Level': 7.05,
        'Temperature (°C)': 26,
        'Conductivity (µS/cm)': 3800,
        '(mg/L)': 2.9,
        'Fecal Count (MPN/100mL)': 5.5,
    },
    'Vijayawada': {
        'ph_level': 7.45,
        'Temp': 25,
        'Conduct': 1923.5,
        'BOD': 1.6,
        'FC': 2,
    },
    'Tirupati': {
        'ph_level': 7.2,
        'Temp': 27,
        'Conduct': 1397,
        'BOD': 1.0,
        'FC': 2.5,
    },
    'Kurnool': {
        'ph_level': 7.85,
        'Temp': 24.5,
        'Conduct': 5091.5,
        'BOD': 1,
        'FC': 2.5,
    },
    'Bilaspur': {
        'ph_level': 7.5,
        'Temp': 27.2,
        'Conduct': 378,
        'BOD': None,
        'FC': 2,
    },
    'Raipur': {
        'ph_level': 7.4,
        'Temp': 28.0,
        'Conduct': 256,
        'BOD': None,
        'FC': 0,
    },
    'Ahmedabad': {
        'ph_level': 7.7,
        'Temp': 31.5,
        'Conduct': 5751.5,
        'BOD': 1.0,
        'FC': 2,
    },
    'Surat': {
        'ph_level': 7.8,
        'Temp': 29.5,
        'Conduct': 3819.5,
        'BOD': 1.85,
        'FC': 2,
    },
    'Rajkot': {
        'ph_level': 7.4,
        'Temp': 27.0,
        'Conduct': 1526,
        'BOD': 1.4,
        'FC': 0,
    },
    'Gandhinagar': {
        'ph_level': 7.7,
        'Temp': 29.0,
        'Conduct': 2091,
        'BOD': 1.0,
        'FC': 2,
    },
    'Shimla': {
        'ph_level': 7.6,
        'Temp': 11.5,
        'Conduct': 6569.5,
        'BOD': 47.9,
        'FC': 1600,
    },
    'Hamirpur': {
        'ph_level': 7.6,
        'Temp': None,
        'Conduct': 514.5,
        'BOD': 1.0,
        'FC': 0,
    },
    'Jammu': {
        'ph_level': 8.3,
        'Temp': 21.0,
        'Conduct': 560,
        'BOD': 1.7,
        'FC': 0,
    },
    'Thiruvananthapuram': {
        'ph_level': 7.0,
        'Temp': 26.0,
        'Conduct': 235.5,
        'BOD': 4.65,
        'FC': 455,
    },
    'Nashik': {
        'ph_level': 7.1,
        'Temp': 21.0,
        'Conduct': 999,
        'BOD': 3.0,
        'FC': 22,
    },
    'Aurangabad': {
        'ph_level': 7.55,
        'Temp': 29.0,
        'Conduct': 2737.5,
        'BOD': 2.5,
        'FC': 0,
    },
    'Nagpur': {
        'ph_level': 8.0,
        'Temp': None,
        'Conduct': 748,
        'BOD': 4.0,
        'FC': 17,
    },
    'Pune': {
        'ph_level': 7.5,
        'Temp': 26.0,
        'Conduct': 5600,
        'BOD': 5.4,
        'FC': 13,
    },

}

    if location in dummy_data:
        return dummy_data[location]
    else:
        return None


# Function to display the water quality report
def display_report():
    location = city_entry.get()
    data = fetch_water_quality_data(location)
    
    
    if data:
        # Display the report in a message box
        ph_value = int(data['ph_level'])
        FC_value = int(data['FC'])
        Conduct_value = int(data['Conduct'])
        report_text = f"Water Quality Report for {location}\n\n" \
                      f"pH Level:    {data['ph_level']}\n" \
                      f"\nTemperature(°C):    {data['Temp']}\n" \
                      f"\nConductivity(µS/cm):  {data['Conduct']}\n" \
                      f"\nB.O.D (mg/L):      {data['BOD']}\n" \
                      f"\nFaecal Coliform (MPN/100mL):  {data['FC']}\n"
        if ph_value in range(7,8) and FC_value in range (0,3) and Conduct_value < 1000:   
            report_text += "\nNOTE: THE WATER IS NEARLY SUITBLE FOR DRINKING"
        else:
            report_text += "\nNOTE: THE WATER SHOULD BE MADE SUITABLE FOR DRINKING"

                      
        messagebox.showinfo("Water Quality Report", report_text)
               
    else:    
        messagebox.showerror("Error", "Location not found or data unavailable.")

#time 
def update_datetime():
    current_time = time.strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
    current_date = time.strftime("%Y-%m-%d")  # Get the current date in YYYY-MM-DD format
    time_label.config(text=current_time)  # Update the time label text
    date_label.config(text=current_date)  # Update the date label text
    root.after(1000, update_datetime)  # Schedule the update_datetime function to run again after 1000 milliseconds (1 second)

root = tk.Tk()
root.title("Environment Statistics")
root.geometry("800x500")
root.maxsize(width=800, height=500)

bg_image = tk.PhotoImage(file="bgd1.png")  # Replace "background.png" with your image file

canvas = tk.Canvas(root, width=bg_image.width(), height=bg_image.height())
canvas.pack()
canvas.create_image(0, 0, image=bg_image, anchor=tk.NW)



# Entry
city_entry = tk.Entry(root, justify = "center", font=("Arial", 25), bg = "#FCCE05", border = 7,fg="black")
city_entry.place(x=60,y=51)
city_entry.insert(0,"")

# Get AQI button
get_aqi_button = tk.Button(text="Get AQI", font=("Arial", 12, "bold"),relief = "raised", fg="black",bg="#FCCE05", command=get_aqi)
get_aqi_button.place(x= 500, y = 60)

#WQI BUTTON 

fetch_button = tk.Button(root, text="Get WQI Report", font=("Arial", 12, "bold"),fg="black",relief = "raised",bg="#FCCE05",command= display_report)
fetch_button.place(x= 623, y = 60)


# AQI label
aqi_frame = tk.Frame(root, bg='#3a83e8', bd=5,relief="sunken")
aqi_frame.place(x=60,y=178, relwidth=0.85, relheight=0.5)
aqi_label = tk.Label(aqi_frame, font=("arial", 15,"bold"), justify='left', bd=5, bg = "#3a83e8",fg="#FFFFFF")
aqi_label.place(relwidth=1, relheight=1)


# Create labels for time and date
time_label = tk.Label(root, text="", font=("Helvetica", 24),fg = "yellow", bg ="#3a83e8")
date_label = tk.Label(root, text="", font=("Helvetica", 24))

# Pack the labels
time_label.place(x= 70, y = 187)



root.mainloop()
