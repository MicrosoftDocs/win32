---
title: ActionCollection.Item property
description: For scripting, gets a specified action from the collection.
ms.assetid: a5567c82-2d56-4c3e-894c-ca6d432a3358
keywords:
- Item property Task Scheduler
- Item property Task Scheduler , ActionCollection object
- ActionCollection object Task Scheduler , Item property
topic_type:
- apiref
api_name:
- ActionCollection.Item
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActionCollection.Item property

For scripting, gets a specified action from the collection.

## Syntax


```VB
ActionCollection.Item( _
  ByVal Index _
) As Action
```



## Property value

An [**Action**](action.md) object that represents the requested action.

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
</dt> <dt>

[**ActionCollection**](actioncollection.md)
</dt> </dl>

 

 





