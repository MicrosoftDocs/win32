---
title: ShowMessageAction object
description: For scripting, represents an action that shows a message box when a task is activated.
ms.assetid: 'fdd22eef-965c-4a81-954c-66011c435ab9'
keywords:
- ShowMessageAction object Task Scheduler
- ShowMessageAction object Task Scheduler , described
topic_type:
- apiref
api_name:
- ShowMessageAction
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ShowMessageAction object

\[This object is no longer supported. You can use IExecAction with the Windows scripting [**MsgBox function**](/previous-versions/sfw6660x(v=vs.80)) to show a message in the user session.\]

For scripting, represents an action that shows a message box when a task is activated.

## Members

The **ShowMessageAction** object has these types of members:

-   [Properties](#properties)

### Properties

The **ShowMessageAction** object has these properties.



| Property                                                        | Access type           | Description                                                                                               |
|:----------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------|
| [**Id**](action-id.md)<br/>                              | Read/write<br/> | Inherited from the [**Action**](action.md) object. Gets or sets the identifier of the action.<br/> |
| [**MessageBody**](showmessageaction-messagebody.md)<br/> | Read/write<br/> | Gets or sets the message text that is displayed in the body of the message box.<br/>                |
| [**Title**](showmessageaction-title.md)<br/>             | Read/write<br/> | Gets or sets the title of the message box.<br/>                                                     |
| [**Type**](action-type.md)<br/>                          | Read-only<br/>  | Inherited from the [**Action**](action.md) object. Gets the type of the action.<br/>               |



 

## Remarks

For a task, that contains a message box action, the message box will be displayed if the task is activated and the task has an interactive logon type. To set the task logon type to interactive, specify 3 (**TASK\_LOGON\_INTERACTIVE\_TOKEN**) or 4 (**TASK\_LOGON\_GROUP**) in the [**LogonType**](principal-logontype.md) property of the task principal, or in the *logonType* parameter of [**TaskFolder.RegisterTask**](taskfolder-registertask.md) or [**TaskFolder.RegisterTaskDefinition**](taskfolder-registertaskdefinition.md).

When reading or writing your own XML for a task, a message box action is specified using the [**ShowMessage**](taskschedulerschema-showmessage-actiongroup-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this scripting object, see [Message Box Example (Scripting)](/previous-versions//aa381916(v=vs.85)).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows 7<br/>                                                                    |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                       |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

