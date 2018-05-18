---
Description: 'Specifies the status of an attempt to resolve a topology.'
ms.assetid: '7c2410ce-e70b-4303-9dbc-caff4a355d6b'
title: 'MF\_TOPOLOGY\_RESOLUTION\_STATUS attribute'
---

# MF\_TOPOLOGY\_RESOLUTION\_STATUS attribute

Specifies the status of an attempt to resolve a topology.

## Data type

**UINT32**

## Remarks

The topology loader or the Media Session might set this attribute on a topology. The value of this attribute is a bitwise **OR** of flags from the [**MF\_TOPOLOGY\_RESOLUTION\_STATUS\_FLAGS**](mf-topology-resolution-status-flags.md) enumeration.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFTopology**](imftopology.md)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> </dl>

 

 




