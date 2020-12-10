---
title: Period Element
description: Specifies how often the task needs to be started during Automatic maintenance.
ms.assetid: E4BE2466-3119-41F8-8238-4627C28B26E5
keywords:
- Period element Task Scheduler
topic_type:
- apiref
api_name:
- Period
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Period Element

Specifies how often the task needs to be started during Automatic maintenance.

The format for this string is *PnYnMnDTnHnMnS*, where *nY* is the number of years, nM is the number of months, *nD* is the number of days, *T* is the date/time separator, *nH* is the number of hours, *nM* is the number of minutes, and *nS* is the number of seconds (for example, "PT5M" specifies 5 minutes and "P1M4DT2H5M" specifies one month, four days, two hours, and five minutes). The minimum value is one minute. For more information about the duration type, see [XML Schema Part 2: Datatypes Second Edition](https://www.w3.org/TR/xmlschema-2/#duration).

``` syntax
<xs:element name="Period"
    maxOccurs="1"
    minOccurs="1"
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

The **Period** element is defined by the [**maintenanceSettingsType**](taskschedulerschema-maintenancesettingstype-complextype.md) complex type.

## Parent element



| Element                                                                                                                          | Derived from                                                                               | Description                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**MaintenanceSettings (maintenanceSettingsType)**](taskschedulerschema-maintenancesettings-maintenancesettingstype-element.md) | [**maintenanceSettingsType**](taskschedulerschema-maintenancesettingstype-complextype.md) | Specifies the task settings the Task scheduler will use to start task during Automatic maintenance.<br/> |



## Remarks

For C++ programming, this idle setting is specified using the [**IMaintenanceSettings::Period**](/windows/desktop/api/Taskschd/nf-taskschd-imaintenancesettings-get_period) property.

## Examples

The following XML defines maintenance task with periodicity requirement set to 5 days.


```XML
<MaintenanceSettings>
    <Period>P5D</Period>
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

 

 





