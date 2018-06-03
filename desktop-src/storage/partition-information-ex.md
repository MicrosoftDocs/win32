---
title: PARTITION\_INFORMATION\_EX structure
description: PARTITION\_INFORMATION\_EX is the extended version of the PARTITION\_INFORMATION structure. It holds information both for partitions with a Master Boot Record and for partitions with a GUID Partition Table.
ms.assetid: de44fe5a-5d47-4b2e-ab94-52cadfdbc345
keywords:
- PARTITION_INFORMATION_EX structure Storage Devices
- PPARTITION_INFORMATION_EX structure pointer Storage Devices
topic_type:
- apiref
api_name:
- PARTITION_INFORMATION_EX
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

# PARTITION\_INFORMATION\_EX structure

PARTITION\_INFORMATION\_EX is the extended version of the [**PARTITION\_INFORMATION**](partition-information.md) structure. It holds information both for partitions with a Master Boot Record and for partitions with a GUID Partition Table.

## Syntax


```C++
typedef struct _PARTITION_INFORMATION_EX {
  PARTITION_STYLE PartitionStyle;
  LARGE_INTEGER   StartingOffset;
  LARGE_INTEGER   PartitionLength;
  ULONG           PartitionNumber;
  BOOLEAN         RewritePartition;
  union {
    PARTITION_INFORMATION_MBR Mbr;
    PARTITION_INFORMATION_GPT Gpt;
  };
} PARTITION_INFORMATION_EX, *PPARTITION_INFORMATION_EX;
```



## Members

<dl> <dt>

**PartitionStyle**
</dt> <dd>

Takes a [**PARTITION\_STYLE**](partition-style.md) enumerated value that specifies the type of partition table that contains the partition.

</dd> <dt>

**StartingOffset**
</dt> <dd>

Specifies the offset in bytes on drive where the partition begins.

</dd> <dt>

**PartitionLength**
</dt> <dd>

Specifies the length in bytes of the partition.

</dd> <dt>

**PartitionNumber**
</dt> <dd>

Specifies the number of the partition.

</dd> <dt>

**RewritePartition**
</dt> <dd>

Indicates, when **TRUE**, that the partition information has changed. When **FALSE**, the information has not changed. This member has a value of **TRUE** when the partition has changed as a result of an [**IOCTL\_DISK\_SET\_DRIVE\_LAYOUT**](ioctl-disk-set-drive-layout.md) IOCTL. This informs the system that the partition information needs to be rewritten.

</dd> <dt>

**Mbr**
</dt> <dd>

Contains a structure of type [**PARTITION\_INFORMATION\_MBR**](partition-information-mbr.md) containing information specific to a partition with a **PartitionStyle** member of PARTITION\_STYLE\_MBR.

</dd> <dt>

**Gpt**
</dt> <dd>

Contains a structure of type [**PARTITION\_INFORMATION\_GPT**](partition-information-gpt.md) containing information specific to a partition with a **PartitionStyle** member of PARTITION\_STYLE\_GPT.

</dd> </dl>

## Remarks

This is the extended version of the partition information structure, PARTITION\_INFORMATION. [**IoReadPartitionTableEx**](ioreadpartitiontableex.md) and [**IoWritePartitionTableEx**](iowritepartitiontableex.md) operate on an array of PARTITON\_INFORMATION\_EX structures contained within the extended drive layout structure, [**DRIVE\_LAYOUT\_INFORMATION\_EX**](drive-layout-information-ex.md). PARTITION\_INFORMATION\_EX replaces the structure PARTITION\_INFORMATION that was used with [**IoReadPartitionTable**](ioreadpartitiontable.md) and [**IoWritePartitionTable**](iowritepartitiontable.md). The principal difference is that the new structures and routines support both Master Boot Record (MBR) partitions and GUID Partition Table (GPT) partitions, whereas the older routines and structures are only used with MBR partitions.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**PARTITION\_INFORMATION\_MBR**](partition-information-mbr.md)
</dt> <dt>

[**PARTITION\_INFORMATION\_GPT**](partition-information-gpt.md)
</dt> <dt>

[**IoReadPartitionTable**](ioreadpartitiontable.md)
</dt> <dt>

[**IoWritePartitionTable**](iowritepartitiontable.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PARTITION_INFORMATION_EX%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






