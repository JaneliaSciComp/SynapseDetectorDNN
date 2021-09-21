import pickle
import matplotlib.pyplot as plt 
import numpy as np 

history_path = '# /pkl directory'
file_name = '# model.pkl'


with open(history_path+file_name, 'rb') as f:
    history = pickle.load(f)

# U-Net
num_epoch = len(history['loss'])
label=['Acc', 'Loss', 'Err_pos', 'Err_neg']
plt.figure()
plt.ylim(-0.1,1.1)
plt.plot(range(num_epoch), history['masked_accuracy'], 'r')
plt.plot(range(num_epoch), history['loss'], 'b')
plt.plot(range(num_epoch), history['masked_error_pos'], 'c')
plt.plot(range(num_epoch), history['masked_error_neg'], 'g')
plt.xlabel('Num epoch', color='k')
plt.ylabel('Performance', color='k')
plt.legend(label)
plt.grid(color='k', linestyle=':')
plt.savefig(history_path+'performance.png')
plt.show()