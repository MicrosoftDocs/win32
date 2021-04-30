---
title: TaskFolder.GetTask property
description: For scripting, gets a task at a specified location in a folder.
ms.assetid: 'c0ad4402-dd63-499f-964c-0eada5665d1b'
keywords:
- GetTask property Task Scheduler
- GetTask property Task Scheduler , TaskFolder object
- TaskFolder object Task Scheduler , GetTask property
topic_type:
- apiref
api_name:
- TaskFolder.GetTask
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskFolder.GetTask property

For scripting, gets a task at a specified location in a folder.

## Syntax


```VB
TaskFolder.GetTask( _
  ByVal path _
)
```



## Property value

The path (location) to the task in a folder. The root task folder is specified with a backslash (\). An example of a task folder path, under the root task folder, is \\MyTaskFolder. The '.' character cannot be used to specify the current task folder and the '..' characters cannot be used to specify the parent task folder in the path.

## Error codes

The task at the specified location. The task is a [**RegisteredTask**](registeredtask.md) object.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





