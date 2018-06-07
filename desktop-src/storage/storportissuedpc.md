---
title: StorPortIssueDpc routine
description: The StorPortIssueDpc routine issues a deferred procedure call (DPC).
ms.assetid: a0c46c51-f6c4-4609-9dba-b730f33c3ed6
keywords:
- StorPortIssueDpc routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortIssueDpc
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortIssueDpc routine

The **StorPortIssueDpc** routine issues a deferred procedure call (DPC).

## Syntax


```C++
BOOLEAN StorPortIssueDpc(
  _In_ PVOID     DeviceExtension,
  _In_ PSTOR_DPC Dpc,
  _In_ PVOID     SystemArgument1,
  _In_ PVOID     SystemArgument2
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the per-adapter device extension.

</dd> <dt>

*Dpc* \[in\]
</dt> <dd>

Pointer to a buffer containing an initialized DPC object of type [**STOR\_DPC**](stor-dpc.md) returned by the [**StorPortInitializeDpc**](storportinitializedpc.md) routine.

</dd> <dt>

*SystemArgument1* \[in\]
</dt> <dd>

Pointer to caller-supplied information that will be passed to the deferred routine.

</dd> <dt>

*SystemArgument2* \[in\]
</dt> <dd>

Pointer to caller-supplied information that will be passed to the deferred routine.

</dd> </dl>

## Return value

The **StorPortIssueDpc** routine returns **TRUE** if the DPC was successfully inserted into the DPC queue, and **FALSE** otherwise.

## Remarks

The **StorPortIssueDpc** routine calls the [**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185) kernel routine to queue the DPC. The **KeInsertQueueDpc** kernel routine does not allow a DPC to be queued multiple times. Thus, if the DPC object specified by the *Dpc* parameter is already in the DPC queue, **KeInsertQueueDpc** ignores the queue request. This ensures that a deferred routine initialized with [**StorPortInitializeDpc**](storportinitializedpc.md) is always synchronized with itself. In other words, the caller does not need to sequentialize calls to the **StorPortIssueDpc** routine to ensure that multiple instances the routine do not run simultaneously.

If a miniport driver has multiple work-items that must be performed by the same DPC, the miniport driver must ensure that each work item completes before issuing the DPC for the next work item.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



## See also

<dl> <dt>

[**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185)
</dt> <dt>

[**StorPortInitializeDpc**](storportinitializedpc.md)
</dt> <dt>

[**STOR\_DPC**](stor-dpc.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortIssueDpc%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






