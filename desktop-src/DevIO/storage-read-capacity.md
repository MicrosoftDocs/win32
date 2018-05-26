---
Description: Contains information about the size of a device. This is returned from the IOCTL\_STORAGE\_READ\_CAPACITY control code.
ms.assetid: c0a2c73c-fae9-40e9-8009-4dffbb03a01d
title: STORAGE\_READ\_CAPACITY structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_READ\_CAPACITY structure

Contains information about the size of a device. This is returned from the [**IOCTL\_STORAGE\_READ\_CAPACITY**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_read_capacity?branch=master) control code.

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

The version of this structure. The caller must set this member to `sizeof(STORAGE_READ_CAPACITY)`.

</dd> <dt>

**Size**
</dt> <dd>

The size of the data returned.

</dd> <dt>

**BlockLength**
</dt> <dd>

The number of bytes per block.

</dd> <dt>

**NumberOfBlocks**
</dt> <dd>

The total number of blocks on the disk.

</dd> <dt>

**DiskLength**
</dt> <dd>

The disk size in bytes.

</dd> </dl>

## Remarks

The header file Ntddstor.h is available in the Windows Driver Kit (WDK).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008, Windows Server 2003 with SP1<br/>                          |
| Header<br/>                   | <dl> <dt>Ntddstor.h</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_READ\_CAPACITY**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_read_capacity?branch=master)
</dt> </dl>

 

 




