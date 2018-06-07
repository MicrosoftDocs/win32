---
title: STORAGE\_READ\_CAPACITY structure
description: The STORAGE\_READ\_CAPACITY contains the disk read capacity information returned from a IOCTL\_STORAGE\_READ\_CAPACITIY request.
ms.assetid: FC4CFD33-5632-400A-90E5-583C6D6DFFD9
keywords:
- STORAGE_READ_CAPACITY structure Storage Devices
- PSTORAGE_READ_CAPACITY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_READ_CAPACITY
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STORAGE\_READ\_CAPACITY structure

The **STORAGE\_READ\_CAPACITY** contains the disk read capacity information returned from a [**IOCTL\_STORAGE\_READ\_CAPACITIY**](ioctl-storage-read-capacity.md) request.

## Syntax


```C++
typedef struct _STORAGE_READ_CAPACITY {
  ULONG         Version;
  ULONG         Size;
  ULONG         BlockLength;
  LARGE_INTEGER NumberOfBlocks;
  LARGE_INTEGER DiskLength;
} STORAGE_READ_CAPACITY, *PSTORAGE_READ_CAPACITY;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. Set to **sizeof**(STORAGE\_READ\_CAPACITY).

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure. Set to **sizeof**(STORAGE\_READ\_CAPACITY).

</dd> <dt>

**BlockLength**
</dt> <dd>

The number of bytes per block on disk.

</dd> <dt>

**NumberOfBlocks**
</dt> <dd>

The total number of blocks on the disk.

</dd> <dt>

**DiskLength**
</dt> <dd>

The total disk size in bytes.

</dd> </dl>

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                              |
| Header<br/>  | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_READ\_CAPACITIY**](ioctl-storage-read-capacity.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_READ_CAPACITY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






