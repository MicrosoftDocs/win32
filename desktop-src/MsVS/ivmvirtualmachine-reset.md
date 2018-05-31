---
title: IVMVirtualMachine Reset method
description: The Reset method resets the virtual machine (like hitting the reset button on a real machine).
ms.assetid: 037e8d9d-492a-4d2d-a0c2-49a3e98f4148
keywords:
- Reset method Virtual Server
- Reset method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , Reset method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Reset
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualMachine::Reset method

The **Reset** method resets the virtual machine (like hitting the reset button on a real machine).

## Syntax


```C++
HRESULT Reset(
  [out] IVMTask **resetTask
);
```



## Parameters

<dl> <dt>

*resetTask* \[out\]
</dt> <dd>

A task that is used to track the completion progress of the virtual machine's reset sequence.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                             | Description                                                                               |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                   | The operation was successful.<br/>                                                  |
| <dl> <dt>**E\_POINTER**</dt> </dl>               | The *resetTask* parameter is **NULL**.<br/>                                         |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>          | The caller must have execute access permissions to reset this virtual machine.<br/> |
| <dl> <dt> **VM\_E\_VM\_NOT\_RUNNING**</dt> </dl> | The virtual machine is not running.<br/>                                            |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>      | An unexpected error has occurred.<br/>                                              |



 

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

 

 





