---
description: Indicates whether a video frame is interlaced or progressive.
ms.assetid: 3cb80e75-e803-493b-a22d-e485e77b5177
title: MFSampleExtension_Interlaced attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_Interlaced attribute

Indicates whether a video frame is interlaced or progressive. If **TRUE**, the frame is interlaced. If **FALSE**, the frame is progressive. If not set, the media type describes the interlacing. This attribute applies to media samples.

## Data type

**BOOL** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)

## Remarks

For video content that contains mixed progressive and interlaced frames, set the media type to interlaced and use this attribute on each frame to indicate whether the frame is progressive or interlaced.

For video content that is entirely interlaced, set the media type to interlaced and omit this attribute, or set it to **TRUE** on every sample.

For video content that is entirely progressive, set the media type to progressive and omit this attribute, or set it to **FALSE** on every sample.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> <dt>

[Video Interlacing](video-interlacing.md)
</dt> </dl>

 

 




