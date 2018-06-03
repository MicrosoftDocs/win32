---
title: MSFT\_FSRMFMJNotificationAction class
description: Represents a new file management job notification action.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 17ddc76c-1aba-4eaf-aab0-034933c6052e
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMFMJNotificationAction class File Server Resource Manager
- MSFT_FSRMFMJNotificationAction class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMFMJNotificationAction
- MSFT_FSRMFMJNotificationAction.Type
- MSFT_FSRMFMJNotificationAction.MailTo
- MSFT_FSRMFMJNotificationAction.MailCC
- MSFT_FSRMFMJNotificationAction.MailBCC
- MSFT_FSRMFMJNotificationAction.Subject
- MSFT_FSRMFMJNotificationAction.Body
- MSFT_FSRMFMJNotificationAction.AttachmentFileListSize
- MSFT_FSRMFMJNotificationAction.EventType
- MSFT_FSRMFMJNotificationAction.Command
- MSFT_FSRMFMJNotificationAction.WorkingDirectory
- MSFT_FSRMFMJNotificationAction.CommandParameters
- MSFT_FSRMFMJNotificationAction.SecurityLevel
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMFMJNotificationAction class

Represents a new file management job notification action.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMFMJNotificationAction
{
  uint32 Type;
  string MailTo = "";
  string MailCC = "";
  string MailBCC = "";
  string Subject = "";
  string Body = "";
  uint32 AttachmentFileListSize = 0;
  uint32 EventType;
  string Command;
  string WorkingDirectory = "";
  string CommandParameters = "";
  uint32 SecurityLevel = 22;
};
```

## Members

The **MSFT\_FSRMFMJNotificationAction** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMFMJNotificationAction** class has these methods.



| Method                                                                                            | Description                                                            |
|:--------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**CreateFMJNotificationAction**](msft-fsrmfmjnotificationaction-createfmjnotificationaction.md) | Creates a new **MSFT\_FSRMFMJNotificationAction** instance.<br/> |



 

### Properties

The **MSFT\_FSRMFMJNotificationAction** class has these properties.

<dl> <dt>

**AttachmentFileListSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of files to include as an attachment to the sent email. When the value is 0, no list is attached. The default value is 0. See the [**AttachmentFileListSize**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactionemail2-get_attachmentfilelistsize) property of the [**IFsrmActionEmail2**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactionemail2) interface.

</dd> <dt>

**Body**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The subject of the email. This property is used if the **Type** property is 1 (Event) or 2 (Email) and is limited to 10KB. The default value is an empty string. See the [**MessageText**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactionemail-get_messagetext) property of the [**IFsrmActionEmail**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactionemail) interface.

</dd> <dt>

**Command**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The full path to the executable program or script to run. The length must not exceed the value of **MAX\_PATH** (260). This property is used if the **Type** property is 3 (Command.) See the [**ExecutablePath**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactioncommand-get_executablepath) property of [**IFsrmActionCommand**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactioncommand).

</dd> <dt>

**CommandParameters**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The parameters for the executable program or script to be run. The maximum length of the string is 10KB. This property is used if the **Type** property is 3 (Command.) See the [**Arguments**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactioncommand-get_arguments) property of [**IFsrmActionCommand**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactioncommand).

</dd> <dt>

**EventType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The event type of the action. This property is used if the **Type** property is 1 (Event.) See the [**FsrmEventType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmeventtype) enumeration.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

The event type is unknown.

</dd> <dt>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>**Information** (1)


</dt> <dd>

The event type is informational.

</dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>**Warning** (2)


</dt> <dd>

The event type is a warning.

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (3)


</dt> <dd>

The event type is an error.

</dd> </dl>

</dd> <dt>

**MailBCC**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A semicolon-separated list of email addresses that are to be on the BCC line of the mail. "\[Admin Email\]" and "\[File Owner\]" are acceptable email addresses. This property is used if the **Type** property is 2 (Email). The default value is an empty string. See the [**MailBcc**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactionemail-get_mailbcc) property of the [**IFsrmActionEmail**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactionemail) interface.

</dd> <dt>

**MailCC**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A semicolon-separated list of email addresses that are to be on the CC line of the mail. "\[Admin Email\]" and "\[File Owner\]" are acceptable email addresses. This property is used if the **Type** property is 2 (Email). The default value is an empty string. See the [**MailCc**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactionemail-get_mailcc) property of the [**IFsrmActionEmail**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactionemail) interface.

</dd> <dt>

**MailTo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A semicolon-separated list of email addresses that are to be on the To: line of the mail. "\[Admin Email\]" and "\[File Owner\]" are acceptable email addresses. This property is used if the **Type** property is 2 (Email). The default value is an empty string. See the [**MailTo**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactionemail-get_mailto) property of the [**IFsrmActionEmail**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactionemail) interface.

</dd> <dt>

**SecurityLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The account under which the executable program or script will be run. The default value is 2 (LocalService). This property is used if the **Type** property is 3 (Command.) See the [**FsrmAccountType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmaccounttype) enumeration.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

The security level is not specified.

</dd> <dt>

<span id="NetworkService"></span><span id="networkservice"></span><span id="NETWORKSERVICE"></span>

<span id="NetworkService"></span><span id="networkservice"></span><span id="NETWORKSERVICE"></span>**NetworkService** (1)


</dt> <dd>

The action is run in the context of the [NetworkService Account](https://msdn.microsoft.com/library/windows/desktop/ms684272).

</dd> <dt>

<span id="LocalService"></span><span id="localservice"></span><span id="LOCALSERVICE"></span>

<span id="LocalService"></span><span id="localservice"></span><span id="LOCALSERVICE"></span>**LocalService** (2)


</dt> <dd>

The action is run in the context of the [LocalService Account](https://msdn.microsoft.com/library/windows/desktop/ms684188).

</dd> <dt>

<span id="LocalSystem"></span><span id="localsystem"></span><span id="LOCALSYSTEM"></span>

<span id="LocalSystem"></span><span id="localsystem"></span><span id="LOCALSYSTEM"></span>**LocalSystem** (3)


</dt> <dd>

The action is run in the context of the [LocalSystem Account](https://msdn.microsoft.com/library/windows/desktop/ms684190).

</dd> </dl>

</dd> <dt>

**Subject**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The subject of the email. This property is used if the **Type** property is 1 (Event) or 2 (Email) and is limited to 1KB. The default value is an empty string. See the [**MailSubject**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactionemail-get_mailsubject) property of the [**IFsrmActionEmail**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactionemail) interface.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Represents the type of the action, which determines the action that is taken in response to a quota or file screen event. See the [**FsrmActionType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmactiontype) enumeration.

<dt>

<span id="Event"></span><span id="event"></span><span id="EVENT"></span>

<span id="Event"></span><span id="event"></span><span id="EVENT"></span>**Event** (1)


</dt> <dd>

The Action is an event logged to the Application event log.

</dd> <dt>

<span id="Email"></span><span id="email"></span><span id="EMAIL"></span>

<span id="Email"></span><span id="email"></span><span id="EMAIL"></span>**Email** (2)


</dt> <dd>

The Action is an email.

</dd> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>**Command** (3)


</dt> <dd>

The Action is to run a command or script.

</dd> </dl>

</dd> <dt>

**WorkingDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional string representing a valid path to a folder. Remote paths are not supported. The length must not **MAX\_PATH** (260). The default value is an empty string. This property is used if the **Type** property is 3 (Command.) See the [**WorkingDirectory**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactioncommand-get_workingdirectory) property of [**IFsrmActionCommand**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactioncommand).

</dd> </dl>

## Remarks

Not all action types support every property in the class. The table below indicates which properties in this class are supported by each action type in the **Type** property.



| Property/Type              | Event (1) | Email (2) | Command (3) |
|----------------------------|-----------|-----------|-------------|
| **MailTo**                 | Yes       | No        | No          |
| **MailCC**                 | Yes       | No        | No          |
| **MailBCC**                | Yes       | No        | No          |
| **Subject**                | Yes       | No        | No          |
| **Body**                   | Yes       | Yes       | No          |
| **AttachmentFileListSize** | Yes       | No        | No          |
| **EventType**              | No        | Yes       | No          |
| **Command**                | No        | No        | Yes         |
| **WorkingDirectory**       | No        | No        | Yes         |
| **CommandParameters**      | No        | No        | Yes         |
| **SecurityLevel**          | No        | No        | Yes         |



 

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> </dl>

 

 





