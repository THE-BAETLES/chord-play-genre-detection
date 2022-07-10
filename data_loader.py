import os
import numpy
import torch
from torch.utils import data


class GTZANDataset(data.dataset):
    def __init__(self, data_path:str, split: str, num_samples: int, num_chunks: int, is_augumentation: bool):
        self.data_path = data_path if data_path else '/home/parker/data/Data'
        self.split = split
        self.num_samples = num_samples
        self.num_chunks = num_chunks
        
        self.genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
        self.song_list = self._get_song_list()
        
    def _get_song_list(self):
        # Train model 30 sec music
        feature_file_name = os.path.join(self.data_path, 'features_30_sec.csv ')
        with open(feature_file_name) as f:
            lines = f.readlines()
        
        return [line.strip() for line in lines]
    
    def __getitem__(): 
        pass
    
    def __len__():
        pass
    
