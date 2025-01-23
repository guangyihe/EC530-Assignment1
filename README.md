# EC530-Assignment1
# README

## Overview
This repository contains Python code that implements a solution for matching geographic points from two arrays, using the Haversine formula to calculate the distance between two GPS locations. The goal is to find the closest point in the second array for each point in the first array.

## Features
- **Haversine Distance Calculation**: Computes the great-circle distance between two geographic coordinates.
- **Point Matching**: Matches each point in the first array with the closest point in the second array and calculates the distance.
- **Example Input/Output**: Includes example data to demonstrate the functionality.

## Code Description

### `haversine_distance(lat1, lon1, lat2, lon2)`
Calculates the Haversine distance (in kilometers) between two points defined by their latitude and longitude.

**Parameters:**
- `lat1`, `lon1`: Latitude and longitude of the first point.
- `lat2`, `lon2`: Latitude and longitude of the second point.

**Returns:**
- Distance in kilometers.

### `find_closest_points(array1, array2)`
Matches each point in `array1` with the closest point in `array2` based on the Haversine distance.

**Parameters:**
- `array1`: List of tuples containing geographic coordinates (latitude, longitude).
- `array2`: List of tuples containing geographic coordinates (latitude, longitude).

**Returns:**
- A list of tuples where each tuple contains:
  - A point from `array1`
  - The closest point from `array2`
  - The distance to the closest point

## Example
### Input:
```python
array1 = [(42.3601, -71.0589), (40.7128, -74.0060)]
array2 = [(34.0522, -118.2437), (41.8781, -87.6298), (47.6062, -122.3321)]
```

### Output:
```plaintext
Point (42.3601, -71.0589) is closest to (41.8781, -87.6298) with a distance of 1367.58 km.
Point (40.7128, -74.006) is closest to (41.8781, -87.6298) with a distance of 1144.29 km.
```

## How to Run
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the repository directory:
   ```bash
   cd <repository-directory>
   ```
3. Run the script:
   ```bash
   python <script_name>.py
   ```

## Dependencies
- Python 3.6+
- No external libraries required (uses built-in `math` module).

## Future Improvements
- Add support for larger datasets with optimized algorithms.
- Include optional visualization of matched points on a map.
- Implement error handling for invalid input data.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this code.

---

For any questions or issues, please open an issue in this repository or contact the maintainer.


