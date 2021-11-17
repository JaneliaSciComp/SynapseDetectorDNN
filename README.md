# ExLLSM Synapse Detector

[![DOI](https://zenodo.org/badge/348389664.svg)](https://zenodo.org/badge/latestdoi/348389664)

This repository contains code to train and evaluate the performance of a 3D U-Net shaped model for synapse detection. It was designed to classify synaptic sites in large scale volumetric images generated via expansion microscopy and lattice light-sheet imaging (ExLLSM). The `inference` directory contains the detector that uses the trained model to make synapse predictions. This code is integrated into the [ExLLSM Circuit Reconstruction Pipeline](https://github.com/JaneliaSciComp/exllsm-circuit-reconstruction) and currently meant to be run there, inside of a Docker container.

**3D U-Net shaped network structure**
![U-net-like](https://user-images.githubusercontent.com/8125635/142205664-c986c90a-87eb-4d44-a239-9b9ce95e764d.png)

## Quick Start

First setup a conda environment using the following command:
```
conda create -n exllsm-synapse
conda env update -n exllsm-synapse -f environment.yml
```
then activate it:
`
conda activate exllsm-synapse
`

## Training

To train a new model, some parameters in the python script ExLLSM_unet_v2_train.py need to be adjusted: 

* modify line 10 to point to the directory containing raw data and corresponding ground truth image crops. 
** 500x500x500 and 100x100x100 crops have been used for testing
* modify line 11-13 (and add additional lines for additional data crops) to indicate the name of each raw data crop and each corresponding ground truth data crop (both in nrrd format)
* modify line 24 to point to the save directory
* modify line 25 to change training parameters if desired
* modify line 27 to change the pkl name if desired
* modify line 30 to name the final trained model

Usage: 

     python ExLLSM_unet_v2_train.py
     
## Plot training progress

To plot the training progress over time, modify lines 5 and 6 of the python script ExLLSM_unet_training_result_plot.py as indicated.

Usage: 

     python ExLLSM_unet_training_result_plot.py

## Model Evaluation

To appropriately evaluate the model performance it should be compared to ground truth data from independent samples (brains/animals) not involved in training. 
     
It is recommended that the trained model is used via the [ExLLSM Circuit Reconstruction Pipeline](https://github.com/JaneliaSciComp/exllsm-circuit-reconstruction) where additional recommended post-U-Net processing steps not included here are found.

To calculate the precision and recall scores of a model run via the ExLLSM Circuit Reconstruction Pipeline to ground truth data from independent samples, use the ExLLSM_unet_performance_evaluate.py script. Modify lines 50-52 as indicated and run the updated python script. 

Usage: 

     python ExLLSM_unet_performance_evaluate.py

## Inference

The `inference` directory contains the detector that uses the trained model to make synapse predictions. This code is integrated into the [Expansion Microscopy Pipeline](https://github.com/JaneliaSciComp/expansion-microscopy-pipeline) and currently meant to be run there, inside of a Docker container.

