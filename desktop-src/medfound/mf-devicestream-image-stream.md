---
description: Specifies whether a stream on a video capture source is a still-image stream.
ms.assetid: 52251A45-3603-41C7-A869-7F6319BD337F
title: MF_DEVICESTREAM_IMAGE_STREAM attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_DEVICESTREAM\_IMAGE\_STREAM attribute

Specifies whether a stream on a video capture source is a still-image stream.

## Data type

**BOOL** stored as **UINT32**

## Remarks

Some video cameras expose a still-image stream that produces high-resolution images. The image stream might produce uncompressed images or JPEG images. If the camera has an image stream, the media source for the capture device sets this attribute to **TRUE** on the image stream.

To get this attribute, do the following:

1.  Query the media source for the [**IMFMediaSourceEx**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasourceex) interface.
2.  Call [**IMFMediaSourceEx::GetStreamAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasourceex-getstreamattributes) to get an [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) pointer for the stream.
3.  Call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32) to get the attribute.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




