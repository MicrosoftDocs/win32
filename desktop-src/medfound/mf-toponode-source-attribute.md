---
Description: 'Contains a pointer to the media source associated with a topology node.'
ms.assetid: '73b84ab6-bdc2-4b22-9ce4-b79b954476e5'
title: 'MF\_TOPONODE\_SOURCE attribute'
---

# MF\_TOPONODE\_SOURCE attribute

Contains a pointer to the media source associated with a topology node.

## Data type

**IUnknown\***

## Remarks

This attribute applies to source nodes (**MF\_TOPOLOGY\_SOURCESTREAM\_NODE**).

The value of the atttribute is a pointer to the media source's [**IMFMediaSource**](imfmediasource.md) interface. This attribute is required.

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

 

 




