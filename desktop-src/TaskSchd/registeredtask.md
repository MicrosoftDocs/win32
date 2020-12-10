---
title: RegisteredTask object
description: Scripting object that provides the methods that are used to run the task immediately, get any running instances of the task, get or set the credentials that are used to register the task, and the properties that describe the task.
ms.assetid: 'd280f22b-4dd1-44df-be12-286fb1c029a3'
keywords:
- RegisteredTask object Task Scheduler
- RegisteredTask object Task Scheduler , described
topic_type:
- apiref
api_name:
- RegisteredTask
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegisteredTask object

Scripting object that provides the methods that are used to run the task immediately, get any running instances of the task, get or set the credentials that are used to register the task, and the properties that describe the task.

## Members

The **RegisteredTask** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **RegisteredTask** object has these methods.



| Method                                                                | Description                                                                                     |
|:----------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**GetInstances**](registeredtask-getinstances.md)                   | Returns all instances of the registered task that are currently running.<br/>             |
| [**GetRunTimes**](/windows/desktop/api/taskschd/nf-taskschd-iregisteredtask-getruntimes)                    | Gets the times that the registered task is scheduled to run during a specified time.<br/> |
| [**GetSecurityDescriptor**](registeredtask-getsecuritydescriptor.md) | Gets the security descriptor that is used as credentials for the registered task.<br/>    |
| [**Run**](registeredtask-run.md)                                     | Runs the registered task immediately.<br/>                                                |
| [**RunEx**](registeredtask-runex.md)                                 | Runs the registered task immediately using specified flags and a session identifier.<br/> |
| [**SetSecurityDescriptor**](registeredtask-setsecuritydescriptor.md) | Sets the security descriptor that is used as credentials for the registered task.<br/>    |
| [**Stop**](registeredtask-stop.md)                                   | Stops the registered task immediately.<br/>                                               |



 

### Properties

The **RegisteredTask** object has these properties.



| Property                                                                   | Access type           | Description                                                                               |
|:---------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------|
| [**Definition**](registeredtask-definition.md)<br/>                 | Read-only<br/>  | Gets the definition of the task.<br/>                                               |
| [**Enabled**](registeredtask-enabled.md)<br/>                       | Read/write<br/> | Gets or set a Boolean value that indicates if the registered task is enabled.<br/>  |
| [**LastRunTime**](registeredtask-lastruntime.md)<br/>               | Read-only<br/>  | Gets the time the registered task was last run.<br/>                                |
| [**LastTaskResult**](registeredtask-lasttaskresult.md)<br/>         | Read-only<br/>  | Gets the results that were returned the last time the registered task was run.<br/> |
| [**Name**](registeredtask-name.md)<br/>                             | Read-only<br/>  | Gets the name of the registered task.<br/>                                          |
| [**NextRunTime**](registeredtask-nextruntime.md)<br/>               | Read-only<br/>  | Gets the time when the registered task is next scheduled to run.<br/>               |
| [**NumberOfMissedRuns**](registeredtask-numberofmissedruns.md)<br/> | Read-only<br/>  | Gets the number of times the registered task has missed a scheduled run.<br/>       |
| [**Path**](registeredtask-path.md)<br/>                             | Read-only<br/>  | Gets the path to where the registered task is stored.<br/>                          |
| [**State**](registeredtask-state.md)<br/>                           | Read-only<br/>  | Gets the operational state of the registered task.<br/>                             |
| [**XML**](registeredtask-xml.md)<br/>                               | Read-only<br/>  | Gets the XML-formatted registration information for the registered task.<br/>       |



 

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md) and [Displaying Task Names and States (Scripting)](displaying-task-names-and-state--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





