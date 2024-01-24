---
title: IVMAccountant interface (VPCCOMInterfaces.h)
description: Provides access to accounting-related information for a virtual machine.
ms.assetid: 047fa4c9-cb2e-4830-bab8-0513247eff9b
keywords:
- IVMAccountant interface Virtual PC
- IVMAccountant interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMAccountant
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMAccountant interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Provides access to accounting-related information for a virtual machine. To retrieve the **IVMAccountant** for a virtual machine, use the [**IVMVirtualMachine::Accountant**](ivmvirtualmachine-accountant.md) property.

## Members

The **IVMAccountant** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMAccountant** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMAccountant** interface has these properties.



| Property                                                                        | Access type          | Description                                                                                             |
|:--------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------|
| [**CPUUtilization**](ivmaccountant-cpuutilization.md)<br/>               | Read-only<br/> | The percentage of current CPU utilization for this virtual machine.<br/>                          |
| [**CPUUtilizationHistory**](ivmaccountant-cpuutilizationhistory.md)<br/> | Read-only<br/> | The recent CPU utilization of this virtual machine (as an array of percentage values).<br/>       |
| [**DiskBytesRead**](ivmaccountant-diskbytesread.md)<br/>                 | Read-only<br/> | The total number of bytes read by all storage controllers for this virtual machine.<br/>          |
| [**DiskBytesWritten**](ivmaccountant-diskbyteswritten.md)<br/>           | Read-only<br/> | The total number of bytes written by all storage controllers for this virtual machine.<br/>       |
| [**NetworkBytesReceived**](ivmaccountant-networkbytesreceived.md)<br/>   | Read-only<br/> | The total number of bytes received by all virtual network adapters for this virtual machine.<br/> |
| [**NetworkBytesSent**](ivmaccountant-networkbytessent.md)<br/>           | Read-only<br/> | The total number of bytes sent by all virtual network adapters for this virtual machine.<br/>     |
| [**UpTime**](ivmaccountant-uptime.md)<br/>                               | Read-only<br/> | The number of seconds that the virtual machine has been running.<br/>                             |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMAccountant is defined as 6376c067-7f57-4d63-b754-06e2e4f51d73<br/>              |



 

