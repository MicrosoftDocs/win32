---
title: TaskService.NewTask method
description: For scripting, returns an empty task definition object to be filled in with settings and properties and then registered using the TaskFolder.RegisterTaskDefinition method.
ms.assetid: 821fc610-cf94-4548-950d-b4fd7b2f90dc
keywords:
- NewTask method Task Scheduler
- NewTask method Task Scheduler , TaskService object
- TaskService object Task Scheduler , NewTask method
topic_type:
- apiref
api_name:
- TaskService.NewTask
api_location:
- taskschd.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TaskService.NewTask method

For scripting, returns an empty task definition object to be filled in with settings and properties and then registered using the [**TaskFolder.RegisterTaskDefinition**](taskfolder-registertaskdefinition.md) method.

## Syntax


```VB
TaskService.NewTask( _
  ByVal flags _
)
```



## Parameters

<dl> <dt>

*flags* \[in\]
</dt> <dd>

This parameter is reserved for future use and must be set to 0.

</dd> </dl>

## Return value

The task definition that specifies all the information required to create a new task.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





