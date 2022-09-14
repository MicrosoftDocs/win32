---
title: Network Tracing in Windows 7
description: Windows 7 expands on the Network Diagnostic Framework (NDF) to provide a quick method for troubleshooting network connectivity issues by enabling collection of all the needed information in one step, and by leveraging Event Tracing for Windows (ETW) to log network events packets in a single file.
ms.assetid: 7d331362-ff26-4ca0-aa45-07cc97304c7c
ms.topic: article
ms.date: 05/31/2018
---

# Network Tracing in Windows 7

As the complexity of the networking stack increases, it is often difficult to quickly trace and diagnose issues within the stack. Windows 7 expands on the Network Diagnostic Framework (NDF) to provide a quick method for troubleshooting network connectivity issues by enabling collection of all the needed information in one step, and by leveraging [Event Tracing for Windows (ETW)](../etw/event-tracing-portal.md) to log network events & packets in a single file.

Related events and packets are grouped together for a given activity, such as browsing a website, across the various components in the networking stack. The output of this process is an Event Trace Log (ETL) file. By allowing all of the events related to a specific activity to be viewed at once in this file, the time required to isolate and diagnose network issues can be greatly reduced.

## In This Section



| Topic                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------|
| [Network Tracing in Windows 7: Architecture](network-tracing-in-windows-7-architecture.md)                                |
| [Tools for Troubleshooting using Network Tracing in Windows 7](tools-for-troubleshooting-network-tracing-in-windows-7.md) |
| [Network Tracing in Windows 7: Scenarios](network-tracing-in-windows-7-scenarios.md)                                      |



 

 

 