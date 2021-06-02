---
title: MultipleInstancesPolicy (settingsType) Element
description: Specifies the policy that defines how the Task Scheduler deals with multiple instances of the task.
ms.assetid: ec82d396-f83c-4684-98ab-f70e15ada075
keywords:
- MultipleInstancesPolicy element Task Scheduler
topic_type:
- apiref
api_name:
- MultipleInstancesPolicy
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MultipleInstancesPolicy (settingsType) Element

Specifies the policy that defines how the Task Scheduler deals with multiple instances of the task.

``` syntax
<xs:element name="MultipleInstancesPolicy"
    type="multipleInstancesPolicyType"
 />
```

The **MultipleInstancesPolicy** element is defined by the [**multipleInstancesPolicyType**](taskschedulerschema-multipleinstancespolicytype-simpletype.md) simple type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

For C++ development, see [**MultipleInstances Property of ITaskSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_multipleinstances).

For script development, see [**TaskSettings.MultipleInstances**](tasksettings-multipleinstances.md).

### Restricted Values

This element is restricted to the following values.

-   Parallel: Starts a new instance while an existing instance is running.
-   Queue: Starts a new instance of task after all other instances of the task are complete.
-   IgnoreNew: Default. Does not start a new instance if an existing instance of the task is running.
-   StopExisting: Stops an existing instance of the task before it starts a new instance.

## Examples

The following XML defines a settings element that allows multiple instances of the task to run in parallel.


```XML
<Settings>
    <MultipleInstancesPolicy>Parallel</MultipleInstancesPolicy>
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

 

 





