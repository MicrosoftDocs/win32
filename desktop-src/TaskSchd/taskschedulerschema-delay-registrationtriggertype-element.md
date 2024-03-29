---
title: Delay (registrationTriggerType) Element
description: Specifies the amount of time between when the task is registered and when the task is started.
ms.assetid: 8955d86c-8306-45e7-93cf-eacf50e10075
keywords:
- Delay element Task Scheduler
topic_type:
- apiref
api_name:
- Delay
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Delay (registrationTriggerType) Element

Specifies the amount of time between when the task is registered and when the task is started. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). For more information about the duration type, see <https://go.microsoft.com/fwlink/p/?linkid=106886>.

``` syntax
<xs:element name="Delay"
    type="duration"
 />
```

The **Delay** element is defined by the [**registrationTriggerType**](taskschedulerschema-registrationtriggertype-complextype.md) complex type.

## Parent element



| Element                                                                                     | Derived from                                                                               | Description                                                                    |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**RegistrationTrigger**](taskschedulerschema-registrationtrigger-triggergroup-element.md) | [**registrationTriggerType**](taskschedulerschema-registrationtriggertype-complextype.md) | Specifies a trigger that starts a task when the task is registered.<br/> |



## Remarks

For scripting development, the registration trigger delay is specified using the [**RegistrationTrigger.Delay**](registrationtrigger-delay.md) property.

For C++ development, the registration trigger delay is specified using the [**IRegistrationTrigger::Delay**](/windows/desktop/api/taskschd/nf-taskschd-iregistrationtrigger-get_delay) property.

## Examples

The following XML defines a registration trigger delay that allows a 5 minute delay between when the task is registered and when the task is started.


```XML
<BootTrigger>
    <StartBoundary>2005-01-01T08:00:00</StartBoundary>
    <EndBounadry>2007-01-01T08:00:00</EndBoundary>
    <Enabled></Enabled>
    <Repetition></Repetition>
    <ExecutionTimeLimit></ExecutionTimeLimit>
    <Delay>PT5M</Delay>
 </BootTrigger>
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

 

 





