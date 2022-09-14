---
title: RunningTask object
description: Scripting object that provides the methods to get information from and control a running task.
ms.assetid: '335e69d8-affa-4845-a067-641184e0f7df'
keywords:
- RunningTask object Task Scheduler
- RunningTask object Task Scheduler , described
topic_type:
- apiref
api_name:
- RunningTask
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RunningTask object

Scripting object that provides the methods to get information from and control a running task.

## Members

The **RunningTask** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **RunningTask** object has these methods.



| Method                                 | Description                                                           |
|:---------------------------------------|:----------------------------------------------------------------------|
| [**Refresh**](runningtask-refresh.md) | Refreshes all of the local instance variables of the task.<br/> |
| [**Stop**](runningtask-stop.md)       | Stops this instance of the task.<br/>                           |



 

### Properties

The **RunningTask** object has these properties.



| Property                                                      | Access type          | Description                                                                         |
|:--------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------|
| [**CurrentAction**](runningtask-currentaction.md)<br/> | Read-only<br/> | Gets the name of the current action that the running task is performing.<br/> |
| [**EnginePID**](runningtask-enginepid.md)<br/>         | Read-only<br/> | Gets the process ID for the engine (process) which is running the task.<br/>  |
| [**InstanceGuid**](runningtask-instanceguid.md)<br/>   | Read-only<br/> | Gets the GUID identifier for this instance of the task.<br/>                  |
| [**Name**](runningtask-name.md)<br/>                   | Read-only<br/> | Gets the name of the task.<br/>                                               |
| [**Path**](runningtask-path.md)<br/>                   | Read-only<br/> | Gets the path to where the task is stored.<br/>                               |
| [**State**](runningtask-state.md)<br/>                 | Read-only<br/> | Gets the state of the running task. <br/>                                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler Objects](task-scheduler-objects.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> <dt>

[**RunningTaskCollection**](runningtaskcollection.md)
</dt> <dt>

[**RegisteredTask.Run**](registeredtask-run.md)
</dt> <dt>

[**RegisteredTask.RunEx**](registeredtask-runex.md)
</dt> </dl>

 

 





