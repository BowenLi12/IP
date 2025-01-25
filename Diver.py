from flask import Flask, render_template, redirect, url_for
import geocoder
import webbrowser

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')  # Render the button page

# Route to handle button click
@app.route('/button_clicked')
def button_clicked():
    # Step 1: Get your current location (latitude and longitude)
    g = geocoder.ip('me')  # Use IP-based geolocation
    lat, lng = 24.691402, -81.189682  # Returns latitude and longitude as a tuple

    # Step 2: Open Google Maps with the current location
    google_maps_url = f"https://www.google.com/maps?q={lat},{lng}"
    return redirect(google_maps_url)  # Redirect back to the index page

