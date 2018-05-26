---
title: DISK\_GEOMETRY structure
description: The DISK\_GEOMETRY structure is obsolete and provided only to support existing drivers.
ms.assetid: f92d1f63-4361-4775-88f8-be1c9bf781ef
keywords:
- DISK_GEOMETRY structure Storage Devices
- PDISK_GEOMETRY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DISK_GEOMETRY
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DISK\_GEOMETRY structure

The DISK\_GEOMETRY structure is obsolete and provided only to support existing drivers. New drivers must use [**DISK\_GEOMETRY\_EX**](disk-geometry-ex.md). DISK\_GEOMETRY is used in conjunction with the [**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY**](ioctl-disk-get-drive-geometry.md) and the [**IOCTL\_DISK\_GET\_MEDIA\_TYPES**](ioctl-disk-get-media-types.md) requests, in order to retrieve information about the geometry of a physical disk.

## Syntax


```C++
typedef struct _DISK_GEOMETRY {
  LARGE_INTEGER Cylinders;
  MEDIA_TYPE    MediaType;
  ULONG         TracksPerCylinder;
  ULONG         SectorsPerTrack;
  ULONG         BytesPerSector;
} DISK_GEOMETRY, *PDISK_GEOMETRY;
```



## Members

<dl> <dt>

**Cylinders**
</dt> <dd>

Indicates the number of cylinders on the disk device.

</dd> <dt>

**MediaType**
</dt> <dd>

Indicates the type of disk. The enumeration [**MEDIA\_TYPE**](media-type.md) lists the values that can be assigned to this member.

</dd> <dt>

**TracksPerCylinder**
</dt> <dd>

Indicates the number of tracks in a cylinder.

</dd> <dt>

**SectorsPerTrack**
</dt> <dd>

Indicates the number of sectors in each track.

</dd> <dt>

**BytesPerSector**
</dt> <dd>

Indicates the number of bytes in a disk sector.

</dd> </dl>

## Remarks

[**DISK\_GEOMETRY\_EX**](disk-geometry-ex.md) must be used with new drivers, in order to accommodate GUID Partition Table (GPT) partitions. The DISK\_GEOMETRY structure is nested within the DISK\_GEOMETRY\_EX structure.

[**IOCTL\_DISK\_GET\_MEDIA\_TYPES**](ioctl-disk-get-media-types.md) causes an array of these structures to be returned.

## Requirements



|                   |                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h, Ntddk.h, or Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_GEOMETRY\_EX**](disk-geometry-ex.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY**](ioctl-disk-get-drive-geometry.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_MEDIA\_TYPES**](ioctl-disk-get-media-types.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_GEOMETRY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






