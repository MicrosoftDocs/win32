---
Description: 'Specifies whether pan/scan mode is enabled.'
ms.assetid: '9e8746c6-13a4-4cf7-9748-82223d9529fa'
title: 'MF\_MT\_PAN\_SCAN\_ENABLED attribute'
---

# MF\_MT\_PAN\_SCAN\_ENABLED attribute

Specifies whether pan/scan mode is enabled.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

If this attribute is **TRUE**, only the pan/scan region of the video should be displayed. The pan/scan region is specified by the [**MF\_MT\_PAN\_SCAN\_APERTURE**](mf-mt-pan-scan-aperture-attribute.md) attribute.

If this attribute is **FALSE** or not set, the entire display aperture of the video should be displayed. The display aperture is specified by the [**MF\_MT\_MINIMUM\_DISPLAY\_APERTURE**](mf-mt-minimum-display-aperture-attribute.md) attribute.

If you set this attribute to **TRUE**, also set the value of the [**MF\_MT\_PAN\_SCAN\_APERTURE**](mf-mt-pan-scan-aperture-attribute.md) attribute.

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
</dt> <dt>

[Picture Aspect Ratio](picture-aspect-ratio.md)
</dt> </dl>

 

 




