---
Description: 'Contains the name of a stream.'
ms.assetid: '80235820-761f-4deb-9bf6-82ef402b3ee4'
title: 'MF\_SD\_STREAM\_NAME attribute'
---

# MF\_SD\_STREAM\_NAME attribute

Contains the name of a stream.

## Data type

**WCHAR\***

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](imfattributes-getstring.md).

To set this attribute, call [**IMFAttributes::SetString**](imfattributes-setstring.md).

## Applies to

[**IMFStreamDescriptor**](imfstreamdescriptor.md)

## Remarks

The AVI media source sets this attribute if the AVI file contains a 'strn' chunk.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Stream Descriptor Attributes](stream-descriptor-attributes.md)
</dt> </dl>

 

 




