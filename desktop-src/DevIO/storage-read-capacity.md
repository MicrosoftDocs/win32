---
description: Contains information about the size of a device. This is returned from the IOCTL\_STORAGE\_READ\_CAPACITY control code.
ms.assetid: 'bd18f4b7-f87e-48f6-b7c2-68990beb8d36'
title: STORAGE_READ_CAPACITY structure (Ntddstor.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- STORAGE_READ_CAPACITY
api_type: 
- HeaderDef
api_location: 
- Ntddstor.h
---

# STORAGE\_READ\_CAPACITY structure

Contains information about the size of a device. This is returned from the [**IOCTL\_STORAGE\_READ\_CAPACITY**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_read_capacity) control code.

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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008, Windows Server 2003 with SP1<br/>                          |
| Header<br/>                   | <dl> <dt>Ntddstor.h</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_READ\_CAPACITY**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_read_capacity)
</dt> </dl>

 

 




