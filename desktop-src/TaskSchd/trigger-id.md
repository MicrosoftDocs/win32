---
title: Trigger.Id property
description: For scripting, gets or sets the identifier for the trigger.
ms.assetid: '15dd3aaa-f3ee-459d-a0bd-327c7a4beb03'
keywords:
- Id property Task Scheduler
- Id property Task Scheduler , Trigger object
- Trigger object Task Scheduler , Id property
topic_type:
- apiref
api_name:
- Trigger.Id
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Trigger.Id property

For scripting, gets or sets the identifier for the trigger.

## Syntax


```VB
Trigger.Id As String
```



## Property value

The identifier for the trigger. This identifier is used by the Task Scheduler for logging purposes.

## Remarks

When reading or writing XML for a task, the trigger identifier is specified in the Id attribute of the individual trigger elements (for example, the Id attribute of the [**BootTrigger**](taskschedulerschema-boottrigger-triggergroup-element.md) element) of the Task Scheduler schema.

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

 

 





