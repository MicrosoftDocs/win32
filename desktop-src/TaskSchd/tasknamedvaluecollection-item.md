---
title: TaskNamedValueCollection.Item property
description: For scripting, gets the specified name-value pair from the collection.
ms.assetid: '89c87b22-e459-435d-8c15-69907e9b1329'
keywords:
- Item property Task Scheduler
- Item property Task Scheduler , TaskNamedValueCollection object
- TaskNamedValueCollection object Task Scheduler , Item property
topic_type:
- apiref
api_name:
- TaskNamedValueCollection.Item
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskNamedValueCollection.Item property

For scripting, gets the specified name-value pair from the collection.

## Syntax


```VB
TaskNamedValueCollection.Item( _
  ByVal index, _
  ByRef pair _
) As long
```



## Property value

A [**TaskNamedValuePair**](tasknamedvaluepair.md) object that represents the requested pair.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





