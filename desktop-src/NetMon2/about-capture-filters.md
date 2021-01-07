---
description: A capture filter is an element of an NPP application that instructs the Network Monitor driver (Nmnt.sys) which frames of network data to retain and which frames to ignore.
ms.assetid: 6ab17e18-bd97-42a8-b569-b205ac19ffd1
title: About Capture Filters
ms.topic: article
ms.date: 05/31/2018
---

# About Capture Filters

A capture filter is an element of an NPP application that instructs the Network Monitor driver (Nmnt.sys) which frames of network data to retain and which frames to ignore. The advantage of setting a capture filter is greater efficiency. You do not have to examine captured frames; the Network Monitor driver examines them. This approach eliminates frame copying, which provides a memory use advantage.

## Capture Filter Structure

Capture filters consist of three elements:

-   Etype/SAP settings
-   Address
-   Pattern match

Together, these elements logically evaluate which frames to include, or exclude, during the operation of an NPP application. The capture filter supplies complex matches and exclusions of frame elements to the NPP application.

Network Monitor implements the capture filter through a data structure, [**CAPTUREFILTER**](the-capturefilter-structure.md), passed to the NPP and then passed on to the Network Monitor driver when the capture starts.

For more information about NPP operations and BLOB functionality, see [Network Packet Providers](network-packet-providers.md) and [Network Monitor BLOBS](network-monitor-blobs.md).

 

 



