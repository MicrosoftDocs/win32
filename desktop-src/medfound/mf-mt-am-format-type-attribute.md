---
Description: Contains a DirectShow format GUID for a media type.
ms.assetid: dc532791-39e1-4acb-9e62-21d8f25be870
title: MF\_MT\_AM\_FORMAT\_TYPE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_AM\_FORMAT\_TYPE attribute

Contains a DirectShow format GUID for a media type.

## Data type

**GUID**

## Remarks

This attribute might be set when a DirectShow media type is converted into a Media Foundation media type. The attribute indicates the original DirectShow format type. The value corresponds to the formattype member of the [**AM\_MEDIA\_TYPE**](dshow.am_media_type) structure.

For an audio format, the [**MF\_MT\_USER\_DATA**](mf-mt-user-data-attribute.md) attribute might contain the original format block, if the DirectShow format type was not recognized.

Do not set this attribute on a media type unless you are converting a DirectShow format structure.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Media Type Conversions](media-type-conversions.md)
</dt> <dt>

[Media Types](media-types.md)
</dt> <dt>

[**IMFAttributes::GetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getguid?branch=master)
</dt> <dt>

[**IMFAttributes::SetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setguid?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[**MFCreateMediaTypeFromRepresentation**](/windows/win32/mfapi/nf-mfapi-mfcreatemediatypefromrepresentation?branch=master)
</dt> </dl>

 

 




