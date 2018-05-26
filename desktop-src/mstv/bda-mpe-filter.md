---
title: BDA MPE Filter
description: BDA MPE Filter
ms.assetid: 156fd52e-f366-48b1-a431-4a4abdbb1b16
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BDA MPE Filter

Multi-Protocol Encapsulation (MPE) is the protocol by which IP data is transmitted over digital television networks. The BDA MPE Filter is a kernel-mode filter that extracts the IP packets from the MPE frames and delivers them to [BDA IP Sink](bda-ip-sink-filter.md) and ultimately on to Winsock, where interested applications can listen for and process the data. The [BDA SLIP Deframer](bda-slip-deframer-filter.md) performs the same function on analog television graphs, where the SLIP framing protocol is used.

The BDA MPE Filter appears in GraphEdit under the "BDA Receiver Component" category. Because this is a kernel-mode filter, applications cannot co-create it directly, but must use the [System Device Enumerator](https://msdn.microsoft.com/library/windows/desktop/dd407180) to instantiate it, as described in [Enumerating Devices and Filters](https://msdn.microsoft.com/library/windows/desktop/dd375615). This filter must be added to the graph manually using the [**IFilterGraph::AddFilter**](https://msdn.microsoft.com/library/windows/desktop/dd390016) method; the [Capture Graph Builder](https://msdn.microsoft.com/library/windows/desktop/dd318619) will not add the filter automatically.

## Related topics

<dl> <dt>

[BDA Filters](bda-filters.md)
</dt> <dt>

[Microsoft TV Technologies](microsoft-tv-technologies-portal.md)
</dt> </dl>

 

 




