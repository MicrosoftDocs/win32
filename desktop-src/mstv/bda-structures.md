---
title: BDA Structures
description: BDA Structures
ms.assetid: 5ae43ac6-519d-486b-aaa5-c766f3194ef2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BDA Structures

The following table lists the structures defined for the Broadcast Driver Architecture (BDA) in DirectShow.



| Structure                                                       | Description                                                                                                                    |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**ATSC\_FILTER\_OPTIONS**](/windows/previous-versions/mpeg2structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0017?branch=master)            | Specifies additional criteria for matching ATSC section headers.                                                               |
| [**BDANODE\_DESCRIPTOR**](bdanode-descriptor.md)               | Describes a control node in BDA device filter.                                                                                 |
| [**DSMCC\_ELEMENT**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-_dsmcc_element?branch=master)                         | Contains information from a DSM-CC element.                                                                                    |
| [**DSMCC\_FILTER\_OPTIONS**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0016?branch=master)          | Specifies additional filtering criteria for the DSM-CC portions of the section header.                                         |
| [**DSMCC\_SECTION**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0011?branch=master)                         | Represents a DSM-CC section header.                                                                                            |
| [**DVB\_EIT\_FILTER\_OPTIONS**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0018?branch=master)     | Specifies a section within a Digital Video Broadcast (DVB) Event Information Table (EIT) section header. (Windows 7 and later) |
| [**DVR\_STREAM\_DESC**](/windows/previous-versions/sbe/ns-sbe-__midl___midl_itf_sbe_0000_0015_0002?branch=master)                    | Describes a stream captured by a tuner. (Windows 7 and later)                                                                  |
| [**EALocationCodeType**](/windows/previous-versions/bdaiface_enums/ns-bdaiface-ealocationcodetype?branch=master)                | Defines an Emergency Alert (EA) location code.                                                                                 |
| [**LONG\_SECTION**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0008?branch=master)                           | Represents a long MPEG-2 section header.                                                                                       |
| [**MPE\_ELEMENT**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-_mpe_element?branch=master)                             | Contains information from a multi-protocol encapsulation (MPE) element.                                                        |
| [**MPEG2\_FILTER**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0019?branch=master)                           | Specifies criteria for matching MPEG-2 section headers.                                                                        |
| [**MPEG2\_FILTER2**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0020?branch=master)                         | Specifies criteria for matching MPEG-2 section headers (Windows 7 and later).                                                  |
| [**MPEG\_BCS\_DEMUX**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0028?branch=master)                      | Identifies the filter graph that is providing the MPEG-2 data stream.                                                          |
| [**MPEG\_CONTEXT**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0030?branch=master)                           | Identifies the source of an MPEG-2 data stream.                                                                                |
| [**MPEG\_DATE**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0025?branch=master)                                 | Specifies a date.                                                                                                              |
| [**MPEG\_DATE\_AND\_TIME**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0026?branch=master)             | Specifies a date and time.                                                                                                     |
| [**MPEG\_DURATION**](mpeg-duration.md)                         | Identical to the [**MPEG\_TIME**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0024?branch=master) structure.                                                                    |
| [**MPEG\_HEADER\_BITS**](/windows/previous-versions/Mpeg2Bits/ns-mpeg2bits-mpeg_header_bits?branch=master)                  | Contains the first 16 bits that follow the table\_id in a generic MPEG-2 section header.                                       |
| [**MPEG\_HEADER\_VERSION\_BITS**](/windows/previous-versions/Mpeg2Bits/ns-mpeg2bits-mpeg_header_version_bits?branch=master) | Contains the first 8 bits following the TSID in an MPEG-2 PSI section.                                                         |
| [**MPEG\_PACKET\_LIST**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0015?branch=master)                  | Contains a list of MPEG-2 sections.                                                                                            |
| [**MPEG\_RQST\_PACKET**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0014?branch=master)                  | Defines a buffer to receive MPEG-2 section data.                                                                               |
| [**MPEG\_STREAM\_BUFFER**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0023?branch=master)              | Defines a buffer that receives MPEG-2 data.                                                                                    |
| [**MPEG\_TIME**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0024?branch=master)                                 | Represents a time of day.                                                                                                      |
| [**MPEG\_WINSOCK**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0029?branch=master)                           | Not supported.                                                                                                                 |
| [**SECTION**](/windows/previous-versions/Mpeg2Structs/ns-mpeg2structs-__midl___midl_itf_mpeg2structs_0000_0000_0006?branch=master)                                      | Represents a short header from an MPEG-2 section.                                                                              |
| [**SmartCardApplication**](/windows/previous-versions/bdaiface_enums/ns-bdaiface-smartcardapplication?branch=master)            | Identifies a smart card application.                                                                                           |



 

## Related topics

<dl> <dt>

[BDA Reference](bda-reference.md)
</dt> </dl>

 

 




