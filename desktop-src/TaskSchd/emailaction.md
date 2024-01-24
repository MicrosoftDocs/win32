---
title: EmailAction object
description: Scripting object that represents an action that sends an email message.
ms.assetid: edc0dc4d-eda0-47e0-981f-8521ac4678eb
keywords:
- EmailAction object Task Scheduler
- EmailAction object Task Scheduler , described
topic_type:
- apiref
api_name:
- EmailAction
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EmailAction object

\[This object is no longer supported. Please use IExecAction with the powershell [**Send-MailMessage**](/powershell/module/microsoft.powershell.utility/send-mailmessage) cmdlet as a workaround.\]

Scripting object that represents an action that sends an email message.

## Members

The **EmailAction** object has these types of members:

-   [Properties](#properties)

### Properties

The **EmailAction** object has these properties.



| Property                                                    | Access type           | Description                                                                                               |
|:------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------|
| [**Attachments**](emailaction-attachments.md)<br/>   | Read/write<br/> | Gets or sets an array of attachments that is sent with the email message.<br/>                      |
| [**Bcc**](emailaction-bcc.md)<br/>                   | Read/write<br/> | Gets or sets the email address or addresses that you want to Bcc in the email message.<br/>         |
| [**Body**](emailaction-body.md)<br/>                 | Read/write<br/> | Gets or sets the body of the email that contains the email message.<br/>                            |
| [**Cc**](emailaction-cc.md)<br/>                     | Read/write<br/> | Gets or sets the email address or addresses that you want to Cc in the email message.<br/>          |
| [**From**](emailaction-from.md)<br/>                 | Read/write<br/> | Gets or sets the email address that you want to send the email from.<br/>                           |
| [**HeaderFields**](emailaction-headerfields.md)<br/> | Read/write<br/> | Gets or sets the header information in the email that you want to send.<br/>                        |
| [**Id**](action-id.md)<br/>                          | Read/write<br/> | Inherited from the [**Action**](action.md) object. Gets or sets the identifier of the action.<br/> |
| [**ReplyTo**](emailaction-replyto.md)<br/>           | Read/write<br/> | Gets or sets the email address that you want to reply to.<br/>                                      |
| [**Server**](emailaction-server.md)<br/>             | Read/write<br/> | Gets or sets the name of the server that you use to send email from.<br/>                           |
| [**Subject**](emailaction-subject.md)<br/>           | Read/write<br/> | Gets or sets the subject of the email message.<br/>                                                 |
| [**To**](emailaction-to.md)<br/>                     | Read/write<br/> | Gets or sets the email address or addresses that you want to send the email to.<br/>                |
| [**Type**](/windows/win32/api/taskschd/nf-taskschd-iaction-get_type)<br/>                     | Read-only<br/>  | Inherited from [**Action**](action.md) object. Gets the type of the action.<br/>                   |



 

## Remarks

The email action must have a valid value for the [**Server**](emailaction-server.md), [**From**](emailaction-from.md), and [**To**](emailaction-to.md) or [**Cc**](emailaction-cc.md) properties for the task to register and run correctly.

When reading or writing your own XML for a task, an email action is specified using the [**SendEmail**](taskschedulerschema-sendemail-actiongroup-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this scripting object, see [Event Trigger Example (Scripting)](/previous-versions//aa446887(v=vs.85)).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows 7<br/>                                                                    |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                       |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

