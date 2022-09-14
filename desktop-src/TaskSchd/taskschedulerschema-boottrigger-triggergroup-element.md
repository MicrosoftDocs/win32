---
title: BootTrigger (triggerGroup) Element
description: Specifies a trigger that starts a task when the system is booted.
ms.assetid: c6833547-0daf-4e8a-b8c5-b422827b1d96
keywords:
- boot trigger Task Scheduler , XML element
- BootTrigger element Task Scheduler
topic_type:
- apiref
api_name:
- BootTrigger
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# BootTrigger (triggerGroup) Element

Specifies a trigger that starts a task when the system is booted.

``` syntax
<xs:element name="BootTrigger"
    type="bootTriggerType"
 />
```

The **BootTrigger** element is defined by the [**bootTriggerType**](taskschedulerschema-boottriggertype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                            |
|-------------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------|
| [**Triggers**](taskschedulerschema-triggers-tasktype-element.md) | [**triggersType**](taskschedulerschema-triggerstype-complextype.md) | Specifies the triggers that start the task.<br/> |



## Child elements



| Element                                                                                                        | Type                                                                     | Description                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**Delay (bootTriggerType)**](taskschedulerschema-delay-boottriggertype-element.md)                           | duration                                                                 | Specifies the amount of time between when the system is booted and when the task is started.<br/>                            |
| [**Enabled (triggerBaseType)**](taskschedulerschema-enabled-triggerbasetype-element.md)                       | boolean                                                                  | Specifies that the trigger is enabled.<br/>                                                                                  |
| [**EndBoundary (triggerBaseType)**](taskschedulerschema-endboundary-triggerbasetype-element.md)               | dateTime                                                                 | Specifies the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/> |
| [**ExecutionTimeLimit (triggerBaseType)**](taskschedulerschema-executiontimelimit-triggerbasetype-element.md) | duration                                                                 | Specifies the maximum amount of time in which the task can be started by the trigger.<br/>                                   |
| [**Repetition (triggerBaseType)**](taskschedulerschema-repetition-triggerbasetype-element.md)                 | [**repetitionType**](taskschedulerschema-repetitiontype-complextype.md) | Specifies how often the task is run and how long the repetition pattern is repeated after the task is started.<br/>          |
| [**StartBoundary (triggerBaseType)**](taskschedulerschema-startboundary-triggerbasetype-element.md)           | dateTime                                                                 | Specifies the date and time when the trigger is activated.<br/>                                                              |



## Attributes



| Name | Type       | Description                               |
|------|------------|-------------------------------------------|
| Id   | **string** | The identifier of the trigger.<br/> |



## Remarks

For script development, a boot trigger is defined by the [**BootTrigger**](boottrigger.md) object.

For C++ development, a boot trigger is defined by the [**IBootTrigger**](/windows/desktop/api/taskschd/nn-taskschd-iboottrigger) object.

## Examples

For a complete example of the XML for a task that specifies a boot trigger, see [Boot Trigger Example (XML)](boot-trigger-example--xml-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





