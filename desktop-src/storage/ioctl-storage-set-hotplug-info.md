---
title: IOCTL\_STORAGE\_SET\_HOTPLUG\_INFO control code
description: Sets the hotplug configuration of the specified device.
ms.assetid: 5badc919-8663-4905-aaec-70f6b51ab2f1
keywords:
- IOCTL_STORAGE_SET_HOTPLUG_INFO control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_SET_HOTPLUG_INFO
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_SET\_HOTPLUG\_INFO control code

Sets the hotplug configuration of the specified device. This request takes a [**STORAGE\_HOTPLUG\_INFO**](storage-hotplug-info.md) structure as input. The **DeviceHotplug** member of the STORAGE\_HOTPLUG\_INFO structure determines what action is taken. If the value of that member is nonzero, the value for the device's removal policy in the registry is set to **ExpectSurpriseRemoval** and all levels of caching are disabled. If the value of **DeviceHotplug** is zero, the removal policy is set to **ExpectOrderlyRemoval**, and caching might be selectively enabled.

## Input Buffer

The input buffer.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be greater than or equal to **sizeof**(STORAGE\_HOTPLUG\_INFO).

## Output Buffer

The driver returns the hotplug configuration data in a STORAGE\_HOTPLUG\_INFO structure in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

The length of a [**STORAGE\_HOTPLUG\_INFO**](storage-hotplug-info.md) structure.

## Status block

The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INFO\_LENGTH\_MISMATCH if the input buffer is too small. It is set to STATUS\_INVALID\_PARAMETER\_1 if the **Size** member of STORAGE\_HOTPLUG\_INFO is not the size expected by the class driver for this device. It is set to STATUS\_INVALID\_PARAMETER\_2 if the **MediaRemoveable** member has a value different from that held by the class driver. It is set to STATUS\_INVALID\_PARAMETER\_3 if the **MediaHotplug** member has a value different from that held by the class driver, and it is set to STATUS\_INVALID\_PARAMETER\_5 if the **WriteCacheEnableOverride** member has a value different from that held by the class driver.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_GET\_HOTPLUG\_INFO**](ioctl-storage-get-hotplug-info.md)
</dt> <dt>

[**STORAGE\_HOTPLUG\_INFO**](storage-hotplug-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_SET_HOTPLUG_INFO%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






