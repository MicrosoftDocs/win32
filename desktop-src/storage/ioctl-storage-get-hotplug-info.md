---
title: IOCTL\_STORAGE\_GET\_HOTPLUG\_INFO control code
description: Retrieves the hotplug configuration of the specified device.
ms.assetid: e549aa75-d847-4276-ab40-29214b0475cf
keywords:
- IOCTL_STORAGE_GET_HOTPLUG_INFO control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_GET_HOTPLUG_INFO
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_STORAGE\_GET\_HOTPLUG\_INFO control code

Retrieves the hotplug configuration of the specified device.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the hotplug configuration data in a [**STORAGE\_HOTPLUG\_INFO**](storage-hotplug-info.md) structure in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be greater than or equal to **sizeof**(STORAGE\_HOTPLUG\_INFO).

## Status block

The **Information** field is set to **sizeof**(STORAGE\_HOTPLUG\_INFO). The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_BUFFER\_TOO\_SMALL if the output buffer is too small.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_SET\_HOTPLUG\_INFO**](ioctl-storage-set-hotplug-info.md)
</dt> <dt>

[**STORAGE\_HOTPLUG\_INFO**](storage-hotplug-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_GET_HOTPLUG_INFO%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






