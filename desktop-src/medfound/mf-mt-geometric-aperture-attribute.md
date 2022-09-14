---
description: Defines the geometric aperture for a video media type.
ms.assetid: a2489ba1-f322-4b63-a479-0d9879c30a8c
title: MF_MT_GEOMETRIC_APERTURE attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_GEOMETRIC\_APERTURE attribute

Defines the geometric aperture for a video media type.

## Data type

Byte array

## Remarks

The value of this attribute is an [**MFVideoArea**](/windows/desktop/api/mfobjects/ns-mfobjects-mfvideoarea) structure.

The picture aspect ratio is calculated relative to the geometric aperture, using the following formula: Picture aspect ratio = (geometric aperture width / geometric aperture height) × pixel aspect ratio.

If this attribute is not set, the geometric aperture is assumed to be the entire video frame. You should set this attribute only when the media type describes a video standard with a defined active area.

For example, in NTSC television the video frame is 720 × 480 with an active area of 704 × 480 and a 10:11 pixel aspect ratio. The resulting picture has an aspect ratio of (704/480) × (10/11) = 4:3.

> [!Note]  
> The default presenter for the [Enhanced Video Renderer](enhanced-video-renderer.md) (EVR) shows the geometric aperture of the video, if specified.

 

The GUID constant for this attribute is exported from mfuuid.lib.

## Examples


```
HRESULT SetGeometricAperture(
    IMFMediaType *pMediaType, 
    const MFVideoArea& area
    )
{
    return pMediaType->SetBlob(
        MF_MT_GEOMETRIC_APERTURE, 
        (UINT8*)&area, 
        sizeof(MFVideoArea)
        );
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Picture Aspect Ratio](picture-aspect-ratio.md)
</dt> <dt>

[Video Media Types](video-media-types.md)
</dt> <dt>

[**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[**MF\_MT\_MINIMUM\_DISPLAY\_APERTURE**](mf-mt-minimum-display-aperture-attribute.md)
</dt> <dt>

[**MF\_MT\_PAN\_SCAN\_APERTURE**](mf-mt-pan-scan-aperture-attribute.md)
</dt> </dl>

 

 




