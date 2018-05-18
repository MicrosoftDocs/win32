---
Description: 'The stream identifier of the stream sink associated with this topology node.'
ms.assetid: '0b8060ab-1463-45c2-8277-d15122561248'
title: 'MF\_TOPONODE\_STREAMID attribute'
---

# MF\_TOPONODE\_STREAMID attribute

The stream identifier of the stream sink associated with this topology node.

## Data type

**UINT32**

## Remarks

This attribute applies to output nodes (**MF\_TOPOLOGY\_OUTPUT\_NODE**).

When the Media Session loads the topology, it queries the media sink for a stream sink with the specified identifier. If that fails, it attempts to add a new stream sink to the media sink.

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

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFTopologyNode**](imftopologynode.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 




