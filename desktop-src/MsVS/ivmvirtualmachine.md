---
title: IVMVirtualMachine interface
description: The IVMVirtualMachine interface defines the interface for a virtual machine.
ms.assetid: 3ced0877-82b8-4e2d-b17b-b73b87137f6d
keywords:
- IVMVirtualMachine interface Virtual Server
- IVMVirtualMachine interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMVirtualMachine
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

# IVMVirtualMachine interface

The **IVMVirtualMachine** interface defines the interface for a virtual machine. **IVMVirtualMachine** can notify clients about events using the [**IVMVirtualMachineEvents**](ivmvirtualmachineevents.md) outgoing interface. **IVMVirtualMachine** objects are returned from [**IVMVirtualServer**](ivmvirtualserver.md) methods such as [**IVMVirtualServer::CreateVirtualMachine**](ivmvirtualserver-createvirtualmachine.md), [**IVMVirtualServer::RegisterVirtualMachine**](ivmvirtualserver-registervirtualmachine.md), and [**IVMVirtualServer::FindVirtualMachine**](ivmvirtualserver-findvirtualmachine.md). You can also retrieve an **IVMVirtualMachine** object from the [**IVMVirtualMachineCollection**](ivmvirtualmachinecollection.md) object returned from the [**IVMVirtualServer::VirtualMachines**](ivmvirtualserver-virtualmachines.md) property.

## Members

The **IVMVirtualMachine** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMVirtualMachine** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMVirtualMachine** interface has these methods.



| Method                                                                           | Description                                                                                           |
|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**AddDVDROMDrive**](ivmvirtualmachine-adddvdromdrive.md)                       | Adds a new CD or DVD drive to the virtual machine.<br/>                                         |
| [**AddHardDiskConnection**](ivmvirtualmachine-addharddiskconnection.md)         | Adds a new hard disk connection to the virtual machine.<br/>                                    |
| [**AddNetworkAdapter**](ivmvirtualmachine-addnetworkadapter.md)                 | Adds a network interface to the virtual machine.<br/>                                           |
| [**AddSCSIController**](ivmvirtualmachine-addscsicontroller.md)                 | Adds a new SCSI controller to the virtual machine.<br/>                                         |
| [**AttachScriptToEvent**](ivmvirtualmachine-attachscripttoevent.md)             | Specifies a script to run when an event occurs.<br/>                                            |
| [**DiscardSavedState**](ivmvirtualmachine-discardsavedstate.md)                 | Discards any saved state information for a saved virtual machine.<br/>                          |
| [**DiscardUndoDisks**](ivmvirtualmachine-discardundodisks.md)                   | Discards the virtual undo disks.<br/>                                                           |
| [**FetchScriptByEvent**](ivmvirtualmachine-fetchscriptbyevent.md)               | Retrieve the script command line associated with the specified event type.<br/>                 |
| [**GetActivationValue**](ivmvirtualmachine-getactivationvalue.md)               | Retrieves the value of the specified activation setting for this virtual machine.<br/>          |
| [**GetConfigurationValue**](ivmvirtualmachine-getconfigurationvalue.md)         | Retrieves the value of the specified configuration setting for this virtual machine.<br/>       |
| [**MergeUndoDisks**](ivmvirtualmachine-mergeundodisks.md)                       | Merges the virtual undo disks.<br/>                                                             |
| [**Pause**](ivmvirtualmachine-pause.md)                                         | Pauses the virtual machine.<br/>                                                                |
| [**RemoveActivationValue**](ivmvirtualmachine-removeactivationvalue.md)         | Removes the value of the specified activation setting for this virtual machine.<br/>            |
| [**RemoveConfigurationValue**](ivmvirtualmachine-removeconfigurationvalue.md)   | Removes the value of the specified configuration setting for this virtual machine.<br/>         |
| [**RemoveDVDROMDrive**](ivmvirtualmachine-removedvdromdrive.md)                 | Removes the specified CD or DVD drive from the virtual machine.<br/>                            |
| [**RemoveHardDiskConnection**](ivmvirtualmachine-removeharddiskconnection.md)   | Removes the specified hard disk connection from the virtual machine.<br/>                       |
| [**RemoveNetworkAdapter**](ivmvirtualmachine-removenetworkadapter.md)           | Removes a network interface from the virtual machine.<br/>                                      |
| [**RemoveScriptFromEvent**](ivmvirtualmachine-removescriptfromevent.md)         | Detaches a script from an event.<br/>                                                           |
| [**RemoveSCSIController**](ivmvirtualmachine-removescsicontroller.md)           | Removes the specified SCSI controller from the virtual machine.<br/>                            |
| [**Reset**](ivmvirtualmachine-reset.md)                                         | Resets the virtual machine (like hitting the reset button on a real machine).<br/>              |
| [**Resume**](ivmvirtualmachine-resume.md)                                       | Resumes the virtual machine.<br/>                                                               |
| [**Save**](ivmvirtualmachine-save.md)                                           | Saves the virtual machine state.<br/>                                                           |
| [**SetAccountNameAndPassword**](ivmvirtualmachine-setaccountnameandpassword.md) | Sets the account name and password for the context in which this virtual machine will run.<br/> |
| [**SetActivationValue**](ivmvirtualmachine-setactivationvalue.md)               | Sets the value of the specified activation setting for this virtual machine.<br/>               |
| [**SetConfigurationValue**](ivmvirtualmachine-setconfigurationvalue.md)         | Sets the value of the specified configuration setting for this virtual machine.<br/>            |
| [**Startup**](ivmvirtualmachine-startup.md)                                     | Starts up the virtual machine.<br/>                                                             |
| [**TurnOff**](ivmvirtualmachine-turnoff.md)                                     | Turns off the virtual machine.<br/>                                                             |



 

