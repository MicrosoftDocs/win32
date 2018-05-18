---
Description: 'Specifies whether the image stream on a video capture source is independent of the video stream.'
ms.assetid: 'DC4ED612-593B-40BF-BB42-946149042D1F'
title: 'MF\_DEVICESTREAM\_INDEPENDENT\_IMAGE\_STREAM attribute'
---

# MF\_DEVICESTREAM\_INDEPENDENT\_IMAGE\_STREAM attribute

Specifies whether the image stream on a video capture source is independent of the video stream.

## Data type

**BOOL** stored as **UINT32**

## Remarks

Some USB video cameras expose a stream that produces still images. In some cameras, the image stream simply returns the next frame from the video stream. In other cameras, the image stream functions independently of the video stream. If the camera has an independent image stream, the media source for the capture device sets this attribute to **TRUE** on the image stream.

To get this attribute, do the following:

1.  Query the media source for the [**IMFMediaSourceEx**](imfmediasourceex.md) interface.
2.  Call [**IMFMediaSourceEx::GetStreamAttributes**](imfmediasourceex-getstreamattributes.md) to get an [**IMFAttributes**](imfattributes.md) pointer for the stream.
3.  Call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md) to get the attribute.

This attribute applies only when the [MF\_DEVICESTREAM\_IMAGE\_STREAM](mf-devicestream-image-stream.md) attribute is **TRUE**.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




