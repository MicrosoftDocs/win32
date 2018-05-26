---
title: Kernel Trace Control Design Guide
description: Kernel Trace Control Design Guide
ms.assetid: 32d805e2-1e14-435a-9d32-69bb1558fe1f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Kernel Trace Control Design Guide

**When to Use Kernel Trace Control API:**

Use the Kernel Trace Control API to meet any of the following requirements:

-   To programmatically capture call stacks that leads to a ready thread or virtual memory events in addition to other kernel events.

-   To programmatically merge multiple trace files.

-   To programmatically include system information in merged trace files to facilitate analysis.

**Where to Implement Kernel Trace Control:**

-   Calling the APIs in an executable (exe). This option allows flexibility at the cost of starting at least one new process and associated threads.

-   Building libraries that can be included in application code.

-   Development of a complete test environment that includes either or both of the previous options.

When you decide where or when to implement the Kernel Trace Control API, consider that the WPT tracing imposes strict limits on the amount of resources used to capture traces. In most cases, event capture has a minimal effect on overall system resource usage.

 

 




