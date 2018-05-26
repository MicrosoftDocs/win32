---
Description: Specifies whether an ASF image stream is a degradable JPEG type.
ms.assetid: e29d0893-8561-4a8c-99e2-168186becd82
title: MF\_MT\_IMAGE\_LOSS\_TOLERANT attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_IMAGE\_LOSS\_TOLERANT attribute

Specifies whether an ASF image stream is a degradable JPEG type.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Applies to

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)

## Remarks

This attribute applies to the media type for image streams in ASF. If the value is **TRUE**, the stream is a degradable JPEG image type. Otherwise, the stream is a JFIF image type. For more information about these stream types, see the ASF specification.

In addition to the MF\_MT\_IMAGE\_LOSS\_TOLERANT attribute, the media type for an ASF image stream contains the following attributes:



| Attribute                                                 | Description                                |
|-----------------------------------------------------------|--------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md) | Contains the value **MFMediaType\_Image**. |
| [**MF\_MT\_FRAME\_SIZE**](mf-mt-frame-size-attribute.md) | Gives the image size in pixels.            |



 

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




