---
Description: 'Specifies when a presentation was last modified.'
ms.assetid: '12990de2-7656-4781-943b-c46f42a0e38d'
title: 'MF\_PD\_LAST\_MODIFIED\_TIME attribute'
---

# MF\_PD\_LAST\_MODIFIED\_TIME attribute

Specifies when a presentation was last modified.

## Data type

Byte array

## Remarks

Media sources can set this attribute on a presentation descriptor. The value of the attribute is a **FILETIME** structure, which is documented in the Windows SDK.

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

[**IMFAttributes::GetBlob**](imfattributes-getblob.md)
</dt> <dt>

[**IMFAttributes::SetBlob**](imfattributes-setblob.md)
</dt> <dt>

[**IMFPresentationDescriptor**](imfpresentationdescriptor.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 




