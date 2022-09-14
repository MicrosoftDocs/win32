---
title: settingsType Complex Type
description: Defines the child elements and sequencing information for the Settings (taskType) element.
ms.assetid: dba6b82d-aaa4-4f77-aeb1-c5a8f81aec25
keywords:
- settingsType complex type Task Scheduler
topic_type:
- apiref
api_name:
- settingsType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# settingsType Complex Type

Defines the child elements and sequencing information for the [**Settings (taskType)**](taskschedulerschema-settings-tasktype-element.md) element.

``` syntax
<xs:complexType name="settingsType">
    <xs:all>
        <xs:element name="AllowStartOnDemand"
            type="boolean"
            default="true"
            minOccurs="0"
         />
        <xs:element name="RestartOnFailure"
            type="restartType"
            minOccurs="0"
         />
        <xs:element name="MultipleInstancesPolicy"
            type="multipleInstancesPolicyType"
            default="IgnoreNew"
            minOccurs="0"
         />
        <xs:element name="DisallowStartIfOnBatteries"
            type="boolean"
            default="true"
            minOccurs="0"
         />
        <xs:element name="StopIfGoingOnBatteries"
            type="boolean"
            default="true"
            minOccurs="0"
         />
        <xs:element name="AllowHardTerminate"
            type="boolean"
            default="true"
            minOccurs="0"
         />
        <xs:element name="StartWhenAvailable"
            type="boolean"
            default="false"
            minOccurs="0"
         />
        <xs:element name="NetworkProfileName"
            type="string"
            minOccurs="0"
         />
        <xs:element name="RunOnlyIfNetworkAvailable"
            type="boolean"
            default="false"
            minOccurs="0"
         />
        <xs:element name="WakeToRun"
            type="boolean"
            default="false"
            minOccurs="0"
         />
        <xs:element name="Enabled"
            type="boolean"
            default="true"
            minOccurs="0"
         />
        <xs:element name="Hidden"
            type="boolean"
            default="false"
            minOccurs="0"
         />
        <xs:element name="DeleteExpiredTaskAfter"
            type="duration"
            default="PT0S"
            minOccurs="0"
         />
        <xs:element name="IdleSettings"
            type="idleSettingsType"
            minOccurs="0"
         />
        <xs:element name="NetworkSettings"
            type="networkSettingsType"
            minOccurs="0"
         />
        <xs:element name="ExecutionTimeLimit"
            type="duration"
            minOccurs="0"
         />
        <xs:element name="Priority"
            type="priorityType"
            default="7"
            minOccurs="0"
         />
        <xs:element name="RunOnlyIfIdle"
            type="boolean"
            default="false"
            minOccurs="0"
         />
        <xs:element name="UseUnifiedSchedulingEngine"
            type="boolean"
            default="false"
            minOccurs="0"
         />
        <xs:element name="DisallowStartOnRemoteAppSession"
            type="boolean"
            default="false"
            minOccurs="0"
         />
    </xs:all>
</xs:complexType>
```

## Child elements



