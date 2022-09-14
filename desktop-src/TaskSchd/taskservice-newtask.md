---
title: TaskService.NewTask method
description: For scripting, returns an empty task definition object to be filled in with settings and properties and then registered using the TaskFolder.RegisterTaskDefinition method.
ms.assetid: '696d57fc-100a-43e6-a8d9-9ec89be40367'
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
ms.topic: reference
ms.date: 05/31/2018
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



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





