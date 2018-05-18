---
title: IVMVirtualMachine DiscardUndoDisks method
description: The DiscardUndoDisks method discards the virtual undo disks.
ms.assetid: '4c076627-3c56-41bc-828d-700163cc7009'
keywords: ["DiscardUndoDisks method Virtual Server", "DiscardUndoDisks method Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , DiscardUndoDisks method"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.DiscardUndoDisks
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::DiscardUndoDisks method

The **DiscardUndoDisks** method discards the virtual undo disks.

## Syntax


```C++
HRESULT DiscardUndoDisks();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                             | Description                                    |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                   | The operation was successful.<br/>       |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>       | Unknown configuration.<br/>              |
| <dl> <dt> **VM\_E\_VM\_NOT\_RUNNING**</dt> </dl> | The virtual machine is not running.<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>      | An unexpected error has occurred.<br/>   |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





