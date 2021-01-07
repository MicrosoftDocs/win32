---
description: Reports the health status of an application that is running in a virtual machine to the Hyper-V integration components running in the same virtual machine.
ms.assetid: C463391B-669C-4CBA-9EC7-7E0ABC5A63A1
title: IVmApplicationHealthMonitor interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmApplicationHealthMonitor
api_type: 
- COM
api_location: 
- VmApplicationHealthMonitor.idl
---

# IVmApplicationHealthMonitor interface

Reports the health status of an application that is running in a virtual machine to the Hyper-V integration components running in the same virtual machine. The state of the applications running in the virtual machine are reflected in the **OperationalStatus**\[1\] property value of the [**Msvm\_HeartbeatComponent**](msvm-heartbeatcomponent.md) class. This interface also provides a way to reset all of the application state accumulated in Hyper-V.

This interface is implemented by the Windows 8 Hyper-V integration components. An instance of this interface is obtained by creating an instance of the **397a2e5f-348c-482d-b9a3-57d383b483cd** CLSID.

## Members

The **IVmApplicationHealthMonitor** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVmApplicationHealthMonitor** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVmApplicationHealthMonitor** interface has these methods.



| Method                                                                                   | Description                                                                              |
|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**ResetAllApplicationState**](ivmapplicationhealthmonitor-resetallapplicationstate.md) | Resets the health state for all applications in a virtual machine.<br/>            |
| [**SetApplicationState**](ivmapplicationhealthmonitor-setapplicationstate.md)           | Sets the health state of an application that is running in a virtual machine.<br/> |



 

## Remarks

To use this programming element, the Windows 8 integration components must be installed on the virtual machine that the application is running in.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                                                                                     |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                                                                                           |
| Version<br/>                  | Integration components for Windows 8<br/>                                                                                                                                |
| IDL<br/>                      | <dl> <dt>VmApplicationHealthMonitor.idl</dt> </dl>                                                                      |
| IID<br/>                      | IID\_IVmApplicationHealthMonitor is defined as 267a0284-848f-447e-a096-5e10a1a76bca<br/> Object Identifier is defined as 397a2e5f-348c-482d-b9a3-57d383b483cd<br/> |



 

