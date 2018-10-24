---
Description: Specifies a Multimedia Class Scheduler Service (MMCSS) task for a topology branch.
ms.assetid: 8668d0f1-9d54-4c56-bb19-09498252bec4
title: MF_TOPONODE_WORKQUEUE_MMCSS_CLASS attribute
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS attribute

Specifies a [Multimedia Class Scheduler Service](https://msdn.microsoft.com/en-us/library/ms684247(v=VS.85).aspx) (MMCSS) task for a topology branch.

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

[**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[**IMFWorkQueueServices::BeginRegisterTopologyWorkQueuesWithMMCSS**](/windows/desktop/api/mfidl/nf-mfidl-imfworkqueueservices-beginregistertopologyworkqueueswithmmcss)
</dt> <dt>

[**MF\_TOPONODE\_WORKQUEUE\_ID**](mf-toponode-workqueue-id-attribute.md)
</dt> <dt>

[**MF\_TOPONODE\_WORKQUEUE\_MMCSS\_TASKID**](mf-toponode-workqueue-mmcss-taskid-attribute.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> <dt>

[Work Queues](work-queues.md)
</dt> </dl>

 

 




