---
title: MOUNTMGR\_MOUNT\_POINTS structure
description: The MOUNTMGR\_MOUNT\_POINTS structure is used by mount manager to send a client the list of mount points associated with a device.
ms.assetid: 'e85c0d92-d989-4afc-8516-c63535d2c728'
keywords: ["MOUNTMGR_MOUNT_POINTS structure Storage Devices", "PMOUNTMGR_MOUNT_POINTS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MOUNTMGR_MOUNT_POINTS
api_location:
- mountmgr.h
api_type:
- HeaderDef
---

# MOUNTMGR\_MOUNT\_POINTS structure

The MOUNTMGR\_MOUNT\_POINTS structure is used by mount manager to send a client the list of mount points associated with a device.

## Syntax


```C++
typedef struct _MOUNTMGR_MOUNT_POINTS {
  ULONG                Size;
  ULONG                NumberOfMountPoints;
  MOUNTMGR_MOUNT_POINT MountPoints[1];
} MOUNTMGR_MOUNT_POINTS, *PMOUNTMGR_MOUNT_POINTS;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Contains the size, in bytes, of the output buffer.

</dd> <dt>

**NumberOfMountPoints**
</dt> <dd>

Contains the number of mount points that the mount manager is returning.

</dd> <dt>

**MountPoints**
</dt> <dd>

Contains an array of elements of type MOUNTMGR\_MOUNT\_POINT that contain information about each mount point associated with the device.

</dd> </dl>

## Remarks

For a discussion of the different between symbolic links, unique IDs, and nonpersistent device names, see [Supporting Mount Manager Requests in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff567603).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MOUNTMGR_MOUNT_POINTS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






