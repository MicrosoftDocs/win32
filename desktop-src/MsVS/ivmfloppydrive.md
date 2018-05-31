---
title: IVMFloppyDrive interface
description: The IVMFloppyDrive interface controls a floppy drive within a virtual machine.
ms.assetid: 9abcd75e-f2b7-4f4d-a66f-f551a1c85cc4
keywords:
- IVMFloppyDrive interface Virtual Server
- IVMFloppyDrive interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMFloppyDrive
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMFloppyDrive interface

The **IVMFloppyDrive** interface controls a floppy drive within a virtual machine. **IVMFloppyDrive** can notify clients about events using the [**IVMFloppyDriveEvents**](ivmfloppydriveevents.md) outgoing interface. You can retrieve an **IVMFloppyDrive** object from the [**IVMFloppyDriveCollection**](ivmfloppydrivecollection.md) object returned from the [**IVMVirtualMachine::FloppyDrives**](ivmvirtualmachine-floppydrives.md) property.

## Members

The **IVMFloppyDrive** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMFloppyDrive** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMFloppyDrive** interface has these methods.



| Method                                                      | Description                                                                                                       |
|:------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| [**AttachHostDrive**](ivmfloppydrive-attachhostdrive.md)   | Attaches a physical floppy drive on the host machine to the floppy drive in the virtual machine.<br/>       |
| [**AttachImage**](ivmfloppydrive-attachimage.md)           | Attaches a floppy media image residing on the host machine to the floppy drive in the virtual machine.<br/> |
| [**ReleaseHostDrive**](ivmfloppydrive-releasehostdrive.md) | Releases the currently attached physical floppy drive from the floppy drive in the virtual machine.<br/>    |
| [**ReleaseImage**](ivmfloppydrive-releaseimage.md)         | Releases the currently attached floppy media image from the floppy drive in the virtual machine.<br/>       |



 

### Properties

The **IVMFloppyDrive** interface has these properties.



| Property                                                             | Access type          | Description                                                                                |
|:---------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------|
| [**Attachment**](ivmfloppydrive-attachment.md)<br/>           | Read-only<br/> | The type of media that is attached to this floppy drive in the virtual machine.<br/> |
| [**DriveNumber**](ivmfloppydrive-drivenumber.md)<br/>         | Read-only<br/> | The zero-based index of the controller to which this floppy drive is attached.<br/>  |
| [**HostDriveLetter**](ivmfloppydrive-hostdriveletter.md)<br/> | Read-only<br/> | The letter of the physical floppy drive to which this floppy drive is attached.<br/> |
| [**ImageFile**](ivmfloppydrive-imagefile.md)<br/>             | Read-only<br/> | The full path of the image file to which this floppy drive is attached.<br/>         |



 

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

 

 





