---
Description: 'Identifies the topology node for a stream sink.'
ms.assetid: '9aa6ca66-5122-4d05-94b9-32be194e9eb3'
title: 'MF\_EVENT\_OUTPUT\_NODE attribute'
---

# MF\_EVENT\_OUTPUT\_NODE attribute

Identifies the topology node for a stream sink.

## Data type

**UINT64**

Treat as [**TOPOID**](topoid.md).

## Remarks

The value of this attribute is a node identifier for an output node on the current topology. To get a pointer to the associated node, call [**IMFTopology::GetNodeByID**](imftopology-getnodebyid.md) on the topology.

This attribute is used with the following events:

-   [MESessionStreamSinkFormatChanged](mesessionstreamsinkformatchanged.md)
-   [MESinkInvalidated](mesinkinvalidated.md)

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

[Event Attributes](event-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT64**](imfattributes-getuint64.md)
</dt> <dt>

[**IMFAttributes::SetUINT64**](imfattributes-setuint64.md)
</dt> </dl>

 

 




