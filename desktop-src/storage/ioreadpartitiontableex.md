---
title: IoReadPartitionTableEx routine
description: The IoReadPartitionTableEx routine reads a list of partitions on a disk having a specified sector size and creates an entry in the partition list for each recognized partition.
ms.assetid: 1aa8665a-1674-4fca-b5c6-d8d25166ca29
keywords:
- IoReadPartitionTableEx routine Storage Devices
topic_type:
- apiref
api_name:
- IoReadPartitionTableEx
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

# IoReadPartitionTableEx routine

The **IoReadPartitionTableEx** routine reads a list of partitions on a disk having a specified sector size and creates an entry in the partition list for each recognized partition.

## Syntax


```C++
NTSTATUS IoReadPartitionTableEx(
  _In_  PDEVICE_OBJECT                      DeviceObject,
  _Out_ struct _DRIVE_LAYOUT_INFORMATION_EX **PartitionBuffer
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Pointer to the device object for the disk whose partitions are to be read.

</dd> <dt>

*PartitionBuffer* \[out\]
</dt> <dd>

Pointer to an uninitialized address. If successful, **IoReadPartitionTableEx** allocates the memory for this buffer from nonpaged pool and returns the drive layout information in it.

</dd> </dl>

## Return value

This routine returns a value of STATUS\_SUCCESS if at least one sector table was read. Otherwise, it returns an error status value and sets the pointer at *PartitionBuffer* to **NULL**.

## Remarks

**IoReadPartitionTableEx** must only be used by disk drivers. Other drivers should use the [**IOCTL\_DISK\_GET\_DRIVE\_LAYOUT\_EX**](ioctl-disk-get-drive-layout-ex.md) disk I/O request instead.

**IoReadPartitionTableEx** is able to read partition table information from GUID Partition Table (GPT) disks as well as legacy Master Boot Record (MBR) disks. Disk device drivers call this routine during driver initialization.

It is the responsibility of the caller to deallocate the *PartitionBuffer* that was allocated by this routine with **ExFreePool**.

Note that disk drivers also return and set partition information in response to IRP\_MJ\_DEVICE\_CONTROL requests with the following I/O control codes:

<dl> <dt>

IOCTL\_DISK\_GET\_PARTITION\_INFO\_EX
</dt> <dt>

IOCTL\_DISK\_SET\_PARTITION\_INFO\_EX
</dt> <dt>

IOCTL\_DISK\_GET\_DRIVE\_LAYOUT\_EX
</dt> <dt>

IOCTL\_DISK\_SET\_DRIVE\_LAYOUT\_EX
</dt> <dt>

IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY
</dt> </dl>

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

[**DRIVE\_LAYOUT\_INFORMATION\_EX**](drive-layout-information-ex.md)
</dt> <dt>

[**PARTITION\_INFORMATION\_EX**](partition-information-ex.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_PARTITION\_INFO\_EX**](ioctl-disk-get-partition-info-ex.md)
</dt> <dt>

[**IOCTL\_DISK\_SET\_PARTITION\_INFO\_EX**](ioctl-disk-set-partition-info-ex.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_DRIVE\_LAYOUT\_EX**](ioctl-disk-get-drive-layout-ex.md)
</dt> <dt>

[**IOCTL\_DISK\_SET\_DRIVE\_LAYOUT\_EX**](ioctl-disk-set-drive-layout-ex.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY**](ioctl-disk-get-drive-geometry.md)
</dt> <dt>

[**IoSetPartitionInformation**](iosetpartitioninformation.md)
</dt> <dt>

[**IoWritePartitionTableEx**](iowritepartitiontableex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IoReadPartitionTableEx%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






