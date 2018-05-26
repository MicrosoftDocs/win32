---
title: StorPortFreeWorker routine
description: Frees a Storport work item previously allocated by the StorPortInitializeWorker routine.
ms.assetid: 90BD61C8-322B-48D5-83E0-7204E3DC4423
keywords:
- StorPortFreeWorker routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortFreeWorker
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortFreeWorker routine

Frees a Storport work item previously allocated by the [**StorPortInitializeWorker**](storportinitializeworker.md) routine.

## Syntax


```C++
ULONG StorPortFreeWorker(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID WorkItem
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*WorkItem* \[in\]
</dt> <dd>

A pointer to an opaque buffer for the work item context returned by [**StorPortInitializeWorker**](storportinitializeworker.md).

</dd> </dl>

## Return value

The [**StorPortInitializeWorker**](storportinitializeworker.md) routine returns one of these status codes:



| Return code                                                                                                     | Description                                                  |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>      | Current IRQL &gt; DISPATCH\_LEVEL.<br/>                |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | Either *HwDeviceExtension* or *WorkItem* is NULL.<br/> |
| <dl> <dt>**STOR\_STATUS\_BUSY**</dt> </dl>               | The work item is currently queued for processing.<br/> |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The work item was successfully freed.<br/>             |
| <dl> <dt>**STOR\_STATUS\_UNSUCCESSFUL**</dt> </dl>       | The work item is already free.<br/>                    |



 

## Remarks

Miniports should call **StorPortFreeWorker** whenever a work item is no longer needed or when the miniport receives a PnP SRB notification that the adapter is removed.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | &lt;= DISPATCH\_LEVEL<br/>                                                                                                        |



## See also

<dl> <dt>

[**StorPortInitializeWorker**](storportinitializeworker.md)
</dt> <dt>

[**StorPortQueueWorkItem**](storportqueueworkitem.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortFreeWorker%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






