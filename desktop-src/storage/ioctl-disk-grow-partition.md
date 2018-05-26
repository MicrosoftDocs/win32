---
title: IOCTL\_DISK\_GROW\_PARTITION control code
description: Increases the size of an existing partition.
ms.assetid: 984e9e7a-c135-4a6a-973d-b8597d9f8fed
keywords:
- IOCTL_DISK_GROW_PARTITION control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_GROW_PARTITION
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_DISK\_GROW\_PARTITION control code

Increases the size of an existing partition. It is used in conjunction with [**IOCTL\_DISK\_UPDATE\_DRIVE\_SIZE**](ioctl-disk-update-drive-size.md) to extend a disk, so that it will contain a new free space area, and then to extend an existing partition on the disk into the newly attached free space. It takes a [**DISK\_GROW\_PARTITION**](disk-grow-partition.md) structure as the only parameter. For this operation to work, the space after the specified partition must be free. A partition cannot be extended over another existing partition.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the [**DISK\_GROW\_PARTITION**](disk-grow-partition.md) values - that will be used to increase the size of the partition.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer made available to the driver, which must be &gt;= **sizeof**(DISK\_GROW\_PARTITION). Otherwise, the driver returns with an error status of STATUS\_BUFFER\_TOO\_SMALL.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_BUFFER\_TOO\_SMALL, STATUS\_INVALID\_PARAMETER, STATUS\_UNSUCCESSFUL, or STATUS\_DRIVER\_INTERNAL\_ERROR.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_GROW\_PARTITION**](disk-grow-partition.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_GROW_PARTITION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






