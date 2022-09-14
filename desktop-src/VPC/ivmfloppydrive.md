---
title: IVMFloppyDrive interface (VPCCOMInterfaces.h)
description: Controls a floppy drive within a virtual machine.
ms.assetid: b652182a-27ae-4390-81b1-b644a82924df
keywords:
- IVMFloppyDrive interface Virtual PC
- IVMFloppyDrive interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMFloppyDrive
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMFloppyDrive interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Controls a floppy drive within a virtual machine. **IVMFloppyDrive** can notify clients about events using the [**IVMFloppyDriveEvents**](ivmfloppydriveevents.md) outgoing interface. You can retrieve an **IVMFloppyDrive** object from the [**IVMFloppyDriveCollection**](ivmfloppydrivecollection.md) object returned from the [**IVMVirtualMachine::FloppyDrives**](ivmvirtualmachine-floppydrives.md) property.

## Members

The **IVMFloppyDrive** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMFloppyDrive** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMFloppyDrive** interface has these methods.



| Method                                                      | Description                                                                                  |
|:------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**AttachHostDrive**](ivmfloppydrive-attachhostdrive.md)   | Attaches a physical drive on the host to the floppy drive in the virtual machine.<br/> |
| [**AttachImage**](ivmfloppydrive-attachimage.md)           | Attaches a floppy media image on the host to the floppy drive.<br/>                    |
| [**ReleaseHostDrive**](ivmfloppydrive-releasehostdrive.md) | Releases a physical drive on the host from the floppy drive.<br/>                      |
| [**ReleaseImage**](ivmfloppydrive-releaseimage.md)         | Releases a floppy media image on the host from the floppy drive.<br/>                  |



 

### Properties

The **IVMFloppyDrive** interface has these properties.



| Property                                                             | Access type          | Description                                                                               |
|:---------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------|
| [**Attachment**](ivmfloppydrive-attachment.md)<br/>           | Read-only<br/> | The type of media attached to the floppy drive within the virtual machine.<br/>     |
| [**DriveNumber**](ivmfloppydrive-drivenumber.md)<br/>         | Read-only<br/> | The zero-based index of the controller to which this floppy drive is attached.<br/> |
| [**HostDriveLetter**](ivmfloppydrive-hostdriveletter.md)<br/> | Read-only<br/> | The letter of the host drive to which the floppy drive is attached.<br/>            |
| [**ImageFile**](ivmfloppydrive-imagefile.md)<br/>             | Read-only<br/> | The full path of the image file to which the floppy drive is attached.<br/>         |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMFloppyDrive is defined as 661abee6-112a-4ed9-babf-3c874969f10e<br/>             |



 

