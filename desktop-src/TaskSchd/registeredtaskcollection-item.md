---
title: RegisteredTaskCollection.Item property
description: For scripting, gets the specified registered task from the collection.
ms.assetid: '4cdb4dbe-e4b4-4520-a58f-7613a980af8f'
keywords: ["Item property Task Scheduler", "Item property Task Scheduler , RegisteredTaskCollection object", "RegisteredTaskCollection object Task Scheduler , Item property"]
topic_type:
- apiref
api_name:
- RegisteredTaskCollection.Item
api_location:
- taskschd.dll
api_type:
- COM
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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





