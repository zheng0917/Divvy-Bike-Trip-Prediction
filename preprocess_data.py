# -*- coding: utf-8 -*-
import pandas as pd
import glob
from math import radians, sin, cos, sqrt, atan2

def read_files(path):
    allFiles = glob.glob(path + "/*.csv")
    l = []
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0)
        l.append(df)
    return pd.concat(l)

"""
you should first create a folder named "Trips" which contains 
"Divvy_Trips_2017_Q1.csv", "Divvy_Trips_2017_Q2.csv", "Divvy_Trips_2017_Q3.csv", "Divvy_Trips_2017_Q4.csv"
"""
trips = read_files(r'./Trips')  
"""
you should first create a folder named "Stations" which contains
"Divvy_Stations_2017_Q1Q2.csv" and "Divvy_Stations_2017_Q3Q4.csv"
"""
stations = read_files(r'./Stations')
stations = stations.drop_duplicates(subset=['name']) # drop the dupilcate stations
  

# calculate the manhattan distance based on geography information
def manhattan_distance(start, end):
    latitude1, longitude1, latitude2, longitude2 = map(radians, [start[0], start[1], end[0], end[1]])
    r = 6371 # radius of Earth
    
    #calculate delta_latitude distance by the haversine formula
    delta_lat = latitude2 - latitude1
    a = sin(delta_lat / 2) ** 2
    lat_d = r * 2 * atan2(sqrt(a), sqrt(1-a))
    
    #calculate delta_longitude distance by the haversine formula
    delta_lon = longitude2 - longitude1
    a = (cos(latitude2) ** 2) * (sin(delta_lon / 2) ** 2)
    lon_d = r * 2 * atan2(sqrt(a), sqrt(1-a))
    
    return lat_d + lon_d
    
# record the distance, latitude and longitude for each trip
stations[['latitude','longitude']] = stations[['latitude','longitude']].astype(float)
distance = []
start_latitude = []
start_longitude = []
for index,row in trips.iterrows():
    if row[6] in stations['name'].values and row[8] in stations['name'].values:
        start = stations.loc[stations['name'] == row[6]]
        end = stations.loc[stations['name'] == row[8]]
        d = manhattan_distance(start[['latitude','longitude']].values[0],end[['latitude','longitude']].values[0])
        latitude = start['latitude'].values[0]
        longitude = start['longitude'].values[0]
    else:
        d = float('nan')
        latitude = float('nan')
        longitude = float('nan')
    distance.append(d)
    start_latitude.append(latitude)
    start_longitude.append(longitude)
    
# create a new dataset which includes features and distance
    
dataset = trips[['start_time','from_station_id','usertype','gender','birthyear']]
dataset['distance'] = pd.Series(distance).values 

# user features
dataset['gender'].fillna('Unknown', inplace=True)
dataset['birthyear'] = 2018 - dataset['birthyear'].values

# trip start time features
dataset['start_time'] = pd.to_datetime(dataset['start_time'])
dataset['month'] = dataset['start_time'].dt.month
dataset['weekday'] = dataset['start_time'].dt.weekday
dataset['hour'] = dataset['start_time'].dt.hour

# station features
dataset['from_station_id'] = dataset['from_station_id']
dataset['latitude'] = pd.Series(start_latitude).values
dataset['longitude'] = pd.Series(start_longitude).values

new_data = dataset[['usertype','gender','birthyear','month','weekday','hour','from_station_id','latitude','longitude','distance']]

# save the new dataset 
new_data.to_csv('preprocess_data.csv')



