---
Description: Specifies for a media type whether each sample is independent of the other samples in the stream.
ms.assetid: 40434f63-e191-45e1-b788-5f80fe7f49ae
title: MF\_MT\_ALL\_SAMPLES\_INDEPENDENT attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_ALL\_SAMPLES\_INDEPENDENT attribute

Specifies for a media type whether each sample is independent of the other samples in the stream.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

If this attribute is **FALSE**, some samples cannot be used without referring to other samples in the stream. For example, if a video format contains delta frames, this attribute should be **FALSE**.

This attribute corresponds to the **bTemporalCompression** field in the DirectShow [**AM\_MEDIA\_TYPE**](dshow.am_media_type) structure.

Set this attribute to **TRUE** for all uncompressed media types.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




