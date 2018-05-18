---
title: IVMTask Cancel method
description: The Cancel method cancels a task.
ms.assetid: '616e0d37-3cff-47e1-909d-b6c0600173cb'
keywords: ["Cancel method Virtual Server", "Cancel method Virtual Server , IVMTask interface", "IVMTask interface Virtual Server , Cancel method", "Cancel method Virtual Server , VMTask interface", "VMTask interface Virtual Server , Cancel method"]
topic_type:
- apiref
api_name:
- IVMTask.Cancel
- VMTask.Cancel
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMTask::Cancel method

The **Cancel** method cancels a task.

## Syntax


```C++
HRESULT Cancel();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                       | Description                              |
|---------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>             | The operation was successful.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>            | The task cannot be canceled.<br/>  |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMTask**](ivmtask.md)
</dt> </dl>

 

 





