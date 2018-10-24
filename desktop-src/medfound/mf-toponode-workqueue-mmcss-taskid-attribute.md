---
Description: Specifies a Multimedia Class Scheduler Service (MMCSS) task identifier for a topology branch.
ms.assetid: ccecc1e6-2d30-4e89-849f-c3acad97f312
title: MF_TOPONODE_WORKQUEUE_MMCSS_TASKID attribute
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_TOPONODE\_WORKQUEUE\_MMCSS\_TASKID attribute

Specifies a Multimedia Class Scheduler Service (MMCSS) task identifier for a topology branch.

## Data type

**UINT32**

## Remarks

This attribute applies to source nodes (**MF\_TOPOLOGY\_SOURCESTREAM\_NODE**). This attribute is optional.

This attribute is ignored unless the following attributes are also set:

-   [**MF\_TOPONODE\_WORKQUEUE\_ID**](mf-toponode-workqueue-id-attribute.md)
-   [**MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS**](mf-toponode-workqueue-mmcss-class-attribute.md)

If the application registers one of its own threads with MMCSS, you can use this attribute to associate the topology work queue with the application's MMCSS group. Set the attribute value equal to the task identifier that the application received when it registered with MMCSS. (The task identifier is returned in the *TaskIndex* parameter of the [**AvSetMmThreadCharacteristics**](https://msdn.microsoft.com/en-us/library/ms681974(v=VS.85).aspx) function. For more information, see the topic [Process and Thread Functions](https://msdn.microsoft.com/en-us/library/ms684847(v=VS.85).aspx).)

If you want MMCSS to assign a new task identifier for the topology, set the [**MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS**](mf-toponode-workqueue-mmcss-class-attribute.md) attribute, but do not set the **MF\_TOPONODE\_WORKQUEUE\_MMCSS\_TASKID** attribute.

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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[**IMFWorkQueueServices::BeginRegisterTopologyWorkQueuesWithMMCSS**](/windows/desktop/api/mfidl/nf-mfidl-imfworkqueueservices-beginregistertopologyworkqueueswithmmcss)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> <dt>

[Work Queues](work-queues.md)
</dt> </dl>

 

 




