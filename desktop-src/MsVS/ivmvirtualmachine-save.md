---
title: IVMVirtualMachine Save method
description: The Save method saves the state of the virtual machine.
ms.assetid: a368a721-ff40-4b92-8065-87145fa317c7
keywords:
- Save method Virtual Server
- Save method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , Save method
- Save method Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , Save method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Save
- VMVirtualMachine.Save
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

# IVMVirtualMachine::Save method

The **Save** method saves the state of the virtual machine.

## Syntax


```C++
HRESULT Save(
  [out] IVMTask **saveTask
);
```



## Parameters

<dl> <dt>

*saveTask* \[out\]
</dt> <dd>

A task that is used to track the completion progress of the virtual machine's state saving sequence.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                              | Description                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>                   | The operation was successful.<br/>                                                                                                                |
| <dl> <dt>**E\_POINTER**</dt> </dl>                | The *saveTask* parameter is **NULL**.<br/>                                                                                                        |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>           | The caller must have execute access permissions to save the state of this virtual machine.<br/>                                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>                   | The [**IVMVirtualMachine::UndoAction**](ivmvirtualmachine-undoaction.md) was set to **vmUndoAction\_Discard** which would cause corruption.<br/> |
| <dl> <dt> **VM\_E\_VM\_NOT\_RUNNING** </dt> </dl> | The virtual machine is not running.<br/>                                                                                                          |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl>      | An unexpected error has occurred.<br/>                                                                                                            |



 

## Remarks

The virtual machine is turned off once the **Save** task reaches completion. The [**IVMVirtualMachine::State**](ivmvirtualmachine-state.md) property will contain [**vmVMState\_Saving**](vmvmstate.md) while the save is in progress, followed by **vmVMState\_Saved** once the save has completed and the virtual machine is turned off.

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

 

 





