---
title: CPU Frequency
description: CPU Frequency
ms.assetid: 10bcb3cf-299e-4e21-ac19-a0b5dd144b4a
keywords:
- usage graph
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CPU Frequency

**Overview:** Displays CPU operating frequency for system processors identified by CPU, as in the following screen shot.

![screen shot of a graph showing cpu frequency by cpu](images/gr-img015.png)

**Graph Type:** Usage graph

**Y-axis Units:** CPU operating Frequency in MHz

**Required Flags:** POWER

**Events Captured:** Power management events

**Legend Description:** Shows active CPUs on the system.

Displays the operating frequency of processors recognized by the system at the start of the trace capture. This graph will not reflect CPUs added to the system after the trace has been started.

Analysis of this graph can serve as the first step in CPU power analysis. CPU power consumption constitutes a significant portion of system power usage. Note that CPU frequency reduction implies a reduction in both power consumption and performance. For more information on CPU Process power consumption see [CPU Power Management](cpu-power-management.md).

 

 




