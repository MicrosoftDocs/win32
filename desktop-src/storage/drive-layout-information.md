---
title: DRIVE\_LAYOUT\_INFORMATION structure
description: The DRIVE\_LAYOUT\_INFORMATION structure is obsolete and is provided only to support existing drivers.
ms.assetid: '980cd307-9048-4054-be8e-967d15862a14'
keywords: ["DRIVE_LAYOUT_INFORMATION structure Storage Devices", "PDRIVE_LAYOUT_INFORMATION structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DRIVE_LAYOUT_INFORMATION
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# DRIVE\_LAYOUT\_INFORMATION structure

The DRIVE\_LAYOUT\_INFORMATION structure is obsolete and is provided only to support existing drivers. New drivers must use [**DRIVE\_LAYOUT\_INFORMATION\_EX**](drive-layout-information-ex.md).

The DRIVE\_LAYOUT\_INFORMATION structure is used to report information about a disk drive and its partitions. It is also used to write new drive layout information to the disk.

## Syntax


```C++
typedef struct _DRIVE_LAYOUT_INFORMATION {
  ULONG                 PartitionCount;
  ULONG                 Signature;
  PARTITION_INFORMATION PartitionEntry[1];
} DRIVE_LAYOUT_INFORMATION, *PDRIVE_LAYOUT_INFORMATION;
```



## Members

<dl> <dt>

**PartitionCount**
</dt> <dd>

Contains the number of partitions on the drive.

</dd> <dt>

**Signature**
</dt> <dd>

Contains the disk signature.

</dd> <dt>

**PartitionEntry**
</dt> <dd>

Contains a variable-length array of [**PARTITION\_INFORMATION**](partition-information.md) structures, one for each partition on the drive.

</dd> </dl>

## Remarks

In Windows 2000 and later operating systems, disk drivers should use structures [**DRIVE\_LAYOUT\_INFORMATION\_EX**](drive-layout-information-ex.md) and [**PARTITION\_INFORMATION\_EX**](partition-information-ex.md) along with routines **IoReadPartitionTableEx** and [**IoSetPartitionInformationEx**](iosetpartitioninformationex.md) to read and alter partition information on the disk.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_GET\_PARTITION\_INFO**](ioctl-disk-get-partition-info.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_DRIVE\_LAYOUT**](ioctl-disk-get-drive-layout.md)
</dt> <dt>

[**IOCTL\_DISK\_SET\_DRIVE\_LAYOUT**](ioctl-disk-set-drive-layout.md)
</dt> <dt>

[**IoReadPartitionTable**](ioreadpartitiontable.md)
</dt> <dt>

[**IoReadPartitionTableEx**](ioreadpartitiontableex.md)
</dt> <dt>

[**IoSetPartitionInformation**](iosetpartitioninformation.md)
</dt> <dt>

[**IoWritePartitionTable**](iowritepartitiontable.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DRIVE_LAYOUT_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






