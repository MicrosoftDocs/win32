---
description: Tells the MPEG-4 MediaSink how much space to reserve in the MP4 file format header for metadata properties.
title: MF_MPEG4SINK_MINIMUM_PROPERTIES_SIZE attribute (Mfidl.h)
ms.topic: reference
ms.date: 10/31/2025
---

# MF\_MPEG4SINK\_MINIMUM\_PROPERTIES\_SIZE attribute

Tells the MPEG-4 MediaSink how much space to reserve in the MP4 file format header for metadata properties.

## Data type

**UINT32**

## Remarks

The default behavior of the MPEG-4 media sink is to only use exactly the amount of storage required to hold only the current metadata properties in the MP4 file header plus required padding. When this attribute is specified, the media sink reserves the specified amount of storage (in bytes) for properties. If the properties are updated later, or if new properties are added, the media sink will attempt to update the file in-place by writing the properties into the previously reserved space.


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 version 1709                                |
| Minimum supported server | Windows Server version 1709                        |
| Header               | Mfidl.h |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




