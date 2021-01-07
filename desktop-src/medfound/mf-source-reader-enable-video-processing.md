---
description: Enables video processing by the Source Reader.
ms.assetid: b1ec1c0e-8042-4486-822f-eb106577c0b1
title: MF_SOURCE_READER_ENABLE_VIDEO_PROCESSING attribute (Mfreadwrite.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SOURCE\_READER\_ENABLE\_VIDEO\_PROCESSING attribute

Enables video processing by the [Source Reader](source-reader.md).

## Data type

**UINT32**



| Value                                                                                                                                                                | Meaning                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <span id="Nonzero"></span><span id="nonzero"></span><span id="NONZERO"></span><dl> <dt>**Nonzero**</dt> </dl> | Enable video processing.<br/>            |
| <span id="Zero"></span><span id="zero"></span><span id="ZERO"></span><dl> <dt>**Zero**</dt> </dl>             | Disable video processing. (Default)<br/> |



 

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

If this attribute is **TRUE** (nonzero), the source reader can perform the following limited video processing on uncompressed video frames:

-   Conversion from YUV to RGB-32.
-   Deinterlacing.

These operations are performed in software, and are not optimized for playback. This feature is intended for applications that process a small number of frames—for example, to create a video thumbnail—or applications that do not decode frames in real time. The deinterlace operation interpolates data from a single field, so it is lossy.

Avoid this setting if you are using Direct3D to display the video frames, because the GPU generally provides better video processing capabilities.

If this attribute is **TRUE**, the following attributes must be **FALSE**:

-   [MF\_SOURCE\_READER\_D3D\_MANAGER](mf-source-reader-d3d-manager.md)
-   [MF\_READWRITE\_DISABLE\_CONVERTERS](mf-readwrite-disable-converters.md)

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Source Reader](source-reader.md)
</dt> <dt>

[Source Reader Attributes](source-reader-attributes.md)
</dt> </dl>

 

 




