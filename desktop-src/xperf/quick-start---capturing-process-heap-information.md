---
title: Quick Start - Capturing Process Heap Information
description: Quick Start - Capturing Process Heap Information
ms.assetid: 677ce539-5de8-415a-b39e-0d0ba59d483d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Quick Start - Capturing Process Heap Information

Process heap analysis is most effective when stacks are collected capturing HeapAlloc and HeapRealloc events. In order for stacks to be decoded with symbols, the \_NT\_SYMBOL\_PATH environment variable must be set prior to starting XPerfview. For more information on setting this environment variable, please see the [Installation](installation.md) section of this document.

WPA offers two options for capturing process heap data

-   Enabling capture on process launch - This option starts the process being analyzed from the command line sequence that starts data capture. Enabling data capture on process launch guarantees that there will be no loss of allocation information or history.

-   Initiating data capture on a process that has been started. The advantage to capturing data on a running process is there is no need to stop and start the subject process.

Enabling data capture on process launch guarantees that there will be no loss of allocation information or history. When enabling data capture on process launch, the application is started by the WPA tools.

It should be noted that lauching the process from Xperf means that the process will be running with administrator privledges. Therefore, enabling data capture on process launch can change some application behaviors related to security and permission levels. Behaviors of both the scenario and the application should be considered when making a decision about when to begin data capture.

This section includes the following topics:

<dl>

[Quick Start - Enabling Data Capture on Process Launch](quick-start---enabling-data-capture-on-process-launch.md)  
[Quick Start - Enabling Data Capture on an Existing Process](quick-start---enabling-data-capture-on-an-existing-process.md)  
</dl>

 

 




