---
title: IVMVirtualPC interface (VPCCOMInterfaces.h)
description: Defines the top-level Windows Virtual PC application object. All other Windows Virtual PC interface objects are retrieved through this object.
ms.assetid: 519d3f1b-0a72-4c67-a2d9-124fda6c8b7a
keywords:
- IVMVirtualPC interface Virtual PC
- IVMVirtualPC interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMVirtualPC
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the top-level Windows Virtual PC application object. All other Windows Virtual PC interface objects are retrieved through this object.

**IVMVirtualPC** can notify clients about events by using the [**IVMVirtualPCEvents**](ivmvirtualpcevents.md) outgoing interface.

## Members

The **IVMVirtualPC** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMVirtualPC** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMVirtualPC** interface has these methods.



| Method                                                                                      | Description                                                                                              |
|:--------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| [**CreateDifferencingVirtualHardDisk**](ivmvirtualpc-createdifferencingvirtualharddisk.md) | Creates a differencing virtual hard disk.<br/>                                                     |
| [**CreateDynamicVirtualHardDisk**](ivmvirtualpc-createdynamicvirtualharddisk.md)           | Creates a dynamically resizing virtual hard disk.<br/>                                             |
| [**CreateFixedVirtualHardDisk**](ivmvirtualpc-createfixedvirtualharddisk.md)               | Creates a fixed-size virtual hard disk.<br/>                                                       |
| [**CreateFloppyDiskImage**](ivmvirtualpc-createfloppydiskimage.md)                         | Creates a floppy disk image file.<br/>                                                             |
| [**CreateVirtualMachine**](ivmvirtualpc-createvirtualmachine.md)                           | Creates a new virtual machine configuration and retrieves the virtual machine object.<br/>         |
| [**DeleteVirtualMachine**](ivmvirtualpc-deletevirtualmachine.md)                           | Deletes a virtual machine configuration.<br/>                                                      |
| [**FindVirtualMachine**](ivmvirtualpc-findvirtualmachine.md)                               | Retrieves a virtual machine object that matches the requested configuration.<br/>                  |
| [**FindVirtualNetwork**](ivmvirtualpc-findvirtualnetwork.md)                               | Retrieves a virtual network object that matches the requested name.<br/>                           |
| [**GetConfigurationValue**](ivmvirtualpc-getconfigurationvalue.md)                         | Retrieves the value of the specified configuration setting.<br/>                                   |
| [**GetDVDFiles**](ivmvirtualpc-getdvdfiles.md)                                             | Retrieves an array of known DVD files.<br/>                                                        |
| [**GetFloppyDiskFiles**](ivmvirtualpc-getfloppydiskfiles.md)                               | Retrieves an array of known virtual floppy disk files.<br/>                                        |
| [**GetFloppyDiskImageType**](ivmvirtualpc-getfloppydiskimagetype.md)                       | Retrieves the type of an existing floppy disk image file.<br/>                                     |
| [**GetHardDisk**](ivmvirtualpc-getharddisk.md)                                             | Retrieves an object corresponding to an existing disk image file.<br/>                             |
| [**GetHardDiskFiles**](ivmvirtualpc-getharddiskfiles.md)                                   | Retrieves an array of known virtual hard disk files.<br/>                                          |
| [**GetVirtualMachineFiles**](ivmvirtualpc-getvirtualmachinefiles.md)                       | Retrieves an array of known virtual machine configuration files.<br/>                              |
| [**RegisterVirtualMachine**](ivmvirtualpc-registervirtualmachine.md)                       | Registers an existing virtual machine configuration and retrieves the virtual machine object.<br/> |
| [**RemoveConfigurationValue**](ivmvirtualpc-removeconfigurationvalue.md)                   | Removes the value of the specified configuration setting.<br/>                                     |
| [**SetConfigurationValue**](ivmvirtualpc-setconfigurationvalue.md)                         | Sets the value of the specified configuration setting.<br/>                                        |
| [**UnregisterVirtualMachine**](ivmvirtualpc-unregistervirtualmachine.md)                   | Unregisters a virtual machine configuration without deleting the configuration file.<br/>          |



 

### Properties

The **IVMVirtualPC** interface has these properties.



