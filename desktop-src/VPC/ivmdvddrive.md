---
title: IVMDVDDrive interface (VPCCOMInterfaces.h)
description: Controls a CD-ROM or DVD-ROM drive within a virtual machine. IVMDVDDrive can notify clients about events using the IVMDVDDriveEvents outgoing interface.
ms.assetid: 0900b3a8-ba52-4c26-bd96-b37334d6d03c
keywords:
- IVMDVDDrive interface Virtual PC
- IVMDVDDrive interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMDVDDrive
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDVDDrive interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Controls a CD-ROM or DVD-ROM drive within a virtual machine. **IVMDVDDrive** can notify clients about events using the [**IVMDVDDriveEvents**](ivmdvddriveevents.md) outgoing interface.

You can add a new CD-ROM or DVD-ROM drive to a virtual machine using the [**IVMVirtualMachine::AddDVDROMDrive**](ivmvirtualmachine-adddvdromdrive.md) method. You can remove an existing CD-ROM or DVD-ROM drive from a virtual machine using the [**IVMVirtualMachine::RemoveDVDROMDrive**](ivmvirtualmachine-removedvdromdrive.md) method. You can retrieve an **IVMDVDDrive** object from the [**IVMDVDDriveCollection**](ivmdvddrivecollection.md) object returned from the [**IVMVirtualMachine::DVDROMDrives**](ivmvirtualmachine-dvdromdrives.md) property.

## Members

The **IVMDVDDrive** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMDVDDrive** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMDVDDrive** interface has these methods.



| Method                                                   | Description                                                                             |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------|
| [**AttachHostDrive**](ivmdvddrive-attachhostdrive.md)   | Attaches a host drive to the DVD drive within the virtual machine.<br/>           |
| [**AttachImage**](ivmdvddrive-attachimage.md)           | Attaches an ISO image to the DVD drive within the virtual machine.<br/>           |
| [**ReleaseHostDrive**](ivmdvddrive-releasehostdrive.md) | Releases a captured host drive from the DVD drive.<br/>                           |
| [**ReleaseImage**](ivmdvddrive-releaseimage.md)         | Releases a captured ISO image from the DVD drive.<br/>                            |
| [**SetBusLocation**](ivmdvddrive-setbuslocation.md)     | Attaches the DVD drive to the specified bus location in the virtual machine.<br/> |



 

### Properties

The **IVMDVDDrive** interface has these properties.



| Property                                                          | Access type          | Description                                                                        |
|:------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------|
| [**Attachment**](ivmdvddrive-attachment.md)<br/>           | Read-only<br/> | The type of media attached to the DVD drive within the virtual machine.<br/> |
| [**BusNumber**](ivmdvddrive-busnumber.md)<br/>             | Read-only<br/> | The bus number to which this device is attached.<br/>                        |
| [**DeviceNumber**](ivmdvddrive-devicenumber.md)<br/>       | Read-only<br/> | The device number to which this drive is attached.<br/>                      |
| [**HostDriveLetter**](ivmdvddrive-hostdriveletter.md)<br/> | Read-only<br/> | The letter of the host drive set for this device.<br/>                       |
| [**ImageFile**](ivmdvddrive-imagefile.md)<br/>             | Read-only<br/> | The full path of the image file set for this device.<br/>                    |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMDVDDrive is defined as b96328f6-6732-437d-a00d-ffa47e43971c<br/>                |



 

