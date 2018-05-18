---
Description: 'Approximate data rate of the video stream, in bits per second, for a video media type.'
ms.assetid: 'cf9374a7-3688-4a6c-8339-d68c267c9bed'
title: 'MF\_MT\_AVG\_BITRATE attribute'
---

# MF\_MT\_AVG\_BITRATE attribute

Approximate data rate of the video stream, in bits per second, for a video media type.

## Data type

**UINT32**

## Remarks

This attribute corresponds to the **dwBitRate** member of the [**VIDEOINFOHEADER**](dshow.videoinfoheader) and [**VIDEOINFOHEADER2**](dshow.videoinfoheader2) structures.

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

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFMediaType**](imfmediatype.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




