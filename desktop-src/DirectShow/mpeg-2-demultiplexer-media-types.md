---
description: MPEG-2 Demultiplexer Media Types
ms.assetid: 240d1753-df8c-45fe-b5a7-9faa96fc5b18
title: MPEG-2 Demultiplexer Media Types
ms.topic: article
ms.date: 05/31/2018
---

# MPEG-2 Demultiplexer Media Types

The [MPEG-2 Demultiplexer](mpeg-2-demultiplexer.md) filter recognizes the following media types.

### Input Types

The major type is always **MEDIATYPE\_Stream**. The subtype can be any of the following.



| GUID                                             | Description                                                                                                                                                                                               |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KSDATAFORMAT\_SUBTYPE\_BDA\_MPEG2\_TRANSPORT** | Transport stream from a Broadcast Driver Architecture (BDA) device filter. The MPEG-2 demultiplexer treats this subtype identically to **MEDIASUBTYPE\_MPEG2\_TRANSPORT**.                                |
| **MEDIASUBTYPE\_MPEG2\_PROGRAM**                 | Program stream                                                                                                                                                                                            |
| **MEDIASUBTYPE\_MPEG2\_TRANSPORT**               | Transport stream (TS), with 188-byte packets                                                                                                                                                              |
| **MEDIASUBTYPE\_MPEG2\_TRANSPORT\_STRIDE**       | Transport stream with "strided" packets. This subtype indicates that the TS packets may be padded with extra bytes. For more information, see [**MPEG2\_TRANSPORT\_STRIDE**](mpeg2-transport-stride.md). |



 

For strided transport packets (**MEDIASUBTYPE\_MPEG2\_TRANSPORT\_STRIDE**), each media sample must contain an integral number of transport packets, as described in [**MPEG2\_TRANSPORT\_STRIDE**](mpeg2-transport-stride.md). For all other input types, there are no restrictions on sample boundaries; individual packets can span sample boundaries.

### Output Types

The MPEG-2 Demultiplexer does not validate output types; the downstream filter is responsible for parsing the data it receives from the demultiplexer. However, the following types are commonly accepted by downstream filters as output from the demultiplexer.

### MPEG-2 Sections




| 
|
| Major Type | <strong>MEDIATYPE_MPEG2_SECTIONS</strong> | 
| Subtype | Any of the following:<br /><ul><li><strong>MEDIASUBTYPE_ATSC_SI</strong>: ATSC Service Information.</li><li><strong>MEDIASUBTYPE_DVB_SI</strong>: DVB Service Information.</li><li><strong>MEDIASUBTYPE_ISDB_SI</strong>: Integrated Services Digital Broadcasting (ISDB) Service Information.</li><li><strong>MEDIASUBTYPE_MPEG2DATA</strong>: MPEG-2 section data.</li></ul> | 
| Format Type | None | 




 

### MPEG-2 Video



| Label | Value |
|------------------|------------------------------------------|
| Major type       | **MEDIATYPE\_Video**                     |
| Subtype          | **MEDIASUBTYPE\_MPEG2\_VIDEO**           |
| Format Type      | **FORMAT\_MPEG2Video**                   |
| Format Structure | [**MPEG2VIDEOINFO**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-mpeg2videoinfo) |



 

### MPEG-2 Audio



| Label | Value |
|------------------|--------------------------------------|
| Major type       | **MEDIATYPE\_Audio**                 |
| Subtype          | **MEDIASUBTYPE\_MPEG2\_AUDIO**       |
| Format Type      | **FORMAT\_WaveFormatEx**             |
| Format Structure | [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) |



 

## Related topics

<dl> <dt>

[MPEG-2 Media Types](mpeg-2-media-types.md)
</dt> </dl>

 

 
