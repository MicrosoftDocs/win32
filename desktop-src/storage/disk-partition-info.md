---
title: DISK\_PARTITION\_INFO structure
description: The DISK\_PARTITION\_INFO structure is used to report information about the disk's partition table.
ms.assetid: 14df0604-39cd-4743-a051-894d63f4417c
keywords:
- DISK_PARTITION_INFO structure Storage Devices
- PDISK_PARTITION_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DISK_PARTITION_INFO
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DISK\_PARTITION\_INFO structure

The **DISK\_PARTITION\_INFO** structure is used to report information about the disk's partition table.

## Syntax


```C++
typedef struct _DISK_PARTITION_INFO {
  ULONG           SizeOfPartitionInfo;
  PARTITION_STYLE PartitionStyle;
  union {
    struct {
      ULONG Signature;
      ULONG CheckSum;
    } Mbr;
    struct {
      GUID DiskId;
    } Gpt;
  };
} DISK_PARTITION_INFO, *PDISK_PARTITION_INFO;
```



## Members

<dl> <dt>

**SizeOfPartitionInfo**
</dt> <dd>

Size of this structure in bytes. Set to **sizeof**(DISK\_PARTITION\_INFO).

</dd> <dt>

**PartitionStyle**
</dt> <dd>

Takes a [**PARTITION\_STYLE**](partition-style.md) enumerated value that specifies the type of partition table the disk contains.

</dd> <dt>

**Mbr**
</dt> <dd>

If **PartitionStyle** == MBR

<dl> <dt>

**Signature**
</dt> <dd>

Specifies the signature value, which uniquely identifies the disk. The **Mbr** member of the union is used to specify the disk signature data for a disk formatted with a Master Boot Record (MBR) format partition table. Any other value indicates that the partition is not a boot partition. This member is valid when **PartitionStyle** is **PARTITION\_STYLE\_MBR**.

</dd> <dt>

**CheckSum**
</dt> <dd>

Specifies the checksum for the master boot record. The **Mbr** member of the union is used to specify the disk signature data for a disk formatted with a Master Boot Record (MBR) format partition table. This member is valid when **PartitionStyle** is **PARTITION\_STYLE\_MBR**.

</dd> </dl> </dd> <dt>

**Gpt**
</dt> <dd>

If **PartitionStyle** == GPT

<dl> <dt>

**DiskId**
</dt> <dd>

Specifies the GUID that uniquely identifies the disk. The **Gpt** member of the union is used to specify the disk signature data for a disk that is formatted with a GUID Partition Table (GPT) format partition table. This member is valid when **PartitionStyle** is **PARTITION\_STYLE\_GPT**. The GUID data type is described on the [Using GUIDs in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff565392) reference page.

</dd> </dl> </dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_GEOMETRY\_EX**](disk-geometry-ex.md)
</dt> <dt>

[**PARTITION\_STYLE**](partition-style.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_PARTITION_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






