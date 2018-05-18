---
title: IVMVirtualMachineEvents interface
description: Defines the outgoing event interface for the IVMVirtualMachine interface.
ms.assetid: 'e086070a-0879-498e-a45f-bbc35bdc18b8'
keywords: ["IVMVirtualMachineEvents interface Virtual Server", "IVMVirtualMachineEvents interface Virtual Server , described"]
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachineEvents interface

The **IVMVirtualMachineEvents** interface defines the outgoing event interface for the [**IVMVirtualMachine**](ivmvirtualmachine.md) interface.

## When to implement

The client implements these methods to receive events sent from [**IVMVirtualMachine**](ivmvirtualmachine.md).

## Members

The **IVMVirtualMachineEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IVMVirtualMachineEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVMVirtualMachineEvents** interface has these methods.



| Method                                                                           | Description                                                                               |
|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**OnConfigurationChanged**](ivmvirtualmachineevents-onconfigurationchanged.md) | Called when a value in the configuration for this virtual machine has changed.<br/> |
| [**OnHeartbeatStopped**](ivmvirtualmachineevents-onheartbeatstopped.md)         | Called when the heartbeat of a virtual machine has stopped.<br/>                    |
| [**OnRequestShutdown**](ivmvirtualmachineevents-onrequestshutdown.md)           | Called to request a shutdown operation.<br/>                                        |
| [**OnReset**](ivmvirtualmachineevents-onreset.md)                               | Called when a virtual machine has been reset.<br/>                                  |
| [**OnStateChange**](ivmvirtualmachineevents-onstatechange.md)                   | Called when the state of a virtual machine has changed.<br/>                        |
| [**OnTripleFault**](ivmvirtualmachineevents-ontriplefault.md)                   | Called when a virtual machine has triple-faulted.<br/>                              |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





