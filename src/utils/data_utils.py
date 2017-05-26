import sys, os  

sys.path.append(os.getcwd())
from config import *

sys.path.append(PROJ_ROOT + "src/utils/")
from preprocessing import *

import csv
import numpy as np

def load_data(path=DATASET_URL, n_points_cap=None):
  print("Initiating data loading")
  DESIRED_FIELDS = ['APL', 'AvgPktPerSec', 'IAT', 'NumForward', 'Protocol', 'BytesEx', 'BitsPerSec', 'NumPackets', 'StdDevLen', 'SameLenPktRatio', 'FPL', 'Duration', 'NPEx', 'Score']
  UNDESIRED_FIELDS = ['Source', 'Destination']
  fields_key = {}
  unfields_key = {}

  points = []
  targets = []
  key = []

  with open(path, 'r') as f:
    first_row = True
    training_data = []
    for row in csv.reader(f):
      # If first row, use it to generate header rows dict
      if first_row:
        j = 0
        for field in row:
          if field in DESIRED_FIELDS:
            fields_key[field] = j
          if field in UNDESIRED_FIELDS:
            unfields_key[field] = j
          j += 1
        for field in DESIRED_FIELDS:
          assert(field in fields_key)
        first_row = False
        print("Header correlation complete")
        continue

      # Terminate if reached points cap
      if n_points_cap:
        if (n_points_cap > i):
          print("Points cap reached. Data loading safely terminated early.")
          break

      # Process row
      point, target = score_extraction(row, fields_key)

      points.append(point)
      targets.append(target)
      key.append((row[unfields_key['Source']], row[unfields_key['Destination']]))

  print("All rows processed")
  seq_points, seq_targets, total_len = sequentialify(points, targets, key)
  seq_train = seq_points[:-N_TEST]
  seq_test = seq_points[-N_TEST:]
  seq_train_targets = seq_targets[:-N_TEST]
  seq_test_targets = seq_targets[-N_TEST:]

  len_training = total_len - N_TEST
  len_testing = N_TEST
  print("Data loading complete")

  return {"x":np.array(seq_train), "y":np.array(seq_train), "targets":np.array(seq_train_targets)}, {"x":np.array(seq_test), "y":np.array(seq_test), "targets":np.array(seq_test_targets)}, len_training, len_testing
  
load_data()

