---
title: ExecAction.Path property
description: For scripting, gets or sets the path to an executable file.
ms.assetid: 00fea05f-4f57-47ac-9812-8cd352fe02a8
keywords:
- Path property Task Scheduler
- Path property Task Scheduler , ExecAction object
- ExecAction object Task Scheduler , Path property
topic_type:
- apiref
api_name:
- ExecAction.Path
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ExecAction.Path property

For scripting, gets or sets the path to an executable file.

## Syntax


```VB
ExecAction.Path As String
```



## Property value

The path to the executable file to be run by the action.

## Remarks

This action performs a command-line operation. For example, the action could run a script or launch an executable.

When reading or writing XML, the command-line operation path is specified in the [**Command**](taskschedulerschema-command-exectype-element.md) element of the Task Scheduler schema.

The path is checked to make sure it is valid when the task is registered, not when this property is set.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExecAction**](execaction.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





