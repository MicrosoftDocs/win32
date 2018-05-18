---
title: StorPortQueueWorkItem routine
description: Schedules a Storport work item to execute within the context of a system worker thread.
ms.assetid: '7B5DD97C-2E3D-4FF7-BF04-36F016B0C6B3'
keywords: ["StorPortQueueWorkItem routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortQueueWorkItem
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortQueueWorkItem routine

Schedules a Storport work item to execute within the context of a system worker thread.

## Syntax


```C++
ULONG StorPortQueueWorkItem(
  _In_     PVOID        HwDeviceExtension,
  _In_     PHW_WORKITEM WorkItemCallback,
  _In_     PVOID        Worker,
  _In_opt_ PVOID        Context
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*WorkItemCallback* \[in\]
</dt> <dd>

A pointer to a work item callback routine supplied by the miniport. This routine is called in context of the system thread to process the scheduled *WorkItem*.

</dd> <dt>

*Worker* \[in\]
</dt> <dd>

A pointer to an opaque buffer for the worker returned by [**StorPortInitializeWorker**](storportinitializeworker.md).

</dd> <dt>

*Context* \[in, optional\]
</dt> <dd>

Optional context for the *WorkItem* that is processed by the callback routine in *WorkItemCallback*.

</dd> </dl>

## Return value

The **StorPortQueueWorkItem** routine returns one of these status codes:



| Return code                                                                                                     | Description                                                              |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>      | Current IRQL &gt; DISPATCH\_LEVEL.<br/>                            |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | *HwDeviceExtension*, *Worker*, or *WorkItemCallback* is NULL.<br/> |
| <dl> <dt>**STOR\_STATUS\_BUSY**</dt> </dl>               | The work item was is already queued for processing.<br/>           |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The work item was successfully queued.<br/>                        |



 

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | &lt;= DISPATCH\_LEVEL<br/>                                                                                                        |



## See also

<dl> <dt>

[**HwStorWorkItem**](hwstorworkitem.md)
</dt> <dt>

[**StorPortFreeWorker**](storportfreeworker.md)
</dt> <dt>

[**StorPortInitializeWorker**](storportinitializeworker.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortQueueWorkItem%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






