# Import Library
import folium

# Create base map
map = folium.Map(location=[37.296933, -121.9574983], zoom_start = 8)

# Add Marker
folium.Marker(location=[37.4074687,-122.086669])

# Save the map
map.save("map.html")