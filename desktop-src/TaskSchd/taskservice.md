---
title: TaskService object
description: For scripting, provides access to the Task Scheduler service for managing registered tasks.
ms.assetid: '6ddd43dc-d027-4792-a53b-07fe4d4a3576'
keywords:
- TaskService object Task Scheduler
- TaskService object Task Scheduler , described
topic_type:
- apiref
api_name:
- TaskService
- HighestVersion
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskService object

For scripting, provides access to the Task Scheduler service for managing registered tasks.

The [**TaskService.Connect**](taskservice-connect.md) method should be called before calling any of the other **TaskService** methods.

## Members

The **TaskService** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **TaskService** object has these methods.



| Method                                                 | Description                                                                                                                                                                                                          |
|:-------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Connect**](taskservice-connect.md)                 | Connects to a remote machine and associates all subsequent calls on this interface with a remote session.<br/>                                                                                                 |
| [**GetFolder**](taskservice-getfolder.md)             | Gets the path to a folder of registered tasks.<br/>                                                                                                                                                            |
| [**GetRunningTasks**](taskservice-getrunningtasks.md) | Gets a collection of running tasks.<br/>                                                                                                                                                                       |
| [**NewTask**](taskservice-newtask.md)                 | Returns an empty task definition object to be filled in with settings and properties and then registered using the [**TaskFolder.RegisterTaskDefinition**](taskfolder-registertaskdefinition.md) method.<br/> |



 

### Properties

The **TaskService** object has these properties.



| Property                                                          | Description                                                                                                                 |
|:------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**Connected**](taskservice-connected.md)<br/>             | Gets a Boolean value that indicates if you are connected to the Task Scheduler service.<br/>                          |
| [**ConnectedDomain**](taskservice-connecteddomain.md)<br/> | Gets the name of the domain to which the [**TargetServer**](taskservice-targetserver.md) computer is connected.<br/> |
| [**ConnectedUser**](taskservice-connecteduser.md)<br/>     | Gets the name of the user that is connected to the Task Scheduler service.<br/>                                       |
| HighestVersion<br/>                                         | Gets the highest version of Task Scheduler that a computer supports.<br/>                                             |
| [**TargetServer**](taskservice-targetserver.md)<br/>       | Gets the name of the computer that is running the Task Scheduler service that the user is connected to.<br/>          |



 

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md), [Event Trigger Example (Scripting)](https://www.bing.com/search?q=Event+Trigger+Example+(Scripting)), [Daily Trigger Example (Scripting)](daily-trigger-example--scripting-.md), [Registration Trigger Example (Scripting)](registration-trigger-example--scripting-.md), [Weekly Trigger Example (Scripting)](weekly-trigger-example--scripting-.md), [Logon Trigger Example (Scripting)](logon-trigger-example--scripting-.md), [Boot Trigger Example (Scripting)](boot-trigger-example--scripting-.md), or [Displaying Task Names and States (Scripting)](displaying-task-names-and-state--scripting-.md).

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

 

 





