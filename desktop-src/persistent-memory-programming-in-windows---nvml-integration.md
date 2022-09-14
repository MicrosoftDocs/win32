---
description: Persistent memory (PM) technology provides byte-level access to non-volatile media while also reducing the latency of storing or retrieving data significantly.
ms.assetid: 68BF6074-09CB-4D6E-8BFD-FBA297391286
title: Persistent Memory Programming in Windows - NVML Integration
ms.topic: article
ms.date: 05/31/2018
---

# Persistent Memory Programming in Windows - NVML Integration

Persistent memory (PM) technology provides byte-level access to non-volatile media while also reducing the latency of storing or retrieving data significantly. It creates a new tier between a system’s memory and traditional storage. Any program that is dependent on or scales with quick writes to a persistent medium can benefit from PM.

The purpose of this article is to outline how the non-volatile memory library (NVML) can be integrated into a Visual Studio project for easy use.

> [!Note]  
> Persistent Memory is sometimes also referred to as Storage Class Memory (SCM).

 

## PM and NVML

First support for persistent memory was introduced in Windows Server 2016 and the Windows 10 Anniversary Update (1607). For a quick overview, check out these two Channel9 videos:

-   [Using Non-volatile Memory (NVDIMM-N) as Block Storage in Windows Server 2016](https://channel9.msdn.com/Events/Build/2016/P466)
-   [Using Non-volatile Memory (NVDIMM-N) as Byte-Addressable Storage in Windows Server 2016](https://channel9.msdn.com/Events/Build/2016/P470)

To help developers take advantage of the benefits persistent memory offers, Microsoft has also contributed to the efforts of bringing the non-volatile memory library (NVML) to Windows. This library provides various tools to make applications persistent-memory aware. For example, it contains code that lets you easily create a PM-aware key-value store for extremely fast look-ups and stores. You can find more information on NVML, including samples, at [NVM Library](https://pmem.io/nvml/).

## Integrating NVML into a Visual Studio Project

1. Download NVML library files and headers

-   NVML is maintained on GitHub. You can either compile the source yourself, or just download compiled binaries directly from here: [NVML Version 1.2 - Windows Technical Preview](https://github.com/pmem/pmdk/releases/tag/1.2%2Bwtp1).

2. Place the library files and headers in a directory of your choosing, for example: “C:\\NVML\\lib” and “C:\\NVML\\inc” respectively.

3. Configure your project as follows:

-   Open your visual studio project and in the “Solution Explorer” right-click on your project’s name.
-   Open the project’s setting pane at the bottom of the resulting pop-up.
-   Navigate to “Configuration Properties -> C/C++” and add the folder in which you stored the header (C:\\NVML\\inc) to the “Additional Include Directories” field.
-   Next, navigate to “Configuration Properties -> Linker” and add the folder in which you stored the library (C:\\NVML\\lib) to the “Additional Library Directories” field

4. Next, make sure you target the project for Windows Server 2016 or Windows 10 Anniversary Update:

-   Navigate to “Configuration Properties -> General” and set the “Target Platform Version” field to “10.0.14393.0” and
-   Navigate to “Configuration Properties -> C/C++” and add “NTDDI\_VERSION=NTDDI\_WIN10\_RS1;” to the “Preprocessor” field.

5. Include the headers in your code and link to the required libraries

-   At this point, you can simply include the header files you are looking to use in your code like any other header files. For example, to use libpmem:
    -   add "\#include <libpmem.h>" and
    -   add "libpmem.lib" to "Configuration Properties -> Linker -> Input -> Additional Dependencies"

At this point you are ready to call the library’s functions directly in your code and take advantage of them.

 

 



