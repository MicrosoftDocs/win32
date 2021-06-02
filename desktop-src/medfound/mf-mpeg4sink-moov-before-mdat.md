---
description: Indicates that moov will be written before mdat box in the generated file.
ms.assetid: 97B68B0A-8266-4FCF-8CD9-35890E1AC774
title: MF_MPEG4SINK_MOOV_BEFORE_MDAT attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MPEG4SINK\_MOOV\_BEFORE\_MDAT attribute

Indicates that 'moov' will be written before 'mdat' box in the generated file.

## Data type

**UINT32**

## Remarks

The default behavior of the mpeg4 media sink is to write 'moov' after 'mdat' box. Setting this attribute causes the generated file to write 'moov' before 'mdat' box.

In order for the mpeg4 sink to use this attribute, the byte stream passed in must not be slow seek or remote for .

This feature involves an additional file copying/remuxing.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




