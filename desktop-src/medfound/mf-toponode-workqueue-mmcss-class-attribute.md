---
Description: Specifies a Multimedia Class Scheduler Service (MMCSS) task for a topology branch.
ms.assetid: 8668d0f1-9d54-4c56-bb19-09498252bec4
title: MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS attribute

Specifies a [Multimedia Class Scheduler Service](base.multimedia_class_scheduler_service) (MMCSS) task for a topology branch.

## Data type

Wide-character string

## Remarks

This attribute applies to source nodes (**MF\_TOPOLOGY\_SOURCESTREAM\_NODE**). This attribute is optional.

This attribute requires the [MF\_TOPONODE\_WORKQUEUE\_ID](mf-toponode-workqueue-id-attribute.md) attribute. If you set this attribute, also set the **MF\_TOPONODE\_WORKQUEUE\_ID** attribute is set on the same node.

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

[**IMFAttributes::GetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getstring?branch=master)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master)
</dt> <dt>

[**IMFTopologyNode**](/windows/win32/mfidl/nn-mfidl-imftopologynode?branch=master)
</dt> <dt>

[**IMFWorkQueueServices::BeginRegisterTopologyWorkQueuesWithMMCSS**](/windows/win32/mfidl/nf-mfidl-imfworkqueueservices-beginregistertopologyworkqueueswithmmcss?branch=master)
</dt> <dt>

[**MF\_TOPONODE\_WORKQUEUE\_ID**](mf-toponode-workqueue-id-attribute.md)
</dt> <dt>

[**MF\_TOPONODE\_WORKQUEUE\_MMCSS\_TASKID**](mf-toponode-workqueue-mmcss-taskid-attribute.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> <dt>

[Work Queues](work-queues.md)
</dt> </dl>

 

 




