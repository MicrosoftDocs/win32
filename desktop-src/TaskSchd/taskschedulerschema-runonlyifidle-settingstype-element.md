---
title: RunOnlyIfIdle (settingsType) Element
description: Specifies that the task is run only when the computer is in an idle state.
ms.assetid: 2ef3dd19-4d5c-4399-89b8-d737be4ef85e
keywords:
- RunOnlyIfIdle element Task Scheduler
topic_type:
- apiref
api_name:
- RunOnlyIfIdle
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RunOnlyIfIdle (settingsType) Element

Specifies that the task is run only when the computer is in an idle state.

``` syntax
<xs:element name="RunOnlyIfIdle"
    type="boolean"
 />
```

The **RunOnlyIfIdle** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

For C++ development, see [**RunOnlyIfIdle Property of ITaskSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_runonlyifidle).

For script development, see [**TaskSettings.RunOnlyIfIdle**](tasksettings-runonlyifidle.md).

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

 

 





