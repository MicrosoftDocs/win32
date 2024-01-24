---
description: Type-specific data for a binary stream in an Advanced Systems Format (ASF) file.
ms.assetid: 45608dde-894b-4204-80dc-505f068fb158
title: MF_MT_ARBITRARY_HEADER attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_ARBITRARY\_HEADER attribute

Type-specific data for a binary stream in an Advanced Systems Format (ASF) file.

## Data type

**[**MT\_ARBITRARY\_HEADER**](/windows/desktop/api/mfapi/ns-mfapi-mt_arbitrary_header)** stored as **BYTE\[\]**

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob).

To set this attribute, call [**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob).

## Remarks

ASF files can contain streams with binary data. The MF\_MT\_ARBITRARY\_HEADER attribute in the media type contains an [**MT\_ARBITRARY\_HEADER**](/windows/desktop/api/mfapi/ns-mfapi-mt_arbitrary_header) structure that describes the stream.

In addition to the MF\_MT\_ARBITRARY\_HEADER attribute, the media type for an ASF binary stream contains the following attributes:



| Attribute                                                 | Description                                            |
|-----------------------------------------------------------|--------------------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md) | The value of the attribute is **MFMediaType\_Binary**. |
| [MF\_MT\_ARBITRARY\_FORMAT](mf-mt-arbitrary-format.md)   | Contains additional format data.                       |



 

> [!Note]  
> In the Windows Media Format SDK, binary streams are called *arbitrary streams* or *arbitrary data streams*.

 

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




