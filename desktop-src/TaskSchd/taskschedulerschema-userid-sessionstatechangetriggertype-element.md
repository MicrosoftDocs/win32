---
title: UserId (sessionStateChangeTriggerType) Element
description: Contains the user for the Terminal Server session. When a session state change is detected for this user, a task is started.
ms.assetid: 7605f444-b2c9-4bba-a035-f1307c01184f
keywords:
- UserId element Task Scheduler
topic_type:
- apiref
api_name:
- UserId
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# UserId (sessionStateChangeTriggerType) Element

Contains the user for the Terminal Server session. When a session state change is detected for this user, a task is started.

``` syntax
<xs:element name="UserId"
    type="nonEmptyString"
    maxOccurs="1"
    minOccurs="0"
 />
```

The **UserId** element is defined by the [**sessionStateChangeTriggerType**](taskschedulerschema-sessionstatechangetriggertype-complextype.md) complex type.

## Parent element



| Element                       | Derived from                                                                                           | Description                                                                                     |
|-------------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **SessionStateChangeTrigger** | [**sessionStateChangeTriggerType**](taskschedulerschema-sessionstatechangetriggertype-complextype.md) | Specifies a trigger that starts a task when a Terminal Server session changes state.<br/> |



## Remarks

For C++ development, see [**UserId Property of ISessionStateChangeTrigger**](/windows/desktop/api/taskschd/nf-taskschd-isessionstatechangetrigger-get_userid).

For script development, see [**SessionStateChangeTrigger.UserId**](sessionstatechangetrigger-userid.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





