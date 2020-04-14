import itertools as it



class CommuterIdentifier:
	"""
	This class helps rationalize and simplify the commuter identification procedure. 

	"""
	def __init__(self, trip_num, diff, od=True, tod=True, morning = (6,10), afternoon = (4,7)):
		"""
		
		:param trips_df: pd.DataFrame 
		:param trip_num: bool, saying a commute is two trips 
		:param diff: int, time differential between the trips
		:param od: bool, that determines 
		:param tod: 

		"""
		self.trip_num = trip_num
		self.diff = diff
		self.od = od
		self.tod = tod
		self.morning = morning 
		self.afternoon = afternoon


	def check_frame(self, com_df):
		"""
		This function ensures that all necessary columns are present
		:param com_df: pd.DataFrame
		:return: Boolean 
		"""
		pass

	def check_data(self, com_df ):
		"""
		
		:param com_df: pd.DataFrame
		:return: Boolean 
		"""
		pass

	def get_tod(self,com_df, start, end, name):
		"""
		The 
		:param com_df: pd.DataFrame
		:return: com_df with added column under name
		"""
		time_bol = ((com_df.start_time.dt.hour > start) 
				& (com_df.start_time.dt.hour <= end)) * 1
		com_df = com_df.insert(len(com_df.columns),name,time_bol)
		return com_df

	def analyze_times(self,com_df):
		"""
		This takes the times of days
		:param com_df: pd.DataFrame
		:return: 
		""" 
		for t1, t2 in it.combinations(com_df.index.values,2):
			tdf = com_df.loc[:,t2].start_time - com_df.loc[:,t1].start_time



	def check_diff(self,com_df):
		"""

		:param com_df: 
		:return:
		"""

	def check_od(self):
		"""
		Checks to 
		"""
		pass


	def __call__(self, com_df):
		"""
		
		:param com_df: pd.DataFrame
		:return: Boolean, returns true if a individual is a commuter false ow 
		"""
		com_df.sort_values(by=['start_time'])
		comd_df = self.get_tod(com_df, self.morning[0],self.morning[1],'MORNING')
		comd_df = self.get_tod(com_df, self.afternoon[0],self.afternoon[1],'AFTERNOON')
		if self.tod:
			self.analyze_times(com_df)


