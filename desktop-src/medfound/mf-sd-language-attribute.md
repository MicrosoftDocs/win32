---
Description: Specifies the language for a stream.
ms.assetid: b64a9554-a560-4212-8964-b68ebbadc046
title: MF\_SD\_LANGUAGE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getstring?branch=master)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master)
</dt> <dt>

[**IMFStreamDescriptor**](/windows/win32/mfidl/nn-mfidl-imfstreamdescriptor?branch=master)
</dt> <dt>

[Stream Descriptor Attributes](stream-descriptor-attributes.md)
</dt> </dl>

 

 




