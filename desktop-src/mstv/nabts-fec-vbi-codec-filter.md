---
title: NABTS/FEC VBI Codec Filter
description: NABTS/FEC VBI Codec Filter
ms.assetid: '34b57979-3aa6-42de-9ea0-8948e0947fe8'
---

# NABTS/FEC VBI Codec Filter

This component has been removed from Windows Vista and later operating systems. It is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems.

The NABTS/FEC VBI codec decodes NABTS (North American Broadcast Teletext Specification) teletext from data in the vertical blanking interval (VBI). It also accepts hardware-decoded NABTS data. The codec delivers forward-error-corrected (FEC) SLIP packets.

Connect this filter to the [BDA SLIP Deframer](bda-slip-deframer-filter.md) filter, and connect the BDA SLIP deframer to the [BDA IP Sink](bda-ip-sink-filter.md) filter. The BDA IP Sink filter delivers IP data to Winsock.

The NABTS/FEC VBI codec has two input pins:

-   The VBI pin accepts raw VBI data
-   The HWNABTS pin accepts hardward-decoded NABTS data. The filter simply passes the data to the BDA SLIP Deframer.

There are no application-callable interfaces on this filter.

This filter appears in the "WDM Streaming VBI Codecs" filter category (AM\_KSCATEGORY\_VBICODEC). Because this is a kernel-mode filter, applications cannot create it directly using **CoCreateInstance**. Instead, use the [System Device Enumerator](https://msdn.microsoft.com/library/windows/desktop/dd407180). For more information, see [Creating Kernel-Mode Filters](https://msdn.microsoft.com/library/windows/desktop/dd375135).

## Related topics

<dl> <dt>

[BDA Filters](bda-filters.md)
</dt> <dt>

[Microsoft TV Technologies](microsoft-tv-technologies-portal.md)
</dt> </dl>

 

 




