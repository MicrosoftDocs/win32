---
Description: 'Contains a pointer to the stream descriptor for the media source.'
ms.assetid: '5acafbc1-823f-4b6d-8737-04b3a6a0cf87'
title: 'MF\_TOPONODE\_STREAM\_DESCRIPTOR attribute'
---

# MF\_TOPONODE\_STREAM\_DESCRIPTOR attribute

Contains a pointer to the stream descriptor for the media source.

## Data type

**IUnknown\***

## Remarks

This attribute applies to source nodes (**MF\_TOPOLOGY\_SOURCESTREAM\_NODE**).

The value of the attribute is a pointer to the stream descriptor's [**IMFStreamDescriptor**](imfstreamdescriptor.md) interface. This attribute is required.

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

[**IMFTopologyNode**](imftopologynode.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 




