---
title: ActionCollection.Context property
description: For scripting, gets or sets the identifier of the principal for the task.
ms.assetid: 5d8ac31c-ce07-4801-a04e-e12e996b88c6
keywords:
- Context property Task Scheduler
- Context property Task Scheduler , ActionCollection object
- ActionCollection object Task Scheduler , Context property
topic_type:
- apiref
api_name:
- ActionCollection.Context
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActionCollection.Context property

For scripting, gets or sets the identifier of the principal for the task.

## Syntax


```VB
ActionCollection.Context As String
```



## Property value

The identifier of the principal for the task. The identifier that is specified here must match the identifier that is specified in the Id property of the IPrincipal interface that defines the principal.

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
</dt> <dt>

[**ActionCollection**](actioncollection.md)
</dt> </dl>

 

 





