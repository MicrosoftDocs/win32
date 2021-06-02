---
title: Actions (taskType) Element
description: Contains the actions performed by the task.
ms.assetid: 0a48fbd6-8a6f-4bad-9b28-0631dce15748
keywords:
- Actions (taskType) element Task Scheduler
- actions Task Scheduler , XML
- Actions element Task Scheduler
topic_type:
- apiref
api_name:
- Actions
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Actions (taskType) Element

Contains the actions performed by the task.

``` syntax
<xs:element name="Actions"
    type="actionsType"
 />
```

The **Actions** element is defined by the [**taskType**](taskschedulerschema-tasktype-complextype.md) complex type.

## Parent element



| Element                                          | Derived from                                                 | Description                                                                    |
|--------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**Task**](taskschedulerschema-task-element.md) | [**taskType**](taskschedulerschema-tasktype-complextype.md) | Describes the task that is performed by the Task Scheduler service.<br/> |



## Child elements



| Element                                                                    | Type                                                                       | Description                                                            |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**ComHandler**](taskschedulerschema-comhandler-actiongroup-element.md)   | [**comHandlerType**](taskschedulerschema-comhandlertype-complextype.md)   | Specifies an action that fires a handler.<br/>                   |
| [**Exec**](taskschedulerschema-exec-actiongroup-element.md)               | [**execType**](taskschedulerschema-exectype-complextype.md)               | Specifies an action that executes a command-line operation.<br/> |
| [**SendEmail**](taskschedulerschema-sendemail-actiongroup-element.md)     | [**sendEmailType**](taskschedulerschema-sendemailtype-complextype.md)     | Specifies an action that sends an email message.<br/>            |
| [**ShowMessage**](taskschedulerschema-showmessage-actiongroup-element.md) | [**showMessageType**](taskschedulerschema-showmessagetype-complextype.md) | Specifies an action that shows a message box.<br/>               |



## Attributes



| Name    | Type | Description                                                                                          |
|---------|------|------------------------------------------------------------------------------------------------------|
| Context |      | Principal identifier of the user who is the security context for the actions of the task.<br/> |



## Remarks

The child elements listed previously (maximum 32) are defined by the [**actionGroup**](taskschedulerschema-actiongroup-group.md) group. These elements can be added in any order.

For C++ development, the actions of a task are defined in the [**IActionCollection**](/windows/desktop/api/taskschd/nn-taskschd-iactioncollection) interface.

For script development, the actions of a task are defined in the [**ActionCollection**](actioncollection.md) object.

## Examples

For more information and a complete example of the XML for a task that contains a single execution action, see [Time Trigger Example (XML)](time-trigger-example--xml-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**taskType**](taskschedulerschema-tasktype-complextype.md)
</dt> <dt>

[**actionGroup**](taskschedulerschema-actiongroup-group.md)
</dt> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





