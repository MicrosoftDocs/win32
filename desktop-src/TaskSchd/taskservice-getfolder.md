---
title: TaskService.GetFolder method
description: For scripting, gets a folder of registered tasks.
ms.assetid: '57e5b411-1fb6-4ee1-9802-ed2adbb4fdf8'
keywords:
- GetFolder method Task Scheduler
- GetFolder method Task Scheduler , TaskService object
- TaskService object Task Scheduler , GetFolder method
topic_type:
- apiref
api_name:
- TaskService.GetFolder
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskService.GetFolder method

For scripting, gets a folder of registered tasks.

## Syntax


```VB
TaskService.GetFolder( _
  ByVal path _
)
```



## Parameters

<dl> <dt>

*path* \[in\]
</dt> <dd>

The path to the folder to be retrieved. Do not use a backslash following the last folder name in the path. The root task folder is specified with a backslash (\\). An example of a task folder path, under the root task folder, is \\MyTaskFolder. The '.' character cannot be used to specify the current task folder and the '..' characters cannot be used to specify the parent task folder in the path.

</dd> </dl>

## Return value

A [**TaskFolder**](taskfolder.md) object for the requested folder.

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

 

 





