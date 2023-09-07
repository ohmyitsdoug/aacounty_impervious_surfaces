import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
def read_geojson_data(geojson_file):
    # Read the geoJSON file using geopandas
    gdf = gpd.read_file(geojson_file)

    # Display the headers and the first 5 rows of the data
    print(gdf.head())

    return gdf
def plot_geojson_file(geojson_file):
    # Read in the GeoJSON data with geopandas
    gdf = gpd.read_file(geojson_file)

    # Create a new matplotlib figure and axis with larger size
    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(10, 15))

    # Plot the GeoDataFrame onto the map
    gdf.plot(ax=ax, transform=ccrs.PlateCarree(), legend=True, legend_kwds={'loc': 'upper left'})

    # Add coastlines and other geographic details
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    # Display the map
    plt.tight_layout()
    plt.show()
def plot_feature_area(geojson_file):
    # Read the geoJSON file using geopandas
    gdf = gpd.read_file(geojson_file)

    # Group by 'FEAT_TYPE' and sum up the 'ShapeSTArea'
    feature_areas = gdf.groupby('FEAT_TYPE')['ShapeSTArea'].sum().sort_values(ascending=False)

    # Plotting
    feature_areas.plot(kind='bar', figsize=(10, 6))
    plt.title("Total Square Footage for Each Feature Type")
    plt.ylabel("Square Footage")
    plt.xlabel("Feature Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
# Manually specify the path to your geoJSON file
geojson_file = 'Impervious_Surfaces.geojson'
data = read_geojson_data(geojson_file)
plot_geojson_file(geojson_file)
plot_feature_area(geojson_file)