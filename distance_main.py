
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time
import ssl
import certifi

def calculate_distance(address1, address2):
    """
    Calculate the distance between two addresses using Nominatim Geocoding and Geodesic distance.
    """
    # Fix SSL certificate verification issue on macOS
    ctx = ssl.create_default_context(cafile=certifi.where())
    
    # Initialize Nominatim API with a unique user-agent and SSL context
    geolocator = Nominatim(user_agent="distance_calculator_script_v1", ssl_context=ctx)

    try:
        # Geocode the first address
        print(f"Geocoding Address 1: {address1}")
        location1 = geolocator.geocode(address1)
        if not location1:
            print("Error: Could not find coordinates for Address 1.")
            return None
        
        # Be polite to the free API
        time.sleep(1)

        # Geocode the second address
        print(f"Geocoding Address 2: {address2}")
        location2 = geolocator.geocode(address2)
        if not location2:
            print("Error: Could not find coordinates for Address 2.")
            return None
            
        print(f"Found coordinates for Address 1: ({location1.latitude}, {location1.longitude})")
        print(f"Found coordinates for Address 2: ({location2.latitude}, {location2.longitude})")

        # Calculate distance
        coord1 = (location1.latitude, location1.longitude)
        coord2 = (location2.latitude, location2.longitude)
        
        # Calculate geodesic distance (more accurate than Haversine)
        distance_km = geodesic(coord1, coord2).kilometers
        distance_mi = geodesic(coord1, coord2).miles
        
        return distance_km, distance_mi

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    print("Welcome to the Distance Calculator!")
    print("Please enter the two addresses below.")
    
    # Take user input
    addr1 = input("Address 1 (or press Enter for default): ").strip()
    if not addr1:
        addr1 = "901 Page Ave, Fremont, CA, 94538"
        print(f"Using default Address 1: {addr1}")

    addr2 = input("Address 2 (or press Enter for default): ").strip()
    if not addr2:
        addr2 = "33 Terraced Hills Way, San Ramon, CA, 94583"
        print(f"Using default Address 2: {addr2}")

    result = calculate_distance(addr1, addr2)
    
    if result:
        dist_km, dist_mi = result
        print("\n" + "="*40)
        print(f"Distance between:\n  1. {addr1}\n  2. {addr2}")
        print("="*40)
        print(f"Distance: {dist_km:.2f} km")
        print(f"Distance: {dist_mi:.2f} miles")

if __name__ == "__main__":
    main()
