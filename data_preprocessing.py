"""

"""

import os.path
import os
import pandas as pd
import numpy as np
import censusgeocode as cg


def geocode(stop_lat,stop_lon):
	"""

	:param stop_lat:
	:param stop_lon:
	"""
	results = cg.coordinates(x=stop_lon, y=stop_lat)['2010 Census Blocks']
    return results[0]['BLOCK']


def get_stops(stop_path):
	"""
	
	:param stop_path:
	"""
	stops = pd.read_csv(os.path.join(data_path,stop_path))
	stops.insert(len(stops.columns),
		'Block',stops.apply(lambda x: gecode(x.stop_lat,x.stop_lon),axis=1))
	return stops

def compile_stops(stops_df):
	"""
	This function 
	:param stops_df: pd.DataFrame
	"""
	if 'Block' in stops_df.columns and 'Rides' in stops_df.columns:
		blocks_df = stops_df.groupby('Block').size()
		return blocks_df
	else:
		return None

def get_census(census_path):
	"""
	
	:param census_path:
	"""
	census = pd.read_csv(census_path)
	return census

def combine_clean(stops_df, census_df, blocks_df):
	"""

	:param stops: pd.DataFrame containing the stops data
	:param census: pd.DataFrame containing the census data
	"""
	census_df = census_df.merge(stops_df, on='Block')
	

def export():
	"""
	"""
	pass



def main():
	"""
	"""
	path = os.path.abspath(os.getcwd())
	data_path = os.path.abspath(os.path.join(path,'Data'))
	stop_path = os.path.join(data_path,'stops.txt')
	census_path = os.path.join(data_path,'census_2010.csv')
	stops = get_stops(stop_path)
	census = get_census()


if __name__ == '__main__':
	main()