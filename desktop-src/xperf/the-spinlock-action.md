---
title: The Spinlock Action
description: The Spinlock Action
ms.assetid: '2da4ac63-62e4-4b37-9b64-5b97016dfc2e'
---

# The Spinlock Action

The spinlock action produces a text file listing information relevant to spinlock activity. The usage for this action is:


```
-a spinlock [-summary] [-counts [n] ] 
```





| Option                 | Description                                                                       |
|------------------------|-----------------------------------------------------------------------------------|
| summary<br/>     | Summarize the Spin Lock event information into a tab delimited format.<br/> |
| count \[n\]<br/> | Maximum number of files to show<br/>                                        |



 

### Target Platforms

Windows Performance Analyzer (WPA) Spin Lock analysis is available for x64 architectures. Spin Lock instrumentation is supported on Windows 7 and Windows Server 2008 R2.

### Introduction

WPA for Windows 7 and Windows Server 2008 R2 includes the ability to capture spinlock events on x64 architectures. WPA Spin Lock analysis supports Normal Spin Locks and Queued Spin Locks. For more information on Spin Locks, please see the [Spin Locks](http://go.microsoft.com/fwlink/p/?linkid=166443) section on MSDN.

WPA Spin Lock Analysis is based on the [Event Tracing for Windows](event-tracing-for-windows.md) (ETW) event architecture. To reduce overhead, ETW Spin Lock instrumentation is sample based. The sampling frequency can be tuned through WPA command line options. For more information on configuring WPA for Spin Lock event collection, please see the [Collecting Spin Lock Data](collecting-spin-lock-data.md) section of this document.

This section includes the following topics:

<dl>

[Preparing the Spin Lock Event Collection Environment](preparing-the-spin-lock-event-collection-environment.md)  
[Collecting Spin Lock Data](collecting-spin-lock-data.md)  
[Evaluating Spin Lock Data](evaluating-spin-lock-data.md)  
</dl>

 

 





