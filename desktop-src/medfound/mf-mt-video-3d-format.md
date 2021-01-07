---
description: For a video media type, specifies how 3D video frames are stored in memory.
ms.assetid: 880DF017-5841-4C0A-82AF-F092DEF5406B
title: MF_MT_VIDEO_3D_FORMAT attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_VIDEO\_3D\_FORMAT attribute

For a video media type, specifies how 3D video frames are stored in memory.

## Data type

**MFVideo3DFormat** stored as **UINT32**

## Remarks

The value of this attribute is a member of the [**MFVideo3DFormat**](/windows/desktop/api/mfapi/ne-mfapi-mfvideo3dformat) enumeration. The attribute applies only if the [MF\_MT\_VIDEO\_3D](mf-mt-video-3d.md) attribute is **TRUE**.

This attribute is required for uncompressed 3D video formats. It is optional for compressed 3D video. A media source that delivers encoded frames might be able to set the attribute, based on information in the file container. Otherwise, the attribute should be set by the decoder in the decoder's output media type.

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

 

 




