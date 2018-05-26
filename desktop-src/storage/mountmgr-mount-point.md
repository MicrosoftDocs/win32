---
title: MOUNTMGR\_MOUNT\_POINT structure
description: The MOUNTMGR\_MOUNT\_POINT structure is used by mount manager clients in conjunction with an IOCTL\_MOUNTMGR\_QUERY\_POINTS request to query the mount manager for all of the mount points (symbolic links) associated with a device.
ms.assetid: a4142380-1596-49dc-a18d-ac5c3cef73fe
keywords:
- MOUNTMGR_MOUNT_POINT structure Storage Devices
- PMOUNTMGR_MOUNT_POINT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MOUNTMGR_MOUNT_POINT
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

# MOUNTMGR\_MOUNT\_POINT structure

The MOUNTMGR\_MOUNT\_POINT structure is used by mount manager clients in conjunction with an [**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md) request to query the mount manager for all of the mount points (symbolic links) associated with a device. The mount manager responds by sending an array of MOUNTMGR\_MOUNT\_POINT structures containing the mount points.

## Syntax


```C++
typedef struct _MOUNTMGR_MOUNT_POINT {
  ULONG  SymbolicLinkNameOffset;
  USHORT SymbolicLinkNameLength;
  ULONG  UniqueIdOffset;
  USHORT UniqueIdLength;
  ULONG  DeviceNameOffset;
  USHORT DeviceNameLength;
} MOUNTMGR_MOUNT_POINT, *PMOUNTMGR_MOUNT_POINT;
```



## Members

<dl> <dt>

**SymbolicLinkNameOffset**
</dt> <dd>

Contains an offset, in bytes, into the output buffer where the symbolic link is located.

</dd> <dt>

**SymbolicLinkNameLength**
</dt> <dd>

Contains the length, in bytes, of the symbolic link.

</dd> <dt>

**UniqueIdOffset**
</dt> <dd>

Contains an offset, in bytes, into the output buffer where the unique ID is located.

</dd> <dt>

**UniqueIdLength**
</dt> <dd>

Contains the length, in bytes, of the unique ID.

</dd> <dt>

**DeviceNameOffset**
</dt> <dd>

Contains an offset, in bytes, into the output buffer where the nonpersistent device name is located.

</dd> <dt>

**DeviceNameLength**
</dt> <dd>

Contains the length, in bytes, of the nonpersistent device name.

</dd> </dl>

## Remarks

None of the names returned are **NULL** terminated, nor do the buffers require terminating **NULL** characters. The caller of [**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md) is not required to provide data in all of the members of the MOUNTMGR\_MOUNT\_POINT structure, but empty members must have an offset of zero.

On input, offsets are from the beginning of the MOUNTMGR\_MOUNT\_POINT structure. On output offsets are from the beginning of the buffer. This is usually the same as the beginning of the [**MOUNTMGR\_MOUNT\_POINTS**](mountmgr-mount-points.md) container structure (as opposed to the embedded MOUNTMGR\_MOUNT\_POINT array instance).

The [**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md) request is available in Windows 2000 and later operating systems.

For a discussion of the different between symbolic links, unique IDs, and nonpersistent device names, see [Supporting Mount Manager Requests in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff567603).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MOUNTMGR_MOUNT_POINT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