| Element                                                                                                             | Type                                                                                              | Description                                                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllowHardTerminate**](taskschedulerschema-allowhardterminate-settingstype-element.md)                           | boolean                                                                                           | Specifies if the Task Scheduler service allows hard termination of the task.<br/>                                                                                                                                                                                                                             |
| [**AllowStartOnDemand**](taskschedulerschema-allowstartondemand-settingstype-element.md)                           | boolean                                                                                           | Specifies that the task can be started by using either the Run command or the Context menu. <br/>                                                                                                                                                                                                             |
| [**DeleteExpiredTaskAfter**](taskschedulerschema-deleteexpiredtaskafter-settingstype-element.md)                   | duration                                                                                          | Specifies the amount of time that the Task Scheduler will wait before deleting the task after it expires. If no value is specified for this element, then the Task Scheduler service will not delete the task.<br/>                                                                                           |
| [**DisallowStartIfOnBatteries**](taskschedulerschema-disallowstartifonbatteries-settingstype-element.md)           | boolean                                                                                           | Specifies that the task will not be started if the computer is running on battery power.<br/>                                                                                                                                                                                                                 |
| [**DisallowStartOnRemoteAppSession**](taskschedulerschema-disallowstartonremoteappsession-settingstype-element.md) | boolean                                                                                           | Specifies that the task should not start if the task is triggered to run in a Remote Applications Integrated Locally (RAIL) session.<br/>                                                                                                                                                                     |
| [**Enabled**](taskschedulerschema-enabled-settingstype-element.md)                                                 | boolean                                                                                           | Specifies that the task is enabled. The task can be performed only when this setting is **True**.<br/>                                                                                                                                                                                                        |
| [**ExecutionTimeLimit**](taskschedulerschema-executiontimelimit-settingstype-element.md)                           | duration                                                                                          | Specifies the amount of time allowed to complete the task.<br/>                                                                                                                                                                                                                                               |
| [**Hidden**](taskschedulerschema-hidden-settingstype-element.md)                                                   | boolean                                                                                           | Specifies, by default, that the task will not be visible in the user interface (UI).<br/>                                                                                                                                                                                                                     |
| [**IdleSettings**](taskschedulerschema-idlesettings-settingstype-element.md)                                       | [**idleSettingsType**](taskschedulerschema-idlesettingstype-complextype.md)                      | Specifies how the Task Scheduler performs tasks when the computer is in an idle state.<br/>                                                                                                                                                                                                                   |
| [**MultipleInstancesPolicy**](taskschedulerschema-multipleinstancespolicy-settingstype-element.md)                 | [**multipleInstancesPolicyType**](taskschedulerschema-multipleinstancespolicytype-simpletype.md) | Specifies the policy that defines how the Task Scheduler deals with multiple instances of the task. <br/>                                                                                                                                                                                                     |
| [**NetworkProfileName**](taskschedulerschema-networkprofilename-settingstype-element.md)                           | string                                                                                            | Specifies the name of a network profile. The Task Scheduler service verifies the availability of this network when the [**RunOnlyIfNetworkAvailable**](taskschedulerschema-runonlyifnetworkavailable-settingstype-element.md) element is set to **True**. The name is used for display purposes.<br/>        |
| [**NetworkSettings**](taskschedulerschema-networksettings-settingstype-element.md)                                 | [**networkSettingsType**](taskschedulerschema-networksettingstype-complextype.md)                | Specifies the settings that the Task Scheduler service uses to obtain a network profile. The Task Scheduler service checks the availability of this network when the [**RunOnlyIfNetworkAvailable**](taskschedulerschema-runonlyifnetworkavailable-settingstype-element.md) element is set to **True**.<br/> |
| [**Priority**](taskschedulerschema-priority-settingstype-element.md)                                               | [**priorityType**](taskschedulerschema-prioritytype-simpletype.md)                               | Specifies the priority level for the task.<br/>                                                                                                                                                                                                                                                               |
| [**RestartOnFailure**](taskschedulerschema-restartonfailure-settingstype-element.md)                               | [**restartType**](taskschedulerschema-restarttype-complextype.md)                                | Specifies that the Task Scheduler will attempt to restart the task if it fails for any reason. <br/>                                                                                                                                                                                                          |
| [**RunOnlyIfIdle**](taskschedulerschema-runonlyifidle-settingstype-element.md)                                     | boolean                                                                                           | Specifies that the task is run only when the computer is in an idle state.<br/>                                                                                                                                                                                                                               |
| [**RunOnlyIfNetworkAvailable**](taskschedulerschema-runonlyifnetworkavailable-settingstype-element.md)             | boolean                                                                                           | Specifies that the Task Scheduler will run the task only when a network is available.<br/>                                                                                                                                                                                                                    |
| [**StartWhenAvailable**](taskschedulerschema-startwhenavailable-settingstype-element.md)                           | boolean                                                                                           | Specifies that the Task Scheduler can start the task at any time after its scheduled time has passed.<br/>                                                                                                                                                                                                    |
| [**StopIfGoingOnBatteries**](taskschedulerschema-stopifgoingonbatteries-settingstype-element.md)                   | boolean                                                                                           | Specifies that the task will be stopped if the computer switches to battery power. <br/>                                                                                                                                                                                                                      |
| [**UseUnifiedSchedulingEngine**](taskschedulerschema-useunifiedschedulingengine-settingstype-element.md)           | boolean                                                                                           | Specifies that the task is run by using the Unified Scheduling Engine.<br/>                                                                                                                                                                                                                                   |
| [**WakeToRun**](taskschedulerschema-waketorun-settingstype-element.md)                                             | boolean                                                                                           | Specifies that Task Scheduler will wake the computer before it runs the task.<br/>                                                                                                                                                                                                                            |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





