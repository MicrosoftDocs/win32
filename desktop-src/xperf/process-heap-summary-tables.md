---
title: Process Heap Summary Tables
description: Process Heap Summary Tables
ms.assetid: 'ed51ff69-fc61-4bef-83e0-bac4c27fbeea'
---

# Process Heap Summary Tables

Summary tables display a highly flexible tabular view of call stack and stack frame information. For an introduction to using summary tables, see the [Viewing Heap Data Using Summary Tables](quick-start---viewing-heap-data-using-summary-tables.md) section of this document.

Using summary tables for process heap analysis, heap allocations can be identified by:

-   Process.

-   Thread.

-   Call stack.

-   Stack frame.

-   Allocation lifetime type relative to a selected time interval, such as Allocated Inside Freed Inside (AIFI). For more information, see [Quick Start - Viewing Heap Data Using Summary Tables](quick-start---viewing-heap-data-using-summary-tables.md).

-   Any column that appears in the summary table.

Summary tables display this information for every allocation that is active for at least part of the given time interval. Summary tables are opened from the graph context menu. Time intervals displayed for a summary table are consistent with the time intervals selected for the graph from which the summary table is opened.

> [!Note]  
> Heap analysis is most effective when stacks are collected capturing HeapAlloc and HeapRealloc events. In order for stacks to be decoded with symbols, the \_NT\_SYMBOL\_PATH environment variable must be set prior to starting XPerfview. For more information on setting this environment variable, please see the [Installation](installation.md) section of this document.

 

> [!Note]  
> The binaries to be used for the data collection must be compiled with Frame Pointer Omission optimization (FPO) disabled. Disabling FPO allows Windows Performance Analyzer to collect complete sets of call stack data.

 

 

 




