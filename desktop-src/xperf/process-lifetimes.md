---
title: Process Lifetimes
description: Process Lifetimes
ms.assetid: 'c6305c50-fc92-4fb1-9f13-a8c7997cda6e'
keywords: ["lifetime graph"]
---

# Process Lifetimes

**Overview:** Displays beginning and ending times for processes active during a defined time interval, as shown in the following screen shot.

![process start and ending times](images/gr-img019.png)

**Graph Type:** Lifetime graph

**Y-axis Units:** The Y-axis units in this graph are lanes representing processes running for a time interval and whose lifetime does not overlap. The bottom lane displays processes that are running for the entire lifetime of the trace.

**Required Flags:** LOADER+PROC\_THREAD

**Events Captured:** Kernel-mode and user-mode Image Load/Unload events, Process and Thread create/delete

**Legend Description:** Displays the colors denoting start and stop of a process.

**Graph Description:** Displays the lifetime of system and application processes. By isolating a process using the legend and overlaying CPU and disk graphs, the user can determine where to look in the trace.

 

 




