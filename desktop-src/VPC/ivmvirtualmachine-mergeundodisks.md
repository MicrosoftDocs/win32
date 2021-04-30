---
title: IVMVirtualMachine MergeUndoDisks method (VPCCOMInterfaces.h)
description: Merges the virtual undo disks.
ms.assetid: 6445b097-220e-48c4-9a7b-1139ca7b3338
keywords:
- MergeUndoDisks method Virtual PC
- MergeUndoDisks method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , MergeUndoDisks method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.MergeUndoDisks
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::MergeUndoDisks method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Merges the virtual undo disks.

## Syntax


```C++
HRESULT MergeUndoDisks(
  [out, retval] IVMTask **undoMergeTask
);
```



## Parameters

<dl> <dt>

*undoMergeTask* \[out, retval\]
</dt> <dd>

An [**IVMTask**](ivmtask.md) object that is used to track the creation of the image.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                            | Description                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                                                                |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                            |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                    | The parameter is **NULL**.<br/>                                                                                                   |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)**</dt> <dt>0x80070003</dt> </dl> | The system cannot find the path specified by the *convertedDiskImagePath* parameter or one of the parent disks is not valid.<br/> |
| <dl> <dt>**E\_ACCESSDENIED**</dt> <dt>0x80070005</dt> </dl>                               | The current user has insufficient access to the parent file.<br/>                                                                 |
| <dl> <dt>**E\_HANDLE**</dt> <dt>0x80070006</dt> </dl>                                     | One of the parent disks is in use.<br/>                                                                                           |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>                            | The configuration is unknown.<br/>                                                                                                |
| <dl> <dt>**VM\_E\_VM\_RUNNING**</dt> <dt>0xA0040500</dt> </dl>                            | The virtual machine is running.<br/>                                                                                              |
| <dl> <dt>**VM\_E\_FILE\_READ\_ONLY**</dt> <dt>0xA004067A</dt> </dl>                       | The parent of virtual undo disks is marked as read only.<br/>                                                                     |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                            |



 

## Remarks

**MergeUndoDisks** cannot be called while the virtual machine is still running. Use [**IVMVirtualMachine::Save**](ivmvirtualmachine-save.md) to save the state of the virtual machine before calling **MergeUndoDisks**, or [**IVMVirtualMachine::TurnOff**](ivmvirtualmachine-turnoff.md) to turn off the virtual machine without saving its current state beforehand.

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

 

