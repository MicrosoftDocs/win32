---
title: RunningTaskCollection.Item property
description: For scripting, gets the specified task from the collection.
ms.assetid: '8b0745da-a11f-426c-9d52-f59d188e0e86'
keywords:
- Item property Task Scheduler
- Item property Task Scheduler , RunningTaskCollection object
- RunningTaskCollection object Task Scheduler , Item property
topic_type:
- apiref
api_name:
- RunningTaskCollection.Item
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RunningTaskCollection.Item property

For scripting, gets the specified task from the collection.

## Syntax


```VB
RunningTaskCollection.Item( _
  ByVal Index _
) As RunningTask
```



## Property value

A [**RunningTask**](runningtask.md) object that contains the requested context.

## Remarks

Collections are 1-based. In other words, the index for the first item in the collection is 1.

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

 

 





