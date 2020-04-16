"""
This class provides a wrapper for the data pipeline. 

"""
import os


class Pipeline:

	def __init__(self, census_path, trips_path):
		"""
		:param census_path: 
		:param df_path:
		"""
		self.census_df = pd.read_csv(census_path)
		self.trips_df = pd.read_csv(trips_path)


	def build_features(self):
		"""
		"""


	def filter(self):
		"""
		This function filters the columns 
		"""

	def make_df(self):
		"""
		"""

	def split(df,y_col):
		"""
		"""

	def make_polynomial(df):
		"""
		"""


	def __call__(self):
		"""

		:param return data frame: 
		"""
		pass