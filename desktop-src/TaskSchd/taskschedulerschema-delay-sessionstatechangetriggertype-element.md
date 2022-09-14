---
title: Delay (sessionStateChangeTriggerType) Element
description: Contains a value that indicates the delay length for a task start time, when a Terminal Server session state change is detected.
ms.assetid: 7fb87c4c-0b69-4c5b-b038-d61fb7c4ab9a
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

# Delay (sessionStateChangeTriggerType) Element

Contains a value that indicates the delay length for a task start time, when a Terminal Server session state change is detected. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). For more information about the duration type, see <https://go.microsoft.com/fwlink/p/?linkid=106886>.

``` syntax
<xs:element name="Delay"
    type="duration"
 />
```

The **Delay** element is defined by the [**sessionStateChangeTriggerType**](taskschedulerschema-sessionstatechangetriggertype-complextype.md) complex type.

## Parent element



| Element                       | Derived from                                                                                           | Description                                                                                      |
|-------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **SessionStateChangeTrigger** | [**sessionStateChangeTriggerType**](taskschedulerschema-sessionstatechangetriggertype-complextype.md) | Specifies a trigger that starts a task when a Terminal Server session changes state. <br/> |



## Remarks

For scripting development, the session state change trigger delay is specified using the [**SessionStateChangeTrigger.Delay**](sessionstatechangetrigger-delay.md) property.

For C++ development, the session state change trigger delay is specified using the [**Delay property of ISessionStateChangeTrigger**](/windows/desktop/api/taskschd/nf-taskschd-isessionstatechangetrigger-get_delay).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





