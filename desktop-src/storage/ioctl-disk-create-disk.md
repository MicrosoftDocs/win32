---
title: IOCTL\_DISK\_CREATE\_DISK control code
description: Creates an empty partition for the device object.
ms.assetid: 9ec6835c-43b8-4878-9ddf-1ca7c24435c2
keywords:
- IOCTL_DISK_CREATE_DISK control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_CREATE_DISK
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_DISK\_CREATE\_DISK control code

Creates an empty partition for the device object. It can operate on either an EFI disk or an MBR disk. The parameters necessary to create an empty disk depend on the type of partition table that will be put onto the disk. For more information, see [**CREATE\_DISK**](create-disk.md).

Disk drivers enumerate partitions as though they were child devices. Thus, upon creating the new partition, the disk class driver notifies the PnP manager by means of a call to **IoInvalidateDeviceRelations** that the disk device has a new child device (partition).

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the CREATE\_DISK data.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer made available to the driver, which must be &gt;= **sizeof**(CREATE\_DISK). Otherwise, the driver returns with an error status of STATUS\_INFO\_LENGTH\_MISMATCH.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS if the operation was successful. Other possible status values are: STATUS\_NOT\_SUPPORTED if the partition style requested is not supported; STATUS\_DEVICE\_NOT\_READY if the class driver failed to retrieve the disk geometry; and STATUS\_INSUFFICIENT\_RESOURCES if the class driver failed to obtain a necessary resource, such as heap memory.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**CREATE\_DISK**](create-disk.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_CREATE_DISK%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






