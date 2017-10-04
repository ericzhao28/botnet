import os


SAVES_DIR = os.path.dirname(os.path.realpath(__file__)) + "/saves/"
GRAPHS_TRAIN_DIR = SAVES_DIR + "graphs/train/"
GRAPHS_TEST_DIR = SAVES_DIR + "graphs/test/"
CHECKPOINTS_DIR = SAVES_DIR + "checkpoints/"

ITERATIONS = 50
BATCH_SIZE = 50
N_FEATURES = 13
N_STEPS = 5
LAYERS = {
    'h_gru': 8,
    'h_att': 4,
}
ENCODED_DIM = 8
N_CLASSES = 2

REPORT_INTERVAL = 5000
SAVE_INTERVAL = 100000
