---
title: StorPortGetLogicalUnit routine
description: The StorPortGetLogicalUnit routine returns a pointer to the miniport driver's per-logical-unit storage area.
ms.assetid: c8972d8b-9eba-4276-af63-1096a76b104f
keywords:
- StorPortGetLogicalUnit routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortGetLogicalUnit
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

# StorPortGetLogicalUnit routine

The **StorPortGetLogicalUnit** routine returns a pointer to the miniport driver's per-logical-unit storage area.

## Syntax


```C++
STORPORT_API PVOID StorPortGetLogicalUnit(
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

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver as soon as the miniport driver's [**HwStorFindAdapter**](hwstorfindadapter.md) routine is called. The port driver frees this memory when it removes the device.

</dd> <dt>

*PathId* \[in\]
</dt> <dd>

Identifies the SCSI bus.

</dd> <dt>

*TargetId* \[in\]
</dt> <dd>

Identifies the target controller or device on the bus.

</dd> <dt>

*Lun* \[in\]
</dt> <dd>

Identifies the logical unit (LU) number of the target device.

</dd> </dl>

## Return value

**StorPortGetLogicalUnit** returns a pointer to the miniport driver's storage area for the requested logical unit. If the logical unit does not exist, it returns **NULL**.

## Remarks

**StorPortGetLogicalUnit** is irrelevant if the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine specified zero for the **LuExtensionSize** in the [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md) when it called [**StorPortInitialize**](storportinitialize.md). Otherwise, the operating system-specific port driver allocates and initializes with zeros a set of LU extensions of the specified size for the miniport driver to use.

Per-LU storage can be used to store data relevant to a particular peripheral, such as saved data pointers. To access this area, the miniport driver calls **StorPortGetLogicalUnit** when the driver is maintaining information about the state of or current operation for any particular peripheral.

The operating system-specific port driver can consider a logical unit to be nonexistent if there is no active request for that logical unit and the device has never been successfully selected.

> [!Note]  
> When the miniport driver calls **StorPortGetLogicalUnit** at IRQL = DISPATCH\_LEVEL, the function acquires the interrupt lock. Calling **StorPortGetLogicalUnit** too often at this IRQL level impacts the performance and scalability of the miniport driver.

 

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows XP and later versions of the Windows operating systems.<br/>                                                 |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md)
</dt> <dt>

[**StorPortInitialize**](storportinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetLogicalUnit%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






