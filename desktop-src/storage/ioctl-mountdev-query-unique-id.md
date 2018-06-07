---
title: IOCTL\_MOUNTDEV\_QUERY\_UNIQUE\_ID control code
description: Support for this IOCTL by mount manager clients is mandatory.
ms.assetid: 866b9383-d73d-4be1-a4de-b78c9558c3ce
keywords:
- IOCTL_MOUNTDEV_QUERY_UNIQUE_ID control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_MOUNTDEV_QUERY_UNIQUE_ID
api_location:
- Mountdev.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_MOUNTDEV\_QUERY\_UNIQUE\_ID control code

Support for this IOCTL by mount manager clients is mandatory. Upon receiving this IOCTL, the mount manager client must provide a counted byte string identifier that is unique to the client (that is, the device or the volume). The client cannot change this unique ID without alerting the mount manager (see [**IOCTL\_MOUNTDEV\_UNIQUE\_ID\_CHANGE\_NOTIFY**](https://msdn.microsoft.com/library/windows/hardware/ff560443)).

## Output Buffer

The device class or volume driver returns the [**MOUNTDEV\_UNIQUE\_ID**](mountdev-unique-id.md) structure in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer, which must be greater than or equal to **sizeof**(MOUNTDEV\_UNIQUE\_ID).

## Status block

The **Information** field is set to FIELD\_OFFSET([**MOUNTDEV\_UNIQUE\_ID**](mountdev-unique-id.md), UniqueId) + output-&gt;UniqueIdLength; or alternatively to sizeof(USHORT) + output-&gt;UniqueIdLength, where output points to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountdev.h (include Mountdev.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTDEV\_UNIQUE\_ID\_CHANGE\_NOTIFY**](https://msdn.microsoft.com/library/windows/hardware/ff560443)
</dt> <dt>

[**MOUNTDEV\_UNIQUE\_ID**](mountdev-unique-id.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTDEV_QUERY_UNIQUE_ID%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






