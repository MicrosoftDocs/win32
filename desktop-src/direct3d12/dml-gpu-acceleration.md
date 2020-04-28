---
title: GPU acceleration in WSL
description: Direct Machine Learning (DirectML) powers GPU-accelleration in Windows Subsystem for Linux
ms.topic: article
ms.date: 05/19/2020
---


> [!NOTE]
> The following features are available in prerelease versions of Windows 10, and are subject to change.

# GPU acceleration in WSL

![Windows ML graphic](images/winml-graphic.png)


Using DirectML, you can access your Windows GPU to accellerate machine learning workloads inside the Windows Subsystem for Linux environment. Here's how to get started.

## Prerequisites 

### Install the latest Windows Insider Fast build 

* Join the [Windows Insider Program](https://insider.windows.com/) and select the "Fast" ring 

* Ensure you Windows 10 19614 or higher. Note that you can check your version number by running winver via the Run command 

### Set up WSL 2 and install Ubuntu 18.04 (LTS) on your system by following [this guidance](https://docs.microsoft.com/windows/wsl/wsl2-install)

> [!NOTE]
> These steps have been validated for Ubuntu 18.04 (LTS). They should work on any other glibc or musl based Linux distro, however.

## Install the right GPU driver 

You will need to install specific preview drivers that enable GPU accessibility inside of the WSL 2 container. In the following instructions there are links to the appropriate hardware vendors depending on the preview path you configure.

## Enable DirectML training capabilities 

Once you’ve completed the prerequisites you are ready to try out DirectML’s new training capabilities to accelerate your machine learning workloads. The following will guide you through the additional steps to configure your WSL 2 environment. 

Since this is a preview we recommend you set up a virtual environment inside your WSL 2 instance. For these instructions, we will use [Anaconda’s Miniconda](https://docs.conda.io/en/latest/miniconda.html).

You can install it by the above link, or in WSL 2 by running the following commands. 

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

./Miniconda3-latest-Linux-x86_64.sh
```

Once Miniconda is installed, use the following command to create an environment using Python 3.6 named **dml**.

```
conda create --name dml python=3.6
```

Now you are ready to install the custom TensorFlow package with a DirectML backend. We have our wheel hosted on pypi.org. To install, run this command.

```
pip install tensorflow-directml
```

Finally, install the right driver that supports the GPU hardware in your system. You can find more information on the drivers on the hardware vendors website – [AMD](https://www.amd.com/en/support) and [Intel](https://downloadcenter.intel.com/). 

Now you can get started with the [TensorFlow tutorial models](https://github.com/tensorflow/docs/tree/master/site/en/r1), and start running machine learning training on your existing hardware! 

Expose CUDA in WSL 

If you are interested in getting your exisiting CUDA workloads running inside WSL then the following will guide you through the additional steps to configure your WSL 2 environment. 