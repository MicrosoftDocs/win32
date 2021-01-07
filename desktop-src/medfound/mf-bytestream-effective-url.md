---
description: Gets the effective URL of a byte stream.
ms.assetid: 0A83CFC0-7EAA-464B-BA39-50DF220AF683
title: MF_BYTESTREAM_EFFECTIVE_URL attribute (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_BYTESTREAM\_EFFECTIVE\_URL attribute

Gets the effective URL of a byte stream.

## Data type

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring).

To set this attribute, call [**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring).

## Applies to

[**IMFByteStream**](/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestream)

## Remarks

The effective URL can differ from the original URL if the original URL contains any extra information, such as search strings or anchors, or if the request was redirected.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfobjects.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Byte Stream Attributes](byte-stream-attributes.md)
</dt> <dt>

[**IMFByteStream**](/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestream)
</dt> </dl>

 

 




