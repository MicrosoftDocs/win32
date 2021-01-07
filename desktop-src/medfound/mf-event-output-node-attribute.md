---
description: Identifies the topology node for a stream sink.
ms.assetid: 9aa6ca66-5122-4d05-94b9-32be194e9eb3
title: MF_EVENT_OUTPUT_NODE attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_EVENT\_OUTPUT\_NODE attribute

Identifies the topology node for a stream sink.

## Data type

**UINT64**

Treat as [**TOPOID**](topoid.md).

## Remarks

The value of this attribute is a node identifier for an output node on the current topology. To get a pointer to the associated node, call [**IMFTopology::GetNodeByID**](/windows/desktop/api/mfidl/nf-mfidl-imftopology-getnodebyid) on the topology.

This attribute is used with the following events:

-   [MESessionStreamSinkFormatChanged](mesessionstreamsinkformatchanged.md)
-   [MESinkInvalidated](mesinkinvalidated.md)

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
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

[**IMFAttributes::GetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint64)
</dt> <dt>

[**IMFAttributes::SetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint64)
</dt> </dl>

 

 




