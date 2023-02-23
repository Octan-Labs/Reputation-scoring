import matplotlib.pyplot as plt
import numpy as np


def logistic(x,
             a=1,
             b=1 / 64):
    return a / (1.0 + np.exp(-b * x))


def logistic_weights_global(blocks_range,
                            current_block_height,
                            blocks_per_day=28800,
                            active_time=90):
    edges_timestamp = [int(block_height / blocks_per_day) for block_height in blocks_range]
    timestamp_weights_dict = dict()
    edges_weights = []
    origin = int(current_block_height/blocks_per_day) - active_time
    for timestamp in edges_timestamp:
        if timestamp not in timestamp_weights_dict.keys():
            timestamp_origin = timestamp - origin
            timestamp_weights_dict[timestamp] = logistic(timestamp_origin)
        edges_weights.append(timestamp_weights_dict[timestamp])
    return edges_weights


def logistic_weights_local(blocks_range,
                           blocks_per_day=28800,
                           active_time=90):
    edges_timestamp = [int(block_height / blocks_per_day) for block_height in blocks_range]
    timestamp_weights_dict = dict()
    edges_weights = []
    local_timestamp = [(i - edges_timestamp[0]) for i in edges_timestamp]
    origin = local_timestamp[-1] - active_time
    for time_count in local_timestamp:
        if time_count not in timestamp_weights_dict.keys():
            timestamp_origin = time_count - origin
            timestamp_weights_dict[time_count] = logistic(timestamp_origin)
        edges_weights.append(timestamp_weights_dict[time_count])
    return edges_weights


# create block height sample
blocks_array = []
for i in range(2000):
    j = (i+5000)*5000
    blocks_array.append(j)

global_weights = logistic_weights_global(blocks_array, current_block_height=21000000)
local_weights = logistic_weights_local(blocks_array)
print(len(blocks_array))
print(len(global_weights))
print(len(local_weights))
# plot weights distribution
plt.plot(local_weights)
plt.show()

