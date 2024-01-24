---
title: IVMVirtualMachine Undoable property (VPCCOMInterfaces.h)
description: Determines whether undo drives are enabled for hard disks connected to the VM.
ms.assetid: 4f591360-1229-46ae-9925-3a3d02ab3202
keywords:
- Undoable property Virtual PC
- Undoable property Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , Undoable property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Undoable
- IVMVirtualMachine.get_Undoable
- IVMVirtualMachine.put_Undoable
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::Undoable property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Determines whether undo drives are enabled for hard disks connected to the virtual machine (VM).

This property is read/write.

## Syntax


```C++
HRESULT put_Undoable(
  [in]          VARIANT_BOOL enableUndo
);

HRESULT get_Undoable(
  [out, retval] VARIANT_BOOL *isUndoable
);
```



## Property value

Specifies **VARIANT\_TRUE** if undo drives are enabled for hard disks connected to the VM and **VARIANT\_FALSE** otherwise.

## Error codes



| Name/value                                                                                                                                                         | Meaning                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                            | The operation was successful.<br/>     |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>      | An unexpected error has occurred.<br/> |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>              | The parameter is **NULL**.<br/>        |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>      | The configuration is unknown.<br/>     |
| <dl> <dt>VM\_E\_PREF\_VM\_ACTIVE</dt> <dt>0xA0040302</dt> </dl> | The VM is running or saved.<br/>       |



## Remarks

If undo drives are disabled, any existing undo drive files will be deleted.

You cannot set this property if the VM is running or saved.

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

 

