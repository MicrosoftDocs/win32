---
title: StopOnIdleEnd (idleSettingsType) Element
description: Specifies that the Task Scheduler will stop the task if the idle condition ends before the task is completed.
ms.assetid: 5e8e4fd9-bba1-4ede-a0b3-9f50feb1b6f3
keywords:
- StopOnIdleEnd element Task Scheduler
topic_type:
- apiref
api_name:
- TerminateOnIdleEnd
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StopOnIdleEnd (idleSettingsType) Element

Specifies that the Task Scheduler will stop the task if the idle condition ends before the task is completed.

``` syntax
<xs:element name="StopOnIdleEnd"
    type="boolean"
    minOccurs="0"
    default="true"
 />
```

The **StopOnIdleEnd** element is defined by the [**idleSettingsType**](taskschedulerschema-idlesettingstype-complextype.md) complex type.

## Parent element



| Element                                                                       | Derived from                                                                 | Description                                                                                       |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**IdleSettings**](taskschedulerschema-idlesettings-settingstype-element.md) | [**idleSettingsType**](taskschedulerschema-idlesettingstype-complextype.md) | Specifies how the Task Scheduler performs tasks when the computer is in an idle state.<br/> |



## Remarks

For C++ development, see [**StopOnIdleEnd Property of IIdleSettings**](/windows/desktop/api/taskschd/nf-taskschd-iidlesettings-get_stoponidleend).

For script development, see [**IdleSettings.StopOnIdleEnd**](idlesettings-stoponidleend.md).

## Examples

The following XML defines an idle setting that indicates the task should not be performed when the idle condition ends.


```XML
<IdleSettings>
    <StopOnIdleEnd>false</StopOnIdleEnd>
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
</dt> </dl>

 

 





