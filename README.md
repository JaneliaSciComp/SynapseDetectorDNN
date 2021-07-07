# Synapse Detector DNN

Deep Neuron Network for synapse detection. There are two possible pipelines. The first pipeline is for detecting synapses in a volume without neuron information. This pipeline can be used with neuron information, but in practice it makes more sense to use the second pipeline when considering neuron information because it allows the U-Net to be run just once, instead of independently for each neuron of interest. The second pipeline is for detecting synapses and assigning those synapses to our neurons. This pipeline requires neuron masks. 

The actual pipelines using this DNN code are available in the [https://github.com/JaneliaSciComp/expansion-microscopy-pipeline](expansion-microscopy-pipeline) repository. There is also a Dockerfile which demonstrates how to install all of the dependencies.

## Detect synapses in a volume, independent of neuron information

Example:

    unet_gpu.py -i /input_directory -o /output_directory -t 400 -s

t = objects below 400vx will be removed, s = convert hdf5 to tiff

This will output the synapse masks in hdf5 and tiff series as well as csv files of the synapse location and size.

Currently it gives a separate csv for each chunk of the volume and we've been consolidating these in a separate action. We should update this to additionally consolidate all of the csv files automatically.

## Detect synapses in a volume, attach those synapses to a neuron 

Runs in three stages as follows:

**Stage 1**

    unet_gpu.py -i /A -o /B

-i = input dir, o = output dir
this will give an hdf5 of the unet results and log files

**Stage 2**

    postprocess_cpu.sh -i /B -o /C -m /D -t 400 -p 0.5 -s 

-i = input dir with hdf5, in this case the output dir from stage 1; -o = output dir; -m = mask dir of neuron 1 (tiff sequence generated via semi-automatic or automatic neuron seg pipeline); -t min vx filter; -p = percentage of synapse voxels that must overlap with neuron  to be assigned to the neuron, here 50%; -s = convert hdf5 to tiff
this will give an hdf5, tiff, and csv files of the synapses assigned to neuron 1 

**Stage 3**

    postprocess_cpu.sh -i /C -o /E -m /F -t 400 -p 0.01 -s

-i = input dir with hdf5, in this case the output dir from stage 2; -o = output dir; -m = mask dir of neuron 2 (tiff sequence generated via semi-automatic or automatic neuron seg pipeline); -t min vx filter; -p = percentage of synapse voxels that must overlap with neuron to be assigned to the neuron, here 1%; -s = convert hdf5 to tiff 
this will give an hdf5, tiff, and csv files of the putative synaptic connections from neuron 1 to neuron 2

