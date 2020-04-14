"""


"""

import os.path as osp
import os
import pandas as pd
from commuter import CommuterIdentifier


def get_trips(trips_path):
	"""
	Loads and cleans the file containing all of the rider files. 
	:param trips_path: path to the trips file
	:return: pd.DataFrame
	"""
	trips = pd.read_csv(trips_path)
	return trips


def add_commute_time(trips_df):
	"""
	This 
	:param trips_df: pd.DataFrame 
	:return: pd.Dataframe 
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

def identify_commuters(trips_df, trip_num, diff, od, day):
	"""

	:param trips_df: pd.DataFrame 
	:param trip_num: bool, saying a commute is two trips 
	:param diff: int, time differential between the trips
	:param od: bool, that determines 
	:param day: bool, defines a commute on the same day
	:return: 
	"""
	



def main():
	dir_path = os.getcwd()
	data_path = osp.abspath(osp.join(dir_path,"Data/"))
	trips_path = osp.join(data_path,'odx/trips.csv')

	commuter_processor = CommuterIdentifier(2,6)
	trips = get_trips(trips_path)
	trips.loc[:,'start_time'] = pd.to_datetime(trips.start_time)
	trips.loc[:,'end_time'] = pd.to_datetime(trips.end_time)
	#trips = add_commute_time(trips)
	for commuter, com_df in trips.groupby('breeze_id'):
		commuter_processor(com_df)
	print(com_df)

if __name__ == '__main__':
	main()