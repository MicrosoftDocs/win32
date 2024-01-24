---
title: WakeToRun (settingsType) Element
description: Specifies that Task Scheduler will wake the computer when it is time to run the task.
ms.assetid: 5fb53016-5778-463d-bb32-3c1da2de6fc2
keywords:
- WakeToRun element Task Scheduler
topic_type:
- apiref
api_name:
- WakeToRun
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WakeToRun (settingsType) Element

Specifies that Task Scheduler will wake the computer when it is time to run the task.

``` syntax
<xs:element name="WakeToRun"
    type="boolean"
 />
```

The **WakeToRun** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

When the Task Scheduler service wakes the computer to run a task, the screen may remain off even though the computer is no longer in the sleep or hibernate mode. The screen will turn on when Windows Vista detects that a user has returned to use the computer.

For C++ development, see [**WakeToRun Property of ITaskSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_waketorun).

For script development, see [**TaskSettings.WakeToRun**](tasksettings-waketorun.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





