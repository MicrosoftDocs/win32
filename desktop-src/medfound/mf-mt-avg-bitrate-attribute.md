---
Description: Approximate data rate of the video stream, in bits per second, for a video media type.
ms.assetid: cf9374a7-3688-4a6c-8339-d68c267c9bed
title: MF\_MT\_AVG\_BITRATE attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MT\_AVG\_BITRATE attribute

Approximate data rate of the video stream, in bits per second, for a video media type.

## Data type

**UINT32**

## Remarks

This attribute corresponds to the **dwBitRate** member of the [**VIDEOINFOHEADER**](https://msdn.microsoft.com/a175592b-0dc1-4001-b52f-785407965932) and [**VIDEOINFOHEADER2**](https://msdn.microsoft.com/5e3d5bf0-435f-45da-8409-a1463b56a7ae) structures.

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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




