---
title: RandomDelay (calendarTriggerType) Element
description: Contains the delay time that is randomly added to the start time of the trigger. | RandomDelay (calendarTriggerType) Element
ms.assetid: 497fab4e-ad63-43e6-a086-2d77b43662d9
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

# RandomDelay (calendarTriggerType) Element

Contains the delay time that is randomly added to the start time of the trigger. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). For more information about the duration type, see <https://go.microsoft.com/fwlink/p/?linkid=106886>.

``` syntax
<xs:element name="RandomDelay"
    type="duration"
    default="PT0M"
    minOccurs="0"
 />
```

The **RandomDelay** element is defined by the [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md) complex type.

## Parent element



| Element                                                                                            | Derived from                                                                       | Description                                                                                 |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**CalendarTrigger (triggerGroup)**](taskschedulerschema-calendartrigger-triggergroup-element.md) | [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md) | Specifies a daily, weekly, monthly, or a monthly day-of-the-week (DOW) trigger. <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





