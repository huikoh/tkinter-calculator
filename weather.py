from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry("400x100")

def zipLookup():
    import requests
    import json
    # zip.get()
    # zipLabel = Label(root, text=zip.get()).pack()
    # zipLabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=FB644A78-657E-49A2-BE79-6AD12CA8A312")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        
        if category == 'Good':
            weather_color = "#0C0"
        elif category == 'Moderate':
            weather_color = "#FFFF00"
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = "#FF9900"
        elif category == 'Unhealthy':
            weather_color = "#FF0000"
        elif category == 'Very Unhealthy':
            weather_color = "#990066"
        elif category == 'Hazardous':
            weather_color = "#660000"
            
        root.configure(background=weather_color)
        
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 10), background=weather_color)
        myLabel.pack()

    except Exception as e:
        api = "Error...."

lookup_frame = LabelFrame(root, text="Look Up Air Quality", padx=5, pady=5)
lookup_frame.pack(padx=10, pady=10)

zip = Entry(root)
zip.pack()

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.pack()

mainloop()