---
title: Enable NVIDIA CUDA in WSL 2
description: Enable the NVIDIA CUDA preview on the Windows Subsystem for Linux
ms.topic: article
ms.date: 06/17/2020
---

# Enable NVIDIA CUDA in WSL 2

The Windows Insider SDK supports running existing ML tools, libraries, and popular frameworks that use NVIDIA CUDA for GPU hardware acceleration inside a WSL 2 instance. This includes PyTorch and TensorFlow as well as all the Docker and NVIDIA Container Toolkit support available in a native Linux environment. 

> [!NOTE]
> The following features are available in prerelease versions of Windows 10, and are subject to change.

## Install the latest Windows Insider Dev Channel build 

To use this preview, you'll need to [register for the Windows Insider Program](https://insider.windows.com/getting-started/#register). Once you do, follow [these instuctions](https://insider.windows.com/getting-started/#install) to install the latest Insider build. When choosing your settings, ensure you're selecting the [Dev Channel](/windows-insider/flight-hub/#active-development-builds-of-windows-10). 

For this preview, you need Build 20150 or higher. You can check your build version number by running `winver` via the **Run** command (Windows logo key + R).

## Install the preview GPU driver 

Download and install the [NVIDIA CUDA-enabled driver for WSL](https://developer.nvidia.com/cuda/wsl) to use with your existing CUDA ML workflows. 

## Set up WSL 2 for the preview 

Once you've installed the above driver, ensure you [enable WSL 2](/windows/wsl/install-win10) and [install a glibc-based distribution](/windows/wsl/install-win10#install-your-linux-distribution-of-choice) (such as Ubuntu or Debian). Ensure you have the latest kernel by selecting **Check for updates** in the **Windows Update** section of the Settings app. 

> [!NOTE]
> Ensure you have **Receive updates for other Microsoft products when you update Windows** enabled. You can find it in **Advanced options** within the **Windows Update** section of the Settings app. 

For this preview, you need a kernel version of 4.19.121 or higher. You can check the version number by running the following command in PowerShell. 

```powershell
wsl cat /proc/version
```

Now you can start using your exisiting Linux workflows through [NVIDIA Docker](https://github.com/NVIDIA/nvidia-docker), or by installing [PyTorch](https://pytorch.org/get-started/locally/) or [TensorFlow](https://www.tensorflow.org/install/gpu) inside WSL 2. More information on getting set up is captured in [NVIDIA's CUDA on WSL User Guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html).

Share feedback on NVIDIA's support via their [Community forum for CUDA on WSL](https://forums.developer.nvidia.com/c/accelerated-computing/cuda/cuda-on-windows-subsystem-for-linux-wsl-2/303).
