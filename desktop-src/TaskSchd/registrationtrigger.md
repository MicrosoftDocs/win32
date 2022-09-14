---
title: RegistrationTrigger object
description: Scripting object that represents a trigger that starts a task when the task is registered or updated.
ms.assetid: '430ef3e0-9409-49ff-8ffb-31833938d8b2'
keywords:
- registration trigger Task Scheduler , object
- RegistrationTrigger object Task Scheduler
- RegistrationTrigger object Task Scheduler , described
topic_type:
- apiref
api_name:
- RegistrationTrigger
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegistrationTrigger object

Scripting object that represents a trigger that starts a task when the task is registered or updated.

## Members

The **RegistrationTrigger** object has these types of members:

-   [Properties](#properties)

### Properties

The **RegistrationTrigger** object has these properties.



| Property                                                            | Access type           | Description                                                                                                                                                                                 |
|:--------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Delay**](registrationtrigger-delay.md)<br/>               | Read/write<br/> | Gets or sets the amount of time between when the task is registered and when the task is started.<br/>                                                                                |
| [**Enabled**](trigger-enabled.md)<br/>                       | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets a Boolean value that indicates whether the trigger is enabled.<br/>                                                |
| [**EndBoundary**](trigger-endboundary.md)<br/>               | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/> |
| [**ExecutionTimeLimit**](trigger-executiontimelimit.md)<br/> | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the maximum amount of time that the task launched by the trigger is allowed to run.<br/>                           |
| [**Id**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_id)<br/>                                | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the identifier for the trigger.<br/>                                                                               |
| [**Repetition**](trigger-repetition.md)<br/>                 | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets how often the task is run and how long the repetition pattern is repeated after the task is started.<br/>          |
| [**StartBoundary**](trigger-startboundary.md)<br/>           | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is activated.<br/>                                                              |
| [**Type**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_type)<br/>                            | Read-only<br/>  | Inherited from the [**Trigger**](trigger.md) object. Gets the type of the trigger.<br/>                                                                                              |



 

## Remarks

When creating your own XML for a task, a registration trigger is specified using the [**RegistrationTrigger**](taskschedulerschema-registrationtrigger-triggergroup-element.md) element of the Task Scheduler schema.

If a task with a delayed registration trigger is registered, and the computer that the task is registered on is shutdown or restarted during the delay, before the task runs, then the task will not run and the delay will be lost.

## Examples

For more information and a code example for this scripting object, see [Registration Trigger Example (Scripting)](registration-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**Trigger**](trigger.md)
</dt> <dt>

[**TriggerCollection**](triggercollection.md)
</dt> <dt>

[**TriggerCollection.Create**](triggercollection-create.md)
</dt> </dl>

 

 





