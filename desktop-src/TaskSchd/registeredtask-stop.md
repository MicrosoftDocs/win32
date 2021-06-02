---
title: RegisteredTask.Stop method
description: For scripting, stops the registered task immediately.
ms.assetid: 'e4a533d8-5cf0-46ba-a603-f7a9c59ab0fd'
keywords:
- Stop method Task Scheduler
- Stop method Task Scheduler , RegisteredTask object
- RegisteredTask object Task Scheduler , Stop method
topic_type:
- apiref
api_name:
- RegisteredTask.Stop
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegisteredTask.Stop method

For scripting, stops the registered task immediately.

## Syntax


```VB
RegisteredTask.Stop( _
  ByVal flags _
)
```



## Parameters

<dl> <dt>

*flags* \[in\]
</dt> <dd>

Reserved. Must be zero.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The **RegisteredTask.Stop** function stops all instances of the task.

System account users can stop a task, users with Administrator group privileges can stop a task, and if a user has rights to execute and read a task, then the user can stop the task. A user can stop the task instances that are running under the same credentials as the user account. In all other cases, the user is denied access to stop the task.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**RegisteredTask**](registeredtask.md)
</dt> </dl>

 

 





