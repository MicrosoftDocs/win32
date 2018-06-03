---
title: DISK\_EXTENT structure
description: The DISK\_EXTENT structure contains information defining the location and length of a volume extent on a disk.
ms.assetid: 74ffdfba-1b80-479d-9637-43222a438fa9
keywords:
- DISK_EXTENT structure Storage Devices
- PDISK_EXTENT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DISK_EXTENT
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

# DISK\_EXTENT structure

The DISK\_EXTENT structure contains information defining the location and length of a volume extent on a disk.

## Syntax


```C++
typedef struct _DISK_EXTENT {
  ULONG         DiskNumber;
  LARGE_INTEGER StartingOffset;
  LARGE_INTEGER ExtentLength;
} DISK_EXTENT, *PDISK_EXTENT;
```



## Members

<dl> <dt>

**DiskNumber**
</dt> <dd>

Specifies the number of the disk that contains this extent. This is the same disk number that is used to construct the name of the disk (for example, *PhysicalDriveX* or *HarddiskX*, where X is the disk number).

</dd> <dt>

**StartingOffset**
</dt> <dd>

Specifies the offset, in bytes, from the beginning of the disk.

</dd> <dt>

**ExtentLength**
</dt> <dd>

Specifies the number of bytes of this extent.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddvol.h (include Ntddvol.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_VOLUME\_GET\_VOLUME\_DISK\_EXTENTS**](ioctl-volume-get-volume-disk-extents.md)
</dt> <dt>

[**VOLUME\_DISK\_EXTENTS**](volume-disk-extents.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_EXTENT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






