# Predictor public interface
import model
import sqlite3

class Predictor():
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
 