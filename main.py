import math


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the Haversine distance between two geographic points (in kilometers).
    """
    R = 6371  # Earth's radius in kilometers
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def find_closest_points(array1, array2):
    """
    Match each point in array1 to the closest point in array2.
    """
    closest_points = []
    for point1 in array1:
        lat1, lon1 = point1
        closest_point = None
        min_distance = float('inf')
        for point2 in array2:
            lat2, lon2 = point2
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            if distance < min_distance:
                min_distance = distance
                closest_point = point2
        closest_points.append((point1, closest_point, min_distance))
    return closest_points

# Example data
array1 = [(42.3601, -71.0589), (40.7128, -74.0060)]  # First set of geographic points (latitude, longitude)
array2 = [(34.0522, -118.2437), (41.8781, -87.6298), (47.6062, -122.3321)]  # Second set of geographic points

# Call the function and display the results
results = find_closest_points(array1, array2)
for point1, closest_point, distance in results:
    print(f"Point {point1} is closest to {closest_point} with a distance of {distance:.2f} km.")
