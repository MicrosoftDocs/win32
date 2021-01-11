---
description: For a media type that describes an MPEG-2 transport stream (TS), specifies the transport packets contain a 4-byte time code.
ms.assetid: B172E7A8-5757-49B7-A784-FAFC7E904A4C
title: MF_MT_MPEG2_TIMECODE attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_MPEG2\_TIMECODE attribute

For a media type that describes an MPEG-2 transport stream (TS), specifies the transport packets contain a 4-byte time code.

## Data type

**UINT32**



| Value                                                                                                | Meaning                                                                                                                                        |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | No time code is added.<br/>                                                                                                              |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | A 4-byte time code is added at the start of each transport packet. This time code is required by some digital television standards.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




