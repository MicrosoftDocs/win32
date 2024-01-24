---
title: IVMVirtualMachine Reset method (VPCCOMInterfaces.h)
description: Resets the virtual machine.
ms.assetid: 44daf6be-66ce-4291-a535-c30369eed60f
keywords:
- Reset method Virtual PC
- Reset method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , Reset method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Reset
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::Reset method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Resets the virtual machine (VM).

## Syntax


```C++
HRESULT Reset(
  [out, retval] IVMTask **resetTask
);
```



## Parameters

<dl> <dt>

*resetTask* \[out, retval\]
</dt> <dd>

An [**IVMTask**](ivmtask.md) object that is used to track the completion progress of the VM's reset sequence.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                          | Description                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                | The operation was successful.<br/>                                     |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                  | The parameter is **NULL**.<br/>                                        |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ACCESS\_DENIED)**</dt> <dt>0x80070005</dt> </dl> | The caller must have execute access permissions to reset this VM.<br/> |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>                     | The VM is not running.<br/>                                            |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>                          | The configuration is unknown.<br/>                                     |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                          | An unexpected error has occurred.<br/>                                 |



 

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

 

