---
title: TaskFolder.DeleteTask method
description: For scripting, deletes a task from the folder.
ms.assetid: 'c030b2bf-fbde-4b8b-b38b-763938855d12'
keywords:
- DeleteTask method Task Scheduler
- DeleteTask method Task Scheduler , TaskFolder object
- TaskFolder object Task Scheduler , DeleteTask method
topic_type:
- apiref
api_name:
- TaskFolder.DeleteTask
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskFolder.DeleteTask method

For scripting, deletes a task from the folder.

## Syntax


```VB
TaskFolder.DeleteTask( _
  ByVal Name, _
  ByVal flags _
)
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the task that is specified when the task was registered. The '.' character cannot be used to specify the current task folder and the '..' characters cannot be used to specify the parent task folder in the path.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Not supported. Value is 0

</dd> </dl>

## Return value

This method does not return a value.

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

 

 





