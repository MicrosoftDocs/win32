---
description: Specifies the kernel streaming (KS) identifier for a stream on a video capture device.
ms.assetid: 03C48CBA-FAD0-4127-89E5-3F1874BF32DB
title: MF_DEVICESTREAM_STREAM_ID attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_DEVICESTREAM\_STREAM\_ID attribute

Specifies the kernel streaming (KS) identifier for a stream on a video capture device.

## Data type

**UINT32**

## Remarks

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

 

 




