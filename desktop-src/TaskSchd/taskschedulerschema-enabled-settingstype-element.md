---
title: Enabled (settingsType) Element
description: Specifies that the task is enabled. The task can be performed only when this setting is True.
ms.assetid: d28f0d54-1205-4b70-a178-72d809da9ce1
keywords:
- Enabled element Task Scheduler
topic_type:
- apiref
api_name:
- Enabled
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Enabled (settingsType) Element

Specifies that the task is enabled. The task can be performed only when this setting is True.

``` syntax
<xs:element name="Enabled"
    type="boolean"
    default="true"
    minOccurs="1"
 />
```

The **Enabled** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

For C++ development, see [**Enabled Property of ITaskSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_enabled).

For script development, see [**TaskSettings.Enabled**](tasksettings-enabled.md).

## Examples

For a complete example of the XML for a task that is enabled, see [Time Trigger Example (XML)](time-trigger-example--xml-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





