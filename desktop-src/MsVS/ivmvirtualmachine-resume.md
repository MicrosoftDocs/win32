---
title: IVMVirtualMachine Resume method
description: The Resume method resumes a paused virtual machine
ms.assetid: c1f0c4d4-50b7-45ae-b050-22897744f6cd
keywords:
- Resume method Virtual Server
- Resume method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , Resume method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Resume
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

# IVMVirtualMachine::Resume method

The **Resume** method resumes a paused virtual machine

## Syntax


```C++
HRESULT Resume();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                         | Description                                                                                |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>                                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>              | The virtual machine was not paused.<br/>                                             |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>      | The caller must have execute access permissions to resume this virtual machine.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>   | Unknown configuration.<br/>                                                          |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl> | An unexpected error has occurred.<br/>                                               |



 

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

 

 





