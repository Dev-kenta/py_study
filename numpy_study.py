import numpy as np
np_list = np.arange(1,21).reshape(4,5)
np_list = np_list / 4 + 1;
print(np.floor(np_list))