---
title: MOUNTMGR\_VOLUME\_MOUNT\_POINT structure
description: The MOUNTMGR\_VOLUME\_MOUNT\_POINT structure is used in conjunction with the IOCTL\_MOUNTMGR\_VOLUME\_MOUNT\_POINT\_CREATED request to inform the mount manager that a volume mount point has been created.
ms.assetid: 2a267992-b4d3-49e1-bb80-3849220f0d1f
keywords:
- MOUNTMGR_VOLUME_MOUNT_POINT structure Storage Devices
- PMOUNTMGR_VOLUME_MOUNT_POINT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MOUNTMGR_VOLUME_MOUNT_POINT
api_location:
- mountmgr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MOUNTMGR\_VOLUME\_MOUNT\_POINT structure

The MOUNTMGR\_VOLUME\_MOUNT\_POINT structure is used in conjunction with the [**IOCTL\_MOUNTMGR\_VOLUME\_MOUNT\_POINT\_CREATED**](ioctl-mountmgr-volume-mount-point-created.md) request to inform the mount manager that a volume mount point has been created.

## Syntax


```C++
typedef struct _MOUNTMGR_VOLUME_MOUNT_POINT {
  USHORT SourceVolumeNameOffset;
  USHORT SourceVolumeNameLength;
  USHORT TargetVolumeNameOffset;
  USHORT TargetVolumeNameLength;
} MOUNTMGR_VOLUME_MOUNT_POINT, *PMOUNTMGR_VOLUME_MOUNT_POINT;
```



## Members

<dl> <dt>

**SourceVolumeNameOffset**
</dt> <dd>

Contains an offset, in bytes, into the output buffer where the name of the mount point is located.

</dd> <dt>

**SourceVolumeNameLength**
</dt> <dd>

Contains the length, in bytes, of the mount point name.

</dd> <dt>

**TargetVolumeNameOffset**
</dt> <dd>

Contains an offset, in bytes, into the output buffer where the unique (persistent) volume name of the target device is located.

</dd> <dt>

**TargetVolumeNameLength**
</dt> <dd>

Contains the length, in bytes, of the target name.

</dd> </dl>

## Remarks

Mount point names must contain the full path of a mount point object name in the system object tree. For example: "\\DosDevices\\E:\\FilesysD\\mnt". For an explanation of unique volume names and how the mount manager uses them, see [Supporting Mount Manager Requests in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff567603).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTMGR\_VOLUME\_MOUNT\_POINT\_CREATED**](ioctl-mountmgr-volume-mount-point-created.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MOUNTMGR_VOLUME_MOUNT_POINT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






