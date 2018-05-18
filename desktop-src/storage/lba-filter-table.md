---
title: LBA\_FILTER\_TABLE structure
description: The LBA\_FILTER\_TABLE structure contains the LBA ranges whose access is controlled by a silo driver.
ms.assetid: '295EE3CC-4244-4411-9684-7C5D38B10EA9'
keywords: ["LBA_FILTER_TABLE structure Storage Devices", "PLBA_FILTER_TABLE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- LBA_FILTER_TABLE
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
---

# LBA\_FILTER\_TABLE structure

The **LBA\_FILTER\_TABLE** structure contains the LBA ranges whose access is controlled by a silo driver. The LBA filter entries in the table define bands on a storage device that are managed by a silo driver. A silo drivers send the LBA filter table to the enhanced storage class driver in an [**IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE**](ioctl-ehstor-driver-update-lba-filter-table.md) request.

## Syntax


```C++
typedef struct _LBA_FILTER_TABLE {
  ULONG   StructSize;
  BOOLEAN GlobalReadLock;
  ULONG   Reserved1;
  BOOLEAN GlobalWriteLock;
  ULONG   Reserved2;
  ULONG   LbaFilterCount;
  ULONG   LbaFilterSize;
  ULONG   LbaFilterOffset;
} LBA_FILTER_TABLE, *PLBA_FILTER_TABLE;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of this structure. This is set to **sizeof**(LBA\_FILTER\_TABLE).

</dd> <dt>

**GlobalReadLock**
</dt> <dd>

If TRUE, LBAs not included in the filter table are not readable. Otherwise unfiltered LBAs are readable if FALSE.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**GlobalWriteLock**
</dt> <dd>

If TRUE, LBAs not included in the filter table are not writeable. Otherwise unfiltered LBAs are writeable if FALSE.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**LbaFilterCount**
</dt> <dd>

The number of filter entries in the filter table.

</dd> <dt>

**LbaFilterSize**
</dt> <dd>

The size in bytes of a filter table entry. This must be set to **sizeof**(LBA\_FILTER\_TABLE\_ENTRY).

</dd> <dt>

**LbaFilterOffset**
</dt> <dd>

The offset of the LBA filter table from the beginning of this structure. This will typically be **sizeof**(LBA\_FILTER\_TABLE).

</dd> </dl>

## Remarks

LBA ranges not included in any filter table entries are considered part of the global band for the device. These ranges are managed independently by the Enhanced Storage Class driver. Access for these ranges is determined by the settings in *GlobalReadLock* and *GlobalWriteLock*.

Following the **LBA\_FILTER\_TABLE** structure is an array of 0 or more [**LBA\_FILTER\_TABLE\_ENTRY**](lba-filter-table-entry.md) structures. Each **LBA\_FILTER\_TABLE\_ENTRY** defines an individual band whose access is controlled by the silo driver through the direction of band management requests forwarded by the Enhanced Storage Class driver. **LBA\_FILTER\_TABLE\_ENTRY** structures can occur in any order, however, an LBA range in a table entry must not overlap with an LBA range from another table entry.

## Requirements



|                    |                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                     |
| Header<br/>  | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE**](ioctl-ehstor-driver-update-lba-filter-table.md)
</dt> <dt>

[**LBA\_FILTER\_TABLE\_ENTRY**](lba-filter-table-entry.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20LBA_FILTER_TABLE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






