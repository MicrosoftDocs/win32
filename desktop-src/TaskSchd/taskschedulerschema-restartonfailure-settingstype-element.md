---
title: RestartOnFailure (settingsType) Element
description: Specifies that the Task Scheduler will attempt to restart the task if the task fails for any reason.
ms.assetid: c90d8c62-dd97-4ea6-bd87-37b0915e0b38
keywords:
- RestartOnFailure element Task Scheduler
topic_type:
- apiref
api_name:
- RestartOnFailure
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RestartOnFailure (settingsType) Element

Specifies that the Task Scheduler will attempt to restart the task if the task fails for any reason.

``` syntax
<xs:element name="RestartOnFailure"
    type="restartType"
    minOccurs="0"
 />
```

The **RestartOnFailure** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Child elements



| Element                                                              | Type         | Description                                                                                        |
|----------------------------------------------------------------------|--------------|----------------------------------------------------------------------------------------------------|
| [**Count**](taskschedulerschema-count-restarttype-element.md)       | unsignedByte | Specifies the number of times that the Task Scheduler will attempt to restart the task.<br/> |
| [**Interval**](taskschedulerschema-interval-restarttype-element.md) | duration     | Specifies how long the Task Scheduler will attempt to restart the task.<br/>                 |



## Remarks

When an application specifies task settings, this information is accessed through the [**RestartCount**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_restartcount) and [**RestartInterval**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_restartinterval) properties of the [**ITaskSettings**](/windows/desktop/api/taskschd/nn-taskschd-itasksettings) interface. For scripting, this information is accessed through the [**TaskSettings.RestartCount**](tasksettings-restartcount.md) and [**TaskSettings.RestartInterval**](tasksettings-restartinterval.md) properties.

Both child elements must be set to specify how the Task Scheduler restarts the task.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





