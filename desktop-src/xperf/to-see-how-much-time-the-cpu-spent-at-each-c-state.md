---
title: To See How Much Time the CPU Spent at Each C-state
description: To See How Much Time the CPU Spent at Each C-state
ms.assetid: 92b97703-8ed8-4730-8c58-4b0b0705c304
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To See How Much Time the CPU Spent at Each C-state

The CPU Idle States graph, as shown in the following screen shot, displays the target and actual C-states for a selected time interval.

![screen shot of a cpu idle states graph](images/pwr-img06.png)

To display the data in tabular form, right-click in the **CPU Idle States** graph area to select the entire view of the C-state graph and select **Select View** from the drop-down menu. After the entire graph is selected, right-click again and select **Simple Summary**. This Simple Summary table provides enough information to perform basic CPU idle state analysis by identifying these metrics, as in the following screen shot.

![screen shot of a graph showing c-state durations](images/pwr-img06.png)

The **Simple Summary** provides the following data:

-   The amount of time the processor spent in C3, the lowest exposed C-state

-   The amount of time spent with the processor Active or in an intermediate C-state

If the processor family supports deeper C-states that are not exposed to the operating system, it is possible that the time shown spent in C3 may have been spent in even deeper C-states with lower power consumption.

 

 




