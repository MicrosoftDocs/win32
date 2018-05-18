---
title: DRIVE\_LAYOUT\_INFORMATION\_EX structure
description: The DRIVE\_LAYOUT\_INFORMATION\_EX structure is used to report information about the driver layout.
ms.assetid: 'e077f9a6-1d94-4d17-9166-b23756df6cc8'
keywords: ["DRIVE_LAYOUT_INFORMATION_EX structure Storage Devices", "PDRIVE_LAYOUT_INFORMATION_EX structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DRIVE_LAYOUT_INFORMATION_EX
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# DRIVE\_LAYOUT\_INFORMATION\_EX structure

The DRIVE\_LAYOUT\_INFORMATION\_EX structure is used to report information about the driver layout.

## Syntax


```C++
typedef struct _DRIVE_LAYOUT_INFORMATION_EX {
  ULONG                    PartitionStyle;
  ULONG                    PartitionCount;
  union {
    DRIVE_LAYOUT_INFORMATION_MBR Mbr;
    DRIVE_LAYOUT_INFORMATION_GPT Gpt;
  };
  PARTITION_INFORMATION_EX PartitionEntry[1];
} DRIVE_LAYOUT_INFORMATION_EX, *PDRIVE_LAYOUT_INFORMATION_EX;
```



## Members

<dl> <dt>

**PartitionStyle**
</dt> <dd>

Takes a [**PARTITION\_STYLE**](partition-style.md) enumerated value that specifies the type of partition table the disk contains.

</dd> <dt>

**PartitionCount**
</dt> <dd>

Indicates the number of partitions detected on the disk.

</dd> <dt>

**Mbr**
</dt> <dd>

Indicates the drive layout information for a disk with a Master Boot Record. This member is valid when **PartitionStyle** is PARTITION\_STYLE\_MBR. See the definition of [**DRIVE\_LAYOUT\_INFORMATION\_MBR**](drive-layout-information-mbr.md) for more information.

</dd> <dt>

**Gpt**
</dt> <dd>

Indicates the drive layout information for a disk with a GUID Partition Table. This member is valid when **PartitionStyle** is PARTITION\_STYLE\_GPT. See definition of [**DRIVE\_LAYOUT\_INFORMATION\_GPT**](drive-layout-information-gpt.md) for more information.

</dd> <dt>

**PartitionEntry**
</dt> <dd>

Contains a variable-length array of [**PARTITION\_INFORMATION\_EX**](partition-information-ex.md) structures, one for each partition on the drive.

</dd> </dl>

## Remarks

This structure is used for both reading and writing disk partition information. It is used with [**IoReadPartitionTableEx**](ioreadpartitiontableex.md) and [**IoWritePartitionTableEx**](iowritepartitiontableex.md) and replaces the obsolete structure DRIVE\_LAYOUT\_INFORMATION that was used with **IoReadPartitionTable** and **IoWritePartitionTable**. The principal difference is that the new structures and routines support both Master Boot Record (MBR) partitions and GUID Partition Table (GPT) partitions, whereas the older routines and structures are only used with MBR partitions.

## Requirements



|                   |                                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntddk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IoReadPartitionTableEx**](ioreadpartitiontableex.md)
</dt> <dt>

[**IoWritePartitionTableEx**](iowritepartitiontableex.md)
</dt> <dt>

[**DRIVE\_LAYOUT\_INFORMATION\_MBR**](drive-layout-information-mbr.md)
</dt> <dt>

[**DRIVE\_LAYOUT\_INFORMATION\_GPT**](drive-layout-information-gpt.md)
</dt> <dt>

[**PARTITION\_STYLE**](partition-style.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DRIVE_LAYOUT_INFORMATION_EX%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






