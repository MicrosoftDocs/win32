---
title: Action object
description: Scripting object that provides the common properties that are inherited by all action objects.
ms.assetid: 9d6fe5e3-1ece-47ea-a644-8cae0419324f
keywords:
- Action object Task Scheduler
- Action object Task Scheduler , described
topic_type:
- apiref
api_name:
- Action
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Action object

Scripting object that provides the common properties that are inherited by all action objects. An action object is created by the [**ActionCollection.Create**](actioncollection-create.md) method.

## Members

The **Action** object has these types of members:

-   [Properties](#properties)

### Properties

The **Action** object has these properties.



| Property                               | Access type           | Description                                           |
|:---------------------------------------|:----------------------|:------------------------------------------------------|
| [**Id**](action-id.md)<br/>     | Read/write<br/> | Gets or sets the identifier of the action.<br/> |
| [**Type**](action-type.md)<br/> | Read-only<br/>  | Gets the type of the action.<br/>               |



 

## Remarks

For information on how actions and tasks work together, see [Task Actions](task-actions.md). The following table contains the scripting objects that represent the actions that can be performed:



| API                                            | Description                                                  |
|------------------------------------------------|--------------------------------------------------------------|
| [**ComHandlerAction**](comhandleraction.md)   | Represents an action that fires a handler.                   |
| [**ExecAction**](execaction.md)               | Represents an action that executes a command-line operation. |
| [**EmailAction**](emailaction.md)             | Represents an action that sends an email message.            |
| [**ShowMessageAction**](showmessageaction.md) | Represents an action that shows a message box.               |



 

When reading or writing XML, the actions of a task are specified in the [**Actions**](taskschedulerschema-actions-tasktype-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md) , [Event Trigger Example (Scripting)](https://www.bing.com/search?q=Event+Trigger+Example+(Scripting)), [Daily Trigger Example (Scripting)](daily-trigger-example--scripting-.md), [Registration Trigger Example (Scripting)](registration-trigger-example--scripting-.md), [Weekly Trigger Example (Scripting)](weekly-trigger-example--scripting-.md), [Logon Trigger Example (Scripting)](logon-trigger-example--scripting-.md), or [Boot Trigger Example (Scripting)](boot-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler Scripting Objects](task-scheduler-objects.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





