---
title: sessionStateChangeTriggerType Complex Type
description: Defines the elements used to create a task trigger for console connect or disconnect, remote connect or disconnect, or workstation lock or unlock notifications.
ms.assetid: 0d452476-1e1f-417d-a97a-5f39d80145f2
keywords:
- sessionStateChangeTriggerType complex type Task Scheduler
topic_type:
- apiref
api_name:
- sessionStateChangeTriggerType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# sessionStateChangeTriggerType Complex Type

Defines the elements used to create a task trigger for console connect or disconnect, remote connect or disconnect, or workstation lock or unlock notifications.

``` syntax
<xs:complexType name="sessionStateChangeTriggerType">
    <xs:complexContent>
        <xs:extension
            base="triggerBaseType"
        >
            <xs:sequence>
                <xs:element name="UserId"
                    type="nonEmptyString"
                    minOccurs="0"
                 />
                <xs:element name="Delay"
                    type="duration"
                    default="PT0M"
                    minOccurs="0"
                 />
                <xs:element name="StateChange"
                    type="sessionStateChangeType"
                    minOccurs="1"
                    maxOccurs="1"
                 />
            </xs:sequence>
        </xs:extension>
    </xs:complexContent>
</xs:complexType>
```

## Child elements



| Element                                                                                      | Type                                                                                    | Description                                                                                                                                           |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Delay**](taskschedulerschema-delay-sessionstatechangetriggertype-element.md)             | duration                                                                                | Specifies a value that indicates the length of the delay before a task is started when a Terminal Server session state change is detected.<br/> |
| [**StateChange**](taskschedulerschema-statechange-sessionstatechangetriggertype-element.md) | [**sessionStateChangeType**](taskschedulerschema-sessionstatechangetype-simpletype.md) | Specifies the kind of Terminal Server session change that would trigger a task launch.<br/>                                                     |
| [**UserId**](taskschedulerschema-userid-sessionstatechangetriggertype-element.md)           | [**nonEmptyString**](taskschedulerschema-nonemptystring-simpletype.md)                 | Specifies the user for the Terminal Server session. When a session state change is detected for this user, a task is started.<br/>              |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





