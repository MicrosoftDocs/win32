---
title: TaskFolder.CreateFolder method
description: For scripting, creates a folder for related tasks.
ms.assetid: '4fdc96bc-8c85-4b36-b3ea-bad7a46c3d35'
keywords:
- CreateFolder method Task Scheduler
- CreateFolder method Task Scheduler , TaskFolder object
- TaskFolder object Task Scheduler , CreateFolder method
topic_type:
- apiref
api_name:
- TaskFolder.CreateFolder
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskFolder.CreateFolder method

For scripting, creates a folder for related tasks.

## Syntax


```VB
ppFolder = .CreateFolder( _
  ByVal folderName, _
  ByVal sddl _
)
```



## Parameters

<dl> <dt>

*folderName* \[in\]
</dt> <dd>

The name that is used to identify the folder. If "FolderName\\SubFolder1\\SubFolder2" is specified, the entire folder tree will be created if the folders do not exist. This parameter can be a relative path to the current [**TaskFolder**](taskfolder.md) instance. The root task folder is specified with a backslash (\\). An example of a task folder path, under the root task folder, is \\MyTaskFolder. The '.' character cannot be used to specify the current task folder and the '..' characters cannot be used to specify the parent task folder in the path.

</dd> <dt>

*sddl* \[in\]
</dt> <dd>

The security descriptor that is associated with the folder.

</dd> </dl>

## Return value

A [**TaskFolder**](taskfolder.md) object that represents the new subfolder.

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

 

 





