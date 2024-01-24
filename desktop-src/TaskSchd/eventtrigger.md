---
title: EventTrigger object (Windows.ui.xaml.h)
description: Scripting object that represents a trigger that starts a task when a system event occurs.
ms.assetid: 79cb6591-0919-441f-ad7f-4eb7cf0f9591
keywords:
- event trigger Task Scheduler , object
- EventTrigger object Task Scheduler
- EventTrigger object Task Scheduler , described
topic_type:
- apiref
api_name:
- EventTrigger
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EventTrigger object

Scripting object that represents a trigger that starts a task when a system event occurs.

## Members

The **EventTrigger** object has these types of members:

-   [Properties](#properties)

### Properties

The **EventTrigger** object has these properties.



| Property                                                            | Access type           | Description                                                                                                                                                                                                                                                                                                                                                                              |
|:--------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Delay**](eventtrigger-delay.md)<br/>                      | Read/write<br/> | Gets or sets a value that indicates the amount of time between when the event occurs and when the task is started.<br/>                                                                                                                                                                                                                                                            |
| [**Enabled**](trigger-enabled.md)<br/>                       | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets a Boolean value that indicates whether the trigger is enabled.<br/>                                                                                                                                                                                                                                             |
| [**EndBoundary**](trigger-endboundary.md)<br/>               | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/>                                                                                                                                                                                              |
| [**ExecutionTimeLimit**](trigger-executiontimelimit.md)<br/> | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the maximum amount of time that the task launched by this trigger is allowed to run.<br/>                                                                                                                                                                                                                       |
| [**Id**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_id)<br/>                                | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the identifier for the trigger.<br/>                                                                                                                                                                                                                                                                            |
| [**Repetition**](trigger-repetition.md)<br/>                 | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets how often the task is run and how long the repetition pattern is repeated after the task is started.<br/>                                                                                                                                                                                                       |
| [**StartBoundary**](trigger-startboundary.md)<br/>           | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is activated.<br/>                                                                                                                                                                                                                                                           |
| [**Subscription**](eventtrigger-subscription.md)<br/>        | Read/write<br/> | Gets or sets the XPath query string that identifies the event that fires the trigger.<br/>                                                                                                                                                                                                                                                                                         |
| [**Type**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_type)<br/>                            | Read-only<br/>  | Inherited from the [**Trigger**](trigger.md) object. Gets the type of the trigger.<br/>                                                                                                                                                                                                                                                                                           |
| [**ValueQueries**](eventtrigger-valuequeries.md)<br/>        | Read/write<br/> | Gets or sets a collection of named XPath queries. Each query in the collection is applied to the last matching event XML that is returned from the subscription query specified in the [**Subscription**](eventtrigger-subscription.md) property. The name of the query can be used as a variable in the message of a [**ShowMessageAction**](showmessageaction.md) action.<br/> |



 

## Remarks

A maximum of 500 tasks with event subscriptions can be created. An event subscription that queries for a variety of events can be used to trigger a task that uses the same action in response to the events being logged.

When reading or writing your own XML for a task, an event trigger is specified using the [**EventTrigger**](taskschedulerschema-eventtrigger-triggergroup-element.md) element of the Task Scheduler schema.

## Examples

For more information and a code example for this scripting object, see [Event Trigger Example (Scripting)](/previous-versions//aa446887(v=vs.85)).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>Windows.ui.xaml.h</dt> </dl> |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl>      |



## See also

<dl> <dt>

[**Trigger**](trigger.md)
</dt> <dt>

[**TriggerCollection**](triggercollection.md)
</dt> <dt>

[**TriggerCollection.Create**](triggercollection-create.md)
</dt> </dl>

 

