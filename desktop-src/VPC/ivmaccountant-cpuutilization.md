---
title: IVMAccountant CPUUtilization property (VPCCOMInterfaces.h)
description: Retrieves the percentage of current CPU utilization for this virtual machine.
ms.assetid: 69bb61ec-af41-4bd0-95bd-4698a1d33098
keywords:
- CPUUtilization property Virtual PC
- CPUUtilization property Virtual PC , IVMAccountant interface
- IVMAccountant interface Virtual PC , CPUUtilization property
topic_type:
- apiref
api_name:
- IVMAccountant.CPUUtilization
- IVMAccountant.get_CPUUtilization
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMAccountant::CPUUtilization property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the percentage of current CPU utilization for this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_CPUUtilization(
  [out, retval] long *percentageUtilization
);
```



## Property value

The percentage of current CPU utilization.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>          |
| <dl> <dt>S\_FALSE</dt> <dt>1</dt> </dl>                    | The virtual machine is not running.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>   |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMAccountant is defined as 6376c067-7f57-4d63-b754-06e2e4f51d73<br/>              |



## See also

<dl> <dt>

[**IVMAccountant**](ivmaccountant.md)
</dt> </dl>

 

