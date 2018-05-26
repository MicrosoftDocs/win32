---
title: TriggerCollection object
description: Scripting object that is used to add to, remove from, and retrieve the triggers of a task.
ms.assetid: 5985ff67-3aa2-4ade-9d53-da4d640f5f6e
keywords:
- triggers Task Scheduler , trigger collection object
- TriggerCollection object Task Scheduler
- TriggerCollection object Task Scheduler , described
topic_type:
- apiref
api_name:
- TriggerCollection
api_location:
- taskschd.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TriggerCollection object

Scripting object that is used to add to, remove from, and retrieve the triggers of a task.

## Members

The **TriggerCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **TriggerCollection** object has these methods.



| Method                                     | Description                                                                                |
|:-------------------------------------------|:-------------------------------------------------------------------------------------------|
| [**Clear**](triggercollection-clear.md)   | Clears all triggers from the collection.<br/>                                        |
| [**Create**](triggercollection-create.md) | Creates a new trigger for the task.<br/>                                             |
| [**Remove**](triggercollection-remove.md) | Removes the specified trigger from the collection of triggers used by the task.<br/> |



 

### Properties

The **TriggerCollection** object has these properties.



| Property                                            | Access type          | Description                                                |
|:----------------------------------------------------|:---------------------|:-----------------------------------------------------------|
| [**Count**](triggercollection-count.md)<br/> | Read-only<br/> | Gets the number of triggers in the collection.<br/>  |
| [**Item**](triggercollection-item.md)<br/>   | Read-only<br/> | Gets the specified trigger from the collection.<br/> |



 

## Remarks

When reading or writing XML for a task, the triggers for the task are specified in the [**Triggers**](taskschedulerschema-triggers-tasktype-element.md) element of the Task Scheduler schema.

For information about each trigger type see [Trigger Types](trigger-types.md).

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md).

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>Windows.ui.xaml.h</dt> </dl> |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl>      |



## See also

<dl> <dt>

[**Trigger**](trigger.md)
</dt> </dl>

 

 





