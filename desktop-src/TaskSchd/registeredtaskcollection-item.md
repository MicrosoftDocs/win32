---
title: RegisteredTaskCollection.Item property
description: For scripting, gets the specified registered task from the collection.
ms.assetid: '8b396478-4cd9-426c-afe8-29539ff0b859'
keywords:
- Item property Task Scheduler
- Item property Task Scheduler , RegisteredTaskCollection object
- RegisteredTaskCollection object Task Scheduler , Item property
topic_type:
- apiref
api_name:
- RegisteredTaskCollection.Item
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegisteredTaskCollection.Item property

For scripting, gets the specified registered task from the collection.

This property is read-only.

## Syntax


```VB
RegisteredTaskCollection.Item( _
  ByVal Index _
) As RegisteredTask
```



## Property value

A [**RegisteredTask**](registeredtask.md) object that contains the registered task.

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

 

 





