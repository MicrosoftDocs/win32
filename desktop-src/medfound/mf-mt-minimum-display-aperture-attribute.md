---
Description: Defines the display aperture, which is the region of a video frame that contains valid image data.
ms.assetid: 86a7509b-c690-49c2-bbe4-8b02d64c307c
title: MF\_MT\_MINIMUM\_DISPLAY\_APERTURE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_MINIMUM\_DISPLAY\_APERTURE attribute

Defines the display aperture, which is the region of a video frame that contains valid image data.

## Data type

Byte array

## Remarks

The attribute value is an [**MFVideoArea**](/windows/win32/mfobjects/ns-mfobjects-_mfvideoarea?branch=master) structure.

The minimum display aperture is the region that contains the valid portion of the signal. The pixels outside the aperture contain invalid data and should not be displayed.

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

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Picture Aspect Ratio](picture-aspect-ratio.md)
</dt> <dt>

[Video Media Types](video-media-types.md)
</dt> <dt>

[**IMFAttributes::GetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getblob?branch=master)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setblob?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[**MF\_MT\_GEOMETRIC\_APERTURE**](mf-mt-geometric-aperture-attribute.md)
</dt> <dt>

[**MF\_MT\_PAN\_SCAN\_APERTURE**](mf-mt-pan-scan-aperture-attribute.md)
</dt> </dl>

 

 




