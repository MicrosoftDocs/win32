---
title: TriggerCollection.Item property
description: For scripting, gets the specified trigger from the collection.
ms.assetid: '517976df-b3fc-4f2e-8d37-262195c65182'
keywords:
- Item property Task Scheduler
- Item property Task Scheduler , TriggerCollection object
- TriggerCollection object Task Scheduler , Item property
topic_type:
- apiref
api_name:
- TriggerCollection.Item
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TriggerCollection.Item property

For scripting, gets the specified trigger from the collection.

## Syntax


```VB
TriggerCollection.Item( _
  ByVal index _
) As Trigger
```



## Property value

A [**Trigger**](trigger.md) object that represents the requested trigger.

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

 

 





