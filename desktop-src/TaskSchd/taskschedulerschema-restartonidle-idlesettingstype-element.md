---
title: RestartOnIdle (idleSettingsType) Element
description: Specifies whether the task is restarted when the computer cycles into an idle condition more than once.
ms.assetid: 7a7a388c-8dc9-4106-82c1-3435d9f89866
keywords:
- RestartOnIdle element Task Scheduler
topic_type:
- apiref
api_name:
- RestartOnIdle
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RestartOnIdle (idleSettingsType) Element

Specifies whether the task is restarted when the computer cycles into an idle condition more than once.

``` syntax
<xs:element name="RestartOnIdle"
    type="boolean"
    default="false"
    minOccurs="0"
 />
```

The **RestartOnIdle** element is defined by the [**idleSettingsType**](taskschedulerschema-idlesettingstype-complextype.md) complex type.

## Parent element



| Element                                                                       | Derived from                                                                 | Description                                                                                       |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**IdleSettings**](taskschedulerschema-idlesettings-settingstype-element.md) | [**idleSettingsType**](taskschedulerschema-idlesettingstype-complextype.md) | Specifies how the Task Scheduler performs tasks when the computer is in an idle state.<br/> |



## Remarks

This element is used only if the [**TerminateOnIdleEnd**](taskschedulerschema-terminateonidleend-idlesettingstype-element.md) element is set to True.

For script development, this task settings is specified using the [**IdleSettings.RestartOnIdle**](idlesettings-restartonidle.md) property.

For C++ development, this task settings is specified using the [**IIdleSettings::RestartOnIdle**](/windows/desktop/api/taskschd/nf-taskschd-iidlesettings-get_restartonidle) property.

## Examples

The following XML defines an idle setting that indicates that the task should not be restarted when the idle condition cycles.


```XML
<IdleSettings>
     <TerminateOnIdleEnd>true</TerminateOnIdleEnd>
     <RestartOnIdle>true</RestartOnIdle>
</IdleSettings>
```



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

 

 





