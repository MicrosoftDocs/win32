---
title: CreateFMJNotificationAction method of the MSFT\_FSRMFMJNotificationAction class
description: Creates a new instance of the MSFT\_FSRMFMJNotificationAction class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ea4745a3-dd27-4aa7-b3c6-964683dec1e2'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["CreateFMJNotificationAction method File Server Resource Manager", "CreateFMJNotificationAction method File Server Resource Manager , MSFT_FSRMFMJNotificationAction class", "MSFT_FSRMFMJNotificationAction class File Server Resource Manager , CreateFMJNotificationAction method"]
topic_type:
- apiref
api_name:
- MSFT_FSRMFMJNotificationAction.CreateFMJNotificationAction
api_location:
- SrmSvc.dll
api_type:
- COM
---

# CreateFMJNotificationAction method of the MSFT\_FSRMFMJNotificationAction class

Creates a new instance of the [**MSFT\_FSRMFMJNotificationAction**](msft-fsrmfmjnotificationaction.md) class.

## Syntax


```mof
uint64 CreateFMJNotificationAction(
  [in]  uint32                         Type,
  [in]  string                         MailTo = "",
  [in]  string                         MailCC = "",
  [in]  string                         MailBCC = "",
  [in]  string                         Subject = "",
  [in]  string                         Body = "",
  [in]  uint32                         AttachmentFileListSize = 0,
  [in]  uint32                         EventType,
  [in]  string                         Command,
  [in]  string                         WorkingDirectory = "",
  [in]  string                         CommandParameters = "",
  [in]  uint32                         SecurityLevel = LocalService,
  [out] MSFT_FSRMFMJNotificationAction NotificationAction
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

Represents the type of the action, which determines the action that is taken in response to a quota or file screen event. See the [**FsrmActionType**](fsrmactiontype.md) enumeration.

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

</dd> </dl> </dd> <dt>

*MailTo* \[in\]
</dt> <dd>

A semicolon-separated list of email addresses that are to be on the To: line of the mail. "\[Admin Email\]" and "\[File Owner\]" are acceptable email addresses. This property is used if the **Type** property is 2 (Email). The default value is an empty string. See the [**MailTo**](ifsrmactionemail-mailto.md) property of the [**IFsrmActionEmail**](ifsrmactionemail.md) interface.

</dd> <dt>

*MailCC* \[in\]
</dt> <dd>

A semicolon-separated list of email addresses that are to be on the CC line of the mail. "\[Admin Email\]" and "\[File Owner\]" are acceptable email addresses. This property is used if the **Type** property is 2 (Email). The default value is an empty string. See the [**MailCc**](ifsrmactionemail-mailcc.md) property of the [**IFsrmActionEmail**](ifsrmactionemail.md) interface.

</dd> <dt>

*MailBCC* \[in\]
</dt> <dd>

A semicolon-separated list of email addresses that are to be on the BCC line of the mail. "\[Admin Email\]" and "\[File Owner\]" are acceptable email addresses. This property is used if the **Type** property is 2 (Email). The default value is an empty string. See the [**MailBcc**](ifsrmactionemail-mailbcc.md) property of the [**IFsrmActionEmail**](ifsrmactionemail.md) interface.

</dd> <dt>

*Subject* \[in\]
</dt> <dd>

The subject of the email. This property is used if the **Type** property is 2 (Email) and is limited to 1KB. The default value is an empty string. See the [**MailSubject**](ifsrmactionemail-mailsubject.md) property of the [**IFsrmActionEmail**](ifsrmactionemail.md) interface.

</dd> <dt>

*Body* \[in\]
</dt> <dd>

The subject of the email. This property is used if the **Type** property is 1 (Event) or 2 (Email) and is limited to 10KB. The default value is an empty string. See the [**MessageText**](ifsrmactionemail-messagetext.md) property of the [**IFsrmActionEmail**](ifsrmactionemail.md) interface.

</dd> <dt>

*AttachmentFileListSize* \[in\]
</dt> <dd>

The number of files to include as an attachment to the sent email. When the value is 0, no list is attached. The default value is 0. See the [**AttachmentFileListSize**](ifsrmactionemail2-attachmentfilelistsize.md) property of the [**IFsrmActionEmail2**](ifsrmactionemail2.md) interface.

</dd> <dt>

*EventType* \[in\]
</dt> <dd>

The event type of the action. This property is used if the **Type** property is 1 (Event.) See the [**FsrmEventType**](fsrmeventtype.md) enumeration.

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

</dd> </dl> </dd> <dt>

*Command* \[in\]
</dt> <dd>

The full path to the executable program or script to run. The length must not exceed the value of **MAX\_PATH** (260). This property is used if the **Type** property is 3 (Command.) See the [**ExecutablePath**](ifsrmactioncommand-executablepath.md) property of [**IFsrmActionCommand**](ifsrmactioncommand.md).

</dd> <dt>

*WorkingDirectory* \[in\]
</dt> <dd>

An optional string representing a valid path to a folder. Remote paths are not supported. The length must not **MAX\_PATH** (260). The default value is an empty string. This property is used if the **Type** property is 3 (Command.) See the [**WorkingDirectory**](ifsrmactioncommand-workingdirectory.md) property of [**IFsrmActionCommand**](ifsrmactioncommand.md).

</dd> <dt>

*CommandParameters* \[in\]
</dt> <dd>

The parameters for the executable program or script to be run. The maximum length of the string is 10KB. This property is used if the **Type** property is 3 (Command.) See the [**Arguments**](ifsrmactioncommand-arguments.md) property of [**IFsrmActionCommand**](ifsrmactioncommand.md).

</dd> <dt>

*SecurityLevel* \[in\]
</dt> <dd>

The account under which the executable program or script will be run. The default value is 2 (LocalService). This property is used if the **Type** property is 3 (Command.) See the [**FsrmAccountType**](fsrmaccounttype.md) enumeration.

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

</dd> </dl> </dd> <dt>

*NotificationAction* \[out\]
</dt> <dd>

Returns a new [**MSFT\_FSRMFMJNotificationAction**](msft-fsrmfmjnotificationaction.md) instance.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_FSRMFMJNotificationAction**](msft-fsrmfmjnotificationaction.md)
</dt> </dl>

 

 