| Property                                                                                   | Access type           | Description                                                                                                                                           |
|:-------------------------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DefaultVMConfigurationPath**](ivmvirtualpc-defaultvmconfigurationpath.md)<br/>   | Read/write<br/> | The default directory to be searched for available virtual machine configuration files.<br/>                                                    |
| [**HostInfo**](ivmvirtualpc-hostinfo.md)<br/>                                       | Read-only<br/>  | Information about the physical computer.<br/>                                                                                                   |
| [**MaximumFloppyDrivesPerVM**](ivmvirtualpc-maximumfloppydrivespervm.md)<br/>       | Read-only<br/>  | The maximum number of floppy drives per virtual machine.<br/>                                                                                   |
| [**MaximumMemoryPerVM**](ivmvirtualpc-maximummemorypervm.md)<br/>                   | Read-only<br/>  | The maximum allowable quantity of physical memory per virtual machine, in megabytes.<br/>                                                       |
| [**MaximumNetworkAdaptersPerVM**](ivmvirtualpc-maximumnetworkadapterspervm.md)<br/> | Read-only<br/>  | The maximum number of networks interfaces per virtual machine.<br/>                                                                             |
| [**MaximumNumberOfIDEBuses**](ivmvirtualpc-maximumnumberofidebuses.md)<br/>         | Read-only<br/>  | The maximum number of buses allowed for IDE.<br/>                                                                                               |
| [**MaximumParallelPortsPerVM**](ivmvirtualpc-maximumparallelportspervm.md)<br/>     | Read-only<br/>  | The maximum number of parallel ports per virtual machine.<br/>                                                                                  |
| [**MaximumSerialPortsPerVM**](ivmvirtualpc-maximumserialportspervm.md)<br/>         | Read-only<br/>  | The maximum number of serial ports per virtual machine.<br/>                                                                                    |
| [**MinimumMemoryPerVM**](ivmvirtualpc-minimummemorypervm.md)<br/>                   | Read-only<br/>  | The minimum allowable quantity of physical memory per virtual machine, in megabytes.<br/>                                                       |
| [**Name**](ivmvirtualpc-name.md)<br/>                                               | Read-only<br/>  | The name of the Windows Virtual PC application.<br/>                                                                                            |
| [**SearchPaths**](ivmvirtualpc-searchpaths.md)<br/>                                 | Read/write<br/> | The file system paths that are used to find files associated with Windows Virtual PC.<br/>                                                      |
| [**SuggestedMaximumMemoryPerVM**](ivmvirtualpc-suggestedmaximummemorypervm.md)<br/> | Read-only<br/>  | The suggested maximum allowable quantity of physical memory per virtual machine, in megabytes, to avoid low memory conditions on the host.<br/> |
| [**Tasks**](ivmvirtualpc-tasks.md)<br/>                                             | Read-only<br/>  | A collection of tasks.<br/>                                                                                                                     |
| [**UnconnectedNetworkAdapters**](ivmvirtualpc-unconnectednetworkadapters.md)<br/>   | Read-only<br/>  | An enumerable collection of unconnected network interfaces.<br/>                                                                                |
| [**UpTime**](ivmvirtualpc-uptime.md)<br/>                                           | Read-only<br/>  | The number of seconds the Windows Virtual PC application has been running.<br/>                                                                 |
| [**USBDeviceCollection**](ivmvirtualpc-usbdevicecollection.md)<br/>                 | Read-only<br/>  | An enumerable collection of all USB devices connected to the host.<br/>                                                                         |
| [**Version**](ivmvirtualpc-version.md)<br/>                                         | Read-only<br/>  | The version of this instance of Windows Virtual PC.<br/>                                                                                        |
| [**VirtualMachines**](ivmvirtualpc-virtualmachines.md)<br/>                         | Read-only<br/>  | An enumerable collection of virtual machines.<br/>                                                                                              |
| [**VirtualNetworks**](ivmvirtualpc-virtualnetworks.md)<br/>                         | Read-only<br/>  | An enumerable collection of virtual networks.<br/>                                                                                              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualPC is defined as 236ba0d9-a24a-4292-a132-27c1421dfd01<br/>               |



 

