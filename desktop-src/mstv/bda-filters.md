---
title: BDA Filters
description: BDA Filters
ms.assetid: 07830ccf-f940-4b7f-a679-93212b47dbf0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BDA Filters

The following table lists the DirectShow filters that are used in the Broadcast Driver Architecture (BDA).



| Filter                                                                                 | Description                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BDA IP Sink](bda-ip-sink-filter.md)                                                  | Delivers IP data to Winsock in BDA as well as non-BDA filter graphs.                                                                                                                                   |
| [BDA MPE Filter](bda-mpe-filter.md)                                                   | Extracts the IP packets from the MPE frames and delivers them to BDA IP Sink and ultimately on to Winsock.                                                                                             |
| [BDA MPEG-2 Transport Information Filter](bda-mpeg-2-transport-information-filter.md) | Parses MPEG-2 DVB and ATSC tables and provides the information to the Network Provider.                                                                                                                |
| [BDA Network Provider](bda-network-provider-filter.md)                                | Source filter in all BDA filter graphs.                                                                                                                                                                |
| [BDA SLIP Deframer](bda-slip-deframer-filter.md)                                      | Used in either BDA or non-BDA analog television graphs where SLIP de-framing of IP data is required.                                                                                                   |
| [MPEG-2 Sections and Tables](mpeg-2-sections-and-tables-filter.md)                    | Receives PSI tables from an MPEG-2 transport stream.                                                                                                                                                   |
| [NABTS/FEC VBI Codec Filter](nabts-fec-vbi-codec-filter.md)                           | Processes captured VBI lines and distributes decoded and/or forward-error-corrected SLIP packets containing NABTS data downstream to the BDA SLIP Deframer, the BDA IP Sink and ultimately to Winsock. |
| [VBICodec Filter](vbicodec-filter.md)                                                 | Slices raw digitized data from the vertical blanking interval (VBI).                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Microsoft TV Technologies](microsoft-tv-technologies-portal.md)
</dt> </dl>

 

 




