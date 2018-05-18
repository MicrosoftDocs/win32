---
title: Trigger.Enabled property
description: For scripting, gets or sets a Boolean value that indicates whether the trigger is enabled.
ms.assetid: '20300470-e434-4296-b3e2-98c65b16e9f2'
keywords: ["Enabled property Task Scheduler", "Enabled property Task Scheduler , Trigger object", "Trigger object Task Scheduler , Enabled property"]
topic_type:
- apiref
api_name:
- Trigger.Enabled
api_location:
- taskschd.dll
api_type:
- COM
---

# Trigger.Enabled property

For scripting, gets or sets a Boolean value that indicates whether the trigger is enabled.

## Syntax


```VB
Trigger.Enabled As Boolean
```



## Property value

True if the trigger is enabled; otherwise, false. The default is true.

## Remarks

When reading or writing XML for a task, the enabled property is specified using the [**Enabled**](taskschedulerschema-enabled-triggerbasetype-element.md) element of the Task Scheduler schema.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





