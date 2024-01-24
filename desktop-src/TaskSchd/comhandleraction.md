---
title: ComHandlerAction object
description: Scripting object that represents an action that fires a handler.
ms.assetid: 47ffe52f-b7b7-4486-a00d-6105395f23c0
keywords:
- COM handler action Task Scheduler , object
- ComHandlerAction object Task Scheduler
- ComHandlerAction object Task Scheduler , described
topic_type:
- apiref
api_name:
- ComHandlerAction
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ComHandlerAction object

Scripting object that represents an action that fires a handler.

## Members

The **ComHandlerAction** object has these types of members:

-   [Properties](#properties)

### Properties

The **ComHandlerAction** object has these properties.



| Property                                               | Access type           | Description                                                                                               |
|:-------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------|
| [**ClassId**](comhandleraction-classid.md)<br/> | Read/write<br/> | Gets or sets the identifier of the handler class.<br/>                                              |
| [**Data**](comhandleraction-data.md)<br/>       | Read/write<br/> | Gets or sets additional data that is associated with the handler.<br/>                              |
| [**Id**](action-id.md)<br/>                     | Read/write<br/> | Inherited from the [**Action**](action.md) object. Gets or sets the identifier of the action.<br/> |
| [**Type**](action-type.md)<br/>                 | Read-only<br/>  | Inherited from the [**Action**](action.md) object. Gets the type of the action.<br/>               |



 

## Remarks

COM handlers must implement the [**ITaskHandler**](/windows/desktop/api/taskschd/nn-taskschd-itaskhandler) interface for the Task Scheduler to start and stop the handler. In turn, the COM handler uses the methods of the [**TaskHandlerStatus**](/windows/desktop/api/taskschd/nn-taskschd-itaskhandlerstatus) object to communicate the status back to the Task Scheduler.

When reading or writing XML, a COM handler action is specified in the [**ComHandler**](taskschedulerschema-comhandler-actiongroup-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TaskHandlerStatus**](/windows/desktop/api/taskschd/nn-taskschd-itaskhandlerstatus)
</dt> <dt>

[Task Scheduler Objects](task-scheduler-objects.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





