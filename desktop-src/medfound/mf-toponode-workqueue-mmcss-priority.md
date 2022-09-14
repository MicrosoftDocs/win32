---
description: Specifies the relative thread priority for a branch of the topology.
ms.assetid: 7BCD2EE0-94FB-4438-9B6A-7B26DBFB5978
title: MF_TOPONODE_WORKQUEUE_MMCSS_PRIORITY attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPONODE\_WORKQUEUE\_MMCSS\_PRIORITY attribute

Specifies the relative thread priority for a branch of the topology.

## Data type

**UINT32**

## Remarks

This attribute applies to source nodes (**MF\_TOPOLOGY\_SOURCESTREAM\_NODE**). The attribute is optional.

This attribute requires the [MF\_TOPONODE\_WORKQUEUE\_ID](mf-toponode-workqueue-id-attribute.md) and [MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS](mf-toponode-workqueue-mmcss-class-attribute.md) attributes on the same node.

The value of the attribute is the relative thread priority of the work queue for this branch of the topology. The [Multimedia Class Scheduler Service](../procthread/multimedia-class-scheduler-service.md) (MMCSS) uses the relative priority when it sets the thread priority. For more information, see [**AvSetMmThreadPriority**](/windows/win32/api/avrt/nf-avrt-avsetmmthreadpriority).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
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

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[**IMFWorkQueueServices::BeginRegisterTopologyWorkQueuesWithMMCSS**](/windows/desktop/api/mfidl/nf-mfidl-imfworkqueueservices-beginregistertopologyworkqueueswithmmcss)
</dt> <dt>

[**MF\_TOPONODE\_WORKQUEUE\_ID**](mf-toponode-workqueue-id-attribute.md)
</dt> <dt>

[**MF\_TOPONODE\_WORKQUEUE\_MMCSS\_TASKID**](mf-toponode-workqueue-mmcss-taskid-attribute.md)
</dt> </dl>

 

 
