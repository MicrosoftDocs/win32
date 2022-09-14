---
description: Disables the use of post-processing camera plug-ins by the Source Reader.
ms.assetid: 837A6BA8-9C79-4B0A-B40D-C094009BFF2C
title: MF_SOURCE_READER_DISABLE_CAMERA_PLUGINS attribute (Mfreadwrite.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SOURCE\_READER\_DISABLE\_CAMERA\_PLUGINS attribute

Disables the use of post-processing camera plug-ins by the [Source Reader](source-reader.md).

## Data type

**BOOL** stored as **UINT32**

## Remarks

This attribute applies when the Source Reader is used with a video capture source. If this attribute is **TRUE**, it prevents the Source Reader from loading any post-processing plug-ins that the camera might provide. Otherwise, by default the Source Reader will load them.

The default value of this attribute is **FALSE**. Set the attribute when you create the source reader.

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

[Source Reader Attributes](source-reader-attributes.md)
</dt> </dl>

 

 




