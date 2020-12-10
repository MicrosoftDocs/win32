---
title: StopIfGoingOnBatteries (settingsType) Element
description: Specifies that the task will be stopped if the computer is going onto batteries.
ms.assetid: 0d772dbb-a552-45ed-9dc0-7159f6ef12ed
keywords:
- StopIfGoingOnBatteries element Task Scheduler
topic_type:
- apiref
api_name:
- StopIfGoingOnBatteries
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StopIfGoingOnBatteries (settingsType) Element

Specifies that the task will be stopped if the computer is going onto batteries.

``` syntax
<xs:element name="StopIfGoingOnBatteries"
    type="boolean"
    default="true"
    minOccurs="0"
 />
```

The **StopIfGoingOnBatteries** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

The default setting for this element is False. Note that the default value has changed from previous versions of Task Scheduler.

For scripting development, this setting is specified using the [**TaskSettings.StopIfGoingOnBatteries**](tasksettings-stopifgoingonbatteries.md) property.

For C++ development, this setting is specified using the [**ITaskSettings::StopIfGoingOnBatteries**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_stopifgoingonbatteries) property.

## Examples

The following XML defines a settings element that allows a hard termination of the task.


```XML
<Settings>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
</Settings>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