### Properties

The **IVMVirtualMachine** interface has these properties.



| Property                                                                              | Access type           | Description                                                                                                                                    |
|:--------------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**Accountant**](ivmvirtualmachine-accountant.md)<br/>                         | Read-only<br/>  | An [**IVMAccountant**](ivmaccountant.md) object for this virtual machine.<br/>                                                          |
| [**AccountName**](ivmvirtualmachine-accountname.md)<br/>                       | Read-only<br/>  | The account name for the context in which this virtual machine will run.<br/>                                                            |
| [**AttachedDriveTypes**](ivmvirtualmachine-attacheddrivetypes.md)<br/>         | Read-only<br/>  | An array indicating the type of drive attached to each location in the virtual machine.<br/>                                             |
| [**AutoStartAtLaunch**](ivmvirtualmachine-autostartatlaunch.md)<br/>           | Read/write<br/> | Indicates whether this virtual machine will start up automatically when Virtual Server is launched.<br/>                                 |
| [**AutoStartAtLaunchDelay**](ivmvirtualmachine-autostartatlaunchdelay.md)<br/> | Read/write<br/> | The delay in seconds to use when this virtual machine is started up automatically when Virtual Server is launched.<br/>                  |
| [**BaseBoardSerialNumber**](ivmvirtualmachine-baseboardserialnumber.md)<br/>   | Read/write<br/> | The base board serial number.<br/>                                                                                                       |
| [**BIOSGUID**](ivmvirtualmachine-biosguid.md)<br/>                             | Read/write<br/> | The BIOS GUID.<br/>                                                                                                                      |
| [**BIOSSerialNumber**](ivmvirtualmachine-biosserialnumber.md)<br/>             | Read/write<br/> | The BIOS serial number.<br/>                                                                                                             |
| [**ChassisAssetTag**](ivmvirtualmachine-chassisassettag.md)<br/>               | Read/write<br/> | The chassis asset tag.<br/>                                                                                                              |
| [**ChassisSerialNumber**](ivmvirtualmachine-chassisserialnumber.md)<br/>       | Read/write<br/> | The chassis serial number.<br/>                                                                                                          |
| [**ConfigID**](ivmvirtualmachine-configid.md)<br/>                             | Read-only<br/>  | The unique ID that identifies the virtual machine.<br/>                                                                                  |
| [**Display**](ivmvirtualmachine-display.md)<br/>                               | Read-only<br/>  | The video display for the virtual machine.<br/>                                                                                          |
| [**DVDROMDrives**](ivmvirtualmachine-dvdromdrives.md)<br/>                     | Read-only<br/>  | An enumerable collection of CD/DVD-ROM drives attached to the virtual machine.<br/>                                                      |
| [**File**](ivmvirtualmachine-file.md)<br/>                                     | Read-only<br/>  | The fully qualified name of the XML file that describes this virtual machine configuration.<br/>                                         |
| [**FloppyDrives**](ivmvirtualmachine-floppydrives.md)<br/>                     | Read-only<br/>  | An enumerable collection of floppy drives attached to the virtual machine.<br/>                                                          |
| [**GuestOS**](ivmvirtualmachine-guestos.md)<br/>                               | Read-only<br/>  | The guest operating system for this virtual machine.<br/>                                                                                |
| [**HardDiskConnections**](ivmvirtualmachine-harddiskconnections.md)<br/>       | Read-only<br/>  | An enumerable collection of hard disk connections.<br/>                                                                                  |
| [**has3DNow**](ivmvirtualmachine-has3dnow.md)<br/>                             | Read-only<br/>  | Indicates whether the processor supports the 3DNow instruction set.<br/>                                                                 |
| [**hasMMX**](ivmvirtualmachine-hasmmx.md)<br/>                                 | Read-only<br/>  | Indicates whether the processor supports the MMX instruction set.<br/>                                                                   |
| [**hasSSE**](ivmvirtualmachine-hassse.md)<br/>                                 | Read-only<br/>  | Indicates whether the processor supports the SSE instruction set.<br/>                                                                   |
| [**hasSSE2**](ivmvirtualmachine-hassse2.md)<br/>                               | Read-only<br/>  | Indicates whether the processor supports the SSE2 instruction set.<br/>                                                                  |
| [**Keyboard**](ivmvirtualmachine-keyboard.md)<br/>                             | Read-only<br/>  | The keyboard device for the virtual machine.<br/>                                                                                        |
| [**Memory**](ivmvirtualmachine-memory.md)<br/>                                 | Read/write<br/> | The quantity, in megabytes, of physical RAM in the virtual machine.<br/>                                                                 |
| [**Mouse**](ivmvirtualmachine-mouse.md)<br/>                                   | Read-only<br/>  | The mouse device for the virtual machine.<br/>                                                                                           |
| [**Name**](ivmvirtualmachine-name.md)<br/>                                     | Read/write<br/> | The name of the virtual machine configuration.<br/>                                                                                      |
| [**NetworkAdapters**](ivmvirtualmachine-networkadapters.md)<br/>               | Read-only<br/>  | An enumerable collection of NICs attached to the virtual machine.<br/>                                                                   |
| [**Notes**](ivmvirtualmachine-notes.md)<br/>                                   | Read/write<br/> | The notes about the virtual machine.<br/>                                                                                                |
| [**ParallelPorts**](ivmvirtualmachine-parallelports.md)<br/>                   | Read-only<br/>  | An enumerable collection of parallel ports.<br/>                                                                                         |
| [**ProcessorSpeed**](ivmvirtualmachine-processorspeed.md)<br/>                 | Read-only<br/>  | The speed, in megahertz, of the processor.<br/>                                                                                          |
| [**RunAsDefinedAccount**](ivmvirtualmachine-runasdefinedaccount.md)<br/>       | Read/write<br/> | Indicates whether this virtual machine should always be run in the same account.<br/>                                                    |
| [**SavedStateFilePath**](ivmvirtualmachine-savedstatefilepath.md)<br/>         | Read-only<br/>  | The full path to the saved state file.<br/>                                                                                              |
| [**SCSIControllers**](ivmvirtualmachine-scsicontrollers.md)<br/>               | Read-only<br/>  | An enumerable collection of SCSI controllers.<br/>                                                                                       |
| [**Security**](ivmvirtualmachine-security.md)<br/>                             | Read-only<br/>  | The [**IVMSecurity**](ivmsecurity.md) object associated with this virtual machine.<br/>                                                 |
| [**SerialPorts**](ivmvirtualmachine-serialports.md)<br/>                       | Read-only<br/>  | An enumerable collection of serial ports.<br/>                                                                                           |
| [**ShutdownActionOnQuit**](ivmvirtualmachine-shutdownactiononquit.md)<br/>     | Read/write<br/> | Specifies how to shut down this virtual machine if it is running when Virtual Server is quit.<br/>                                       |
| [**State**](ivmvirtualmachine-state.md)<br/>                                   | Read-only<br/>  | The current state of the virtual machine.<br/>                                                                                           |
| [**Undoable**](ivmvirtualmachine-undoable.md)<br/>                             | Read/write<br/> | Indicates whether undo drives are enabled for hard disks connected to the virtual machine.<br/>                                          |
| [**UndoAction**](ivmvirtualmachine-undoaction.md)<br/>                         | Read/write<br/> | The default action to be performed on all undo drives when the virtual machine is shut down from within the guest operating system.<br/> |



 

