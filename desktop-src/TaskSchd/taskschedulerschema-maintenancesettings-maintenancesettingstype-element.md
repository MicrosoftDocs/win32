---
title: MaintenanceSettings (maintenanceSettingsType) Element
description: Specifies how the Task Scheduler performs tasks during Automatic maintenance.
ms.assetid: 6A204980-851D-4487-A6CC-01BE262A517A
keywords:
- MaintenanceSettings element Task Scheduler
topic_type:
- apiref
api_name:
- MaintenanceSettings
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MaintenanceSettings (maintenanceSettingsType) Element

Specifies how the Task Scheduler performs tasks during Automatic maintenance.

``` syntax
<xs:element name="MaintenanceSettings"
    type="maintenanceSettingsType"
    minOccurs="0"
 />
```

The **MaintenanceSettings** element is defined by the [**maintenanceSettingsType**](taskschedulerschema-maintenancesettingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Child elements



| Element                                                    | Type    | Description                                                                                                                                                                                     |
|------------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Deadline**](taskschedulerschema-deadline-element.md)   |         | Specifies the amount of time after which the Task scheduler will attempt to start task during emergency Automatic maintenance, if it failed to complete during regular maintenance. <br/> |
| [**Exclusive**](taskschedulerschema-exclusive-element.md) | boolean | If set to true, the task will be started exclusively among other maintenance tasks. <br/>                                                                                                 |
| [**Period**](taskschedulerschema-period-element.md)       |         | Specifies how often the task needs to be started during Automatic maintenance. <br/>                                                                                                      |



## Remarks

For C++ programming, this idle setting is specified using the [**ITaskSettings3::MaintenanceSettings**](/windows/desktop/api/Taskschd/nf-taskschd-itasksettings3-get_maintenancesettings) property.

## Examples

The following XML defines a settings element that instructs Task Scheduler to execute task once in 5 days during regular Automatic maintenance and if failed for 15 days, start attempting the task during the emergency Automatic maintenance.


```XML
<Settings>
    <MaintenanceSettings>
        <Period>P5D</Period>
        <Deadline>P15D</Deadline>
    </MaintenanceSettings>       
</Settings>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





