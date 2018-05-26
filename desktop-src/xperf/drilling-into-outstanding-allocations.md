---
title: Drilling into Outstanding Allocations
description: Drilling into Outstanding Allocations
ms.assetid: c6ccea81-8326-435b-b150-03dbcad22430
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Drilling into Outstanding Allocations

The summary table below, Summary table sorted by allocation type, presents event data from the heapTrace.etl file generated in the [Quick Start](heap-analysis-quick-start.md) section of this document. The data has been sorted by allocation type.

Note that the selection contains a large number of transient allocations (AIFI), 816,500 that total 373,578,345 bytes. An inordinately large number of transient allocations may indicate the need for a code review to determine if frequently accessed data structures could be accessed more efficiently as stack variables.

The outstanding size (AIFO) selected is 9,091,425 bytes made by 24,578 allocations, as shown in the following screen shot.

![screen shot of a summary table sorted by allocation type](images/he-img13.png)

 

 




