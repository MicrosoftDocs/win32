---
title: Windows Virtual PC Interfaces
description: The following interfaces are supported by Windows Virtual PC.
ms.assetid: de003075-8609-4303-838e-da449b91dc8d
keywords:
- Windows Virtual PC Virtual PC , interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Windows Virtual PC Interfaces

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

The following interfaces are supported by Windows Virtual PC.



| Interface                                                                             | Description                                                                                                       |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [**IVMAccountant**](ivmaccountant.md)<br/>                                     | Provides access to accounting-related information for a virtual machine (VM).<br/>                          |
| [**IVMDisplay**](ivmdisplay.md)<br/>                                           | Controls the display settings of a VM.<br/>                                                                 |
| [**IVMDVDDrive**](ivmdvddrive.md)<br/>                                         | Controls a CD-ROM or DVD-ROM drive within a VM.<br/>                                                        |
| [**IVMDVDDriveCollection**](ivmdvddrivecollection.md)<br/>                     | Defines the collection of CD and DVD drives within the VM.<br/>                                             |
| [**IVMDVDDriveEvents**](ivmdvddriveevents.md)<br/>                             | Defines the outgoing event interface for the [**IVMDVDDrive**](ivmdvddrive.md) interface.<br/>             |
| [**IVMFloppyDrive**](ivmfloppydrive.md)<br/>                                   | Controls a floppy drive within a VM.<br/>                                                                   |
| [**IVMFloppyDriveCollection**](ivmfloppydrivecollection.md)<br/>               | Defines a collection of floppy drives within the VM.<br/>                                                   |
| [**IVMFloppyDriveEvents**](ivmfloppydriveevents.md)<br/>                       | Defines the outgoing event interface for the [**IVMFloppyDrive**](ivmfloppydrive.md) interface.<br/>       |
| [**IVMGuestOS**](ivmguestos.md)<br/>                                           | Defines the guest operating system running inside a VM.<br/>                                                |
| [**IVMHardDisk**](ivmharddisk.md)<br/>                                         | Provides access to a hard disk image.<br/>                                                                  |
| [**IVMHardDiskConnection**](ivmharddiskconnection.md)<br/>                     | Defines the connection for a hard disk within the VM.<br/>                                                  |
| [**IVMHardDiskConnectionCollection**](ivmharddiskconnectioncollection.md)<br/> | Defines the collection of hard disk connections within the VM.<br/>                                         |
| [**IVMHostInfo**](ivmhostinfo.md)<br/>                                         | Retrieves information about the host machine.<br/>                                                          |
| [**IVMKeyboard**](ivmkeyboard.md)<br/>                                         | Controls the keyboard device within a VM.<br/>                                                              |
| [**IVMMouse**](ivmmouse.md)<br/>                                               | Controls the mouse device within a VM.<br/>                                                                 |
| [**IVMNetworkAdapter**](ivmnetworkadapter.md)<br/>                             | Serves as the interface to a virtual network interface card (NIC) within a VM.<br/>                         |
| [**IVMNetworkAdapterCollection**](ivmnetworkadaptercollection.md)<br/>         | Defines a collection of virtual NICs within a VM.<br/>                                                      |
| [**IVMParallelPort**](ivmparallelport.md)<br/>                                 | Defines a parallel port inside a VM.<br/>                                                                   |
| [**IVMParallelPortCollection**](ivmparallelportcollection.md)<br/>             | Defines the collection of parallel ports within the VM.<br/>                                                |
| [**IVMSerialPort**](ivmserialport.md)<br/>                                     | Defines a serial port inside a VM.<br/>                                                                     |
| [**IVMSerialPortCollection**](ivmserialportcollection.md)<br/>                 | Defines the collection of serial ports within the VM.<br/>                                                  |
| [**IVMTask**](ivmtask.md)<br/>                                                 | Used to monitor and control asynchronous tasks for various methods.<br/>                                    |
| [**IVMTaskCollection**](ivmtaskcollection.md)<br/>                             | Defines the collection of task objects within a VM.<br/>                                                    |
| [**IVMUSBDevice**](ivmusbdevice.md)<br/>                                       | Defines the interface for a USB device attached to the host system.<br/>                                    |
| [**IVMUSBDeviceCollection**](ivmusbdevicecollection.md)<br/>                   | Defines the collection of USB devices attached to the host system.<br/>                                     |
| [**IVMVirtualMachine**](ivmvirtualmachine.md)<br/>                             | Defines the interface for a VM.<br/>                                                                        |
| [**IVMVirtualMachineCollection**](ivmvirtualmachinecollection.md)<br/>         | Defines the collection of VMs within Windows Virtual PC.<br/>                                               |
| [**IVMVirtualMachineEvents**](ivmvirtualmachineevents.md)<br/>                 | Defines the outgoing event interface for the [**IVMVirtualMachine**](ivmvirtualmachine.md) interface.<br/> |
| [**IVMVirtualNetwork**](ivmvirtualnetwork.md)<br/>                             | Defines a virtual network.<br/>                                                                             |
| [**IVMVirtualNetworkCollection**](ivmvirtualnetworkcollection.md)<br/>         | Defines a collection of [**IVMVirtualNetwork**](ivmvirtualnetwork.md) objects.<br/>                        |
| [**IVMVirtualPC**](ivmvirtualpc.md)<br/>                                       | Defines the top-level Windows Virtual PC application object.<br/>                                           |
| [**IVMVirtualPCEvents**](ivmvirtualpcevents.md)<br/>                           | Defines the outgoing event interface for the [**IVMVirtualPC**](ivmvirtualpc.md) interface.<br/>           |



 

## Note for developers on 64-bit Windows

On 64-bit editions of Windows, the type library for Windows Virtual PC is in a 64-bit binary (VPC.exe) in the %WinDir%\\System32 directory. That directory is not visible by default to 32-bit processes; WOW64 maps all access to the %WinDir%\\System32 directory to the %WinDir%\\SysWOW64 directory by default. Visual Studio is a 32-bit binary and therefore cannot open the file in this location. To generate an interoperability assembly for Windows Virtual PC, use TlbImp.exe, which comes with Visual Studio and the Windows SDK. To generate *Microsoft.VirtualPC.Interop.dll*, use the following command line:

**TlbImp.exe /out:***Microsoft.VirtualPC.Interop.dll* **/namespace:Microsoft.VirtualPC.Interop %WinDir%\\System32\\VPC.exe**

Other solutions include copying VPC.exe to a different directory where the compiler can find it, or using the OleView.exe tool from the Windows SDK to extract an .idl file from the type library in VPC.exe.

 

