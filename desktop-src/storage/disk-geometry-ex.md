---
title: DISK\_GEOMETRY\_EX structure
description: The DISK\_GEOMETRY\_EX structure is a variable-length structure composed of a DISK\_GEOMETRY structure followed by a DISK\_PARTITION\_INFO structure followed, in turn, by a DISK\_DETECTION\_INFO structure.
ms.assetid: 6397c0dd-4dc7-49fa-85a7-841f6c2b30d8
keywords:
- DISK_GEOMETRY_EX structure Storage Devices
- PDISK_GEOMETRY_EX structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DISK_GEOMETRY_EX
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

# DISK\_GEOMETRY\_EX structure

The **DISK\_GEOMETRY\_EX** structure is a variable-length structure composed of a [**DISK\_GEOMETRY**](disk-geometry.md) structure followed by a [**DISK\_PARTITION\_INFO**](disk-partition-info.md) structure followed, in turn, by a [**DISK\_DETECTION\_INFO**](disk-detection-info.md) structure.

## Syntax


```C++
typedef struct _DISK_GEOMETRY_EX {
  DISK_GEOMETRY Geometry;
  LARGE_INTEGER DiskSize;
  UCHAR         Data[1];
} DISK_GEOMETRY_EX, *PDISK_GEOMETRY_EX;
```



## Members

<dl> <dt>

**Geometry**
</dt> <dd>

See [**DISK\_GEOMETRY**](disk-geometry.md) for a description of this member.

</dd> <dt>

**DiskSize**
</dt> <dd>

Contains the size in bytes of the disk.

</dd> <dt>

**Data**
</dt> <dd>

Pointer to a variable length area containing a [**DISK\_PARTITION\_INFO**](disk-partition-info.md) structure followed by a [**DISK\_DETECTION\_INFO**](disk-detection-info.md) structure.

</dd> </dl>

## Remarks

DISK\_GEOMETRY\_EX is used in conjunction with the [**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX**](ioctl-disk-get-drive-geometry-ex.md) and the [**IOCTL\_DISK\_GET\_MEDIA\_TYPES**](ioctl-disk-get-media-types.md) IOCTLs, in order to retrieve information about the geometry of a physical disk (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).

Because the partition and detect information are not at fixed locations within the **DISK\_GEOMETRY\_EX** structure, *ntdddisk.h* provides two macros for accessing this information. Both macros take a pointer to a structure of type **DISK\_GEOMETRY\_EX** as an argument:

``` syntax
#if (NTDDI_VERSION < NTDDI_WS03)
#define DiskGeometryGetPartition(Geometry)\
                        ((PDISK_PARTITION_INFO)((Geometry)+1))

#define DiskGeometryGetDetect(Geometry)\
                        ((PDISK_DETECTION_INFO)(((PBYTE)DiskGeometryGetPartition(Geometry)+\
                                        DiskGeometryGetPartition(Geometry)->SizeOfPartitionInfo)))
#else
#define DiskGeometryGetPartition(Geometry)\
                        ((PDISK_PARTITION_INFO)((Geometry)->Data))

#define DiskGeometryGetDetect(Geometry)\
                        ((PDISK_DETECTION_INFO)(((ULONG_PTR)DiskGeometryGetPartition(Geometry)+\
                                        DiskGeometryGetPartition(Geometry)->SizeOfPartitionInfo)))
#endif
```

## Requirements



|                   |                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h, Ntddk.h, or Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_GEOMETRY**](disk-geometry.md)
</dt> <dt>

[**DISK\_PARTITION\_INFO**](disk-partition-info.md)
</dt> <dt>

[**DISK\_DETECTION\_INFO**](disk-detection-info.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY**](ioctl-disk-get-drive-geometry.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_MEDIA\_TYPES**](ioctl-disk-get-media-types.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_GEOMETRY_EX%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






