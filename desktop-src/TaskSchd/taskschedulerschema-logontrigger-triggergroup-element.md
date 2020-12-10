---
title: LogonTrigger (triggerGroup) Element
description: Specifies a trigger that starts a task when a user logs on.
ms.assetid: c3edee50-e053-4813-a1b2-bf1e7b575ff7
keywords:
- logon trigger, XML element
- LogonTrigger element Task Scheduler
topic_type:
- apiref
api_name:
- LogonTrigger
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# LogonTrigger (triggerGroup) Element

Specifies a trigger that starts a task when a user logs on.

``` syntax
<xs:element name="LogonTrigger"
    type="logonTriggerType"
 />
```

The **LogonTrigger** element is defined by the [**triggerGroup**](taskschedulerschema-triggergroup-group.md) .

## Parent element



| Element                                                           | Derived from                                                         | Description                                            |
|-------------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------|
| [**Triggers**](taskschedulerschema-triggers-tasktype-element.md) | [**triggersType**](taskschedulerschema-triggerstype-complextype.md) | Specifies the triggers that start the task.<br/> |



## Child elements



| Element                                                                                                        | Type                                                                     | Description                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**Delay (logonTriggerType)**](taskschedulerschema-delay-logontriggertype-element.md)                         | duration                                                                 | Amount of time between when the user logs on and when the task is started.<br/>                                              |
| [**Enabled (triggerBaseType)**](taskschedulerschema-enabled-triggerbasetype-element.md)                       | boolean                                                                  | Specifies that the trigger is enabled.<br/>                                                                                  |
| [**EndBoundary (triggerBaseType)**](taskschedulerschema-endboundary-triggerbasetype-element.md)               | dateTime                                                                 | Specifies the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/> |
| [**ExecutionTimeLimit (triggerBaseType)**](taskschedulerschema-executiontimelimit-triggerbasetype-element.md) | duration                                                                 | Specifies the maximum amount of time in which the task can be started by the trigger.<br/>                                   |
| [**Repetition (triggerBaseType)**](taskschedulerschema-repetition-triggerbasetype-element.md)                 | [**repetitionType**](taskschedulerschema-repetitiontype-complextype.md) | Specifies how often the task is run and how long the repetition pattern is repeated after the task is started.<br/>          |
| [**StartBoundary (triggerBaseType)**](taskschedulerschema-startboundary-triggerbasetype-element.md)           | dateTime                                                                 | Specifies the date and time when the trigger is activated.<br/>                                                              |
| [**UserId (logonTriggerType)**](taskschedulerschema-userid-logontriggertype-element.md)                       | string                                                                   | Identifier of the user. The task is started when this user logs onto the computer.<br/>                                      |



## Remarks

For scripting development, a logon trigger is specified using the [**LogonTrigger**](logontrigger.md) object.

For C++ development, a logon trigger is specified using the [**ILogonTrigger**](/windows/desktop/api/taskschd/nn-taskschd-ilogontrigger) interface.

The child elements listed above are defined by the [**triggerBaseType**](taskschedulerschema-triggerbasetype-complextype.md) and [**logonTriggerType**](taskschedulerschema-logontriggertype-complextype.md) complex element types. These elements must be added in the sequence shown below.

-   [**StartBoundary (triggerBaseType)**](taskschedulerschema-startboundary-triggerbasetype-element.md)
-   [**EndBoundary (triggerBaseType)**](taskschedulerschema-endboundary-triggerbasetype-element.md)
-   [**Enabled (triggerBaseType)**](taskschedulerschema-enabled-triggerbasetype-element.md)
-   [**Repetition (triggerBaseType)**](taskschedulerschema-repetition-triggerbasetype-element.md)
-   [**ExecutionTimeLimit (triggerBaseType)**](taskschedulerschema-executiontimelimit-triggerbasetype-element.md)
-   [**UserId (logonTriggerType)**](taskschedulerschema-userid-logontriggertype-element.md)
-   [**Delay (logonTriggerType)**](taskschedulerschema-delay-logontriggertype-element.md)

### Attributes

The attribute listed below is defined by the [**triggerBaseType**](taskschedulerschema-triggerbasetype-complextype.md) complex element types.

-   Id: Identifier of the trigger.

## Examples

For a complete example of the XML for a task that uses a logon trigger, see [Logon Trigger Example (XML)](logon-trigger-example--xml-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





