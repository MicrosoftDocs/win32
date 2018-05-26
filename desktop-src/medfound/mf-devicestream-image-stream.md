---
Description: Specifies whether a stream on a video capture source is a still-image stream.
ms.assetid: 52251A45-3603-41C7-A869-7F6319BD337F
title: MF\_DEVICESTREAM\_IMAGE\_STREAM attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_DEVICESTREAM\_IMAGE\_STREAM attribute

Specifies whether a stream on a video capture source is a still-image stream.

## Data type

**BOOL** stored as **UINT32**

## Remarks

Some video cameras expose a still-image stream that produces high-resolution images. The image stream might produce uncompressed images or JPEG images. If the camera has an image stream, the media source for the capture device sets this attribute to **TRUE** on the image stream.

To get this attribute, do the following:

1.  Query the media source for the [**IMFMediaSourceEx**](/windows/win32/mfidl/nn-mfidl-imfmediasourceex?branch=master) interface.
2.  Call [**IMFMediaSourceEx::GetStreamAttributes**](/windows/win32/mfidl/nf-mfidl-imfmediasourceex-getstreamattributes?branch=master) to get an [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) pointer for the stream.
3.  Call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master) to get the attribute.

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

 

 




