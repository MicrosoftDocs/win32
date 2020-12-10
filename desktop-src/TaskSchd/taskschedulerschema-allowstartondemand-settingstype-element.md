---
title: AllowStartOnDemand (settingsType) Element
description: Specifies that the task can be started using either the Run command or the Context menu.
ms.assetid: 5a0f0842-9f09-4d52-bed2-45740945d9a5
keywords:
- AllowStartOnDemand element Task Scheduler
topic_type:
- apiref
api_name:
- AllowStartOnDemand
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# AllowStartOnDemand (settingsType) Element

Specifies that the task can be started using either the Run command or the Context menu.

``` syntax
<xs:element name="AllowStartOnDemand"
    type="boolean"
    minOccurs="0"
    default="true"
 />
```

The **AllowStartOnDemand** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

When this element is set to True, the task can be started independently of when any triggers start the task.

For C++ development, see the [**AllowDemandStart property of ITaskSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_allowdemandstart).

For script development, see [**TaskSettings.AllowDemandStart**](tasksettings-allowdemandstart.md).

## Examples

For a complete example of the XML for a task that allows demand start, see [Time Trigger Example (XML)](time-trigger-example--xml-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





