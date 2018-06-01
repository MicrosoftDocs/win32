---
title: BDA Structures
description: BDA Structures
ms.assetid: 5ae43ac6-519d-486b-aaa5-c766f3194ef2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BDA Structures

The following table lists the structures defined for the Broadcast Driver Architecture (BDA) in DirectShow.



| Structure                                                       | Description                                                                                                                    |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**ATSC\_FILTER\_OPTIONS**](/previous-versions/windows/desktop/api/mpeg2structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0017)            | Specifies additional criteria for matching ATSC section headers.                                                               |
| [**BDANODE\_DESCRIPTOR**](bdanode-descriptor.md)               | Describes a control node in BDA device filter.                                                                                 |
| [**DSMCC\_ELEMENT**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-_dsmcc_element)                         | Contains information from a DSM-CC element.                                                                                    |
| [**DSMCC\_FILTER\_OPTIONS**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0016)          | Specifies additional filtering criteria for the DSM-CC portions of the section header.                                         |
| [**DSMCC\_SECTION**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0011)                         | Represents a DSM-CC section header.                                                                                            |
| [**DVB\_EIT\_FILTER\_OPTIONS**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0018)     | Specifies a section within a Digital Video Broadcast (DVB) Event Information Table (EIT) section header. (Windows 7 and later) |
| [**DVR\_STREAM\_DESC**](/previous-versions/windows/desktop/api/sbe/ns-sbe-__midl___midl_itf_sbe_0000_0015_0002)                    | Describes a stream captured by a tuner. (Windows 7 and later)                                                                  |
| [**EALocationCodeType**](/previous-versions/windows/desktop/api/bdaiface_enums/ns-bdaiface-ealocationcodetype)                | Defines an Emergency Alert (EA) location code.                                                                                 |
| [**LONG\_SECTION**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0008)                           | Represents a long MPEG-2 section header.                                                                                       |
| [**MPE\_ELEMENT**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-_mpe_element)                             | Contains information from a multi-protocol encapsulation (MPE) element.                                                        |
| [**MPEG2\_FILTER**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0019)                           | Specifies criteria for matching MPEG-2 section headers.                                                                        |
| [**MPEG2\_FILTER2**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0020)                         | Specifies criteria for matching MPEG-2 section headers (Windows 7 and later).                                                  |
| [**MPEG\_BCS\_DEMUX**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0028)                      | Identifies the filter graph that is providing the MPEG-2 data stream.                                                          |
| [**MPEG\_CONTEXT**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0030)                           | Identifies the source of an MPEG-2 data stream.                                                                                |
| [**MPEG\_DATE**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0025)                                 | Specifies a date.                                                                                                              |
| [**MPEG\_DATE\_AND\_TIME**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0026)             | Specifies a date and time.                                                                                                     |
| [**MPEG\_DURATION**](https://www.bing.com/search?q=**MPEG\_DURATION**)                         | Identical to the [**MPEG\_TIME**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0024) structure.                                                                    |
| [**MPEG\_HEADER\_BITS**](/previous-versions/windows/desktop/api/Mpeg2Bits/ns-mpeg2bits-mpeg_header_bits)                  | Contains the first 16 bits that follow the table\_id in a generic MPEG-2 section header.                                       |
| [**MPEG\_HEADER\_VERSION\_BITS**](/previous-versions/windows/desktop/api/Mpeg2Bits/ns-mpeg2bits-mpeg_header_version_bits) | Contains the first 8 bits following the TSID in an MPEG-2 PSI section.                                                         |
| [**MPEG\_PACKET\_LIST**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0015)                  | Contains a list of MPEG-2 sections.                                                                                            |
| [**MPEG\_RQST\_PACKET**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0014)                  | Defines a buffer to receive MPEG-2 section data.                                                                               |
| [**MPEG\_STREAM\_BUFFER**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0023)              | Defines a buffer that receives MPEG-2 data.                                                                                    |
| [**MPEG\_TIME**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0024)                                 | Represents a time of day.                                                                                                      |
| [**MPEG\_WINSOCK**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0029)                           | Not supported.                                                                                                                 |
| [**SECTION**](/previous-versions/windows/desktop/api/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0006)                                      | Represents a short header from an MPEG-2 section.                                                                              |
| [**SmartCardApplication**](/previous-versions/windows/desktop/api/bdaiface_enums/ns-bdaiface-smartcardapplication)            | Identifies a smart card application.                                                                                           |



 

## Related topics

<dl> <dt>

[BDA Reference](bda-reference.md)
</dt> </dl>

 

 




