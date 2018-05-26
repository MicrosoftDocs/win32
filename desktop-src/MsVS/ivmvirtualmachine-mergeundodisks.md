---
title: IVMVirtualMachine MergeUndoDisks method
description: The MergeUndoDisks method merges the virtual undo disks.
ms.assetid: f129d05b-46a6-4441-952d-cd1bcdb9a866
keywords:
- MergeUndoDisks method Virtual Server
- MergeUndoDisks method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , MergeUndoDisks method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.MergeUndoDisks
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualMachine::MergeUndoDisks method

The **MergeUndoDisks** method merges the virtual undo disks.

## Syntax


```C++
HRESULT MergeUndoDisks(
  [out] IVMTask **undoMergeTask
);
```



## Parameters

<dl> <dt>

*undoMergeTask* \[out\]
</dt> <dd>

Retrieves the task which is used to track the creation of the image.

</dd> </dl>

## Return value



| Return code                                                                                        | Description                                                         |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>              | The operation was successful.<br/>                            |
| <dl> <dt>**E\_POINTER**</dt> </dl>          | The *undoMergeTask* parameter is **NULL**.<br/>               |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>  | Unknown configuration.<br/>                                   |
| <dl> <dt> **VM\_E\_VM\_RUNNING**</dt> </dl> | Cannot merge disks while the virtual machine is running.<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error has occurred.<br/>                        |



 

## Remarks

**MergeUndoDisks** cannot be called while the virtual machine is still running. Use [**IVMVirtualMachine::Save**](ivmvirtualmachine-save.md) to save the state of the virtual machine before calling **MergeUndoDisks**, or [**IVMVirtualMachine::TurnOff**](ivmvirtualmachine-turnoff.md) to turn off the virtual machine without saving its current state beforehand.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





