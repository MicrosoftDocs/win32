---
title: RegisteredTask.NextRunTime property
description: For scripting, gets the time when the registered task is next scheduled to run.
ms.assetid: 'f63298a8-c9fa-4fea-ad0b-2c8739aced19'
keywords:
- NextRunTime property Task Scheduler
- NextRunTime property Task Scheduler , RegisteredTask object
- RegisteredTask object Task Scheduler , NextRunTime property
topic_type:
- apiref
api_name:
- RegisteredTask.NextRunTime
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegisteredTask.NextRunTime property

For scripting, gets the time when the registered task is next scheduled to run.

## Syntax


```VB
RegisteredTask.NextRunTime As String
```



## Property value

The time when the registered task is next scheduled to run.

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

 

 





