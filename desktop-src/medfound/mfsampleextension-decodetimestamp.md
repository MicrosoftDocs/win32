---
description: Contains the decode time stamp (DTS) for the sample.
ms.assetid: 4E0B8266-FF48-49A1-AB7B-A47C4F96AECD
title: MFSampleExtension_DecodeTimestamp attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_DecodeTimestamp attribute

Contains the decode time stamp (DTS) for the sample.

## Data type

**UINT64**

## Remarks

The value of the attribute is the DTS in 100-nanosecond units. The DTS is defined in some encoding standards, including MPEG. The DTS specifies when the encoded picture should be decoded. If the encoded video contains B frames, the DTS can differ from the presentation time, because B pictures appear out of temporal order in the bitstream.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> </dl>

 

 




