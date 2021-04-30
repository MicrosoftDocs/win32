---
title: TriggerCollection.Remove method
description: For scripting, removes the specified trigger from the collection of triggers used by the task.
ms.assetid: '30dccf16-2b4c-4776-9c19-f82ddd859d45'
keywords:
- triggers Task Scheduler , removing
- Remove method Task Scheduler
- Remove method Task Scheduler , TriggerCollection object
- TriggerCollection object Task Scheduler , Remove method
topic_type:
- apiref
api_name:
- TriggerCollection.Remove
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TriggerCollection.Remove method

For scripting, removes the specified trigger from the collection of triggers used by the task.

## Syntax


```VB
TriggerCollection.Remove( _
  ByVal index _
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The index of the trigger to be removed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

When removing items, note that the index for the first item in the collection is 1 and the index for the last item is the value of the [**TriggerCollection.Count**](triggercollection-count.md) property.

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

 

 





