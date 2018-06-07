---
title: TaskNamedValueCollection.Item property
description: For scripting, gets the specified name-value pair from the collection.
ms.assetid: a243b814-7d83-466d-bd49-3414f3240780
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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





