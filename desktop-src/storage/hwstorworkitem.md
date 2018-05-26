---
title: HW\_WORKITEM routine
description: A miniport-provided callback function for processing a Storport work item request.
ms.assetid: CBBB1350-66BE-4F74-A0CE-0400245352F3
keywords:
- HwStorWorkItem routine Storage Devices
- HW_WORKITEM
topic_type:
- apiref
api_name:
- HwStorWorkItem
api_location:
- storport.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HW\_WORKITEM routine

A miniport-provided callback function for processing a Storport work item request.

## Syntax


```C++
HW_WORKITEM HwStorWorkItem;

VOID HwStorWorkItem(
  _In_     IN PVOID HwDeviceExtension,
  _In_opt_ PVOID    Context,
  _In_     PVOID    Worker
)
{ ... }
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*Context* \[in, optional\]
</dt> <dd>

Optional context provided by the miniport in the *Callback* parameter of [**StorPortQueueWorkItem**](storportqueueworkitem.md).

</dd> <dt>

*Worker* \[in\]
</dt> <dd>

A pointer to an opaque buffer that holds context information for the work item returned by [**StorPortInitializeWorker**](storportinitializeworker.md).

</dd> </dl>

## Return value

None.

## Remarks

If needed, a work item can be queued within **HwStorWorkItem**. Call [**StorPortQueueWorkItem**](storportqueueworkitem.md) with the current work item to reuse it. Otherwise, call [**StorPortFreeWorker**](storportfreeworker.md) to release the work item.

No locks are acquired by Storport when the callback is invoked. The miniport is responsible for any synchronization required in the callback routine.

The name *HwStorWorkItem* is just a placeholder for the miniport function that is pointed to by the *Callback* parameter of [**StorPortQueueWorkItem**](storportqueueworkitem.md). The actual prototype of this routine is defined in *Storport.h* as follows:


```
typedef
VOID
HW_WORKITEM (
    _In_     PVOID HwDeviceExtension,
    _In_Opt_ PVOID Context,
    _In_     PVOID Worker,
    );
```



## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                                               |



## See also

<dl> <dt>

[**StorPortFreeWorker**](storportfreeworker.md)
</dt> <dt>

[**StorPortInitializeWorker**](storportinitializeworker.md)
</dt> <dt>

[**StorPortQueueWorkItem**](storportqueueworkitem.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_WORKITEM%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






