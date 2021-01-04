---
title: IVMVirtualMachine Save method (VPCCOMInterfaces.h)
description: Saves the virtual machine (VM) state.
ms.assetid: e9f6e773-4e2d-4d7b-9624-e7864d5b248b
keywords:
- Save method Virtual PC
- Save method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , Save method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Save
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::Save method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Saves the virtual machine (VM) state.

## Syntax


```C++
HRESULT Save(
  [out, retval] IVMTask **saveTask
);
```



## Parameters

<dl> <dt>

*saveTask* \[out, retval\]
</dt> <dd>

An [**IVMTask**](ivmtask.md) object that is used to track the completion progress of the VM's state saving sequence.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                          | Description                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                | The operation was successful.<br/>                                                 |
| <dl> <dt>**E\_FAIL**</dt> <dt>0x80004005</dt> </dl>                                     | The VM could not be saved because the undo disks were marked for deletion.<br/>    |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                  | The parameter is **NULL**.<br/>                                                    |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ACCESS\_DENIED)**</dt> <dt>0x80070005</dt> </dl> | The caller must have execute access permissions to save the state of this VM.<br/> |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>                     | The VM is not running.<br/>                                                        |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                          | An unexpected error has occurred.<br/>                                             |



 

## Remarks

The VM is turned off when the **Save** task reaches completion. The [**IVMVirtualMachine::State**](ivmvirtualmachine-state.md) property will contain **vmVMState\_Saving** while the save is in progress, followed by **vmVMState\_Saved** when the save has completed and the VM is turned off.

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

 

