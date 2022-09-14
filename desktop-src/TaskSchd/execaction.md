---
title: ExecAction object
description: Scripting object that represents an action that executes a command-line operation.
ms.assetid: 51d2746d-3a90-4e8b-ac2b-d73193b3aa74
keywords:
- execute action Task Scheduler , interface
- ExecAction object Task Scheduler
- ExecAction object Task Scheduler , described
topic_type:
- apiref
api_name:
- ExecAction
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ExecAction object

Scripting object that represents an action that executes a command-line operation.

## Members

The **ExecAction** object has these types of members:

-   [Properties](#properties)

### Properties

The **ExecAction** object has these properties.



| Property                                                            | Access type           | Description                                                                                                                       |
|:--------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| [**Arguments**](/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_arguments)<br/>               | Read/write<br/> | Gets or sets the arguments associated with the command-line operation.<br/>                                                 |
| [**Id**](/windows/desktop/api/taskschd/nf-taskschd-iaction-get_id)<br/>                                 | Read/write<br/> | Inherited from the [**Action**](action.md) object. Gets or sets the identifier of the action.<br/>                         |
| [**Path**](/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_path)<br/>                         | Read/write<br/> | Gets or sets the path to an executable file.<br/>                                                                           |
| [**Type**](/windows/desktop/api/taskschd/nf-taskschd-iaction-get_type)<br/>                             | Read-only<br/>  | Inherited from the [**Action**](action.md) object. Gets the type of the action.<br/>                                       |
| [**WorkingDirectory**](/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_workingdirectory)<br/> | Read/write<br/> | Gets or sets the directory that contains either the executable file or the files that are used by the executable file.<br/> |



 

## Remarks

If environment variables are used in the [**Path**](/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_path), [**Arguments**](/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_arguments), or [**WorkingDirectory**](/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_workingdirectory) properties, then the values of the environment variables are cached and used when the Taskeng.exe (the task engine) is launched. Changes to the environment variables that occur after the task engine is launched will not be used by the task engine.

This action performs a command-line operation. For example, the action could run a script or launch an executable.

When reading or writing XML, an execution action is specified in the [**Exec**](taskschedulerschema-exec-actiongroup-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





