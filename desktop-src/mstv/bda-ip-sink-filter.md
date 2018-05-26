---
title: BDA IP Sink Filter
description: BDA IP Sink Filter
ms.assetid: 78cd6cba-3bd7-4ad4-b65d-c6b866a18d4e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BDA IP Sink Filter

> [!Note]  
> This component has been removed from Windows Vista and later operating systems. It is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems.

 

The BDA IP Sink filter is a kernel-mode filter that delivers IP data to Winsock. This filter can be used in television filter graphs, both analog and digital, and BDA or non-BDA.

In an analog graph, the input pin connects to the [BDA SLIP Deframer](bda-slip-deframer-filter.md). In a digital graph, the input pin connects to the [BDA MPE Filter](bda-mpe-filter.md). The filter has an output pin, but it does not send any IP data through this pin; all IP data goes to Winsock.

The filter exposes the [**IBDA\_IPSinkInfo**](/windows/win32/bdaiface/nn-bdaiface-ibda_ipsinkinfo?branch=master) interface.

BDA IP Sink appears in GraphEdit under the "BDA Rendering Filters" category. Because this is a kernel-mode filter, applications cannot create it directly. Instead, use the [System Device Enumerator](https://msdn.microsoft.com/library/windows/desktop/dd407180), as described in [Enumerating Devices and Filters](https://msdn.microsoft.com/library/windows/desktop/dd375615). Add the filter to the filter graph by calling the [**IFilterGraph::AddFilter**](https://msdn.microsoft.com/library/windows/desktop/dd390016) method.

This filter poses a security risk on systems which have source routing enabled because it could allow a malicious broadcast stream to mount a denial of service attack by flooding a network with a large amount of IP data packets. For this reason, if source routing is enabled at any time on the host system, the BDA IP Sink filter will be automatically disabled. It will continue to exist in the graph, and it will be able to transition into the run state, but it will drop all packets without sending them to the NDIS stack. If source routing is then disabled, data indication to NDIS resumes after a brief lapse of time. The filter monitors the state of source routing by periodically examining the registry key HKLM\\System\\CurrentControlSet\\Services\\Tcpip\\Parameters\\IPEnableRouter. If you require the BDA IP Sink filter to be enabled while source routing is enabled, please contact Microsoft Product Support Services to obtain special instructions.

## Related topics

<dl> <dt>

[BDA Filters](bda-filters.md)
</dt> <dt>

[Microsoft TV Technologies](microsoft-tv-technologies-portal.md)
</dt> </dl>

 

 




