---
title: Tensorflow with DirectML on WSL 2
description: Enable TensorFlow with DirectML on the Windows Subsystem for Linux
ms.topic: article
ms.date: 06/17/2020
---

# Enable TensorFlow with DirectML in WSL 2

This preview provides students and beginners a way to start building knowledge in the ML space on their existing hardware by using the TensorFlow with DirectML package. Once set up, users can start with the [TensorFlow tutorial models](https://github.com/tensorflow/docs/tree/master/site/en/r1/tutorials) or our [DirectML samples](https://github.com/microsoft/DirectML). 

> [!NOTE]
> The following features are available in prerelease versions of Windows 10, and are subject to change.

## Install the latest Windows Insider Dev Channel build 

To use this preview, you'll need to [register for the Windows Insider Program](https://insider.windows.com/getting-started/#register). Once you do, follow [these instuctions](https://insider.windows.com/getting-started/#install) to install the latest insider build. When choosing your settings, ensure you're selecting the [Dev Channel](/windows-insider/flight-hub/#active-development-builds-of-windows-10). 

For this preview, you need Build 20150 or higher. You can check your build version number by running `winver` via the **Run** command (Windows logo key + R).

## Install the preview GPU driver 

Before installing the TensorFlow with DirectML package inside WSL 2, you need to install drivers from your GPU hardware vendor. These drivers enable the Windows GPU to work with WSL 2.

### AMD 

[Download and install AMD’s preview driver](https://www.amd.com/en/support/kb/release-notes/rn-rad-win-wsl-support) from their website. This preview driver supports the following hardware: 

* AMD Radeon™ RX series and Radeon™ VII graphics. 
* AMD Radeon™ Pro series graphics. 
* AMD Ryzen™ and Ryzen™ PRO Processors with Radeon™ Vega graphics. 
* AMD Ryzen™ and Ryzen™ PRO Mobile Processors with Radeon™ Vega graphics. 

For a complete list of compatible AMD products, please refer to the AMD Release Notes. 

### Intel 

[Download and install Intel’s preview driver](https://downloadcenter.intel.com/download/29526) to use with DirectML from their website. 

### NVIDIA 

[Download and install NVIDIA's preview driver](https://developer.nvidia.com/cuda/wsl/download) to use with DirectML from their website. For more information, see [NVIDIA's GPU in Windows Subsystem for Linux (WSL)](https://developer.nvidia.com/cuda/wsl) page.

## Set up the TensorFlow with DirectML preview 

### Install WSL 2 

Once you've installed the above driver, ensure you [enable WSL 2](/windows/wsl/install-win10) and [install a glibc-based distribution](/windows/wsl/install-win10#install-your-linux-distribution-of-choice) (like Ubuntu or Debian). For our testing, we used Ubuntu. Ensure you have the latest kernel by selecting **Check for updates** in the **Windows Update** section of the Settings app. 

> [!NOTE]
> Ensure you have the **Receive updates for other Microsoft products when you update Windows** enabled. You can find it in **Advanced options** within the **Windows Update** section of the Settings app. 

For this preview, you need a kernel version of 4.19.121 or higher. You can check the version number by running the following command in PowerShell. 

```
wsl cat /proc/version
```

### Set up Python environment 

We recommend setting up a virtual Python environment inside your WSL 2 instance. There are many tools you can use to setup a virtual Python environment — for these instructions, we'll use [Anaconda’s Miniconda](https://docs.conda.io/en/latest/miniconda.html). The rest of this setup assumes you use a miniconda environment. 

Install Miniconda by following the [guidance on Anaconda’s site](https://conda.io/projects/conda/en/latest/user-guide/install/index.html), or by running the following commands in WSL. 

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
bash Miniconda3-latest-Linux-x86_64.sh 
```

Once Miniconda is installed in WSL, create an environment using Python named “directml” and activate it through the following commands. 

> [!NOTE]
> In the commands below, we use Python 3.6. However, the tensorflow-directml package works in a Python 3.5, 3.6 or 3.7 environment. 

```
conda create --name directml python=3.6 

conda activate directml 
```

### Install the Tensorflow with DirectML package 

Install the package of TensorFlow with a DirectML backend through pip by running the following command.

> [!NOTE]
> The tensorflow-directml package only supports TensorFlow 1.15. 

```
pip install tensorflow-directml
```

Once you’ve installed the tensorflow-directml package, you can verify that it runs correctly by adding two tensors. Copy the following lines into an interactive Python session. 

```
import tensorflow.compat.v1 as tf 

tf.enable_eager_execution(tf.ConfigProto(log_device_placement=True)) 

print(tf.add([1.0, 2.0], [3.0, 4.0])) 
```

You should see output similar to the following, with the add operator placed on the DML device. 

```
2020-06-15 11:27:18.235973: I tensorflow/core/common_runtime/dml/dml_device_factory.cc:45] DirectML device enumeration: found 1 compatible adapters. 

2020-06-15 11:27:18.240065: I tensorflow/core/common_runtime/dml/dml_device_factory.cc:32] DirectML: creating device on adapter 0 (AMD Radeon VII) 

2020-06-15 11:27:18.323949: I tensorflow/stream_executor/platform/default/dso_loader.cc:60] Successfully opened dynamic library libdirectml.so.ba106a7c621ea741d21598708ee581c11918380 

2020-06-15 11:27:18.337830: I tensorflow/core/common_runtime/eager/execute.cc:571] Executing op Add in device /job:localhost/replica:0/task:0/device:DML:0 

tf.Tensor([4. 6.], shape=(2,), dtype=float32) 
```

## Tensorflow with DirectML samples and feedback 

Now you’re ready to start learning more about ML training. Check out the [TensorFlow tutorials](https://github.com/tensorflow/docs/tree/master/site/en/r1/tutorials) or [our samples](https://github.com/microsoft/DirectML). We used this content as validation for this initial preview package of TensorFlow with DirectML. 

If you run into issues or have feedback on the TensorFlow with DirectML package, please [connect with our team here](https://github.com/microsoft/DirectML/issues).
