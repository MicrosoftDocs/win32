---
title: IVMVirtualMachineEvents interface (VPCCOMInterfaces.h)
description: Defines the outgoing event interface for the IVMVirtualMachine interface.
ms.assetid: 52901a95-0f4f-4503-97c5-1459179feeb8
keywords:
- IVMVirtualMachineEvents interface Virtual PC
- IVMVirtualMachineEvents interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachineEvents interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the outgoing event interface for the [**IVMVirtualMachine**](ivmvirtualmachine.md) interface. The client implements these methods to receive events sent from [**IVMVirtualMachine**](ivmvirtualmachine.md).

## Members

The **IVMVirtualMachineEvents** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMVirtualMachineEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVMVirtualMachineEvents** interface has these methods.



| Method                                                                                   | Description                                                                                                                                     |
|:-----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OnAdditionsAvailable**](ivmvirtualmachineevents-onadditionsavailable.md)             | Receives notification that integration components are available in a virtual machine.<br/>                                                |
| [**OnAdditionsUninstalled**](ivmvirtualmachineevents-onadditionsuninstalled.md)         | Receives notification that integration components are uninstalled in a virtual machine.<br/>                                              |
| [**OnConfigurationChanged**](ivmvirtualmachineevents-onconfigurationchanged.md)         | Receives notification that a value in the configuration for this virtual machine has changed.<br/>                                        |
| [**OnDiskOutOfSpace**](ivmvirtualmachineevents-ondiskoutofspace.md)                     | Receives notification that a disk required for a virtual machine is out of space and the virtual machine is unable to run.<br/>           |
| [**OnEnhancedVideoModeChanged**](ivmvirtualmachineevents-onenhancedvideomodechanged.md) | Receives notification that a virtual machine's support for enhanced video mode has changed.<br/>                                          |
| [**OnGuestLogoff**](ivmvirtualmachineevents-onguestlogoff.md)                           | Receives notification that a user has logged off from the guest operating system.<br/>                                                    |
| [**OnGuestShutdown**](ivmvirtualmachineevents-onguestshutdown.md)                       | Receives notification that guest operating system has shut down.<br/>                                                                     |
| [**OnHeartbeatStopped**](ivmvirtualmachineevents-onheartbeatstopped.md)                 | Receives notification that a virtual machine's heartbeat has stopped. This usually indicates the guest operating system has crashed.<br/> |
| [**OnRequestShutdown**](ivmvirtualmachineevents-onrequestshutdown.md)                   | Receives notification that a shutdown request has been made.<br/>                                                                         |
| [**OnReset**](ivmvirtualmachineevents-onreset.md)                                       | Receives notification that a virtual machine has been reset.<br/>                                                                         |
| [**OnStateChange**](ivmvirtualmachineevents-onstatechange.md)                           | Receives notification that a virtual machine's state has changed.<br/>                                                                    |
| [**OnTripleFault**](ivmvirtualmachineevents-ontriplefault.md)                           | Receives notification that a virtual machine has triple-faulted.<br/>                                                                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | DIID\_IVMVirtualMachineEvents is defined as 9d84f560-bb67-4961-bd12-a4da780c67e4<br/>   |



 

