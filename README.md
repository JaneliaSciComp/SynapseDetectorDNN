# Synapse Detector DNN

Deep Neuron Network for synapse detection.

## Training

The `training` directory contains everything necessary for training the model. To train a new model, in the python script ExLLSM_unet_v2_train.py: 

* modify line 10 to point to the directory containing raw data and corresponding ground truth image crops. 500x500x500 and 100x100x100 crops have been used for testing
* modify line 11-13 (and add additional lines for additional data crops) to indicate the name of each raw data crop and each corresponding ground truth data crop (both in nrrd format)
* modify line 24 to point to the save directory
* modify line 25 to change training parameters if desired
* modify line 27 to change the pkl name if desired
* modify line 30 to name the final trained model

Activate the training environment included and run the updated python script to train.

To plot the training progress over time, modify lines 5 and 6 of the python script ExLLSM_unet_training_result_plot.py as indicated and run the updated python script.

Finally, the ExLLSM_unet_performance_evaluate.py script can be used to calculate the precision and recall (sensitivity) of predicted synapses compared to ground truth data. To use this, modify lines 50-52 as indicated and run the updated python script. It is recommended that the trained model and postprocessing steps are run via the [Expansion Microscopy Pipeline](https://github.com/JaneliaSciComp/expansion-microscopy-pipeline) before evaluating performance versus ground truth data.  


## Inference

The `inference` directory contains the detector that uses the trained model to make synapse predictions. This code is integrated into the [Expansion Microscopy Pipeline](https://github.com/JaneliaSciComp/expansion-microscopy-pipeline) and currently meant to be run there, inside of a Docker container.

