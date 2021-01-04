---
title: TaskDefinition object
description: Scripting object that defines all the components of a task, such as the task settings, triggers, actions, and registration information.
ms.assetid: 'd5887024-21af-40cf-a97d-f695f60394d9'
keywords:
- TaskDefinition object Task Scheduler
- TaskDefinition object Task Scheduler , described
topic_type:
- apiref
api_name:
- TaskDefinition
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskDefinition object

Scripting object that defines all the components of a task, such as the task settings, triggers, actions, and registration information.

## Members

The **TaskDefinition** object has these types of members:

-   [Properties](#properties)

### Properties

The **TaskDefinition** object has these properties.



| Property                                                               | Access type           | Description                                                                                                                                                                             |
|:-----------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Actions**](taskdefinition-actions.md)<br/>                   | Read/write<br/> | Gets or sets a collection of actions that are performed by the task.<br/>                                                                                                         |
| [**Data**](taskdefinition-data.md)<br/>                         | Read/write<br/> | Gets or sets the data that is associated with the task. This data is ignored by the Task Scheduler service, but is used by third-parties who wish to extend the task format.<br/> |
| [**Principal**](taskdefinition-principal.md)<br/>               | Read/write<br/> | Gets or sets the principal for the task that provides the security credentials for the task.<br/>                                                                                 |
| [**RegistrationInfo**](taskdefinition-registrationinfo.md)<br/> | Read/write<br/> | Gets or sets the registration information that is used to describe a task, such as the description of the task, the author of the task, and the date the task is registered.<br/> |
| [**Settings**](taskdefinition-settings.md)<br/>                 | Read/write<br/> | Gets or sets the settings that define how the Task Scheduler service performs the task.<br/>                                                                                      |
| [**Triggers**](taskdefinition-triggers.md)<br/>                 | Read/write<br/> | Gets or sets a collection of triggers that are used to start a task.<br/>                                                                                                         |
| [**XmlText**](taskdefinition-xmltext.md)<br/>                   | Read/write<br/> | Gets or sets the XML-formatted definition of the task.<br/>                                                                                                                       |



 

## Remarks

When reading or writing your own XML for a task, a task definition is specified using the [**Task**](taskschedulerschema-task-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md) , [Event Trigger Example (Scripting)](https://www.bing.com/search?q=Event+Trigger+Example+(Scripting)), [Daily Trigger Example (Scripting)](daily-trigger-example--scripting-.md), [Registration Trigger Example (Scripting)](registration-trigger-example--scripting-.md), [Weekly Trigger Example (Scripting)](weekly-trigger-example--scripting-.md), [Logon Trigger Example (Scripting)](logon-trigger-example--scripting-.md), or [Boot Trigger Example (Scripting)](boot-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





