---
title: Exclusive Element
description: Indicates whether the Task scheduler must start the task during the Automatic maintenance in exclusive mode.
ms.assetid: F690FD8F-BCCB-456D-92E3-25A262D6DCF1
keywords:
- Exclusive element Task Scheduler
topic_type:
- apiref
api_name:
- Exclusive
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Exclusive Element

Indicates whether the Task scheduler must start the task during the Automatic maintenance in exclusive mode.

The exclusivity is guaranteed only between other maintenance tasks and doesn't grant any ordering priority of the task. If exclusivity is not specified, the task is started in parallel with other maintenance tasks.

``` syntax
<xs:element name="Exclusive"
    type="xsd:boolean"
    maxOccurs="1"
    minOccurs="0"
 />
```

The **Exclusive** element is defined by the [**maintenanceSettingsType**](taskschedulerschema-maintenancesettingstype-complextype.md) complex type.

## Parent element



| Element                                                                                                                          | Derived from                                                                               | Description                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**MaintenanceSettings (maintenanceSettingsType)**](taskschedulerschema-maintenancesettings-maintenancesettingstype-element.md) | [**maintenanceSettingsType**](taskschedulerschema-maintenancesettingstype-complextype.md) | Specifies the task settings the Task scheduler will use to start task during Automatic maintenance.<br/> |



## Remarks

For C++ programming, this idle setting is specified using the [**IMaintenanceSettings::Exclusive**](/windows/desktop/api/Taskschd/nf-taskschd-imaintenancesettings-get_exclusive) property.

## Examples

The following XML defines maintenance task with deadline requirement set to 15 days.


```XML
<MaintenanceSettings>
    <Period>P5D</Period>
    <Deadline>P15D</Deadline>
    <Exclusive>true</Exclusive>
</MaintenanceSettings>
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

 

 





