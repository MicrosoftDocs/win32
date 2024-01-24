---
title: LogonTrigger.UserId property
description: For scripting, gets or sets the identifier of the user.
ms.assetid: 'd28eea9b-8238-49e7-afec-5a96281b3063'
keywords:
- UserId property Task Scheduler
- UserId property Task Scheduler , LogonTrigger object
- LogonTrigger object Task Scheduler , UserId property
topic_type:
- apiref
api_name:
- LogonTrigger.UserId
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# LogonTrigger.UserId property

For scripting, gets or sets the identifier of the user.

## Syntax


```VB
LogonTrigger.UserId As String
```



## Property value

The identifier of the user. For example, "MyDomain\\MyName" or for a local account, "Administrator".

This property can be in one of the following formats:

-   User name or SID: The task is started when the user logs on to the computer.
-   NULL: The task is started when any user logs on to the computer.

## Remarks

If you want a task to be triggered when any member of a group logs on to the computer rather than when a specific user logs on, then do not assign a value to the **LogonTrigger.UserId** property. Instead, create a logon trigger with an empty **LogonTrigger.UserId** property and assign a value to the principal for the task using the [**Principal.GroupId**](principal-groupid.md) property.

When reading or writing XML for a task, the logon user identifier is specified using the [**UserId**](taskschedulerschema-userid-logontriggertype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**LogonTrigger**](logontrigger.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





