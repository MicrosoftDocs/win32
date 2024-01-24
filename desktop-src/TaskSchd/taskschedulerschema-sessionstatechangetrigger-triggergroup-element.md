---
title: SessionStateChangeTrigger (triggerGroup) Element
description: Specifies a trigger that starts a task when a Terminal Server session changes state.
ms.assetid: 38b0da3c-205f-48c5-83e6-ff7c432c02b9
keywords:
- SessionStateChangeTrigger element Task Scheduler
topic_type:
- apiref
api_name:
- SessionStateChangeTrigger
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# SessionStateChangeTrigger (triggerGroup) Element

Specifies a trigger that starts a task when a Terminal Server session changes state.

``` syntax
<xs:element name="SessionStateChangeTrigger"
    type="sessionStateChangeTriggerType"
 />
```

The **SessionStateChangeTrigger** element is defined by the [**triggerGroup**](taskschedulerschema-triggergroup-group.md) .

## Parent element



| Element                                                           | Derived from                                                         | Description                                            |
|-------------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------|
| [**Triggers**](taskschedulerschema-triggers-tasktype-element.md) | [**triggersType**](taskschedulerschema-triggerstype-complextype.md) | Specifies the triggers that start the task.<br/> |



## Child elements



| Element                                                                                      | Type                                                                                    | Description                                                                                                                                           |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Delay**](taskschedulerschema-delay-sessionstatechangetriggertype-element.md)             | duration                                                                                | Specifies a value that indicates the length of the delay before a task is started when a Terminal Server session state change is detected.<br/> |
| [**StateChange**](taskschedulerschema-statechange-sessionstatechangetriggertype-element.md) | [**sessionStateChangeType**](taskschedulerschema-sessionstatechangetype-simpletype.md) | Specifies the kind of Terminal Server session change that would trigger a task launch.<br/>                                                     |
| [**UserId**](taskschedulerschema-userid-sessionstatechangetriggertype-element.md)           | [**nonEmptyString**](taskschedulerschema-nonemptystring-simpletype.md)                 | Specifies the user for the Terminal Server session. When a session state change is detected for this user, a task is started.<br/>              |



## Remarks

For scripting development, a session state change trigger is specified using the [**SessionStateChangeTrigger**](sessionstatechangetrigger.md) object.

For C++ development, a session state change trigger is specified using the [**ISessionStateChangeTrigger**](/windows/desktop/api/taskschd/nn-taskschd-isessionstatechangetrigger) interface.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





