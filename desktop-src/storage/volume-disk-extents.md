---
title: VOLUME\_DISK\_EXTENTS structure
description: The VOLUME\_DISK\_EXTENTS structure is used in conjunction with the IOCTL\_VOLUME\_GET\_VOLUME\_DISK\_EXTENTS request to retrieve information about all the extents on a given volume.
ms.assetid: d831ea36-16ee-4723-95b1-f9903106b7c0
keywords:
- VOLUME_DISK_EXTENTS structure Storage Devices
- PVOLUME_DISK_EXTENTS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- VOLUME_DISK_EXTENTS
api_location:
- ntddvol.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# VOLUME\_DISK\_EXTENTS structure

The VOLUME\_DISK\_EXTENTS structure is used in conjunction with the [**IOCTL\_VOLUME\_GET\_VOLUME\_DISK\_EXTENTS**](ioctl-volume-get-volume-disk-extents.md) request to retrieve information about all the extents on a given volume.

## Syntax


```C++
typedef struct _VOLUME_DISK_EXTENTS {
  ULONG       NumberOfDiskExtents;
  DISK_EXTENT Extents[ANYSIZE_ARRAY];
} VOLUME_DISK_EXTENTS, *PVOLUME_DISK_EXTENTS;
```



## Members

<dl> <dt>

**NumberOfDiskExtents**
</dt> <dd>

Indicates the number of extents that comprise the volume, which can span multiple disks.

</dd> <dt>

**Extents**
</dt> <dd>

Indicates the number of extents that comprise the volume, which can span multiple disks.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddvol.h (include Ntddvol.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_EXTENT**](disk-extent.md)
</dt> <dt>

[**IOCTL\_VOLUME\_GET\_VOLUME\_DISK\_EXTENTS**](ioctl-volume-get-volume-disk-extents.md)
</dt> <dt>

disk extent
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20VOLUME_DISK_EXTENTS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






