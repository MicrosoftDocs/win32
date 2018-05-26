---
title: TriggerCollection.Item property
description: For scripting, gets the specified trigger from the collection.
ms.assetid: 007e5792-bb91-435f-abe9-27366e6ec58a
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





