---
title: LogonTrigger object
description: Scripting object that represents a trigger that starts a task when a user logs on.
ms.assetid: '1a1c10ce-4273-490a-a732-a8d39773203b'
keywords:
- logon trigger Task Scheduler , object
- LogonTrigger object Task Scheduler
- LogonTrigger object Task Scheduler , described
topic_type:
- apiref
api_name:
- LogonTrigger
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# LogonTrigger object

Scripting object that represents a trigger that starts a task when a user logs on. When the Task Scheduler service starts, all logged-on users are enumerated and any tasks registered with logon triggers that match the logged on user are run.

## Members

The **LogonTrigger** object has these types of members:

-   [Properties](#properties)

### Properties

The **LogonTrigger** object has these properties.



| Property                                                            | Access type           | Description                                                                                                                                                                                               |
|:--------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Delay**](logontrigger-delay.md)<br/>                      | Read/write<br/> | Gets or sets a value that indicates the amount of time between when the user logs on and when the job is started.<br/>                                                                              |
| [**Enabled**](trigger-enabled.md)<br/>                       | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets a Boolean value that indicates whether the trigger is enabled.<br/>                                                              |
| [**EndBoundary**](trigger-endboundary.md)<br/>               | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/>               |
| [**ExecutionTimeLimit**](trigger-executiontimelimit.md)<br/> | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the maximum amount of time that the task launched by the trigger is allowed to run.<br/>                                         |
| [**Id**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_id)<br/>                                | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the identifier for the trigger.<br/>                                                                                             |
| [**Repetition**](trigger-repetition.md)<br/>                 | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets a value that indicates how often the task is run and how long the repetition pattern is repeated after the task is started.<br/> |
| [**StartBoundary**](trigger-startboundary.md)<br/>           | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is activated.<br/>                                                                            |
| [**Type**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_type)<br/>                            | Read-only<br/>  | Inherited from the [**Trigger**](trigger.md) object. Gets the type of the trigger.<br/>                                                                                                            |
| [**UserId**](logontrigger-userid.md)<br/>                    | Read/write<br/> | Gets or sets the identifier of the user.<br/>                                                                                                                                                       |



 

## Remarks

If you want a task to be triggered when any member of a group logs on to the computer rather than when a specific user logs on, then do not assign a value to the [**LogonTrigger.UserId**](logontrigger-userid.md) property. Instead, create a logon trigger with an empty **LogonTrigger.UserId** property and assign a value to the principal for the task using the [**Principal.GroupId**](principal-groupid.md) property.

When reading or writing XML for a task, a logon trigger is specified using the [**LogonTrigger**](taskschedulerschema-logontrigger-triggergroup-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this scripting object, see [Logon Trigger Example (Scripting)](logon-trigger-example--scripting-.md).

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
</dt> </dl>

 

 





