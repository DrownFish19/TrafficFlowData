import numpy as np

data01 = np.genfromtxt(
    "/Users/drownfish19/Documents/MATLAB/tra_Y_tr.csv", delimiter=","
)
data02 = np.genfromtxt(
    "/Users/drownfish19/Documents/MATLAB/tra_Y_te.csv", delimiter=","
)

data = np.concatenate([data01, data02], axis=-1).transpose(1, 0)[:, :, np.newaxis]
np.savez("TrafficFlowPrediction.npz", data=data)
print()
