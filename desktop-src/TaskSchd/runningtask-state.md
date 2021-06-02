---
title: RunningTask.State property
description: For scripting, gets an identifier for the state of the running task.
ms.assetid: '048863f4-b80b-42ab-bd74-ec761a8f03aa'
keywords:
- State property Task Scheduler
- State property Task Scheduler , RunningTask object
- RunningTask object Task Scheduler , State property
topic_type:
- apiref
api_name:
- RunningTask.State
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RunningTask.State property

For scripting, gets an identifier for the state of the running task.

This property is read-only.

## Syntax


```VB
RunningTask.State As String
```



## Property value

An identifier for the state of the running task.



| Value                                                                                                                                                                                                                                   | Meaning                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TASK_STATE_UNKNOWN"></span><span id="task_state_unknown"></span><dl> <dt>**TASK\_STATE\_UNKNOWN**</dt> <dt>0</dt> </dl>    | The state of the task is unknown.<br/>                                                                                                      |
| <span id="TASK_STATE_DISABLED"></span><span id="task_state_disabled"></span><dl> <dt>**TASK\_STATE\_DISABLED**</dt> <dt>1</dt> </dl> | The task is registered but is disabled and no instances of the task are queued or running. The task cannot be run until it is enabled.<br/> |
| <span id="TASK_STATE_QUEUED"></span><span id="task_state_queued"></span><dl> <dt>**TASK\_STATE\_QUEUED**</dt> <dt>2</dt> </dl>       | Instances of the task are queued.<br/>                                                                                                      |
| <span id="TASK_STATE_READY"></span><span id="task_state_ready"></span><dl> <dt>**TASK\_STATE\_READY**</dt> <dt>3</dt> </dl>          | The task is ready to be executed, but no instances are queued or running.<br/>                                                              |
| <span id="TASK_STATE_RUNNING"></span><span id="task_state_running"></span><dl> <dt>**TASK\_STATE\_RUNNING**</dt> <dt>4</dt> </dl>    | One or more instances of the task are running.<br/>                                                                                         |



 

## Remarks

The [**RunningTask.Refresh**](runningtask-refresh.md) method is called before the property value is returned.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





