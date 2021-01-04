---
title: Duration (idleSettingsType) Element
description: Specifies how long the computer must be in an idle state before the task is run.
ms.assetid: 89584694-0685-44e2-b8b7-69e47ee28d5d
keywords:
- Duration element Task Scheduler
topic_type:
- apiref
api_name:
- Duration
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Duration (idleSettingsType) Element

Specifies how long the computer must be in an idle state before the task is run. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). The minimum value is one minute. For more information about the duration type, see <https://go.microsoft.com/fwlink/p/?linkid=106886>.

``` syntax
<xs:element name="Duration"
    default="PT10M"
    minOccurs="0"
>
    <xs:simpleType>
        <xs:restriction
            base="duration"
        >
            <xs:minInclusive
                value="PT1M"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The element is defined by the [**idleSettingsType**](taskschedulerschema-idlesettingstype-complextype.md) complex type.

## Parent element



| Element                                                                       | Derived from                                                                 | Description                                                                                       |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**IdleSettings**](taskschedulerschema-idlesettings-settingstype-element.md) | [**idleSettingsType**](taskschedulerschema-idlesettingstype-complextype.md) | Specifies how the Task Scheduler performs tasks when the computer is in an idle state.<br/> |



## Remarks

For script programming, this idle setting is specified using the [**IdleSettings.IdleDuration**](idlesettings-idleduration.md) property.

For C++ programming, this idle setting is specified using the [**IIdleSettings::IdleDuration**](/windows/desktop/api/taskschd/nf-taskschd-iidlesettings-get_idleduration) property.

## Examples

The following XML defines an idle setting that allows 5 minutes for the task to start.


```XML
<IdleSettings>
    <Duration>PT5M</Duration>
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

 

 





