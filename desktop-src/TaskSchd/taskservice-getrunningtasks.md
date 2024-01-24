---
title: TaskService.GetRunningTasks method
description: For scripting, gets a collection of running tasks.
ms.assetid: 'bae3c035-a6b2-4ca5-970b-d4bc808068ad'
keywords:
- GetRunningTasks method Task Scheduler
- GetRunningTasks method Task Scheduler , TaskService object
- TaskService object Task Scheduler , GetRunningTasks method
topic_type:
- apiref
api_name:
- TaskService.GetRunningTasks
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskService.GetRunningTasks method

For scripting, gets a collection of running tasks.

> [!Note]  
> **TaskService.GetRunningTasks** will only return a collection of running tasks that are running at or below a user's security context. For example, for members of the Administrators group, **GetRunningTasks** will return a collection of all running tasks, but for members of the Users group, **GetRunningTasks** will only return a collection of tasks that are running under the Users group security context.

 

## Syntax


```VB
TaskService.GetRunningTasks( _
  ByVal flags _
)
```



## Parameters

<dl> <dt>

*flags* \[in\]
</dt> <dd>

Pass in 1 to return all running tasks, including hidden tasks. Pass in 0 to return a collection of running tasks that are not hidden tasks.

</dd> </dl>

## Return value

A [**RunningTaskCollection**](runningtaskcollection.md) object that contains the currently running tasks.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





