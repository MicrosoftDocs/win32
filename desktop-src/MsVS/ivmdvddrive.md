---
title: IVMDVDDrive interface
description: The IVMDVDDrive interface controls a CD-ROM or DVD-ROM drive within a virtual machine. IVMDVDDrive can notify clients about events using the IVMDVDDriveEvents outgoing interface.
ms.assetid: 64431ed5-9ea0-4a79-b81e-94eab494a18a
keywords:
- IVMDVDDrive interface Virtual Server
- IVMDVDDrive interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMDVDDrive
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IVMDVDDrive interface

The **IVMDVDDrive** interface controls a CD-ROM or DVD-ROM drive within a virtual machine. **IVMDVDDrive** can notify clients about events using the [**IVMDVDDriveEvents**](ivmdvddriveevents.md) outgoing interface.

## When to use

You can add a new CD-ROM or DVD-ROM drive to a virtual machine using the [**IVMVirtualMachine::AddDVDROMDrive**](ivmvirtualmachine-adddvdromdrive.md) method. You can remove an existing CD-ROM or DVD-ROM drive from a virtual machine using the [**IVMVirtualMachine::RemoveDVDROMDrive**](ivmvirtualmachine-removedvdromdrive.md) method. You can retrieve an **IVMDVDDrive** object from the [**IVMDVDDriveCollection**](ivmdvddrivecollection.md) object returned from the [**IVMVirtualMachine::DVDROMDrives**](ivmvirtualmachine-dvdromdrives.md) property.

## Members

The **IVMDVDDrive** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMDVDDrive** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMDVDDrive** interface has these methods.



| Method                                                   | Description                                                                             |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------|
| [**AttachHostDrive**](ivmdvddrive-attachhostdrive.md)   | Attaches a host DVD drive to the DVD drive within the virtual machine.<br/>       |
| [**AttachImage**](ivmdvddrive-attachimage.md)           | Attaches an ISO image to the DVD drive within the virtual machine.<br/>           |
| [**ReleaseHostDrive**](ivmdvddrive-releasehostdrive.md) | Releases a captured host drive from the DVD drive.<br/>                           |
| [**ReleaseImage**](ivmdvddrive-releaseimage.md)         | Releases a captured ISO image from the DVD drive.<br/>                            |
| [**SetBusLocation**](ivmdvddrive-setbuslocation.md)     | Attaches the DVD drive to the specified bus location in the virtual machine.<br/> |



 

### Properties

The **IVMDVDDrive** interface has these properties.



| Property                                                          | Access type          | Description                                                                                                                                                     |
|:------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Attachment**](ivmdvddrive-attachment.md)<br/>           | Read-only<br/> | An enumerated value representing the type of media attached to the DVD drive within the virtual machine.<br/>                                             |
| [**BusNumber**](ivmdvddrive-busnumber.md)<br/>             | Read-only<br/> | The bus number to which this DVD drive is attached. For example, on an IDE bus, this value would represent either the primary or secondary location.<br/> |
| [**BusType**](ivmdvddrive-bustype.md)<br/>                 | Read-only<br/> | The bus type (that is, IDE or SCSI) to which this DVD drive is attached.<br/>                                                                             |
| [**DeviceNumber**](ivmdvddrive-devicenumber.md)<br/>       | Read-only<br/> | The device number to which this DVD drive is attached.<br/>                                                                                               |
| [**HostDriveLetter**](ivmdvddrive-hostdriveletter.md)<br/> | Read-only<br/> | The letter of the host drive captured by this DVD drive.<br/>                                                                                             |
| [**ImageFile**](ivmdvddrive-imagefile.md)<br/>             | Read-only<br/> | The full path of the image file captured by this DVD drive.<br/>                                                                                          |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





