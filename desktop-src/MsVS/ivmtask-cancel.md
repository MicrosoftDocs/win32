---
error-parsing-yaml: 
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
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMTask**](ivmtask.md)
</dt> </dl>

 

 





