---
title: StorPortDeviceBusy routine
description: The StorPortDeviceBusy routine notifies the port driver that the specified logical unit is currently busy, handling outstanding requests.
ms.assetid: 9b774f05-f2f6-4148-8fee-0efe209f7e4d
keywords:
- StorPortDeviceBusy routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortDeviceBusy
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortDeviceBusy routine

The **StorPortDeviceBusy** routine notifies the port driver that the specified logical unit is currently busy, handling outstanding requests.

## Syntax


```C++
STORPORT_API BOOLEAN StorPortDeviceBusy(
  _In_ PVOID HwDeviceExtension,
  _In_ UCHAR PathId,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun,
  _In_ ULONG RequestsToComplete
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*PathId* \[in\]
</dt> <dd>

Identifies the SCSI bus.

</dd> <dt>

*TargetId* \[in\]
</dt> <dd>

Identifies the target controller or device on the given buses.

</dd> <dt>

*Lun* \[in\]
</dt> <dd>

Identifies the logical unit for the given target controller or device.

</dd> <dt>

*RequestsToComplete* \[in\]
</dt> <dd>

Indicates the number of requests that the logical unit must complete before resuming I/O requests to the miniport driver. If *RequestsToComplete* is greater than the number of currently outstanding requests, the Storport driver will complete all outstanding requests to the logical unit before resuming requests.

</dd> </dl>

## Return value

**StorPortDeviceBusy** returns **TRUE** if the miniport driver succeeded in notifying the port driver, **FALSE** if not.

## Remarks

No error log is generated when a device is busy.

The port driver will not issue any new requests to the logical unit until the logical unit's queue has been drained to a sufficient level where processing can continue.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**StorPortBusy**](storportbusy.md)
</dt> <dt>

[**StorPortReady**](storportready.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortDeviceBusy%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






