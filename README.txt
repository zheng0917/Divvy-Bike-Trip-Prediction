
I will analyze the Divvy data in 2017 include "2017 Q1 & Q2 DATA" and "2017 Q3 & Q4 DATA" which can be download from https://www.divvybikes.com/system-data .

1. I provide a python file "preprocess_data.py" which includes feature engineering and distance computation. It will create a csv file "preprocess_data.csv" for model predction.  

To run "preprocess_data.py", you should first create a folder named "Trips" in the same path which contains "Divvy_Trips_2017_Q1.csv", "Divvy_Trips_2017_Q2.csv", "Divvy_Trips_2017_Q3.csv", "Divvy_Trips_2017_Q4.csv" and 
create a folder named "Stations" which contains "Divvy_Stations_2017_Q1Q2.csv" and "Divvy_Stations_2017_Q3Q4.csv".

It may take a bit long time to run the "preprocess_data.py". I can also directly provide the "preprocess_data.csv" if necessary.

2. I also provide a jupyter notebook named "Trip Prediction.ipynb" which includes the code and report for this prediction problem.

To run this file, you may have to install packages "xgboost" and "plotly". You can just install "plotly" in terminal: pip install plotly and install "xgboost" with conda run: conda install -c anaconda py-xgboost

3. If having any problem, please contact me via email: simon.z.xu23@gmail.com