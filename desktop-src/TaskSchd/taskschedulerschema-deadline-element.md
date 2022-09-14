---
title: Deadline Element
description: Specifies when the Task scheduler must to start the task during emergency Automatic maintenance, if it failed to complete during regular Automatic maintenance.
ms.assetid: 34E33FAE-888E-4E82-83B8-059FB4A64B52
keywords:
- Deadline element Task Scheduler
topic_type:
- apiref
api_name:
- Deadline
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Deadline Element

Specifies when the Task scheduler must to start the task during emergency Automatic maintenance, if it failed to complete during regular Automatic maintenance.

The format for this string is *PnYnMnDTnHnMnS*, where *nY* is the number of years, nM is the number of months, *nD* is the number of days, *T* is the date/time separator, *nH* is the number of hours, *nM* is the number of minutes, and *nS* is the number of seconds (for example, "PT5M" specifies 5 minutes and "P1M4DT2H5M" specifies one month, four days, two hours, and five minutes). The minimum value is one minute. For more information about the duration type, see [XML Schema Part 2: Datatypes Second Edition](https://www.w3.org/TR/xmlschema-2/#duration). Minimum Deadline a task can use is 1 day. The value of the **Deadline** element should be greater than the value of the [**Period**](taskschedulerschema-period-element.md) element. If the deadline is not specified the task will not be started during emergency Automatic maintenance.

``` syntax
<xs:element name="Deadline"
    maxOccurs="1"
    minOccurs="0"
>
    <xs:simpleType>
        <xs:restriction
            base="duration"
        >
            <xs:minInclusive
                value="P1D"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **Deadline** element is defined by the [**maintenanceSettingsType**](taskschedulerschema-maintenancesettingstype-complextype.md) complex type.

## Parent element



| Element                                                                                                                          | Derived from                                                                               | Description                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**MaintenanceSettings (maintenanceSettingsType)**](taskschedulerschema-maintenancesettings-maintenancesettingstype-element.md) | [**maintenanceSettingsType**](taskschedulerschema-maintenancesettingstype-complextype.md) | Specifies the task settings the Task scheduler will use to start task during Automatic maintenance.<br/> |



## Remarks

For C++ programming, this idle setting is specified using the [**IMaintenanceSettings::Deadline**](/windows/desktop/api/Taskschd/nf-taskschd-imaintenancesettings-get_deadline) property.

## Examples

The following XML defines a months calendar that runs the task in March.


```XML
<MaintenanceSettings>
    <Period>P5D</Period>
    <Deadline>P15D</Deadline>
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

 

 





