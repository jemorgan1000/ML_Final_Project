"""
This file preprocesses and combines data from all of our
data sources to create a single data frame

"""

import geopandas as gpd 
import os.path as osp
import os
import pandas as pd

def get_stops(stop_path):
	"""
	Loads all the stops 
	:param stop_path: path to the shape file
	:return: return gpd.GeoDataFrame
	"""
	stops = pd.read_csv(stop_path)
	stops = gpd.GeoDataFrame(stops,geometry=gpd.points_from_xy(stops.stop_lon,stops.stop_lat))
	return stops

def get_blocks(shape_path):
	"""
	This function loads the shape file containing the shapes
	:param shape_path: path to the shape file
	:return: gpd.GeoDataFrame
	"""
	blocks = gpd.read_file(shape_path)
	return blocks

def get_trips(trips_path):
	"""
	Loads and cleans the file containing all of the rider files. 
	:param trips_path: path to the trips file
	"""
	trips = pd.read_csv(trips_path)
	return trips

def add_commute_time(trips_df):
	"""
	Adds commute times to each of the trips
	:param trips_df: pd.DataFrame 
	:return: returns Dataframe 
	"""
	trips_df.loc[:,'start_time'] = pd.to_datetime(trips_df.start_time)
	trips_df.loc[:,'end_time'] = pd.to_datetime(trips_df.end_time)
	trips_df.insert(len(trips_df.columns),
			"MORNING",
			((trips_df.start_time.dt.hour >= 5) & (trips_df.start_time.dt.hour <= 10)) * 1)
	trips_df.insert(len(trips_df.columns),
		'AFTERNOON',
		((trips_df.start_time.dt.hour >= 16) & (trips_df.start_time.dt.hour < 20)) * 1)
	return trips_df

def identify_commuters(trips_df):
	"""
	This function identifies each trip as either a commuter or not
	:param trips_df:
	:return:
	"""

def create_UID(combined):
	"""
	:param combined: pd.DataFrame with combined data
	:return: new data_frame with a UID for each Block
	"""
	UID = combined.apply(lambda x: (x.COUNTYFP10, x.TRACTCE10,x.BLOCKCE10),axis=1)
	combined.insert(len(combined.columns),'UID',UID)
	return combined


def preprocess_combo(combined):
	"""
	The number of stops 
	:param combined: gpd.GeoDataFrame like object
	:return: the number of stops within a given census block
	"""
	stops_rides = combined.groupby("UID")['stop_id'].size()
	stops_rides = stops_rides.reset_index()
	stops_rides.rename({0:"STOPS"},axis=1,inplace=True)
	trips = combined.groupby("UID")['TRIPS'].sum()
	trips = trips.reset_index()
	stops_rides = stops_rides.merge(trips,on='UID')
	return stops_rides

def join_stops(blocks, stops):
	"""
	This function takes all of the blocks and  
	:param blocks: gpd.GeoDataFrame object containing all the shape files 
	:param stops: gpd.GeoDataFrame object containing all the stops files 
	"""
	combined = gpd.sjoin(blocks,stops)
	return combined

def join_trips(combined, trips):
	"""
	This function combines the whole thing an
	"""
	return combined.merge(trips,on='stop_id')

def preprocess_trips(trips):
	"""
	This function filters trips for our desired ones, without errors and in the morning
	:param trips: pd.DataFrame
	:return: data 
	"""
	trips = trips[trips.error_bool == 0]
	trips = add_commute_time(trips)
	trips = trips[trips.MORNING == 1]
	num_rides = trips.groupby('start_stop')['trip_id'].size()
	stop_morn_rides = num_rides.reset_index()
	stop_morn_rides.rename(columns = {'start_stop':'stop_id','trip_id':'TRIPS'},inplace=True)
	return stop_morn_rides

def output_data(path, df):
	"""
	This file removes unwanted columns and outputs the final dataset
	:param path:
	:param df: 
	:return: 
	"""
	df.to_csv(path,index=False)

def get_duration(path):
	"""
	loads the duration file
	:param path: osp.path object
	:return: pd.DataFrame containing travel times 
	"""
	dur_df = pd.read_csv(path)
	return dur_df

def make_dur_nums(dur_df):
	"""
	:param dur_df:
	:return:
	"""
	pass


def main():
	# setting up the path information
	dir_path = os.getcwd()
	data_path = osp.abspath(osp.join(dir_path,"Data/"))
	stop_path = osp.join(data_path, "stops.txt")
	shape_path = osp.join(data_path,'census.dbf')
	trips_path = osp.join(data_path,'odx/trips.csv')
	out_path = osp.join(data_path,'preprocessed_data.csv')
	#
	stops = get_stops(stop_path)
	blocks = get_blocks(shape_path)
	combined = join_stops(blocks,stops)
	trips = get_trips(trips_path)
	num_rides = preprocess_trips(trips)
	combined = join_trips(combined,num_rides)
	combined = create_UID(combined)
	final_df = preprocess_combo(combined)
	output_data(out_path, final_df)


if __name__ == '__main__':
	main()