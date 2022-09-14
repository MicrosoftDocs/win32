---
description: Enables the Source Reader to use Media Foundation transforms (MFTs) that are optimized for transcoding.
ms.assetid: 9463EB8C-2CA3-4F8F-8A2A-B1292879DD1B
title: MF_SOURCE_READER_ENABLE_TRANSCODE_ONLY_TRANSFORMS attribute (Mfreadwrite.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SOURCE\_READER\_ENABLE\_TRANSCODE\_ONLY\_TRANSFORMS attribute

Enables the [Source Reader](source-reader.md) to use Media Foundation transforms (MFTs) that are optimized for transcoding.

## Data type

**UINT32**

Treat as Boolean.

## Remarks

Some MFTs, particularly decoders, are optimized for transcoding rather than playback. By default, the Source Reader will not load such transforms. Set this attribute to **TRUE** if you want to use transcoding MFTs with the Source Reader.

An application might set this attribute if it does not process the data in real time (for transcoding or similar scenarios). Otherwise, for real-time playback, use the default behavior.

Internally, this attribute causes the Source Reader to include the **MFT\_ENUM\_FLAG\_TRANSCODE\_ONLY** flag when it calls [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Source Reader](source-reader.md)
</dt> </dl>

 

 




