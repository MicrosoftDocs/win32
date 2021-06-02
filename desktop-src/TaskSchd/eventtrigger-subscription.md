---
title: EventTrigger.Subscription property
description: For scripting, gets or sets a query string that identifies the event that fires the trigger.
ms.assetid: 31d32426-3dd7-41f9-89cc-b13767871b74
keywords:
- Subscription property Task Scheduler
- Subscription property Task Scheduler , EventTrigger object
- EventTrigger object Task Scheduler , Subscription property
topic_type:
- apiref
api_name:
- EventTrigger.Subscription
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EventTrigger.Subscription property

For scripting, gets or sets a query string that identifies the event that fires the trigger.

## Syntax


```VB
EventTrigger.Subscription As String
```



## Property value

A query string that identifies the event that fires the trigger.

## Remarks

When reading or writing your own XML for a task, the event subscription is specified using the [**Subscription**](taskschedulerschema-subscription-eventtriggertype-element.md) element of the Task Scheduler schema.

For more information about writing a query string for certain events, see [Event Selection](/previous-versions//aa385231(v=vs.85)) and [Subscribing to Events](../wes/subscribing-to-events.md).

## Examples

The following query string defines a subscription to all level 2 events in the System channel:


```XML
"<QueryList>
    <Query Id='1'>
        <Select Path='System'>*[System/Level=2]</Select>
    </Query>
</QueryList>" 
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> <dt>

[**EventTrigger**](eventtrigger.md)
</dt> </dl>

 

