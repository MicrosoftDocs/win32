---
title: StateChange (sessionStateChangeTriggerType) Element
description: Contains the kind of Terminal Server session change that would trigger a task launch.
ms.assetid: 0b17a4a5-caa7-4b58-a1a4-cbc7564838bb
keywords:
- StateChange element Task Scheduler
topic_type:
- apiref
api_name:
- StateChange
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StateChange (sessionStateChangeTriggerType) Element

Contains the kind of Terminal Server session change that would trigger a task launch.

``` syntax
<xs:element name="StateChange"
    type="sessionStateChangeType"
 />
```

The **StateChange** element is defined by the [**sessionStateChangeTriggerType**](taskschedulerschema-sessionstatechangetriggertype-complextype.md) complex type.

## Parent element



| Element                       | Derived from                                                                                           | Description                                                                                     |
|-------------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **SessionStateChangeTrigger** | [**sessionStateChangeTriggerType**](taskschedulerschema-sessionstatechangetriggertype-complextype.md) | Specifies a trigger that starts a task when a Terminal Server session changes state.<br/> |



## Remarks

For C++ development, see [**StateChange Property of ISessionStateChangeTrigger**](/windows/desktop/api/taskschd/nf-taskschd-isessionstatechangetrigger-get_statechange).

For script development, see [**SessionStateChangeTrigger.StateChange**](sessionstatechangetrigger-statechange.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





