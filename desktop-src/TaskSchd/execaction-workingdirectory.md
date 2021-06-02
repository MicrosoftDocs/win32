---
title: ExecAction.WorkingDirectory property
description: For scripting, gets or sets the directory that contains either the executable file or the files that are used by the executable file.
ms.assetid: 7b1e3c9d-ba08-4812-b50e-f97b6c12f8bd
keywords:
- WorkingDirectory property Task Scheduler
- WorkingDirectory property Task Scheduler , ExecAction object
- ExecAction object Task Scheduler , WorkingDirectory property
topic_type:
- apiref
api_name:
- ExecAction.WorkingDirectory
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ExecAction.WorkingDirectory property

For scripting, gets or sets the directory that contains either the executable file or the files that are used by the executable file.

## Syntax


```VB
ExecAction.WorkingDirectory As String
```



## Property value

The directory that contains either the executable file or the files that are used by the executable file.

## Remarks

When reading or writing XML, the working directory of the application is specified in the [**WorkingDirectory**](taskschedulerschema-workingdirectory-exectype-element.md) element of the Task Scheduler schema.

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

 

 





