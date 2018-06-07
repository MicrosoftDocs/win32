---
title: IoWritePartitionTable routine
description: The IoWritePartitionTable routine is obsolete and is provided only to support existing drivers.
ms.assetid: 406508b2-7509-4d2b-ac22-63644eedcec0
keywords:
- IoWritePartitionTable routine Storage Devices
topic_type:
- apiref
api_name:
- IoWritePartitionTable
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IoWritePartitionTable routine

The **IoWritePartitionTable** routine is **obsolete** and is provided only to support existing drivers. New drivers must use [**IoWritePartitionTableEx**](iowritepartitiontableex.md).

**IoWritePartitionTable** writes partition tables from the entries in the partition list buffer for each partition on the disk represented by the given device object.

## Syntax


```C++
NTSTATUS FASTCALL IoWritePartitionTable(
  _In_ PDEVICE_OBJECT                   DeviceObject,
  _In_ ULONG                            SectorSize,
  _In_ ULONG                            SectorsPerTrack,
  _In_ ULONG                            NumberOfHeads,
  _In_ struct _DRIVE_LAYOUT_INFORMATION *PartitionBuffer
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Pointer to the device object representing the disk whose partition tables are to be written.

</dd> <dt>

*SectorSize* \[in\]
</dt> <dd>

Specifies the size in bytes of sectors on the device.

</dd> <dt>

*SectorsPerTrack* \[in\]
</dt> <dd>

Specifies the track size on the device.

</dd> <dt>

*NumberOfHeads* \[in\]
</dt> <dd>

Specifies the number of tracks per cylinder.

</dd> <dt>

*PartitionBuffer* \[in\]
</dt> <dd>

Pointer to the drive layout buffer that contains the partition list entries. For more detailed information see [**DRIVE\_LAYOUT\_INFORMATION**](drive-layout-information.md).

</dd> </dl>

## Return value

**IoWritePartitionTablo** returns a status code of STATUS\_SUCCESS if all writes were completed without error. In case of failure, the error codes returned by **IoWritePartitionTable** might include, but are not limited to, the following list:



| Return code                                                                                                    | Description                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STATUS\_DEVICE\_NOT\_READY**</dt> </dl>      | Indicates a failure read the correct disk geometry.<br/>                                         |
| <dl> <dt>**STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | Indicates a failure to allocate necessary resources (for example, heap memory, IRPs, etc.).<br/> |
| <dl> <dt>**STATUS\_UNSUCCESSFUL**</dt> </dl>            | Indicates that sector zero did not have the expected MBR disk signature.<br/>                    |



 

## Remarks

**IoWritePartitionTable** must only be used by disk drivers. Other drivers should use the [**IOCTL\_DISK\_SET\_DRIVE\_LAYOUT**](ioctl-disk-set-drive-layout.md) disk I/O request instead.

**IoWritePartitionTable** is called when a disk device driver is requested to set the partition type in a partition table entry or to repartition the disk by an IRP\_MJ\_DEVICE\_CONTROL request. The device control request is generally issued by the format utility, which performs I/O control functions on the partitions and disks in the machine.

To reset a partition type, the driver passes a pointer to the device object representing the physical disk and the number of the partition associated with the device object that the format utility has open. When a disk is to be repartitioned dynamically, the disk driver must tear down its set of device objects representing the current disk partitions and create a new set of device objects representing the new partitions on the disk.

Applications that create and delete partitions and require full descriptions of the system should call **IoReadPartitionTable** with *ReturnRecognizedPartitions* set to **FALSE**. The drive layout structure can be modified by the system format utility to reflect a new configuration of the disk.

**IoWritePartitionTable** is synchronous. It must be called by the disk driver's Dispatch routine or by a driver thread. Thus, all user and file system threads must be prepared to enter a wait state when issuing the device control request to reset partition types for the device.

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

[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)
</dt> <dt>

[**IoReadPartitionTable**](ioreadpartitiontable.md)
</dt> <dt>

[**IoSetPartitionInformation**](iosetpartitioninformation.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IoWritePartitionTable%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






