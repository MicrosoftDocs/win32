---
title: Principal.Id property
description: For scripting, gets or sets the identifier of the principal.
ms.assetid: '54112977-9c30-4c52-bffd-7625eeb79f82'
keywords:
- Id property Task Scheduler
- Id property Task Scheduler , Principal object
- Principal object Task Scheduler , Id property
topic_type:
- apiref
api_name:
- Principal.Id
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Principal.Id property

For scripting, gets or sets the identifier of the principal.

## Syntax


```VB
Principal.Id As String
```



## Property value

The identifier of the principal.

## Remarks

This identifier is also used when specifying the [**ActionCollection.Context**](actioncollection-context.md) property.

When reading or writing XML for a task, the identifier of the principal is specified in the Id attribute of the [**Principal**](taskschedulerschema-principal-principaltype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ActionCollection.Context**](actioncollection-context.md)
</dt> <dt>

[**Principal**](principal.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





