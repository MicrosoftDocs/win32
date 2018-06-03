---
title: PARTITION\_INFORMATION structure
description: The PARTITION\_INFORMATION structure contains partition information for a partition with a traditional AT-style Master Boot Record (MBR).
ms.assetid: 06c3ed56-3640-431d-a4f0-bf3228a02cc2
keywords:
- PARTITION_INFORMATION structure Storage Devices
- PPARTITION_INFORMATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- PARTITION_INFORMATION
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

# PARTITION\_INFORMATION structure

The PARTITION\_INFORMATION structure contains partition information for a partition with a traditional AT-style Master Boot Record (MBR).

## Syntax


```C++
typedef struct _PARTITION_INFORMATION {
  LARGE_INTEGER StartingOffset;
  LARGE_INTEGER PartitionLength;
  ULONG         HiddenSectors;
  ULONG         PartitionNumber;
  UCHAR         PartitionType;
  BOOLEAN       BootIndicator;
  BOOLEAN       RecognizedPartition;
  BOOLEAN       RewritePartition;
} PARTITION_INFORMATION, *PPARTITION_INFORMATION;
```



## Members

<dl> <dt>

**StartingOffset**
</dt> <dd>

Specifies the offset in bytes on drive where the partition begins.

</dd> <dt>

**PartitionLength**
</dt> <dd>

Specifies the length in bytes of the partition.

</dd> <dt>

**HiddenSectors**
</dt> <dd>

Specifies the number of hidden sectors.

</dd> <dt>

**PartitionNumber**
</dt> <dd>

Specifies the number of the partition.

</dd> <dt>

**PartitionType**
</dt> <dd> <dl> <dt>

Indicates the system-defined MBR partition type. Possible values are as follows:
</dt> <dt>





| Partition Type                         | Meaning                                                                                                                                          |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| PARTITION\_ENTRY\_UNUSED<br/>    | Unused entry.<br/>                                                                                                                         |
| PARTITION\_FAT\_12 <br/>         | Specifies a partition with 12-bit FAT entries.<br/>                                                                                        |
| PARTITION\_XENIX\_1 <br/>        | Specifies a XENIX Type 1 partition.<br/>                                                                                                   |
| PARTITION\_XENIX\_2<br/>         | Specifies a XENIX Type 2 partition.<br/>                                                                                                   |
| PARTITION\_FAT\_16<br/>          | Specifies a partition with 16-bit FAT entries.<br/>                                                                                        |
| PARTITION\_EXTENDED<br/>         | Specifies an MS-DOS V4 extended partition.<br/>                                                                                            |
| PARTITION\_HUGE<br/>             | Specifies an MS-DOS V4 huge partition.<br/>                                                                                                |
| PARTITION\_IFS<br/>              | Specifies an IFS partition.<br/>                                                                                                           |
| PARTITION\_FAT32<br/>            | Specifies a FAT32 partition.<br/>                                                                                                          |
| PARTITION\_FAT32\_XINT13<br/>    | **Windows 95/98:** Specifies a partition that uses extended INT 13 services.<br/>                                                          |
| PARTITION\_XINT13\_EXTENDED<br/> | **Windows 95/98:** Same as PARTITION\_EXTENDED, but uses extended INT 13 services.<br/>                                                    |
| PARTITION\_PREP<br/>             | Specifies a PowerPC Reference Platform partition.<br/>                                                                                     |
| PARTITION\_LDM<br/>              | Specifies a logical disk manager partition.<br/>                                                                                           |
| PARTITION\_UNIX<br/>             | Specifies a UNIX partition.<br/>                                                                                                           |
| PARTITION\_NTFT<br/>             | Specifies an NTFT partition. This value is used in combination (that is, bitwise logically ORed) with the other values in this table.<br/> |



 


</dt> </dl> </dd> <dt>

**BootIndicator**
</dt> <dd>

Indicates, when **TRUE**, that this partition is a bootable (active) partition for this device. When **FALSE**, this partition is not bootable. This member is set according to the partition list entry boot indicator returned by [**IoReadPartitionTable**](ioreadpartitiontable.md).

</dd> <dt>

**RecognizedPartition**
</dt> <dd>

Indicates, when **TRUE**, that the system recognized the type of the partition. When **FALSE**, the system did not recognize the type of the partition.

</dd> <dt>

**RewritePartition**
</dt> <dd>

Indicates, when **TRUE**, that the partition information has changed. When **FALSE**, the partition information has not changed. This member has a value of **TRUE** when the partition has changed as a result of an [**IOCTL\_DISK\_SET\_DRIVE\_LAYOUT**](ioctl-disk-set-drive-layout.md) IOCTL. This informs the system that the partition information needs to be rewritten.

</dd> </dl>

## Remarks

The partition entry data in PARTITION\_INFORMATION forms part of the drive layout information reported by the legacy routine [**IoReadPartitionTable**](ioreadpartitiontable.md) in the [**DRIVE\_LAYOUT\_INFORMATION**](drive-layout-information.md) structure. DRIVE\_LAYOUT\_INFORMATION contains an array of PARTITION\_INFORMATION structures pointed to by its **PartitionEntry** member. Each partition entry contains information for a partition on the drive. PARTITION\_INFORMATION is also used with the legacy routine [**IoSetPartitionInformation**](iosetpartitioninformation.md) to change the properties of the partition, such as its type, recorded on the disk.

In Windows 2000 and later operating systems, disk drivers should use structures [**DRIVE\_LAYOUT\_INFORMATION\_EX**](drive-layout-information-ex.md) and [**PARTITION\_INFORMATION\_EX**](partition-information-ex.md) along with routines [**IoReadPartitionTableEx**](ioreadpartitiontableex.md) and [**IoSetPartitionInformationEx**](iosetpartitioninformationex.md) to read and alter partition information on the disk.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IoReadPartitionTable**](ioreadpartitiontable.md)
</dt> <dt>

[**IoSetPartitionInformation**](iosetpartitioninformation.md)
</dt> <dt>

[**IoReadPartitionTableEx**](ioreadpartitiontableex.md)
</dt> <dt>

[**IoSetPartitionInformationEx**](iosetpartitioninformationex.md)
</dt> <dt>

[**DRIVE\_LAYOUT\_INFORMATION**](drive-layout-information.md)
</dt> <dt>

[**DRIVE\_LAYOUT\_INFORMATION\_EX**](drive-layout-information-ex.md)
</dt> <dt>

[**PARTITION\_INFORMATION\_EX**](partition-information-ex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PARTITION_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






