---
title: StorPortDeviceReady routine
description: The StorPortDeviceReady routine notifies the port driver that the indicated logical unit is ready to handle new requests.
ms.assetid: 6dd3abdb-9037-4cf5-abe7-7776dcf67bd5
keywords:
- StorPortDeviceReady routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortDeviceReady
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortDeviceReady routine

The **StorPortDeviceReady** routine notifies the port driver that the indicated logical unit is ready to handle new requests.

## Syntax


```C++
STORPORT_API BOOLEAN StorPortDeviceReady(
  _In_ PVOID HwDeviceExtension,
  _In_ UCHAR PathId,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun
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

</dd> </dl>

## Return value

**StorPortDeviceReady** returns **TRUE** if the miniport driver succeeded in notifying the port driver, **FALSE** if not.

## Remarks

It is not generally necessary to notify the target device that new requests are required.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**StorPortDeviceBusy**](storportdevicebusy.md)
</dt> <dt>

[**StorPortReady**](storportready.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortDeviceReady%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






