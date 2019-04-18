---
title: Direct Machine Learning (DirectML)
description: TBD
ms.custom: 19H1
ms.topic: article
ms.date: 04/19/2019
---

# Direct Machine Learning (DirectML)

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). The earliest version in which these feature appears is Windows 10 Insider Preview, version 1903 (10.0; Build 18309).

Direct Machine Learning (DirectML) is a low-level API for machine learning. It has a familiar (native C++, nano-COM) programming interface and workflow in the style of DirectX 12. You can integrate machine learning inferencing workloads into your game, engine, middleware, backend, or other application. DirectML is supported by all DirectX 12-compatible hardware.

## In this section

| Topic | Description |
|-|-|
| [Introduction to DirectML](dml-intro.md) | Direct Machine Learning (DirectML) is a low-level API for machine learning (ML). |
| [Binding in DirectML](dml-binding.md) | In DirectML, *binding* refers to the attachment of resources to the pipeline for the GPU to use during the initialization and execution of your machine learning operators. These resources can be input and output tensors, for example, as well as any temporary or persistent resources that the operator needs. |
| [UAV barriers and resource state barriers in DirectML](dml-barriers.md) | Describes the correctness benefits of barriers, and how you can work with them in DirectML. |
| [Using strides to express padding and memory layout](dml-strides.md) | DirectML tensors are described by properties known as the *sizes* and the *strides* of the tensor. |
| [Resource lifetime and synchronization](dml-resource-lifetime.md) | In order to avoid undefined behavior, your DirectML application must correctly manage object lifetimes and synchronization between the CPU and the GPU. |
| [Using the DirectML debug layer](dml-debug-layer.md) | The DirectML debug layer is an optional development-time component that helps you in debugging your DirectML code. |
| [Handling errors and device-removal](dml-errors.md) | This topic discusses how to debug DirectML device-removal, and other error conditions. |
| [DirectML helper functions](dml-helper-functions.md) | Code listings of essential DirectML helper functions. |
| [DirectML sample applications](dml-min-app.md) | Links to DirectML sample applications, including a sample of a minimal DirectML application. |
| [DirectML reference](http://download.microsoft.com/download/C/5/A/C5A81A2A-78C9-4E8F-AB3B-A40D344B05FF/directmlref.chm) | For this pre-release version of the DirectML documentation, the API reference content is available as a Compiled HTML Help download. Download `directmlref.chm` using the link in the first column. Then, in File Explorer, navigate to your Downloads folder, right-click `directmlref.chm` > **Properties** > **General** > **Security** > **Unblock** > **OK**. Then double-click the file to open and view it. |

## Related topics

* [Direct3D 12 programming guide](directx-12-programming-guide.md)
