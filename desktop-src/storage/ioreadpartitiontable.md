---
title: IoReadPartitionTable routine
description: The IoReadPartitionTable routine is obsolete and is provided only to support existing drivers.
ms.assetid: f87c74c3-fcb1-4358-ade6-6c0afc0020e2
keywords:
- IoReadPartitionTable routine Storage Devices
topic_type:
- apiref
api_name:
- IoReadPartitionTable
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IoReadPartitionTable routine

The **IoReadPartitionTable** routine is **obsolete** and is provided only to support existing drivers. New drivers must use [**IoReadPartitionTableEx**](ioreadpartitiontableex.md). **IoReadPartitionTable** reads a list of partitions on a disk having a specified sector size and creates an entry in the partition list for each recognized partition.

## Syntax


```C++
NTSTATUS FASTCALL IoReadPartitionTable(
  _In_  PDEVICE_OBJECT                   DeviceObject,
  _In_  ULONG                            SectorSize,
  _In_  BOOLEAN                          ReturnRecognizedPartitions,
  _Out_ struct _DRIVE_LAYOUT_INFORMATION **PartitionBuffer
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Pointer to the device object for the disk whose partitions are to be read.

</dd> <dt>

*SectorSize* \[in\]
</dt> <dd>

Specifies the size of the sectors on the disk.

</dd> <dt>

*ReturnRecognizedPartitions* \[in\]
</dt> <dd>

Indicates whether only recognized partitions or all partition entries should be returned.

</dd> <dt>

*PartitionBuffer* \[out\]
</dt> <dd>

Pointer to an uninitialized address. If successful, **IoReadPartitionTable** allocates the memory for this buffer from nonpaged pool and returns the drive layout information in it.

</dd> </dl>

## Return value

This routine returns a value of STATUS\_SUCCESS if at least one sector table was read. Otherwise, it returns an error status and sets the pointer at *PartitionBuffer* to **NULL**.

## Remarks

**IoReadPartitionTable** must only be used by disk drivers. Other drivers should use the [**IOCTL\_DISK\_GET\_DRIVE\_LAYOUT**](ioctl-disk-get-drive-layout.md) disk I/O request instead.

Disk device drivers call this routine during driver initialization.

It is the responsibility of the caller to deallocate the *PartitionBuffer* that was allocated by this routine with **ExFreePool**.

The algorithm used by this routine is determined by the Boolean value *ReturnRecognizedPartitions*:

-   Read each partition table and, for each valid and recognized partition found, fill in an element in an array of [**PARTITION\_INFORMATION**](partition-information.md) entries. The array of partition information entries is pointed to by the **PartitionEntry** member of a [**DRIVE\_LAYOUT\_INFORMATION**](drive-layout-information.md) structure. The DRIVE\_LAYOUT\_INFORMATION structure is found at the location pointed to by *PartitionBuffer*. Extended partitions are located in order to find other partition tables, but no entries are built for them.

Read each partition table and, for each and every entry, fill in a partition information entry. Extended partitions are located to find each partition on the disk; entries are built for these as well.

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Ntddk.h (include Ntddk.h)</dt> </dl>                                    |
| Library<br/>              | <dl> <dt>NtosKrnl.lib</dt> </dl>                                                 |
| DLL<br/>                  | <dl> <dt>NtosKrnl.exe</dt> </dl>                                                 |
| IRQL<br/>                 | PASSIVE\_LEVEL<br/>                                                                                                               |
| DDI compliance rules<br/> | [**HwStorPortProhibitedDDIs**](https://msdn.microsoft.com/library/windows/hardware/hh454220)                                                               |



## See also

<dl> <dt>

[**IOCTL\_DISK\_GET\_PARTITION\_INFO**](ioctl-disk-get-partition-info.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_DRIVE\_LAYOUT**](ioctl-disk-get-drive-layout.md)
</dt> <dt>

[**IOCTL\_DISK\_SET\_DRIVE\_LAYOUT**](ioctl-disk-set-drive-layout.md)
</dt> <dt>

[**IoSetPartitionInformation**](iosetpartitioninformation.md)
</dt> <dt>

[**IoWritePartitionTable**](iowritepartitiontable.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IoReadPartitionTable%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






