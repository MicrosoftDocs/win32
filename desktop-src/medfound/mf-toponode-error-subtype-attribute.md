---
Description: 'Contains the media subtype for a topology node. This attribute is set when the topology fails to load because the correct decoder could not be found.'
ms.assetid: '89da33c8-97af-4c56-8bdb-2ac588810d77'
title: 'MF\_TOPONODE\_ERROR\_SUBTYPE attribute'
---

# MF\_TOPONODE\_ERROR\_SUBTYPE attribute

Contains the media subtype for a topology node. This attribute is set when the topology fails to load because the correct decoder could not be found.

## Data type

**GUID**

## Remarks

This attribute applies to all node types.

The topology loader might set the attribute. Applications typically read this attribute but do not set it.

For a list of possible values, see [Media Type GUIDs](media-type-guids.md).

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

[**IMFAttributes::GetGUID**](imfattributes-getguid.md)
</dt> <dt>

[**IMFAttributes::SetGUID**](imfattributes-setguid.md)
</dt> <dt>

[**IMFTopologyNode**](imftopologynode.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 




