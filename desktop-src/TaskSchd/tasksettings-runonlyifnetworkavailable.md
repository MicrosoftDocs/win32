---
title: TaskSettings.RunOnlyIfNetworkAvailable property
description: For scripting, gets or sets a Boolean value that indicates that the Task Scheduler will run the task only when a network is available.
ms.assetid: '1a2b085f-0572-47d3-ac1f-0032c8427af0'
keywords:
- RunOnlyIfNetworkAvailable property Task Scheduler
- RunOnlyIfNetworkAvailable property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , RunOnlyIfNetworkAvailable property
topic_type:
- apiref
api_name:
- TaskSettings.RunOnlyIfNetworkAvailable
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.RunOnlyIfNetworkAvailable property

For scripting, gets or sets a Boolean value that indicates that the Task Scheduler will run the task only when a network is available.

This property is read/write.

## Syntax


```VB
TaskSettings.RunOnlyIfNetworkAvailable As Boolean
```



## Property value

If True, the property indicates that the Task Scheduler will run the task only when a network is available. The default is False.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**RunOnlyIfNetworkAvailable**](taskschedulerschema-runonlyifnetworkavailable-settingstype-element.md) element of the Task Scheduler schema.

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

 

 





