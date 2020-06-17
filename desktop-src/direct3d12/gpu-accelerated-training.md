---
title: GPU acceleration in WSL
description: Direct Machine Learning (DirectML) powers GPU-accelleration in Windows Subsystem for Linux
ms.topic: article
ms.date: 06/17/2020
---

# GPU accelerated ML training

![Windows ML graphic](images/winml-graphic.png)

This documentation covers what is currently supported by the GPU accelerated machine learning (ML) training preview for the [Windows Subsystem for Linux](https://docs.microsoft.com/windows/wsl/about) (WSL) and native Windows.  

This preview supports both professional and beginner scenarios. Below you will find pointers to step-by-step guides on how to get your system setup depending on your level of expertise in ML, GPU vendor, and the software library you intend to use. 

> [!NOTE]
> The following features are in preview, and are subject to change.


## Professionals

If you’re a professional data scientist that uses a native Linux environment day-to-day for inner-loop ML development and experimentation, and you have an NVIDIA GPU, we recommend setting up the [NVIDIA CUDA preview in WSL 2.](gpu-cuda-in-wsl.md)

## Students and beginners 

If you’re a student or beginner looking to start building your knowledge in the ML space, we recommend setting up the TensorFlow with DirectML backend package. This package currently accelerates workflows on AMD and Intel GPUs. Support for NVIDIA GPUs is coming soon. 

For those more familiar with a native Linux environment that are getting started with ML workflows, we recommend running the [TensorFlow with DirectML package inside WSL 2](gpu-tensorflow-wsl.md). 

For those more familiar with Windows that are getting started with ML workflows, we recommend setting up the [TensorFlow with DirectML package on native Windows](gpu-tensorflow-windows.md). 

## Next steps

* [Enable NVIDIA CUDA preview in WSL 2](gpu-cuda-in-wsl.md).
* [Enable TensorFlow with DirectML package inside WSL 2](gpu-tensorflow-wsl.md).
* [Enable TensorFlow with DirectML package on native Windows](gpu-tensorflow-windows.md).
