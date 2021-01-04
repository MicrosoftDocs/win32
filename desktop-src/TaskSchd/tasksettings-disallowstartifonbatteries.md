---
title: TaskSettings.DisallowStartIfOnBatteries property
description: For scripting, gets or sets a Boolean value that indicates that the task will not be started if the computer is running on batteries.
ms.assetid: '5e13f168-a396-495f-a486-e64e8524c8cd'
keywords:
- DisallowStartIfOnBatteries property Task Scheduler
- DisallowStartIfOnBatteries property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , DisallowStartIfOnBatteries property
topic_type:
- apiref
api_name:
- TaskSettings.DisallowStartIfOnBatteries
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.DisallowStartIfOnBatteries property

For scripting, gets or sets a Boolean value that indicates that the task will not be started if the computer is running on batteries.

This property is read/write.

## Syntax


```VB
TaskSettings.DisallowStartIfOnBatteries As Boolean
```



## Property value

A Boolean value that indicates that the task will not be started if the computer is running on batteries. If True, the task will not be started if the computer is running on batteries. If False, the task will be started if the computer is running on batteries. The default is True.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**DisallowStartIfOnBatteries**](taskschedulerschema-disallowstartifonbatteries-settingstype-element.md) element of the Task Scheduler schema.

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

 

 





