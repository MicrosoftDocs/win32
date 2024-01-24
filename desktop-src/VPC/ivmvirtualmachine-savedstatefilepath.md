---
title: IVMVirtualMachine SavedStateFilePath property (VPCCOMInterfaces.h)
description: Retrieves the full path to the saved state file.
ms.assetid: 01bd5491-4d08-4558-ac33-01b096f057a2
keywords:
- SavedStateFilePath property Virtual PC
- SavedStateFilePath property Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , SavedStateFilePath property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.SavedStateFilePath
- IVMVirtualMachine.get_SavedStateFilePath
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::SavedStateFilePath property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the full path to the saved state file.

This property is read-only.

## Syntax


```C++
HRESULT get_SavedStateFilePath(
  [out, retval] BSTR *savedStateFilePath
);
```



## Property value

The fully qualified path to the virtual machine's saved state file.

## Error codes



| Name/value                                                                                                                                                              | Meaning                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                 | The operation was successful.<br/>                           |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                   | The parameter is **NULL**.<br/>                              |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>           | The configuration is unknown.<br/>                           |
| <dl> <dt>VM\_E\_VM\_NO\_SAVED\_STATE</dt> <dt>0xA00400501</dt> </dl> | The virtual machine has no associated saved state file.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>           | An unexpected error has occurred.<br/>                       |



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

 

