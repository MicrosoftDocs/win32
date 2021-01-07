---
description: Contains the original codec FOURCC for a video stream.
ms.assetid: 2e6ef198-5754-4ded-9fe3-61edd0742a17
title: MF_MT_ORIGINAL_4CC attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_ORIGINAL\_4CC attribute

Contains the original codec FOURCC for a video stream.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)

## Remarks

Depending on the source file, the AVI media source might set this attribute on the media types that it offers.

An AVI file contains a stream header for each stream in the file. The AVI media source translates the stream header into a media type. For compressed video streams, the stream header contains a FOURCC that identifies the video codec. In most cases, the AVI media source converts this FOURCC directly to a subtype GUID, as described in the topic [Video Subtype GUIDs](video-subtype-guids.md). In some cases, however, it maps the original FOURCC to another FOURCC that is equivalent. If so, the media source stores the original FOURCC in the media type, using the MF\_MT\_ORIGINAL\_4CC attribute.

The FOURCC mappings are stored in the Registry under the following key:

**HKEY\_CLASSES\_ROOT**\\**MediaFoundation**\\**MapVideo4cc**

Each entry is a **DWORD** value. The name of the entry is the hexadecimal representation of the FOURCC, without an "0x" prefix, and with the first character appearing first in the string. For example, the FOURCC code 'abcd' would appear as "61626364". The value of the entry is the equivalent FOURCC code.

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

 

 




