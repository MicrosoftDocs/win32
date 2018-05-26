---
title: DISK\_COPY\_DATA\_PARAMETERS structure
description: DISK\_COPY\_DATA\_PARAMETERS is used with IOCTL\_DISK\_COPY\_DATA to copy data from one area of the disk to another.
ms.assetid: 17d75b0e-2521-441f-99ea-75d2ea1d52b3
keywords:
- DISK_COPY_DATA_PARAMETERS structure Storage Devices
- PDISK_COPY_DATA_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DISK_COPY_DATA_PARAMETERS
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

# DISK\_COPY\_DATA\_PARAMETERS structure

DISK\_COPY\_DATA\_PARAMETERS is used with IOCTL\_DISK\_COPY\_DATA to copy data from one area of the disk to another.

## Syntax


```C++
typedef struct _DISK_COPY_DATA_PARAMETERS {
  LARGE_INTEGER SourceOffset;
  LARGE_INTEGER DestinationOffset;
  LARGE_INTEGER CopyLength;
  ULONGLONG     Reserved;
} DISK_COPY_DATA_PARAMETERS, *PDISK_COPY_DATA_PARAMETERS;
```



## Members

<dl> <dt>

**SourceOffset**
</dt> <dd>

Contains the byte offset of the source for the copy. This number must be sector-aligned.

</dd> <dt>

**DestinationOffset**
</dt> <dd>

Contains the byte offset of the destination of the copy. This number must be sector-aligned.

</dd> <dt>

**CopyLength**
</dt> <dd>

Contains the number of bytes to copy. This number must be sector-aligned.

</dd> <dt>

**Reserved**
</dt> <dd>

Must be zero.

</dd> </dl>

## Remarks

The source and destination areas must not overlap.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_COPY\_DATA**](ioctl-disk-copy-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_COPY_DATA_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






