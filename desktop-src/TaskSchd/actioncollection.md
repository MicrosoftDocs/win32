---
title: ActionCollection object
description: Scripting object that contains the actions performed by the task.
ms.assetid: e887680d-e7e8-4bea-8f00-fb7645d79e60
keywords:
- actions Task Scheduler , collection object
- ActionCollection object Task Scheduler
- ActionCollection object Task Scheduler , described
topic_type:
- apiref
api_name:
- ActionCollection
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActionCollection object

Scripting object that contains the actions performed by the task.

## Members

The **ActionCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ActionCollection** object has these methods.



| Method                                    | Description                                                 |
|:------------------------------------------|:------------------------------------------------------------|
| [**Clear**](actioncollection-clear.md)   | Clears all the actions from the collection.<br/>      |
| [**Create**](actioncollection-create.md) | Creates and adds a new action to the collection.<br/> |
| [**Remove**](actioncollection-remove.md) | Removes a specified action from the collection.<br/>  |



 

### Properties

The **ActionCollection** object has these properties.



| Property                                               | Access type           | Description                                                           |
|:-------------------------------------------------------|:----------------------|:----------------------------------------------------------------------|
| [**Context**](actioncollection-context.md)<br/> | Read/write<br/> | Gets or sets the identifier of the principal for the task.<br/> |
| [**Count**](actioncollection-count.md)<br/>     | Read-only<br/>  | Gets the number of actions in the collection.<br/>              |
| [**Item**](actioncollection-item.md)<br/>       | Read-only<br/>  | Gets a specified action from the collection.<br/>               |
| [**XmlText**](actioncollection-xmltext.md)<br/> | Read/write<br/> | Gets or sets an XML-formatted version of the collection.<br/>   |



 

## Remarks

When reading or writing XML, the actions of a task are specified in the [**Actions**](taskschedulerschema-actions-tasktype-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md), [Event Trigger Example (Scripting)](https://www.bing.com/search?q=Event+Trigger+Example+(Scripting)), [Daily Trigger Example (Scripting)](daily-trigger-example--scripting-.md), [Registration Trigger Example (Scripting)](registration-trigger-example--scripting-.md), [Weekly Trigger Example (Scripting)](weekly-trigger-example--scripting-.md), [Logon Trigger Example (Scripting)](logon-trigger-example--scripting-.md), or [Boot Trigger Example (Scripting)](boot-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





