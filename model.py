import json
from config import ConfigProduction
import pandas as pd

class DataHandling:
    
    def __init__(self):
        self.dataset = pd.read_csv("mlb_players.csv")
    
    def histogram(self,column_name):
        
        data= self.dataset[column_name].value_counts()
        name = self.dataset.Position.unique()
        data = self.dataset['Position'].value_counts()
        y_axis= self.dataset['Position'].value_counts().tolist()
        x_axis = data.index.tolist()
        
        dic={"x_axis":x_axis,"y_axis":y_axis}
    
        return dic