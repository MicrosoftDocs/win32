---
title: IOCTL\_CDROM\_GET\_DRIVE\_GEOMETRY\_EX control code
description: Returns information about a CD-ROM's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).The IOCTL\_CDROM\_GET\_DRIVE\_GEOMETRY\_EX request differs from the older IOCTL\_CDROM\_GET\_DRIVE\_GEOMETRY request.
ms.assetid: ef04ba90-698f-4ae2-9ac6-106d66b61080
keywords:
- IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_CDROM\_GET\_DRIVE\_GEOMETRY\_EX control code

Returns information about a CD-ROM's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).

The IOCTL\_CDROM\_GET\_DRIVE\_GEOMETRY\_EX request differs from the older [**IOCTL\_CDROM\_GET\_DRIVE\_GEOMETRY**](ioctl-cdrom-get-drive-geometry.md) request. The IOCTL\_CDROM\_GET\_DRIVE\_GEOMETRY\_EX request can retrieve information from both Master Boot Record (MBR) and GUID Partition Table (GPT) partitioned media. However, IOCTL\_CDROM\_GET\_DRIVE\_GEOMETRY can read only MBR-style media.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the [**DISK\_GEOMETRY\_EX**](disk-geometry-ex.md)-type information in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the IO\_STACK\_LOCATION structure of the IRP indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(DISK\_GEOMETRY\_EX).

## Status block

The **Information** field is set to the size, in bytes, of the returned data. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_UNRECOGNIZED\_MEDIA, STATUS\_INVALID\_PARAMETER, STATUS\_INFO\_LENGTH\_MISMATCH, or STATUS\_BUFFER\_TOO\_SMALL.

## Remarks

TBD

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_GEOMETRY\_EX**](disk-geometry-ex.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX**](ioctl-disk-get-drive-geometry-ex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






