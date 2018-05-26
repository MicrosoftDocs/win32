---
title: StorPortSetDeviceQueueDepth routine
description: The StorPortSetDeviceQueueDepth routine sets the maximum depth of the device queue for the indicated device.
ms.assetid: e79b4294-5ba4-4fcc-97e2-69613b65f574
keywords:
- StorPortSetDeviceQueueDepth routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortSetDeviceQueueDepth
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

# StorPortSetDeviceQueueDepth routine

The **StorPortSetDeviceQueueDepth** routine sets the maximum depth of the device queue for the indicated device.

## Syntax


```C++
STORPORT_API BOOLEAN StorPortSetDeviceQueueDepth(
  _In_ PVOID HwDeviceExtension,
  _In_ UCHAR PathId,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun,
  _In_ ULONG Depth
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*PathId* \[in\]
</dt> <dd>

Contains the path ID of the target device.

</dd> <dt>

*TargetId* \[in\]
</dt> <dd>

Contains the device number of the target device.

</dd> <dt>

*Lun* \[in\]
</dt> <dd>

Contains the logical unit number of the target device.

</dd> <dt>

*Depth* \[in\]
</dt> <dd>

Supplies the depth to which the queue is to be set. This value is always &gt; 0.

</dd> </dl>

## Return value

**StorPortSetDeviceQueueDepth** returns **TRUE** if the queue depth was successfully set, or **FALSE** if the operation failed.

## Remarks

Before the first call to **StorPortSetDeviceQueueDepth**, the device queue depth is set to the default value. The following conditional description determines the default queue depth.

<dl> If the **InitialQueueDepth** member of the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure is non-zero, the default depth will be the value of **InitialQueueDepth**.  
Otherwise, if the **MaxIOsPerLun** member of the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure is non-zero, the default depth will be the value of **MaxIOsPerLun**.  
Otherwise, the default depth is 250 for virtual miniports and 20 for physical miniports. Unless a device supports extended SRBs, the maximum queue depth is 255.  
</dl>

The **StorPortSetDeviceQueueDepth** routine should be called when the miniport driver receives the first SCSI Inquiry command for the specified LUN, or at any time thereafter (but not before), as long as the LUN is valid.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortSetDeviceQueueDepth%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





