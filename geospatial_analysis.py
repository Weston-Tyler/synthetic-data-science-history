from geopy.distance import geodesic

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

if __name__ == "__main__":
    coord1 = (40.7128, -74.0060)  # New York City
    coord2 = (34.0522, -118.2437)  # Los Angeles
    distance = calculate_distance(coord1, coord2)
    print(f"The distance between New York City and Los Angeles is: {distance} kilometers")
