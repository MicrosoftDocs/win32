---
title: TaskFolder object
description: Scripting object that provides the methods that are used to register (create) tasks in the folder, remove tasks from the folder, and create or remove subfolders from the folder.
ms.assetid: 'f6fd09ec-2777-4903-83b5-e3ac1aa472a0'
keywords:
- TaskFolder object Task Scheduler
- TaskFolder object Task Scheduler , described
topic_type:
- apiref
api_name:
- TaskFolder
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskFolder object

Scripting object that provides the methods that are used to register (create) tasks in the folder, remove tasks from the folder, and create or remove subfolders from the folder.

## Members

The **TaskFolder** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **TaskFolder** object has these methods.



| Method                                                              | Description                                                                                                                                    |
|:--------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateFolder**](taskfolder-createfolder.md)                     | Creates a folder for related tasks.<br/>                                                                                                 |
| [**DeleteFolder**](taskfolder-deletefolder.md)                     | Deletes a subfolder from the parent folder.<br/>                                                                                         |
| [**DeleteTask**](taskfolder-deletetask.md)                         | Deletes a task from the folder.<br/>                                                                                                     |
| [**GetFolder**](taskfolder-getfolder.md)                           | Gets a folder that contains tasks at a specified location.<br/>                                                                          |
| [**GetFolders**](taskfolder-getfolders.md)                         | Gets all the subfolders in the folder.<br/>                                                                                              |
| [**GetSecurityDescriptor**](taskfolder-getsecuritydescriptor.md)   | Gets the security descriptor for the folder.<br/>                                                                                        |
| [**GetTask**](taskfolder-gettask.md)                               | Gets a task at a specified location in a folder.<br/>                                                                                    |
| [**GetTasks**](taskfolder-gettasks.md)                             | Gets all the tasks in the folder.<br/>                                                                                                   |
| [**RegisterTask**](taskfolder-registertask.md)                     | Registers (creates) a new task in the folder using XML to define the task.<br/>                                                          |
| [**RegisterTaskDefinition**](taskfolder-registertaskdefinition.md) | Registers (creates) a task in a specified location using the [**ITaskDefinition**](/windows/desktop/api/taskschd/nn-taskschd-itaskdefinition) interface to define a task.<br/> |
| [**SetSecurityDescriptor**](taskfolder-setsecuritydescriptor.md)   | Sets the security descriptor for the folder.<br/>                                                                                        |



 

### Properties

The **TaskFolder** object has these properties.



| Property                                   | Access type          | Description                                                                        |
|:-------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------|
| [**Name**](taskfolder-name.md)<br/> | Read-only<br/> | Gets the name that is used to identify the folder that contains a task.<br/> |
| [**Path**](taskfolder-path.md)<br/> | Read-only<br/> | Gets the path to where the folder is stored.<br/>                            |



 

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

[Task Scheduler Objects](task-scheduler-objects.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





