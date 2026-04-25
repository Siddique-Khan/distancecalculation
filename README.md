# distancecalculation
I have implemented a robust solution using the geopy library, which provides accurate geocoding (converting addresses to coordinates) and distance calculation (using the geodesic formula).

Features
Geocoding: Uses OpenStreetMap's Nominatim service to find latitude/longitude for any address.

Distance Calculation: Uses the geodesic distance method for high accuracy.

Interactive: Prompts the user for two addresses (or uses defaults if left blank).

Error Handling: Includes fixes for SSL certificate verification and handles network errors gracefully.

# How to run
You can run the script from your terminal:

bash
python3 distance_main.py

When prompted, you can enter the addresses:

Address 1: 901 Page Ave, Fremont, CA, 94538
Address 2: 33 Terraced Hills Way, San Ramon, CA, 94583
The output will display the distance in both kilometers and miles. 
