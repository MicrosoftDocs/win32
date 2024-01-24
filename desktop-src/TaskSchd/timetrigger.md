---
title: TimeTrigger object (Windows.applicationmodel.background.h)
description: Scripting object that represents a trigger that starts a task at a specific date and time.
ms.assetid: '3c277827-8e70-42e7-a849-773ecc997a93'
keywords:
- time trigger Task Scheduler , object
- TimeTrigger object Task Scheduler
- TimeTrigger object Task Scheduler , described
topic_type:
- apiref
api_name:
- TimeTrigger
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TimeTrigger object

Scripting object that represents a trigger that starts a task at a specific date and time.

## Members

The **TimeTrigger** object has these types of members:

-   [Properties](#properties)

### Properties

The **TimeTrigger** object has these properties.



| Property                                                            | Access type           | Description                                                                                                                                                                      |
|:--------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Enabled**](trigger-enabled.md)<br/>                       | Read/write<br/> | Inherited from [**Trigger**](trigger.md). Gets or sets a Boolean value that indicates whether the trigger is enabled.<br/>                                                |
| [**EndBoundary**](trigger-endboundary.md)<br/>               | Read/write<br/> | Inherited from [**Trigger**](trigger.md). Gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/> |
| [**ExecutionTimeLimit**](trigger-executiontimelimit.md)<br/> | Read/write<br/> | Inherited from [**Trigger**](trigger.md). Gets or sets the maximum amount of time that the task launched by the trigger is allowed to run.<br/>                           |
| [**Id**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_id)<br/>                                | Read/write<br/> | Inherited from [**Trigger**](trigger.md). Gets or sets the identifier for the trigger.<br/>                                                                               |
| [**RandomDelay**](dailytrigger-randomdelay.md)<br/>          | Read/write<br/> | Gets or sets a delay time that is randomly added to the start time of the trigger.<br/>                                                                                    |
| [**Repetition**](trigger-repetition.md)<br/>                 | Read/write<br/> | Inherited from [**Trigger**](trigger.md). Gets or sets how often the task is run and how long the repetition pattern is repeated after the task is started.<br/>          |
| [**StartBoundary**](trigger-startboundary.md)<br/>           | Read/write<br/> | Inherited from [**Trigger**](trigger.md). Gets or sets the date and time when the trigger is activated. This element is required.<br/>                                    |
| [**Type**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_type)<br/>                            | Read-only<br/>  | Inherited from [**Trigger**](trigger.md). Gets the type of the trigger.<br/>                                                                                              |



 

## Remarks

The [**StartBoundary**](taskschedulerschema-startboundary-triggerbasetype-element.md) element is a required element for time and calendar triggers ([**TimeTrigger**](taskschedulerschema-timetrigger-triggergroup-element.md) and [**CalendarTrigger**](taskschedulerschema-calendartrigger-triggergroup-element.md)).

When reading or writing XML for a task, an idle trigger is specified using the [**TimeTrigger**](taskschedulerschema-timetrigger-triggergroup-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                             |
| Header<br/>                   | <dl> <dt>Windows.applicationmodel.background.h</dt> </dl> |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**Trigger**](trigger.md)
</dt> <dt>

[**TriggerCollection**](triggercollection.md)
</dt> <dt>

[**TriggerCollection.Create**](triggercollection-create.md)
</dt> </dl>

 

 





