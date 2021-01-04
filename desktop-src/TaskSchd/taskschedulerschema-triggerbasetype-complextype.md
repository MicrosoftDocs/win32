---
title: triggerBaseType Complex Type
description: Defines the attribute, base child elements, and sequencing information for all trigger complex types.
ms.assetid: 1a2d004a-6f52-42b7-b0d0-ace8d27e9166
keywords:
- triggerBaseType complex type Task Scheduler
topic_type:
- apiref
api_name:
- triggerBaseType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# triggerBaseType Complex Type

Defines the attribute, base child elements, and sequencing information for all trigger complex types.

``` syntax
<xs:complexType name="triggerBaseType"
    abstract="true"
>
    <xs:sequence>
        <xs:element name="Enabled"
            type="boolean"
            default="true"
            minOccurs="0"
         />
        <xs:element name="StartBoundary"
            type="dateTime"
            minOccurs="0"
         />
        <xs:element name="EndBoundary"
            type="dateTime"
            minOccurs="0"
         />
        <xs:element name="Repetition"
            type="repetitionType"
            minOccurs="0"
         />
        <xs:element name="ExecutionTimeLimit"
            type="duration"
            minOccurs="0"
         />
    </xs:sequence>
    <xs:attribute name="id"
        type="ID"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element                                                                                      | Type                                                                     | Description                                                                                                            |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**Enabled**](taskschedulerschema-enabled-triggerbasetype-element.md)                       | boolean                                                                  | Specifies that the trigger is enabled.<br/>                                                                      |
| [**EndBoundary**](taskschedulerschema-endboundary-triggerbasetype-element.md)               | dateTime                                                                 | The date and time when the trigger is deactivated.<br/>                                                          |
| [**ExecutionTimeLimit**](taskschedulerschema-executiontimelimit-triggerbasetype-element.md) | duration                                                                 | Specifies the interval when the trigger can start the task.<br/>                                                 |
| [**Repetition**](taskschedulerschema-repetition-triggerbasetype-element.md)                 | [**repetitionType**](taskschedulerschema-repetitiontype-complextype.md) | Specifies how often the task is run and how long the repetition pattern is repeated once the trigger fires.<br/> |
| [**StartBoundary**](taskschedulerschema-startboundary-triggerbasetype-element.md)           | dateTime                                                                 | The date and time when the trigger is activated.<br/>                                                            |



## Attributes



| Name | Type | Description                           |
|------|------|---------------------------------------|
| id   | ID   | Identifier of the trigger.<br/> |



## Remarks

Trigger complex types include the following.

-   [**bootTriggerType**](taskschedulerschema-boottriggertype-complextype.md)
-   [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md)
-   [**eventTriggerType**](taskschedulerschema-eventtriggertype-complextype.md)
-   [**idleTriggerType**](taskschedulerschema-idletriggertype-complextype.md)
-   [**logonTriggerType**](taskschedulerschema-logontriggertype-complextype.md)
-   [**registrationTriggerType**](taskschedulerschema-registrationtriggertype-complextype.md)
-   [**timeTriggerType**](taskschedulerschema-timetriggertype-complextype.md)

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





