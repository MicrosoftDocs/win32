---
title: Settings (taskType) Element
description: Specifies the settings that the Task Scheduler uses to perform the task.
ms.assetid: 72d2929a-0dd2-44cd-be7b-72eca23a5e14
keywords:
- Settings element Task Scheduler
topic_type:
- apiref
api_name:
- Settings
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Settings (taskType) Element

Specifies the settings that the Task Scheduler uses to perform the task.

``` syntax
<xs:element name="Settings"
    type="settingsType"
    minOccurs="0"
 />
```

The **Settings** element is defined by the [**taskType**](taskschedulerschema-tasktype-complextype.md) complex type.

## Parent element



| Element                                          | Derived from                                                 | Description                                                                    |
|--------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**Task**](taskschedulerschema-task-element.md) | [**taskType**](taskschedulerschema-tasktype-complextype.md) | Specifies the task that is performed by the Task Scheduler service.<br/> |



## Child elements



| Element                                                                                                          | Type                                                                                              | Description                                                                                                          |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**AllowHardTerminate**](taskschedulerschema-allowhardterminate-settingstype-element.md)                        | boolean                                                                                           | Specifies that the task may be terminated using TerminateProcess.<br/>                                         |
| [**AllowStartOnDemand**](taskschedulerschema-allowstartondemand-settingstype-element.md)                        | boolean                                                                                           | Specifies that the task can be started using either the Run command or the Context menu.<br/>                  |
| [**DeleteExpiredTaskAfter**](taskschedulerschema-deleteexpiredtaskafter-settingstype-element.md)                | duration                                                                                          | Specifies the amount of time that the Task Scheduler will wait before deleting the task after it expires.<br/> |
| [**DisallowStartIfOnBatteries**](taskschedulerschema-disallowstartifonbatteries-settingstype-element.md)        | boolean                                                                                           | Specifies that the task will not be started if the computer is running on batteries.<br/>                      |
| [**Enabled**](taskschedulerschema-enabled-settingstype-element.md)                                              | boolean                                                                                           | Specifies that the task is enabled. The task can be performed only when this setting is True.<br/>             |
| [**ExecutionTimeLimit**](taskschedulerschema-executiontimelimit-settingstype-element.md)                        | duration                                                                                          | Amount of time allowed to complete the task.<br/>                                                              |
| [**Hidden**](taskschedulerschema-hidden-settingstype-element.md)                                                | boolean                                                                                           | Specifies that the task will not be visible in the UI by default.<br/>                                         |
| [**IdleSettings**](taskschedulerschema-idlesettings-settingstype-element.md)                                    | [**idleSettingsType**](taskschedulerschema-idlesettingstype-complextype.md)                      | Specifies how the Task Scheduler performs tasks when the computer is in an idle state.<br/>                    |
| [**MaintenanceSettings**](taskschedulerschema-maintenancesettings-maintenancesettingstype-element.md)           | [**maintenanceSettingsType**](taskschedulerschema-maintenancesettingstype-complextype.md)        | Specifies how the Task Scheduler performs tasks during Automatic maintenance.<br/>                             |
| [**MultipleInstancesPolicy**](taskschedulerschema-multipleinstancespolicy-settingstype-element.md)              | [**multipleInstancesPolicyType**](taskschedulerschema-multipleinstancespolicytype-simpletype.md) | Specifies the policy that defines how the Task Scheduler deals with multiple instances of the task.<br/>       |
| [**Priority**](taskschedulerschema-priority-settingstype-element.md)                                            | [**priorityType**](taskschedulerschema-prioritytype-simpletype.md)                               | Specifies the priority level for the task.<br/>                                                                |
| [**RestartOnFailure**](taskschedulerschema-restartonfailure-settingstype-element.md)                            | [**restartType**](taskschedulerschema-restarttype-complextype.md)                                | Specifies that the Task Scheduler will attempt to restart the task if the task fails for any reason.<br/>      |
| [**RunOnlyIfIdle**](taskschedulerschema-runonlyifidle-settingstype-element.md)                                  | boolean                                                                                           | Specifies that the task is run only when the computer is in an idle state.<br/>                                |
| [**RunOnlyIfNetworkAvailable**](taskschedulerschema-runonlyifnetworkavailable-settingstype-element.md)          | boolean                                                                                           | Specifies that the Task Scheduler will run the task only when a network is available.<br/>                     |
| [**StartWhenAvailable**](taskschedulerschema-startwhenavailable-settingstype-element.md)                        | boolean                                                                                           | Specifies that the Task Scheduler can start the task at any time after its scheduled time has passed.<br/>     |
| [**StopIfGoingOnBatteries (settingsType)**](taskschedulerschema-stopifgoingonbatteries-settingstype-element.md) | boolean                                                                                           | Specifies that the task will be stopped if the computer is going onto batteries.<br/>                          |
| [**Volatile**](taskschedulerschema-volatile-element.md)                                                         | boolean                                                                                           | Specifies if the task is automatically disabled by Task Scheduler at Windows startup.<br/>                     |
| [**WakeToRun (settingsType)**](taskschedulerschema-waketorun-settingstype-element.md)                           | boolean                                                                                           | Specifies that Task Scheduler will wake the computer when it is time to run the task.<br/>                     |



## Remarks

You can select one or more of the child elements referenced above.

For C++ development, the registration information of a task is specified using the [**Settings property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_settings).

For scripting development, the registration information of a task is specified using the [**TaskDefinition.Settings**](taskdefinition-settings.md) property.

## Examples

The following XML code example defines a settings element that allows a hard termination of the task.


```XML
<task>
    <Settings>
        <AllowHardTerminate>true</AllowHardTerminate>
        <AllowStartOnDemand>true</AllowStartOnDemand>
    </Settings>
</task>
```



For more information and a complete example of the XML for setting task settings, see [Time Trigger Example (XML)](time-trigger-example--xml-.md).

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

 

 





