---
title: TimeTrigger (triggerGroup) Element
description: Specifies a trigger that starts a task when the trigger is activated.
ms.assetid: bb467f36-47cd-4db4-97c4-60c09937caac
keywords:
- TimeTrigger element Task Scheduler
topic_type:
- apiref
api_name:
- TimeTrigger
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TimeTrigger (triggerGroup) Element

Specifies a trigger that starts a task when the trigger is activated.

``` syntax
<xs:element name="TimeTrigger"
    type="timeTriggerType"
 />
```

The **TimeTrigger** element is defined by the [**triggerGroup**](taskschedulerschema-triggergroup-group.md) .

## Parent element



| Element                                                           | Derived from                                                         | Description                                            |
|-------------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------|
| [**Triggers**](taskschedulerschema-triggers-tasktype-element.md) | [**triggersType**](taskschedulerschema-triggerstype-complextype.md) | Specifies the triggers that start the task.<br/> |



## Child elements



| Element                                                                                                        | Type                                                                     | Description                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**Enabled (triggerBaseType)**](taskschedulerschema-enabled-triggerbasetype-element.md)                       | boolean                                                                  | Specifies that the trigger is enabled.<br/>                                                                                  |
| [**EndBoundary (triggerBaseType)**](taskschedulerschema-endboundary-triggerbasetype-element.md)               | dateTime                                                                 | Specifies the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/> |
| [**ExecutionTimeLimit (triggerBaseType)**](taskschedulerschema-executiontimelimit-triggerbasetype-element.md) | duration                                                                 | Specifies the maximum amount of time in which the task can be started by the trigger.<br/>                                   |
| [**Repetition (triggerBaseType)**](taskschedulerschema-repetition-triggerbasetype-element.md)                 | [**repetitionType**](taskschedulerschema-repetitiontype-complextype.md) | Specifies how often the task is run and how long the repetition pattern is repeated after the task is started.<br/>          |
| [**StartBoundary (triggerBaseType)**](taskschedulerschema-startboundary-triggerbasetype-element.md)           | dateTime                                                                 | Specifies the date and time when the trigger is activated. This element is required.<br/>                                    |



## Attributes



| Name | Type       | Description                               |
|------|------------|-------------------------------------------|
| Id   | **string** | The identifier of the trigger.<br/> |



## Remarks

The [**StartBoundary**](taskschedulerschema-startboundary-triggerbasetype-element.md) element is a required element for time and calendar triggers (**TimeTrigger** and [**CalendarTrigger**](taskschedulerschema-calendartrigger-triggergroup-element.md)).

For scripting development, a time trigger is specified using the [**TimeTrigger**](timetrigger.md) object.

For C++ development, a time trigger is specified using the [**ITimeTrigger**](/windows/desktop/api/taskschd/nn-taskschd-itimetrigger) interface.

The child elements listed above are defined by the [**triggerBaseType**](taskschedulerschema-triggerbasetype-complextype.md) complex element types. These elements must be added in the sequence shown below.

-   [**StartBoundary (triggerBaseType)**](taskschedulerschema-startboundary-triggerbasetype-element.md)
-   [**EndBoundary (triggerBaseType)**](taskschedulerschema-endboundary-triggerbasetype-element.md)
-   [**Enabled (triggerBaseType)**](taskschedulerschema-enabled-triggerbasetype-element.md)
-   [**Repetition (triggerBaseType)**](taskschedulerschema-repetition-triggerbasetype-element.md)
-   [**ExecutionTimeLimit (triggerBaseType)**](taskschedulerschema-executiontimelimit-triggerbasetype-element.md)

## Examples

For a complete example of the XML for a task that specifies a time trigger, see [Time Trigger Example (XML)](time-trigger-example--xml-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





