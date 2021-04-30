---
title: TaskFolder.GetFolder property
description: For scripting, gets a folder that contains tasks at a specified location.
ms.assetid: '73e60b10-7a8c-4b07-9f8c-be7715f4e032'
keywords:
- GetFolder property Task Scheduler
- GetFolder property Task Scheduler , TaskFolder object
- TaskFolder object Task Scheduler , GetFolder property
topic_type:
- apiref
api_name:
- TaskFolder.GetFolder
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskFolder.GetFolder property

For scripting, gets a folder that contains tasks at a specified location.

## Syntax


```VB
TaskFolder.GetFolder( _
  ByVal path _
)
```



## Property value

The path (location) to the folder. Do not use a backslash following the last folder name in the path. The root task folder is specified with a backslash (\). An example of a task folder path, under the root task folder, is \\MyTaskFolder. The '.' character cannot be used to specify the current task folder and the '..' characters cannot be used to specify the parent task folder in the path.

## Error codes

The folder at the specified location. The folder is a [**TaskFolder**](taskfolder.md) object.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





