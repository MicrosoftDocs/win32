---
title: IVMVirtualMachine Mouse property (VPCCOMInterfaces.h)
description: Retrieves the mouse device for the virtual machine.
ms.assetid: 917bbcc1-615d-4fd7-87e1-62abf2ece539
keywords:
- Mouse property Virtual PC
- Mouse property Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , Mouse property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Mouse
- IVMVirtualMachine.get_Mouse
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::Mouse property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the mouse device for the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_Mouse(
  [out, retval] IVMMouse **mouse
);
```



## Property value

An [**IVMMouse**](ivmmouse.md) object.

## Error codes



| Name/value                                                                                                                                                         | Meaning                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                            | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>              | The parameter is **NULL**.<br/>          |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>      | The configuration is unknown.<br/>       |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl> | The virtual machine is not running.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>      | An unexpected error has occurred.<br/>   |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualMachine is defined as f7092aa1-33ed-4f78-a59f-c00adfc2edd7<br/>          |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

