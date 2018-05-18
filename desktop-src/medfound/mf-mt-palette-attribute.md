---
Description: 'Contains the palette entries for a video media type. Use this attribute for palettized video formats, such as RGB 8.'
ms.assetid: '3efc124b-073e-4c48-9550-c100e29f2d6f'
title: 'MF\_MT\_PALETTE attribute'
---

# MF\_MT\_PALETTE attribute

Contains the palette entries for a video media type. Use this attribute for palettized video formats, such as RGB 8.

## Data type

Byte array

## Remarks

The attribute data is an array of [**MFPaletteEntry**](mfpaletteentry.md) unions.

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

[**IMFAttributes::GetBlob**](imfattributes-getblob.md)
</dt> <dt>

[**IMFAttributes::SetBlob**](imfattributes-setblob.md)
</dt> <dt>

[**IMFMediaType**](imfmediatype.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




