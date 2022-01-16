# Predictor public interface
import model
import sqlite3
import numpy as np
import pandas as pd

class Predictor:
    def __init__(self, csv):
        self.LR = model.createModel(csv)

    def dump(self):
        import joblib
        joblib.dump(self.LR, "model.pkl")

    def load(self, modelname):
        import joblib
        self.LR = joblib.load("modelname")

    def getNewData(self, dbPath):
        pass # TODO: convert sqlite db to csv

    def predictCost(self, pickup_long, pickup_lat, dest_long, dest_lat, num_pas):
        arr = {'pickup_longitude': [pickup_long],
                'pickup_latitude': [pickup_lat], 
                'dropoff_longitude': [dest_long], 
                'dropoff_latitude': [dest_lat], 
                'passenger_count': [num_pas]}
        df = pd.DataFrame(arr)
        pred = self.LR.predict(df)
        print("Predicted Cost", pred)
        
        return pred[0]

if (__name__ == '__main__'):
    pr = Predictor("train_data.csv")
    pr.predictCost(-73.844311,40.721319,-73.84161,40.712278,1)
    pr.dump()