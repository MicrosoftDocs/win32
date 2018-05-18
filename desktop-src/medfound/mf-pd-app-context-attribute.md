---
Description: 'Contains a pointer to the presentation descriptor from the Protected Media Path (PMP).'
ms.assetid: 'cf12552e-0963-46fa-9a26-44dd601ab68c'
title: 'MF\_PD\_APP\_CONTEXT attribute'
---

# MF\_PD\_APP\_CONTEXT attribute

Contains a pointer to the presentation descriptor from the Protected Media Path (PMP).

## Data type

**IUnknown\***

## Remarks

The media source proxy, which is created in the PMP process, uses this attribute to store the remote presentation descriptor on the application's presentation descriptor.

The value of this attribute is a pointer to the [**IMFPresentationDescriptor**](imfpresentationdescriptor.md) interface.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUnknown**](imfattributes-getunknown.md)
</dt> <dt>

[**IMFAttributes::SetUnknown**](imfattributes-setunknown.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 




