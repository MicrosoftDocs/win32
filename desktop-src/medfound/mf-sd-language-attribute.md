---
description: Specifies the language for a stream.
ms.assetid: b64a9554-a560-4212-8964-b68ebbadc046
title: MF_SD_LANGUAGE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SD\_LANGUAGE attribute

Specifies the language for a stream.

## Data type

Wide-character string

## Remarks

The value of this attribute is an RFC 1766-compliant language tag. This attribute applies to stream descriptors.

A media source (or any object that creates a stream descriptor) can set this attribute if the stream has a specified language. Applications can query this attribute to get the language. If the attribute is not set, the stream does not have a specified language.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring)
</dt> <dt>

[**IMFStreamDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamdescriptor)
</dt> <dt>

[Stream Descriptor Attributes](stream-descriptor-attributes.md)
</dt> </dl>

 

 




