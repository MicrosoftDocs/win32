---
Description: Specifies custom color primaries for a video media type.
ms.assetid: dc5df755-53cf-4910-af42-309f1f46b1ed
title: MF\_MT\_CUSTOM\_VIDEO\_PRIMARIES attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_CUSTOM\_VIDEO\_PRIMARIES attribute

Specifies custom color primaries for a video media type.

## Data type

**UINT32**

Byte array

## Remarks

The attribute data is an [**MT\_CUSTOM\_VIDEO\_PRIMARIES**](/windows/win32/mfapi/ns-mfapi-_mt_custom_video_primaries?branch=master) structure.

This attribute specifies the actual color volume of content or a display. CEA-861.3 / SMPTE ST.2086 color volume mastering information is stored in this attribute by decoders. Note that this attribute does not replace the [**MF\_MT\_VIDEO\_PRIMARIES**](mf-mt-video-primaries-attribute.md)attribute. This attribute describes a hint about the color volume of the content, whereas **MF\_MT\_VIDEO\_PRIMARIES** describes the color primaries in which the content is actually coded (e.g: the meaning of 1.0 in the R/G/B channels of a floating point representation).

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

[**IMFAttributes::GetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getblob?branch=master)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setblob?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> </dl>

 

 




