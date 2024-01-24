---
title: ActionCollection.Remove method
description: For scripting, removes the specified action from the collection.
ms.assetid: ae1da6a9-5851-4ccb-80dc-75d7a99e7c6a
keywords:
- Remove method Task Scheduler
- Remove method Task Scheduler , ActionCollection object
- ActionCollection object Task Scheduler , Remove method
topic_type:
- apiref
api_name:
- ActionCollection.Remove
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActionCollection.Remove method

For scripting, removes the specified action from the collection.

## Syntax


```VB
ActionCollection.Remove( _
  ByVal index _
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The index of the action to be removed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

When removing items, note that the index for the first item in the collection is 1 and the index for the last item is the value of the [**ActionCollection.Count**](actioncollection-count.md) property.

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

 

 





