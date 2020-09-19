---
title: IdleSettings (settingsType) Element
description: Specifies how the Task Scheduler performs tasks when the computer is in an idle state.
ms.assetid: 23d57417-95a9-42e3-904c-7f0859fcda7c
keywords:
- IdleSettings element Task Scheduler
topic_type:
- apiref
api_name:
- IdleSettings
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IdleSettings (settingsType) Element

Specifies how the Task Scheduler performs tasks when the computer is in an idle state. For information about idle conditions, see [Task Idle Conditions](task-idle-conditions.md).

``` syntax
<xs:element name="IdleSettings"
    type="idleSettingsType"
    minOccurs="0"
 />
```

The **IdleSettings** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |

Please note that WaitTimeout and Duration settings have been deprecated. While they are still present in Task Scheduler UI and their interface methods may still return valid values, they are no longer used.


## Child elements



| Element                                                                                  | Type     | Description                                                                                                              |
|------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------|
| [**RestartOnIdle**](taskschedulerschema-restartonidle-idlesettingstype-element.md)      | boolean  | Specifies whether the task is restarted when the computer cycles into an idle condition more than once.<br/>       |
| [**StopOnIdleEnd**](taskschedulerschema-terminateonidleend-idlesettingstype-element.md) | boolean  | Specifies that the Task Scheduler will stop the task if the idle condition ends before the task is completed.<br/> |
Deprecated:
| [**Duration**](taskschedulerschema-duration-idlesettingstype-element.md)                | duration | Specifies how long the computer must be in an idle state before the task is run.<br/>                              |
| [**WaitTimeout**](taskschedulerschema-waittimeout-idlesettingstype-element.md)          | duration | Specifies the amount of time that the Task Scheduler will wait for an idle condition to occur.<br/>                |



## Remarks

For script development, idle settings are specified using the [**TaskSettings.IdleSettings**](tasksettings-idlesettings.md) property.

For C++ development, idle settings are specified using the [**ITaskSettings::IdleSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_idlesettings) property.

## Examples

The following XML defines a settings element that allows Task Scheduler to wait 24 hours for an idle condition and then allows only 10 minutes {IdleDuration) to initiate the task.


```XML
<Settings>
    <IdleSettings>
        <StopOnIdleEnd>false</StopOnIdleEnd>
        <RestartOnIdle>false</RestartOnIdle> 
        <!-- WaitTimeout and Duration have been deprecated -->
        <Duration>PT5M</Duration>
        <WaitTimeout>PT24H</WaitTimeout>
    </IdleSettings>       
</Settings>
```



## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





