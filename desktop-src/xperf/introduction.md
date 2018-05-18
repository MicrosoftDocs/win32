---
title: Introduction
description: Introduction
ms.assetid: '16bc5e09-12f8-4050-be58-a5972b4c36a7'
---

# Introduction

The Windows Performance Analyzer (WPA) is a set of analysis tools used to produce detailed performance profiles of Microsoft Windows operating systems and applications. WPA is useful to a broad audience including:

-   System builders

-   Hardware manufacturers

-   Driver developers

-   General application developers

WPA has been engineered specifically to measure and provide a broad system-level view of performance across different components such as the CPU, disk, and GPU. WPA was built for Windows Vista and Windows Server 2008. Limited function is provided for Windows XP SP2 and Windows Server 2003. For more information regarding Windows XP SP2 and Windows Server 2003, see the [Installation](installation.md) section of this document.

To save power usage in laptop and desktop computers is a critical topic for system designers, OEMs, and software architects. CPUs constitute a significant percentage of overall system power budgets. Additionally, the emergence of multi-core and multithreaded processor designs has introduced new complexities into platform and operating system support for CPU processor power management (PPM).

This section focuses on using Windows Performance Analyzer to identify CPU processor power management states. Because the measurements are obtained from the Windows kernel power manager, any differences between processor families and manufacturers are abstracted.

Some of the metrics made available using WPA are:

-   Time and utilization by CPU

-   Time spent in P-states and C-states

-   Correlation of CPU frequency changes across time, processes, or threads

This information is especially useful for original equipment manufacturers (OEMs) who want to improve the overall power performance of their systems. Although portable computers users are obvious beneficiaries of this information, understanding power usage profiles is important to anyone with an interest in power consumption.

 

 




