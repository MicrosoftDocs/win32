---
Description: Specifies the work-item priority for a branch of the topology.
ms.assetid: B2FA1151-08D3-46F9-A38D-AC8908EFA6A2
title: MF\_TOPONODE\_WORKQUEUE\_ITEM\_PRIORITY attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPONODE\_WORKQUEUE\_ITEM\_PRIORITY attribute

Specifies the work-item priority for a branch of the topology.

## Data type

**UINT32**

## Remarks

This attribute applies to source nodes (**MF\_TOPOLOGY\_SOURCESTREAM\_NODE**). The attribute is optional.

This attribute requires the [MF\_TOPONODE\_WORKQUEUE\_ID](mf-toponode-workqueue-id-attribute.md) attribute on the same node.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> <dt>

[Work Queue and Threading Improvements](media-foundation-work-queue-and-threading-improvements.md)
</dt> <dt>

[**IMFTopologyNode**](/windows/win32/mfidl/nn-mfidl-imftopologynode?branch=master)
</dt> <dt>

[**IMFWorkQueueServices::BeginRegisterTopologyWorkQueuesWithMMCSS**](/windows/win32/mfidl/nf-mfidl-imfworkqueueservices-beginregistertopologyworkqueueswithmmcss?branch=master)
</dt> <dt>

[**MF\_TOPONODE\_WORKQUEUE\_ID**](mf-toponode-workqueue-id-attribute.md)
</dt> </dl>

 

 




