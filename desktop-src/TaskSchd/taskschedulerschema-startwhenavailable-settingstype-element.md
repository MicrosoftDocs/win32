---
title: StartWhenAvailable (settingsType) Element
description: Specifies that the Task Scheduler can start the task at any time after its scheduled time has passed.
ms.assetid: 1d65fd51-3a94-4083-8e38-2a652383656a
keywords:
- StartWhenAvailable element Task Scheduler
topic_type:
- apiref
api_name:
- StartWhenAvailable
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StartWhenAvailable (settingsType) Element

Specifies that the Task Scheduler can start the task at any time after its scheduled time has passed.

``` syntax
<xs:element name="StartWhenAvailable"
    type="boolean"
    default="false"
    minOccurs="0"
 />
```

The **StartWhenAvailable** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

This property applies only to timed tasks.

For C++ development, see [**StartWhenAvailable Property of ITaskSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_startwhenavailable).

For script development, see [**TaskSettings.StartWhenAvailable**](tasksettings-startwhenavailable.md).

## Examples

The following XML defines a settings element that allows the Task Scheduler to start the task when it is available.


```XML
<Settings>
    <StartWhenAvailable>true</StartWhenAvailable>
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

 

 





