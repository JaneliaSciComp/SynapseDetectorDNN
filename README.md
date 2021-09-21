# Synapse Detector DNN

Deep Neuron Network for synapse detection.

## Training

The `training` directory contains everything necessary for training the model.

## Inference

The `inference` directory contains the detector that uses the trained model to make synapse predictions. This code is integrated into the [Expansion Microscopy Pipeline](https://github.com/JaneliaSciComp/expansion-microscopy-pipeline) and currently meant to be run there, inside of a Docker container.

