---
title: Duration (repetitionType) Element
description: Specifies how long the pattern is repeated.
ms.assetid: a24f3827-18b2-465e-b132-77dce139e0d4
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

# Duration (repetitionType) Element

Specifies how long the pattern is repeated. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). For more information about the duration type, see <https://go.microsoft.com/fwlink/p/?linkid=106886>. If no value is specified for the duration, then the pattern is repeated indefinitely. The minimum value is one minute.

``` syntax
<xs:element name="Duration"
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

The element is defined by the [**repetitionType**](taskschedulerschema-repetitiontype-complextype.md) complex type.

## Parent element



| Element                                                                      | Derived from                                                             | Description                                                                                                               |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**Repetition**](taskschedulerschema-repetition-triggerbasetype-element.md) | [**repetitionType**](taskschedulerschema-repetitiontype-complextype.md) | Specifies how often the task is run and how long the repetition pattern is repeated after the task is started.<br/> |



## Remarks

For scripting applications, the duration of the pattern is specified using the [**RepetitionPattern.Duration**](repetitionpattern-duration.md) property.

For C++ applications, the duration of the pattern is specified using the [**IRepetitionPattern::Duration**](/windows/desktop/api/taskschd/nf-taskschd-irepetitionpattern-get_duration) property.

## Examples

The following XML defines a repetition pattern for a trigger.


```XML
<Repetition>
    <Interval></Interval>
    <Duration></Duration>
    <StopAtDurationEnd>true</StopAtDirationEnd>
</Repetition>
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

 

 





