---
title: TaskNamedValueCollection.Create method
description: For scripting, creates a name-value pair in the collection.
ms.assetid: 'f64e0548-fad3-4682-b50b-ff8ec685af36'
keywords:
- Create method Task Scheduler
- Create method Task Scheduler , TaskNamedValueCollection object
- TaskNamedValueCollection object Task Scheduler , Create method
topic_type:
- apiref
api_name:
- TaskNamedValueCollection.Create
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskNamedValueCollection.Create method

For scripting, creates a name-value pair in the collection.

## Syntax


```VB
TaskNamedValueCollection.Create( _
  ByVal name, _
  ByVal value, _
  ByRef pair _
)
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

The name that is associated with a value in a name-value pair.

</dd> <dt>

*value* \[in\]
</dt> <dd>

The value that is associated with a name in a name-value pair.

</dd> <dt>

*pair* \[out\]
</dt> <dd>

The name-value pair that is created in the collection.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





