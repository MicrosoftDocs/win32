---
Description: Specifies the kernel streaming (KS) identifier for a stream on a video capture device.
ms.assetid: 03C48CBA-FAD0-4127-89E5-3F1874BF32DB
title: MF\_DEVICESTREAM\_STREAM\_ID attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_DEVICESTREAM\_STREAM\_ID attribute

Specifies the kernel streaming (KS) identifier for a stream on a video capture device.

## Data type

**UINT32**

## Remarks

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

 

 




