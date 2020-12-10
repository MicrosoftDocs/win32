---
title: IVMVirtualMachine interface (VPCCOMInterfaces.h)
description: Defines the interface for a virtual machine.
ms.assetid: c1c243f2-0fb7-4249-8dc9-f0b70059e78f
keywords:
- IVMVirtualMachine interface Virtual PC
- IVMVirtualMachine interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMVirtualMachine
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the interface for a virtual machine. **IVMVirtualMachine** can notify clients about events using the [**IVMVirtualMachineEvents**](ivmvirtualmachineevents.md) outgoing interface. **IVMVirtualMachine** objects are returned from [**IVMVirtualPC**](ivmvirtualpc.md) methods such as [**CreateVirtualMachine**](ivmvirtualpc-createvirtualmachine.md), [**RegisterVirtualMachine**](ivmvirtualpc-registervirtualmachine.md), and [**FindVirtualMachine**](ivmvirtualpc-findvirtualmachine.md). You can also retrieve an **IVMVirtualMachine** object from the [**IVMVirtualMachineCollection**](ivmvirtualmachinecollection.md) object returned from the [**IVMVirtualPC::VirtualMachines**](ivmvirtualpc-virtualmachines.md) property.

## Members

The **IVMVirtualMachine** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMVirtualMachine** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMVirtualMachine** interface has these methods.



| Method                                                                           | Description                                                                                                |
|:---------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**AddDVDROMDrive**](ivmvirtualmachine-adddvdromdrive.md)                       | Adds a new CD or DVD drive to the virtual machine.<br/>                                              |
| [**AddHardDiskConnection**](ivmvirtualmachine-addharddiskconnection.md)         | Adds a new hard disk connection to the virtual machine.<br/>                                         |
| [**AddNetworkAdapter**](ivmvirtualmachine-addnetworkadapter.md)                 | Adds a network interface to the virtual machine.<br/>                                                |
| [**AttachUSBDevice**](ivmvirtualmachine-attachusbdevice.md)                     | Attaches a USB device to a virtual machine.<br/>                                                     |
| [**DetachUSBDevice**](ivmvirtualmachine-detachusbdevice.md)                     | Releases a USB device from a virtual machine.<br/>                                                   |
| [**DiscardSavedState**](ivmvirtualmachine-discardsavedstate.md)                 | Discards any saved state information for a saved virtual machine.<br/>                               |
| [**DiscardUndoDisks**](ivmvirtualmachine-discardundodisks.md)                   | Discards the virtual undo disks.<br/>                                                                |
| [**GetActivationValue**](ivmvirtualmachine-getactivationvalue.md)               | Retrieves the value of the specified activation setting for this virtual machine.<br/>               |
| [**GetConfigurationValue**](ivmvirtualmachine-getconfigurationvalue.md)         | Retrieves the value of the specified configuration setting for this virtual machine.<br/>            |
| [**MergeUndoDisks**](ivmvirtualmachine-mergeundodisks.md)                       | Merges the virtual undo disks.<br/>                                                                  |
| [**Pause**](ivmvirtualmachine-pause.md)                                         | Pauses the virtual machine.<br/>                                                                     |
| [**RemoveActivationValue**](ivmvirtualmachine-removeactivationvalue.md)         | Removes the value of the specified activation setting for this virtual machine.<br/>                 |
| [**RemoveConfigurationValue**](ivmvirtualmachine-removeconfigurationvalue.md)   | Removes the value of the specified configuration setting for this virtual machine.<br/>              |
| [**RemoveDVDROMDrive**](ivmvirtualmachine-removedvdromdrive.md)                 | Removes the specified CD or DVD drive from the virtual machine.<br/>                                 |
| [**RemoveHardDiskConnection**](ivmvirtualmachine-removeharddiskconnection.md)   | Removes the specified hard disk connection from the virtual machine.<br/>                            |
| [**RemoveNetworkAdapter**](ivmvirtualmachine-removenetworkadapter.md)           | Removes a network interface from the virtual machine.<br/>                                           |
| [**Reset**](ivmvirtualmachine-reset.md)                                         | Resets the virtual machine.<br/>                                                                     |
| [**Resume**](ivmvirtualmachine-resume.md)                                       | Resumes the virtual machine.<br/>                                                                    |
| [**Save**](ivmvirtualmachine-save.md)                                           | Saves the virtual machine state.<br/>                                                                |
| [**SetActivationValue**](ivmvirtualmachine-setactivationvalue.md)               | Sets the value of the specified activation setting for this virtual machine.<br/>                    |
| [**SetConfigurationValue**](ivmvirtualmachine-setconfigurationvalue.md)         | Sets the value of the specified configuration setting for this virtual machine.<br/>                 |
| [**StartCommunicationChannel**](ivmvirtualmachine-startcommunicationchannel.md) | Sets up a communication channel between host and guest.<br/>                                         |
| [**Startup**](ivmvirtualmachine-startup.md)                                     | Starts the virtual machine from either the uninitialized or saved state.<br/>                        |
| [**Startup2**](ivmvirtualmachine-startup2.md)                                   | Starts the virtual machine from either the uninitialized or saved state, with advanced options.<br/> |
| [**TurnOff**](ivmvirtualmachine-turnoff.md)                                     | Turns off the virtual machine.<br/>                                                                  |



 

