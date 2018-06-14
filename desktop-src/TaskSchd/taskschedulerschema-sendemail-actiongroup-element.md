---
title: SendEmail (actionGroup) Element
description: Represents an action that sends an email message.
ms.assetid: 83416b02-8327-47b3-9dfc-1bf5b9365728
keywords:
- SendEmail element Task Scheduler
topic_type:
- apiref
api_name:
- SendEmail
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SendEmail (actionGroup) Element

Represents an action that sends an email message.

``` syntax
<xs:element name="SendEmail"
    type="sendEmailType"
 />
```

The **SendEmail** element is defined by the [**actionGroup**](taskschedulerschema-actiongroup-group.md) .

## Parent element



| Element                                                         | Derived from                                                       | Description                                            |
|-----------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------|
| [**Actions**](taskschedulerschema-actions-tasktype-element.md) | [**actionsType**](taskschedulerschema-actionstype-complextype.md) | Contains the actions performed by the task.<br/> |



## Child elements



| Element                                                                        | Type                                                                         | Description                                                                                      |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**Attachments**](taskschedulerschema-attachments-sendemailtype-element.md)   | [**attachmentsType**](taskschedulerschema-attachmentstype-complextype.md)   | Specifies a list of attachments in the email message.<br/>                                 |
| [**Bcc**](taskschedulerschema-bcc-sendemailtype-element.md)                   | **string**                                                                   | Specifies the email addresses used on the Bcc line of an email message.<br/>               |
| [**Body**](taskschedulerschema-body-sendemailtype-element.md)                 | **string**                                                                   | Specifies the text in the body of the email message.<br/>                                  |
| [**Cc**](taskschedulerschema-cc-sendemailtype-element.md)                     | **string**                                                                   | Specifies the email addresses used on the Cc line of an email message.<br/>                |
| [**From**](taskschedulerschema-from-sendemailtype-element.md)                 | **string**                                                                   | Specifies the email address of the sender.<br/>                                            |
| [**HeaderFields**](taskschedulerschema-headerfields-sendemailtype-element.md) | [**headerFieldsType**](taskschedulerschema-headerfieldstype-complextype.md) | Specifies the header fields and their values used in the header of the email message.<br/> |
| [**ReplyTo**](taskschedulerschema-replyto-sendemailtype-element.md)           | **string**                                                                   | Specifies the email addresses that are replied to in the email message.<br/>               |
| [**Server**](taskschedulerschema-server-sendemailtype-element.md)             | [**nonEmptyString**](taskschedulerschema-nonemptystring-simpletype.md)      | Specifies the email server used to send the email message. <br/>                           |
| [**Subject**](taskschedulerschema-subject-sendemailtype-element.md)           | **string**                                                                   | Specifies the subject of the email message.<br/>                                           |
| [**To**](taskschedulerschema-to-sendemailtype-element.md)                     | **string**                                                                   | Specifies the email addresses to which the email will be sent.<br/>                        |



## Remarks

For C++ development, see the [**IEmailAction**](/windows/desktop/api/taskschd/nn-taskschd-iemailaction) interface.

For script development, see the [**EmailAction**](emailaction.md) object.

**Windows 8 and Windows Server 2012:** This element has been removed. Please use IExecAction with the powershell [**Send-MailMessage**](https://msdn.microsoft.com/en-us/library/Hh849925(v=WPS.620).aspx) cmdlet as a workaround.

## Examples

For a complete example of the XML for a task that specifies an email action, see [Event Trigger Example (XML)](https://www.bing.com/search?q=Event+Trigger+Example+(XML)).

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows 7<br/>                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                    |



 

 





