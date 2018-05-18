---
title: Storage Classes
description: The storage objects are separated into three types controllers, drives, and media.
ms.assetid: 'c1b6c8f7-049e-4cb1-8423-969cb230ffbe'
---

# Storage Classes

The storage objects are separated into three types: controllers, drives, and media.

There are two controllers, an emulated IDE controller and a synthetic SCSI controller. Both controllers support the attachment of drives that host the media.

The following are virtualization WMI classes related to storage. There is also support for synthetic floppy disk media. Attaching to a physical floppy drive is not supported.

## In this section



| Class                                                                                | Description                                                                                                                                                 |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Msvm\_AffectedStorageJobElement**](msvm-affectedstoragejobelement.md)<br/> | Represents the association between a job and the managed elements that may be affected by its execution.<br/>                                         |
| [**Msvm\_ControlledBy**](msvm-controlledby.md)<br/>                           | Associates a storage device with the storage controller that owns the device.<br/>                                                                    |
| [**Msvm\_DiskDrive**](msvm-diskdrive.md)<br/>                                 | Represents a hard disk drive inside of a virtual machine.<br/>                                                                                        |
| [**Msvm\_DisketteController**](msvm-diskettecontroller.md)<br/>               | Represents the floppy controller in the virtual machine (VM).<br/>                                                                                    |
| [**Msvm\_DisketteDrive**](msvm-diskettedrive.md)<br/>                         | Represents a floppy drive inside the virtual machine.<br/>                                                                                            |
| [**Msvm\_DVDDrive**](msvm-dvddrive.md)<br/>                                   | Represents a DVD drive inside of a virtual machine.<br/>                                                                                              |
| [**Msvm\_IDEController**](msvm-idecontroller.md)<br/>                         | Represents an IDE controller.<br/>                                                                                                                    |
| [**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)<br/>       | Manages the virtual media (.vhd, .iso, or .vfd files) for a virtual machine.<br/>                                                                     |
| [**Msvm\_LogicalDisk**](msvm-logicaldisk.md)<br/>                             | Represents storage drive media and is used to populate the storage drives.<br/>                                                                       |
| [**Msvm\_MediaPresent**](msvm-mediapresent.md)<br/>                           | Associates a storage drive with the media inserted into the drive.<br/>                                                                               |
| [**Msvm\_MountedStorageImage**](msvm-mountedstorageimage.md)<br/>             | Provides detailed information about a manually mounted storage image.<br/>                                                                            |
| [**Msvm\_ProtocolControllerForUnit**](msvm-protocolcontrollerforunit.md)<br/> | This association indicates that a subclass of logical device (for example a storage volume) is connected through a specific protocol controller.<br/> |
| [**Msvm\_SCSIProtocolController**](msvm-scsiprotocolcontroller.md)<br/>       | Represents a synthetic SCSI controller.<br/>                                                                                                          |
| [**Msvm\_StorageJob**](msvm-storagejob.md)<br/>                               | Represents an image operation job created by the Microsoft Hyper-V Image Management Service.<br/>                                                     |
| [**Msvm\_VirtualHardDiskInfo**](msvm-virtualharddiskinfo.md)<br/>             | Provides detailed information about an existing virtual hard disk image.<br/>                                                                         |



 

## Related topics

<dl> <dt>

[Virtualization WMI Classes](virtualization-wmi-classes.md)
</dt> </dl>

 

 