## Examples

The following example displays the current property values of the **IVMVirtualMachine** object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name

Set colVMs = objVS.VirtualMachines
For Each objVM in colVMS
  Wscript.Echo "Account name: " & objVM.AccountName
  Wscript.Echo "Autostart at launch: " & objVM.AutoStartAtLaunch
  Wscript.Echo "Autostart at launch delay: " & objVM.AutoStartAtLaunchDelay

  If objVM.BaseBoardSerialNumber = "" Then
    Wscript.Echo "Baseboard serial number: [null]"
  Else
    Wscript.Echo "Baseboard serial number: " & objVM.BaseBoardSerialNumber
  End If

  If objVM.BIOSGUID = "" Then
    Wscript.Echo "BIOS GUID: [null]"
  Else
    Wscript.Echo "BIOS GUID: " & objVM.BIOSGUID
  End If

  If objVM.BIOSSerialNumber = "" Then
    Wscript.Echo "BIOS serial number: [null]"
  Else
    Wscript.Echo "BIOS serial number: " & objVM.BIOSSerialNumber
  End If

  If objVM.ChassisAssetTag = "" Then
    Wscript.Echo "Chassis asset tag: [null]"
  Else
    Wscript.Echo "Chassis asset tag: " & objVM.ChassisAssetTag
  End If

  If objVM.ChassisSerialNumber = "" Then
    Wscript.Echo "Chassis serial number: [null]"
  Else
    Wscript.Echo "Chassis serial number: " & objVM.ChassisSerialNumber
  End If

  Wscript.Echo "Config ID: " & objVM.ConfigID

  Set objDisplay = objVM.Display
  WScript.Echo "Display Dimensions: " & objDisplay.Width & "x" & objDisplay.Height

  Set colDVDs = objVM.DVDROMDrives
  Wscript.Echo "DVD/CDROM drives installed: " & colDVDs.Count

  Wscript.Echo "File: " & objVM.File

  Set colFDs = objVM.FloppyDrives
  Wscript.Echo "Floppy drives installed: " & colFDs.Count

  Set objGOS = objVM.GuestOS
  Wscript.Echo "Guest OS: " & objGOS.OSName

  Set colHDCons = objVM.HardDiskConnections
  Wscript.Echo "Hard disk connections: " & colHDCons.Count

  Wscript.Echo "Has MMX: " & objVM.HasMMX
  Wscript.Echo "Has SSE: " & objVM.HasSSE
  Wscript.Echo "Has SSE2: " & objVM.HasSSE2
  Wscript.Echo "Has 3DNow: " & objVM.Has3DNow
  Wscript.Echo "Memory: " & objVM.Memory
  Wscript.Echo "Name: " & objVM.Name

  Set colNICs = objVM.NetworkAdapters
  Wscript.Echo "Network adapters: " & colNICs.Count

  Wscript.Echo "Notes: " & objVM.Notes

  Set colPPs = objVM.ParallelPorts
  Wscript.Echo "Parallel Ports: " & colPPs.Count

  Wscript.Echo "Processor speed: " & objVM.ProcessorSpeed
  Wscript.Echo "Run as defined account: " & objVM.RunAsDefinedAccount
  Wscript.Echo "Saved state file path: " & objVM.SavedStateFilePath

  Set colSCSICons = objVM.SCSIControllers
  Wscript.Echo "SCSI controllers: " & colSCSICons.Count

  Set colSPs = objVM.SerialPorts
  Wscript.Echo "Serial Ports: " & colSPs.Count

  Wscript.Echo "Shutdown action on quit: " & objVM.ShutdownActionOnQuit
  Wscript.Echo "State: " & objVM.State
  Wscript.Echo "Undoable: " & objVM.Undoable
  Wscript.Echo "Undo action: " & objVM.UndoAction
  Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