### Properties

The **IVMVirtualMachine** interface has these properties.



| Property                                                                            | Access type           | Description                                                                                                                                    |
|:------------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**Accountant**](ivmvirtualmachine-accountant.md)<br/>                       | Read-only<br/>  | An accountant for this virtual machine.<br/>                                                                                             |
| [**AttachedDriveTypes**](ivmvirtualmachine-attacheddrivetypes.md)<br/>       | Read-only<br/>  | An array indicating the type of drive attached to each location in the virtual machine.<br/>                                             |
| [**BaseBoardSerialNumber**](ivmvirtualmachine-baseboardserialnumber.md)<br/> | Read/write<br/> | The Base board serial number.<br/>                                                                                                       |
| [**BIOSGUID**](ivmvirtualmachine-biosguid.md)<br/>                           | Read/write<br/> | The BIOS GUID.<br/>                                                                                                                      |
| [**BIOSSerialNumber**](ivmvirtualmachine-biosserialnumber.md)<br/>           | Read/write<br/> | The BIOS serial number.<br/>                                                                                                             |
| [**ChassisAssetTag**](ivmvirtualmachine-chassisassettag.md)<br/>             | Read/write<br/> | The Chassis asset tag.<br/>                                                                                                              |
| [**ChassisSerialNumber**](ivmvirtualmachine-chassisserialnumber.md)<br/>     | Read/write<br/> | The Chassis serial number.<br/>                                                                                                          |
| [**ConfigID**](ivmvirtualmachine-configid.md)<br/>                           | Read-only<br/>  | The unique identifier for the virtual machine.<br/>                                                                                      |
| [**Display**](ivmvirtualmachine-display.md)<br/>                             | Read-only<br/>  | The video display for the virtual machine.<br/>                                                                                          |
| [**DVDROMDrives**](ivmvirtualmachine-dvdromdrives.md)<br/>                   | Read-only<br/>  | An enumerable collection of CD and DVD drives attached to the virtual machine.<br/>                                                      |
| [**File**](ivmvirtualmachine-file.md)<br/>                                   | Read-only<br/>  | The fully qualified path of the .vmc file for the virtual machine configuration.<br/>                                                    |
| [**FloppyDrives**](ivmvirtualmachine-floppydrives.md)<br/>                   | Read-only<br/>  | An enumerable collection of floppy drives attached to the virtual machine.<br/>                                                          |
| [**GuestOS**](ivmvirtualmachine-guestos.md)<br/>                             | Read-only<br/>  | The guest operating system for this virtual machine.<br/>                                                                                |
| [**HardDiskConnections**](ivmvirtualmachine-harddiskconnections.md)<br/>     | Read-only<br/>  | An enumerable collection of hard disk connections.<br/>                                                                                  |
| [**Has3DNow**](ivmvirtualmachine-has3dnow.md)<br/>                           | Read-only<br/>  | Indicates whether the processor supports the 3DNow instruction set.<br/>                                                                 |
| [**HasMMX**](ivmvirtualmachine-hasmmx.md)<br/>                               | Read-only<br/>  | Indicates whether the processor supports the MMX instruction set.<br/>                                                                   |
| [**HasSSE**](ivmvirtualmachine-hassse.md)<br/>                               | Read-only<br/>  | Indicates whether the processor supports the SSE instruction set.<br/>                                                                   |
| [**HasSSE2**](ivmvirtualmachine-hassse2.md)<br/>                             | Read-only<br/>  | Indicates whether the processor supports the SSE2 instruction set.<br/>                                                                  |
| [**Keyboard**](ivmvirtualmachine-keyboard.md)<br/>                           | Read-only<br/>  | The keyboard device for the virtual machine.<br/>                                                                                        |
| [**Memory**](ivmvirtualmachine-memory.md)<br/>                               | Read/write<br/> | The amount of physical memory in the virtual machine, in megabytes.<br/>                                                                 |
| [**Mouse**](ivmvirtualmachine-mouse.md)<br/>                                 | Read-only<br/>  | The mouse device for the virtual machine.<br/>                                                                                           |
| [**Name**](ivmvirtualmachine-name.md)<br/>                                   | Read/write<br/> | The name of the virtual machine configuration.<br/>                                                                                      |
| [**NetworkAdapters**](ivmvirtualmachine-networkadapters.md)<br/>             | Read-only<br/>  | An enumerable collection of NICs attached to the virtual machine.<br/>                                                                   |
| [**Notes**](ivmvirtualmachine-notes.md)<br/>                                 | Read/write<br/> | The notes for the virtual machine.<br/>                                                                                                  |
| [**ParallelPorts**](ivmvirtualmachine-parallelports.md)<br/>                 | Read-only<br/>  | An enumerable collection of parallel ports.<br/>                                                                                         |
| [**ProcessorSpeed**](ivmvirtualmachine-processorspeed.md)<br/>               | Read-only<br/>  | The speed of the processor, in megahertz (MHz).<br/>                                                                                     |
| [**RdpPipeName**](ivmvirtualmachine-rdppipename.md)<br/>                     | Read-only<br/>  | Name of the RDP connection named pipe used for video and input.<br/>                                                                     |
| [**SavedStateFilePath**](ivmvirtualmachine-savedstatefilepath.md)<br/>       | Read-only<br/>  | The full path to the saved state file.<br/>                                                                                              |
| [**SerialPorts**](ivmvirtualmachine-serialports.md)<br/>                     | Read-only<br/>  | An enumerable collection of serial ports.<br/>                                                                                           |
| [**ShutdownActionOnQuit**](ivmvirtualmachine-shutdownactiononquit.md)<br/>   | Read/write<br/> | The action to be performed on this virtual machine if it is running when Windows Virtual PC is quit.<br/>                                |
| [**State**](ivmvirtualmachine-state.md)<br/>                                 | Read-only<br/>  | The current state of the virtual machine.<br/>                                                                                           |
| [**Undoable**](ivmvirtualmachine-undoable.md)<br/>                           | Read/write<br/> | Indicates whether the undo drives are enabled for hard disks connected to the virtual machine.<br/>                                      |
| [**UndoAction**](ivmvirtualmachine-undoaction.md)<br/>                       | Read/write<br/> | The default action to be performed on all undo drives when the virtual machine is shut down from within the guest operating system.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualMachine is defined as f7092aa1-33ed-4f78-a59f-c00adfc2edd7<br/>          |



 

