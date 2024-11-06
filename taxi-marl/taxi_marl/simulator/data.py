import os
import numpy as np
import pickle as pkl

dir_prefix = ('/mnt/c/Users/Mr Brownstone/Documents/Work/School/McGill University/'
              'COMP 597 - Machine Learning Applications in Real-World Systems/'
              'Project - Taxi Carpool MARL/code/')

data_dir = dir_prefix + 'data/dispatch_realdata/data_for_simulator/'

# Number of timesteps in an episode
ep_len = 144
n_valid_cells = 8

mapped_matrix_int = np.array([[1, -100, 3],
                              [5, 4, 2],
                              [6, 7, 8]])
M, N = mapped_matrix_int.shape
order_num_dist = []

# A 2d list of size 144 x number of grids.
# idle_driver_location_mat[0][grid_matrix_id] = 100 indicate mean of idle drivers at cell _grid_matrix_id_ at time 0.
idle_driver_location_mat = np.zeros((len_ep, n_valid_cells))
    
for i in range(ep_len):
    time_dict = {j: [2] for j in range(M*N)} # M*N total num of cells/nodes
    order_num_dist.append(time_dict)
    idle_driver_location_mat[i, :] = [2] * n_valid_cells

mapped_matrix_int = pkl.load(open(data_dir+"mapped_matrix_int.pkl", 'rb'))
order_num_dist = pkl.load(open(data_dir+"order_num_dist", 'rb'))
idle_driver_dist_time = pkl.load(open(data_dir+"idle_driver_dist_time", 'rb'))
idle_driver_location_mat = pkl.load(open(data_dir+"idle_driver_location_mat", 'rb'))
target_ids = pkl.load(open(data_dir+"target_grid_id.pkl", 'rb'))
onoff_driver_location_mat = pkl.load(open(data_dir + "onoff_driver_location_mat", 'rb'))
order_filename = dir_prefix + "dispatch_realdata/orders/all_orders_target"
order_real = pkl.load(open(order_filename, 'rb'))