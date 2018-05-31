---
title: IVMVirtualMachine DiscardSavedState method
description: The DiscardSavedState method discards any saved state information for a saved virtual machine.
ms.assetid: cb359580-aed7-46dd-89de-583e99b5b48c
keywords:
- DiscardSavedState method Virtual Server
- DiscardSavedState method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , DiscardSavedState method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.DiscardSavedState
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

# IVMVirtualMachine::DiscardSavedState method

The **DiscardSavedState** method discards any saved state information for a saved virtual machine.

## Syntax


```C++
HRESULT DiscardSavedState();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                                | Description                                                            |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                      | The operation was successful.<br/>                               |
| <dl> <dt> **VM\_E\_VM\_UNKNOWN**</dt> </dl>         | The configuration is unknown.<br/>                               |
| <dl> <dt>**VM\_E\_VM\_RUNNING**</dt> </dl>          | The virtual machine is running.<br/>                             |
| <dl> <dt>**VM\_E\_VM\_NO\_SAVED\_STATE**</dt> </dl> | The virtual machine is not running, but has no saved state.<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>         | An unexpected error has occurred.<br/>                           |



 

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

 

 





