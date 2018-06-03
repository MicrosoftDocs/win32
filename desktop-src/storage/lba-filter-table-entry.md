---
title: LBA\_FILTER\_TABLE\_ENTRY structure
description: The LBA\_FILTER\_TABLE\_ENTRY structure contains an individual LBA range for the LBA\_FILTER\_TABLE sent in an IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE request.
ms.assetid: 092B54D7-FFEA-48BB-993E-14443BD0C7AA
keywords:
- LBA_FILTER_TABLE_ENTRY structure Storage Devices
- PLBA_FILTER_TABLE_ENTRY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- LBA_FILTER_TABLE_ENTRY
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# LBA\_FILTER\_TABLE\_ENTRY structure

The **LBA\_FILTER\_TABLE\_ENTRY** structure contains an individual LBA range for the [**LBA\_FILTER\_TABLE**](lba-filter-table.md) sent in an [**IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE**](ioctl-ehstor-driver-update-lba-filter-table.md) request.

## Syntax


```C++
typedef struct _LBA_FILTER_TABLE_ENTRY {
  ULARGE_INTEGER StartLba;
  ULARGE_INTEGER LbaCount;
  BOOLEAN        ReadLock;
  BOOLEAN        WriteLock;
} LBA_FILTER_TABLE_ENTRY, *PLBA_FILTER_TABLE_ENTRY;
```



## Members

<dl> <dt>

**StartLba**
</dt> <dd>

The starting LBA of the LBA range for this entry.

</dd> <dt>

**LbaCount**
</dt> <dd>

The number of LBAs in the LBA range.

</dd> <dt>

**ReadLock**
</dt> <dd>

Set to TRUE if the LBA range in this entry is not readable. Otherwise, this member is FALSE and the LBA range is readable.

</dd> <dt>

**WriteLock**
</dt> <dd>

Set to TRUE if the LBA range in this entry is not writeable. Otherwise, this member is FALSE and the LBA range is writable

</dd> </dl>

## Remarks

An LBA range is valid only if LbaCount is &gt; 0 and it is not overlapping with another entry in [**LBA\_FILTER\_TABLE**](lba-filter-table.md).

## Requirements



|                    |                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                     |
| Header<br/>  | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE**](ioctl-ehstor-driver-update-lba-filter-table.md)
</dt> <dt>

[**LBA\_FILTER\_TABLE**](lba-filter-table.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20LBA_FILTER_TABLE_ENTRY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






