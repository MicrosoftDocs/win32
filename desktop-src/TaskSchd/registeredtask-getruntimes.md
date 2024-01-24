---
title: RegisteredTask.GetRunTimes method
description: For scripting, gets the times that the registered task is scheduled to run during a specified time.
ms.assetid: 'fc3d93eb-3186-419f-9f6f-7d54f8ade1ad'
keywords:
- GetRunTimes method Task Scheduler
- GetRunTimes method Task Scheduler , RegisteredTask object
- RegisteredTask object Task Scheduler , GetRunTimes method
topic_type:
- apiref
api_name:
- RegisteredTask.GetRunTimes
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegisteredTask.GetRunTimes method

For scripting, gets the times that the registered task is scheduled to run during a specified time.

## Syntax


```VB
RegisteredTask.GetRunTimes( _
  ByVal begin, _
  ByVal end, _
  ByRef count, _
  ByRef rgstTaskTimes _
)
```



## Parameters

<dl> <dt>

*begin* \[in\]
</dt> <dd>

The starting time for the query.

</dd> <dt>

*end* \[in\]
</dt> <dd>

The ending time for the query.

</dd> <dt>

*count* \[out\]
</dt> <dd>

The number of scheduled times the task will run.

</dd> <dt>

*rgstTaskTimes* \[out\]
</dt> <dd>

The scheduled times that the task will run.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If the registered task contains triggers that are individually disabled, these triggers will still affect the next scheduled run time that is returned even though they are disabled.

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
</dt> <dt>

[**RegisteredTask**](registeredtask.md)
</dt> </dl>

 

 





