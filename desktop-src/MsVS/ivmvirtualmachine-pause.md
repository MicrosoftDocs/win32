---
title: IVMVirtualMachine Pause method
description: The Pause method pauses the virtual machine.
ms.assetid: 3cb5950c-a709-438d-8845-2c1c84aa1d40
keywords:
- Pause method Virtual Server
- Pause method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , Pause method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Pause
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::Pause method

The **Pause** method pauses the virtual machine.

## Syntax


```C++
HRESULT Pause();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                         | Description                                                                               |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>                                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>              | The virtual machine is already paused.<br/>                                         |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>      | The caller must have execute access permissions to pause this virtual machine.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>   | Unknown configuration.<br/>                                                         |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl> | An unexpected error has occurred.<br/>                                              |



 

## Remarks

**Pause** does not save the current state of the virtual machine.

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

 

 





