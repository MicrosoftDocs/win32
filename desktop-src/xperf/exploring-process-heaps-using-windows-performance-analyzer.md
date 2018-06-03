---
title: Exploring Process Heaps Using Windows Performance Analyzer
description: Exploring Process Heaps Using Windows Performance Analyzer
ms.assetid: 55d2f0dd-3fec-4135-8ec4-0f0e1f21946c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Exploring Process Heaps Using Windows Performance Analyzer

Prior to the introduction of Windows Performance Analyzer (WPA), the analysis of process specific heap allocation and heap usage patterns was challenging. Custom instrumentations were needed to identify heap allocation and de-allocation instructions. These instrumentations often introduced tracing mechanisms that skewed the data collected for analysis.

The WPA Heap Analysis tool provides a comprehensive view of process heap behavior by producing graphs, summary tables and text based reports. WPA is based on Event Tracing for Windows (ETW). ETW is an Application Programming Interface that provides a mechanism to trace and log user and kernel mode events in a non-intrusive manner. No code changes are required to investigate problematic scenarios and to incorporate heap data collection into a test matrix. For more information on ETW please see the [Event Tracing for Windows](event-tracing-for-windows.md) section of this document.

This section includes the following topics:

<dl>

[Heap Analysis Quick Start](heap-analysis-quick-start.md)  
[Collecting Process Heap Data](collecting-process-heap-data.md)  
[Analyzing Process Heap Data](analyzing-process-heap-data.md)  
[Windows 7 Advanced Heap Data Collection](windows-7-advanced-heap-data-collection.md)  
[Advanced Topics and Appendix](advanced-topics-and-appendix.md)  
</dl>

 

 




