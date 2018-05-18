---
title: TaskFolder.DeleteFolder method
description: For scripting, deletes a subfolder from the parent folder.
ms.assetid: '7758afc5-73d8-456c-98a9-89e4b7ad42b9'
keywords: ["DeleteFolder method Task Scheduler", "DeleteFolder method Task Scheduler , TaskFolder object", "TaskFolder object Task Scheduler , DeleteFolder method"]
topic_type:
- apiref
api_name:
- TaskFolder.DeleteFolder
api_location:
- taskschd.dll
api_type:
- COM
---

# TaskFolder.DeleteFolder method

For scripting, deletes a subfolder from the parent folder.

## Syntax


```VB
TaskFolder.DeleteFolder( _
  ByVal folderName, _
  ByVal flags _
)
```



## Parameters

<dl> <dt>

*folderName* \[in\]
</dt> <dd>

The name of the subfolder to be removed. The root task folder is specified with a backslash (\). This parameter can be a relative path to the folder you want to delete. An example of a task folder path, under the root task folder, is \\MyTaskFolder. The '.' character cannot be used to specify the current task folder and the '..' characters cannot be used to specify the parent task folder in the path.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Not supported.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TaskFolder**](taskfolder.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





