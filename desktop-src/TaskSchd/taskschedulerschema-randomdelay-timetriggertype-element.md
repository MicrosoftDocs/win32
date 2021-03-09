---
title: RandomDelay (timeTriggerType) Element
description: Contains the delay time that is randomly added to the start time of the trigger. | RandomDelay (timeTriggerType) Element
ms.assetid: 84dffd18-651d-4e81-8c02-6cee9759a9b9
keywords:
- RandomDelay element Task Scheduler
topic_type:
- apiref
api_name:
- RandomDelay
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RandomDelay (timeTriggerType) Element

Contains the delay time that is randomly added to the start time of the trigger. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). For more information about the duration type, see <https://go.microsoft.com/fwlink/p/?linkid=106886>.

``` syntax
<xs:element name="RandomDelay"
    type="duration"
    default="PT0M"
    minOccurs="0"
 />
```

The element is defined by the [**timeTriggerType**](taskschedulerschema-timetriggertype-complextype.md) complex type.

## Parent element



| Element                                                                                    | Derived from                                                               | Description                                                                      |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**TimeTrigger (triggerGroup)**](taskschedulerschema-timetrigger-triggergroup-element.md) | [**timeTriggerType**](taskschedulerschema-timetriggertype-complextype.md) | Specifies a trigger that starts a task when the trigger is activated.<br/> |



## Remarks

For C++ development, see [**RandomDelay Property of ITimeTrigger**](/windows/desktop/api/taskschd/nf-taskschd-itimetrigger-get_randomdelay).

For script development, see [**TimeTrigger.RandomDelay**](timetrigger-randomdelay.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





