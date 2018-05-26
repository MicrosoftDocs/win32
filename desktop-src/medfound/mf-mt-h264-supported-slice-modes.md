---
Description: Specifies the supported slice modes for an H.264 video stream.
ms.assetid: 72DA62EC-A509-4C3B-A51D-7313C176AAA9
title: MF\_MT\_H264\_SUPPORTED\_SLICE\_MODES attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_H264\_SUPPORTED\_SLICE\_MODES attribute

Specifies the supported slice modes for an H.264 video stream.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Applies to

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)

## Remarks

This attribute applies to media types for H.264 streams transmitted over USB. The value corresponds to the **bmSupportedSliceModes** field in the UVC 1.5 H.264 video format descriptor.

This attribute is also used with [H.264 UVC 1.5 camera encoders](camera-encoder-h264-uvc-1-5.md).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




