# Predictor public interface
from . import model
import sqlite3

class Predictor():
    def _init_(self, csv):
        LR = model.createModel(csv)

    def dump(self):
        import joblib
        joblib.dump(self.LR, "model.pkl")

    def load(self, modelname):
        import joblib
        self.LR = joblib.load("modelname")

    def getNewData(self, dbPath):
        pass