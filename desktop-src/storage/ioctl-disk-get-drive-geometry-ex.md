---
title: IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX control code
description: Returns information about the physical disk's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).The difference between IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX and the older IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY request is that IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX can retrieve information from both Master Boot Record (MBR) and GUID Partition Table (GPT)-type partitioned media, whereas IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY can only read MBR-style media.
ms.assetid: c0cf6b73-3283-4a58-845a-79f3b078db46
keywords:
- IOCTL_DISK_GET_DRIVE_GEOMETRY_EX control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_GET_DRIVE_GEOMETRY_EX
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

# IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX control code

Returns information about the physical disk's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).

The difference between IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX and the older [**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY**](ioctl-disk-get-drive-geometry.md) request is that IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX can retrieve information from both Master Boot Record (MBR) and GUID Partition Table (GPT)-type partitioned media, whereas IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY can only read MBR-style media.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the [**DISK\_GEOMETRY\_EX**](disk-geometry-ex.md) data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The size of the output buffer may not be the same size as the input buffer.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be at least (**sizeof**(DISK\_GEOMETRY) + **sizeof**(LARGE\_INTEGER)) and up to (**sizeof**(DISK\_GEOMETRY) + **sizeof**(LARGE\_INTEGER) + **sizeof**(DISK\_PARTITION\_INFO) + **sizeof**(DISK\_DETECTION\_INFO)).

## Status block

The **Information** field is set to the size, in bytes, of the returned data.

The **Status** field returns one of the following values:

-   **STATUS\_SUCCESS**
-   **STATUS\_UNRECOGNIZED\_MEDIA**
-   **STATUS\_INVALID\_PARAMETER**
-   **STATUS\_INVALID\_DEVICE\_REQUEST**
-   **STATUS\_INFO\_LENGTH\_MISMATCH**
-   **STATUS\_INSUFFICIENT\_RESOURCES**
-   **STATUS\_BUFFER\_TOO\_SMALL**

## Remarks

Only callers above Partmgr.sys may call this IOCTL as it contains disk partition information.

This IOCTL uses [**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY**](https://msdn.microsoft.com/library/windows/hardware/ff560357) to get the [**DISK\_GEOMETRY**](disk-geometry.md) structure and [**IOCTL\_DISK\_GET\_LENGTH\_INFO**](ioctl-disk-get-length-info.md) to get the [**GET\_LENGTH\_INFORMATION**](get-length-information.md) structure. Both of these IOCTL's are supported for use at the disk.sys level.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_GET_DRIVE_GEOMETRY_EX%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





