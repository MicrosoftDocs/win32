---
title: SessionStateChangeTrigger object
description: Scripting object that triggers tasks for console connect or disconnect, remote connect or disconnect, or workstation lock or unlock notifications.
ms.assetid: '0bf56d67-6c44-4978-93a9-7b525f2bf140'
keywords: ["SessionStateChangeTrigger object Task Scheduler", "SessionStateChangeTrigger object Task Scheduler , described"]
topic_type:
- apiref
api_name:
- SessionStateChangeTrigger
api_location:
- taskschd.dll
api_type:
- COM
---

# SessionStateChangeTrigger object

Scripting object that triggers tasks for console connect or disconnect, remote connect or disconnect, or workstation lock or unlock notifications.

## Members

The **SessionStateChangeTrigger** object has these types of members:

-   [Properties](#properties)

### Properties

The **SessionStateChangeTrigger** object has these properties.



| Property                                                                | Access type           | Description                                                                                                                                                                                               |
|:------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Delay**](sessionstatechangetrigger-delay.md)<br/>             | Read/write<br/> | Gets or sets a value that indicates how long of a delay takes place before a task is started after a Terminal Server session state change is detected.<br/>                                         |
| [**Enabled**](itrigger-enabled.md)<br/>                          | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets a Boolean value that indicates whether the trigger is enabled.<br/>                                                              |
| [**EndBoundary**](itrigger-endboundary.md)<br/>                  | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/>               |
| [**ExecutionTimeLimit**](itrigger-executiontimelimit.md)<br/>    | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the maximum amount of time in which the task can be started by the trigger.<br/>                                                 |
| [**Id**](itrigger-id.md)<br/>                                    | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the identifier for the trigger.<br/>                                                                                             |
| [**Repetition**](itrigger-repetition.md)<br/>                    | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets a value that indicates how often the task is run and how long the repetition pattern is repeated after the task is started.<br/> |
| [**StartBoundary**](itrigger-startboundary.md)<br/>              | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is activated.<br/>                                                                            |
| [**StateChange**](sessionstatechangetrigger-statechange.md)<br/> | Read/write<br/> | Gets or sets the kind of Terminal Server session change that would trigger a task launch.<br/>                                                                                                      |
| [**Type**](itrigger-type.md)<br/>                                | Read-only<br/>  | Inherited from the [**Trigger**](trigger.md) object. Gets the type of the trigger.<br/>                                                                                                            |
| [**UserId**](sessionstatechangetrigger-userid.md)<br/>           | Read/write<br/> | Gets or sets the user for the Terminal Server session. When a session state change is detected for this user, a task is started.<br/>                                                               |



 

## Remarks

When reading or writing your own XML for a task, a session state change trigger is specified using the [**SessionStateChangeTrigger**](taskschedulerschema-sessionstatechangetrigger-triggergroup-element.md) element of the Task Scheduler schema.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TriggerCollection**](triggercollection.md)
</dt> <dt>

[**TriggerCollection.Create**](triggercollection-create.md)
</dt> </dl>

 

 





