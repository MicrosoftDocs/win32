---
title: IOCTL\_MOUNTMGR\_VOLUME\_MOUNT\_POINT\_DELETED control code
description: The mount manager clients use this IOCTL to alert the mount manager that a volume mount point has been deleted so that the mount manager can replicate the database entry for the given mount point.
ms.assetid: 8a436053-87c2-4fa2-9280-7035a990d0b4
keywords:
- IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_DELETED control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_DELETED
api_location:
- Mountmgr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_MOUNTMGR\_VOLUME\_MOUNT\_POINT\_DELETED control code

The mount manager clients use this IOCTL to alert the mount manager that a volume mount point has been deleted so that the mount manager can replicate the database entry for the given mount point.

The Microsoft Win32 routine **DeleteVolumeMountPoint** sends this IOCTL to the mount manager, to inform the mount manager that a directory junction is no longer pointing to a volume name. The mount manager responds by deleting the volume name formerly contained in the directory junction along with its unique ID from the volume hosting the directory junction.

## Input Buffer

The mount manager client initializes the [**MOUNTMGR\_VOLUME\_MOUNT\_POINT**](mountmgr-volume-mount-point.md) structure, defined in *Mountmgr.h*, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to **sizeof**(MOUNTMGR\_VOLUME\_MOUNT\_POINT).

## Output Buffer

None

## Output Buffer Length

None

## Status block

If the operation is successful, the **Status** field is set to STATUS\_SUCCESS.

If **InputBufferLength** is less than **sizeof**(MOUNTMGR\_VOLUME\_MOUNT\_POINT), the **Status** field is set to STATUS\_INVALID\_PARAMETER.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**MOUNTMGR\_VOLUME\_MOUNT\_POINT**](mountmgr-volume-mount-point.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_DELETED%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






