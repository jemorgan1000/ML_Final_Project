"""
This file preprocesses all of the data and makes a new 
"""
import geopandas as gpd 
import os.path as osp
import os
import pandas as pd

def get_stops(stop_path):
	"""
	Loads all the stops 
	:param stop_path: path to the shape file
	"""
	stops = pd.read_csv(stop_path)
	stops = gpd.GeoDataFrame(stops,geometry=gpd.points_from_xy(stops.stop_lon,stops.stop_lat))
	return stops

def get_blocks(shape_path):
	"""
	This function loads the shape file containing the shapes
	:param shape_path: path to the shape file
	"""
	blocks = gpd.read_file(shape_path)
	return blocks

def get_trips(trip_path):
	"""
	Loads and cleans the file containing all of the rider files. 
	:param ride_path: path to the ride file
	"""
	trip = pd.read_csv(trip_path)
	return trip

def get_number_stops(combined):
	"""

	:param combined: gpd.GeoDataFrame like object
	"""
	stops_rides = combined.groupby("BLOCKCE10").size()
	stops_rides = stops_rides.reset_index()
	stops_rides.rename({0:"STOPS",'BLOCKCE10':"BLOCK"},axis=1,inplace=True)
	return stops_rides



def join_stops(blocks, stops):
	"""
	This function takes all of the blocks and  
	:param blocks: gpd.GeoDataFrame object containing all the shape files 
	:param stops: gpd.GeoDataFrame object containing all the stops files 
	"""
	combined = gpd.sjoin(blocks,stops)
	return combined

def main():
	dir_path = os.getcwd()
	data_path = osp.abspath(osp.join(dir_path,"Data/"))
	stop_path = osp.join(data_path, "stops.txt")
	trips_path = osp.join(data_path,' trips.csv')
	stops = get_stops(stop_path)
	shape_path = osp.join(data_path,'census.dbf')
	blocks = get_blocks(shape_path)
	combined = join_stops(blocks,stops)
	get_number_stops(combined)
	


if __name__ == '__main__':
	main()