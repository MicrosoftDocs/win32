---
title: Trigger object
description: Scripting object that provides the common properties that are inherited by all trigger objects.
ms.assetid: 'dfc4cb36-8bdb-4aec-963e-5f1ec1ff85aa'
keywords:
- triggers Task Scheduler , trigger object
- Trigger object Task Scheduler
- Trigger object Task Scheduler , described
topic_type:
- apiref
api_name:
- Trigger
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Trigger object

Scripting object that provides the common properties that are inherited by all trigger objects.

## Members

The **Trigger** object has these types of members:

-   [Properties](#properties)

### Properties

The **Trigger** object has these properties.



| Property                                                            | Access type           | Description                                                                                                                                         |
|:--------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Enabled**](trigger-enabled.md)<br/>                       | Read/write<br/> | Gets or sets a Boolean value that indicates whether the trigger is enabled.<br/>                                                              |
| [**EndBoundary**](trigger-endboundary.md)<br/>               | Read/write<br/> | Gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/>               |
| [**ExecutionTimeLimit**](trigger-executiontimelimit.md)<br/> | Read/write<br/> | Gets or sets the maximum amount of time that the task launched by the trigger is allowed to run.<br/>                                         |
| [**Id**](trigger-id.md)<br/>                                 | Read/write<br/> | Gets or sets the identifier for the trigger.<br/>                                                                                             |
| [**Repetition**](trigger-repetition.md)<br/>                 | Read/write<br/> | Gets or sets a value that indicates how often the task is run and how long the repetition pattern is repeated after the task is started.<br/> |
| [**StartBoundary**](trigger-startboundary.md)<br/>           | Read/write<br/> | Gets or sets the date and time when the trigger is activated. The trigger can start the task after the trigger is activated.<br/>             |
| [**Type**](trigger-type.md)<br/>                             |                       | Gets the type of the trigger.<br/>                                                                                                            |



 

## Remarks

The Task Scheduler provides the following individual objects for the different triggers that a task can use:

-   [**BootTrigger**](boottrigger.md)
-   [**DailyTrigger**](dailytrigger.md)
-   [**EventTrigger**](eventtrigger.md)
-   [**IdleTrigger**](idletrigger.md)
-   [**LogonTrigger**](logontrigger.md)
-   [**MonthlyDOWTrigger**](monthlydowtrigger.md)
-   [**MonthlyTrigger**](monthlytrigger.md)
-   [**RegistrationTrigger**](registrationtrigger.md)
-   [**TimeTrigger**](timetrigger.md)
-   [**WeeklyTrigger**](weeklytrigger.md)
-   [**SessionStateChangeTrigger**](sessionstatechangetrigger.md)

When reading or writing XML, the triggers of a task are specified in the [**Triggers**](taskschedulerschema-triggers-tasktype-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TriggerCollection**](triggercollection.md)
</dt> </dl>

 

 





