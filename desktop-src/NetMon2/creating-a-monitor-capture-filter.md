---
description: Creating a capture filter that works with Network Monitor is a five-step process.
ms.assetid: 04be791c-43c5-44c2-8ab0-799a99974bf6
title: Creating a Monitor Capture Filter
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Monitor Capture Filter

Creating a capture filter that works with Network Monitor is a five-step process:

-   [Setting the Etype or SAP Filter](writing-etypesap-filter-portion.md)
-   [Writing ADDRESSTABLE Filter](writing-addresstable-filter-portion.md)
-   [Writing the PATTERNMATCH Filter](writing-the-patternmatch-filter.md)
-   [Clipping a Frame](clipping-a-frame.md)
-   [Implementing the Capture Filter Code](implementing-the-capture-filter-code.md)

A [*capture filter*](c.md) is a series of additions to the NPP BLOB that selects which frames are passed back to the monitor. If a monitor does not alter the NPP BLOB, then the NPP will go into promiscuous mode and send all network traffic to the monitor. The NPP is most efficient if it can reduce the data handed up to a driver, so a monitor should create a capture filter. A monitor sets its capture filter by writing to the NPP BLOB in the call to the [DoConfigure](imonitor-doconfigure.md) function. The MCSVC then calls the NPP with the NPP BLOB. See [Capture Filters](capture-filters.md) for more details on the capture filter, [Network Packet Providers](network-packet-providers.md) on NPPs, and [Network Monitor Blobs](network-monitor-blobs.md) on BLOB functions.

 

 



