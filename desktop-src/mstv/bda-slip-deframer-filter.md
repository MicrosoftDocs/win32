---
title: BDA SLIP Deframer Filter
description: BDA SLIP Deframer Filter
ms.assetid: 21a64adf-ff3d-4dc1-80d4-875e10acd7e6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BDA SLIP Deframer Filter

This component has been removed from Windows Vista and later operating systems. It is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems.

The BDA SLIP Deframer is a kernel-mode filter that can be used in either BDA or non-BDA analog television graphs where SLIP de-framing of IP data (such as that found on the NABTS VBI scan lines) is required. It connects upstream to the [NABTS/FEC VBI Codec](nabts-fec-vbi-codec-filter.md) and downstream to [BDA IP Sink](bda-ip-sink-filter.md), which makes the IP packets available to interested applications via Winsock. There are no application-callable interfaces on the BDA SLIP Deframer. In digital television graphs, the [BDA MPE Filter](bda-mpe-filter.md) is used to extract the IP packets from the data stream.

The SLIP Deframer can process compressed IP headers. With IP header compression, the sender removes redundant header information from successive IP packets and replaces it with a shorter token. Typically, the sender compresses three out of four packets on each IP address. If the receiver starts in the middle of a cycle, the filter may be unable to decode the first few packets, until it receives the full header. The sender should send data redundantly, or else avoid using IP header compression.

The BDA SLIP Deframer appears in GraphEdit under the "BDA Receiver Component" category. Because this is a kernel-mode filter, applications cannot co-create it directly, but must use the [System Device Enumerator](https://msdn.microsoft.com/library/windows/desktop/dd407180) to instantiate it, as described in [Enumerating Devices and Filters](https://msdn.microsoft.com/library/windows/desktop/dd375615). This filter must be added to the graph manually using the [**IFilterGraph::AddFilter**](https://msdn.microsoft.com/library/windows/desktop/dd390016) method; the Capture Graph Builder cannot be used to add this filter to the graph.

This filter does not expose any application-callable interfaces.

## Related topics

<dl> <dt>

[BDA Filters](bda-filters.md)
</dt> <dt>

[Microsoft TV Technologies](microsoft-tv-technologies-portal.md)
</dt> </dl>

 

 




