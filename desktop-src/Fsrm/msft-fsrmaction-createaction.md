---
title: CreateAction method of the MSFT\_FSRMAction class
description: Creates a new MSFT\_FSRMAction instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6f234d63-7cb2-4a03-b611-d0fe6f5258e5
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- CreateAction method File Server Resource Manager
- CreateAction method File Server Resource Manager , MSFT_FSRMAction class
- MSFT_FSRMAction class File Server Resource Manager , CreateAction method
topic_type:
- apiref
api_name:
- MSFT_FSRMAction.CreateAction
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateAction method of the MSFT\_FSRMAction class

Creates a new [**MSFT\_FSRMAction**](msft-fsrmaction.md) instance.

## Syntax


```mof
uint64 CreateAction(
  [in]  uint32          Type,
  [in]  string          MailTo,
  [in]  string          MailCC,
  [in]  string          MailBCC,
  [in]  string          Subject,
  [in]  string          Body,
  [in]  uint32          EventType,
  [in]  string          Command,
  [in]  string          WorkingDirectory,
  [in]  string          CommandParameters,
  [in]  uint32          SecurityLevel = LocalService,
  [in]  sint32          KillTimeOut,
  [in]  boolean         ShouldLogError,
  [in]  uint32          ReportTypes[],
  [in]  sint32          RunLimitInterval,
  [out] MSFT_FSRMAction Action
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The type of the action, which determines the action that is taken in response to a quota or file screen event. See the [**FsrmActionType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmactiontype?branch=master) enumeration.

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

</dd> <dt>

<span id="Report"></span><span id="report"></span><span id="REPORT"></span>

<span id="Report"></span><span id="report"></span><span id="REPORT"></span>**Report** (4)


</dt> <dd>

The Action is to generate a report.

</dd> </dl> </dd> <dt>

*MailTo* \[in\]
</dt> <dd>

A semicolon-separated list of email addresses that are to be on the to line of the mail. This parameter is used if the *Type* parameter is 2 (Email) or 4 (Report.)

</dd> <dt>

*MailCC* \[in\]
</dt> <dd>

A semicolon-separated list of email addresses that are to be on the to line of the mail. This parameter is used if the *Type* parameter is 2 (Email.)

</dd> <dt>

*MailBCC* \[in\]
</dt> <dd>

A semicolon-separated list of email addresses that are to be on the to line of the mail. This parameter is used if the *Type* parameter is 2 (Email.)

</dd> <dt>

*Subject* \[in\]
</dt> <dd>

The subject of the email. This parameter is used if the *Type* parameter is 2 (Email) and is limited to 1 KB.

</dd> <dt>

*Body* \[in\]
</dt> <dd>

The content of the event or email. This parameter is used if the *Type* parameter is 1 (Event) or 2 (Email) and is limited to 10 KB.

</dd> <dt>

*EventType* \[in\]
</dt> <dd>

The event type of the action. This parameter is used if the *Type* parameter is 1 (Event.) See the [**FsrmEventType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmeventtype?branch=master) enumeration.

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

The full path to the executable program or script to run. This parameter is used if the *Type* parameter is 3 (Command.) See the [**ExecutablePath**](/windows/previous-versions/Fsrm/nf-fsrm-ifsrmactioncommand-get_executablepath?branch=master) property of [**IFsrmActionCommand**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactioncommand?branch=master).

</dd> <dt>

*WorkingDirectory* \[in\]
</dt> <dd>

The working directory in which the executable program or script will run. This parameter is used if the *Type* parameter is 3 (Command.) See the [**WorkingDirectory**](/windows/previous-versions/Fsrm/nf-fsrm-ifsrmactioncommand-get_workingdirectory?branch=master) property of [**IFsrmActionCommand**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactioncommand?branch=master).

</dd> <dt>

*CommandParameters* \[in\]
</dt> <dd>

The parameters for the executable program or script to be run. This parameter is used if the *Type* parameter is 3 (Command.) See the [**Arguments**](/windows/previous-versions/Fsrm/nf-fsrm-ifsrmactioncommand-get_arguments?branch=master) property of [**IFsrmActionCommand**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactioncommand?branch=master).

</dd> <dt>

*SecurityLevel* \[in\]
</dt> <dd>

The account under which the executable program or script will be run. This parameter is used if the *Type* parameter is 3 (Command.) See the [**FsrmAccountType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmaccounttype?branch=master) enumeration.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

No account is specified.

</dd> <dt>

<span id="NetworkService"></span><span id="networkservice"></span><span id="NETWORKSERVICE"></span>

<span id="NetworkService"></span><span id="networkservice"></span><span id="NETWORKSERVICE"></span>**NetworkService** (1)


</dt> <dd>

The command will be run by the "NetworkService" account.

</dd> <dt>

<span id="LocalService"></span><span id="localservice"></span><span id="LOCALSERVICE"></span>

<span id="LocalService"></span><span id="localservice"></span><span id="LOCALSERVICE"></span>**LocalService** (2)


</dt> <dd>

The command will be run by the "LocalService" account.

</dd> <dt>

<span id="LocalSystem"></span><span id="localsystem"></span><span id="LOCALSYSTEM"></span>

<span id="LocalSystem"></span><span id="localsystem"></span><span id="LOCALSYSTEM"></span>**LocalSystem** (3)


</dt> <dd>

The command will be run by the "LocalSystem" account.

</dd> </dl> </dd> <dt>

*KillTimeOut* \[in\]
</dt> <dd>

The timeout period, in minutes, after which the process created by the action will be terminated, or -1 (0xffffffff, the default value) if the process is not to be terminated. This parameter is used if the *Type* parameter is 3 (Command.) See the [**KillTimeOut**](/windows/previous-versions/Fsrm/nf-fsrm-ifsrmactioncommand-get_killtimeout?branch=master) property of [**IFsrmActionCommand**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactioncommand?branch=master).

</dd> <dt>

*ShouldLogError* \[in\]
</dt> <dd>

If **true**, error codes from executed commands are logged in the event log. This parameter is used if the *Type* parameter is 3 (Command. See the [**LogResult**](/windows/previous-versions/Fsrm/nf-fsrm-ifsrmactioncommand-get_logresult?branch=master) property of [**IFsrmActionCommand**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactioncommand?branch=master).

</dd> <dt>

*ReportTypes* \[in\]
</dt> <dd>

Specifies the type of the report to be generated by this action. This parameter is used if the *Type* parameter is 4 (Report.) See the [**FsrmReportType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmreporttype?branch=master) enumeration type.

<dt>

<span id="LargeFiles"></span><span id="largefiles"></span><span id="LARGEFILES"></span>

<span id="LargeFiles"></span><span id="largefiles"></span><span id="LARGEFILES"></span>**LargeFiles** (1)


</dt> <dd>

A report is generated for any files that match the **ReportLargeFileMinimum** and **ReportLargeFilePattern** properties of the [**MSFT\_FSRMSettings**](msft-fsrmsettings.md) class.

</dd> <dt>

<span id="FilesByFileGroup"></span><span id="filesbyfilegroup"></span><span id="FILESBYFILEGROUP"></span>

<span id="FilesByFileGroup"></span><span id="filesbyfilegroup"></span><span id="FILESBYFILEGROUP"></span>**FilesByFileGroup** (2)


</dt> <dd>

Lists groups of files. Create file groups using the [**MSFT\_FSRMFileGroup**](msft-fsrmfilegroup.md) class and put the names of the groups in the **ReportFileGroupsIncluded** property of the [**MSFT\_FSRMSettings**](msft-fsrmsettings.md) class. The **ReportLimitMaxFilesPerFileGroup** and **ReportLimitMaxFileGroup** properties of the **MSFT\_FSRMSettings** class can be used to limit the report.

</dd> <dt>

<span id="LeastRecentlyAccessed"></span><span id="leastrecentlyaccessed"></span><span id="LEASTRECENTLYACCESSED"></span>

<span id="LeastRecentlyAccessed"></span><span id="leastrecentlyaccessed"></span><span id="LEASTRECENTLYACCESSED"></span>**LeastRecentlyAccessed** (3)


</dt> <dd>

A report is generated for any files that matches the **ReportLeastAccessedMinimum** and **ReportLeastAccessedFilePattern** properties of the [**MSFT\_FSRMSettings**](msft-fsrmsettings.md) class.

</dd> <dt>

<span id="MostRecentlyAccessed"></span><span id="mostrecentlyaccessed"></span><span id="MOSTRECENTLYACCESSED"></span>

<span id="MostRecentlyAccessed"></span><span id="mostrecentlyaccessed"></span><span id="MOSTRECENTLYACCESSED"></span>**MostRecentlyAccessed** (4)


</dt> <dd>

A report is generated for any files that matches the pattern in the **ReportMostAccessedMaximum** and **ReportMostAccessedFilePattern** properties of the [**MSFT\_FSRMSettings**](msft-fsrmsettings.md) class.

</dd> <dt>

<span id="QuotaUsage"></span><span id="quotausage"></span><span id="QUOTAUSAGE"></span>

<span id="QuotaUsage"></span><span id="quotausage"></span><span id="QUOTAUSAGE"></span>**QuotaUsage** (5)


</dt> <dd>

A report is generated for any files that matches the **ReportQuotaMinimumUsage** properties of the [**MSFT\_FSRMSettings**](msft-fsrmsettings.md) class, up to the limit specified by the **ReportLimitMaxQuota** property of the **MSFT\_FSRMSettings** class.

</dd> <dt>

<span id="FilesByOwner"></span><span id="filesbyowner"></span><span id="FILESBYOWNER"></span>

<span id="FilesByOwner"></span><span id="filesbyowner"></span><span id="FILESBYOWNER"></span>**FilesByOwner** (6)


</dt> <dd>

A report is generated for any files that matches the **ReportFileOwnerUser** and **ReportFileOwnerFilePattern** properties of the [**MSFT\_FSRMSettings**](msft-fsrmsettings.md) class up to the limits specified by the **ReportLimitMaxOwner** and **ReportLimitMaxFilesPerOwner** properties of the **MSFT\_FSRMSettings** class.

</dd> <dt>

<span id="DuplicateFiles"></span><span id="duplicatefiles"></span><span id="DUPLICATEFILES"></span>

<span id="DuplicateFiles"></span><span id="duplicatefiles"></span><span id="DUPLICATEFILES"></span>**DuplicateFiles** (8)


</dt> <dd>

Lists duplicate files. All files with the same file name, file size, and last modify time under the scope of the report job are considered duplicates. For example, if the scope of the report is C:\\ and D:\\ and file file1.txt exists in C:\\*folder1*\\, C:\\*folder2*\\ and D:\\*folder1*\\ with the same modify time and file size, then the files are considered duplicates.

</dd> <dt>

<span id="FileScreenAuditFiles"></span><span id="filescreenauditfiles"></span><span id="FILESCREENAUDITFILES"></span>

<span id="FileScreenAuditFiles"></span><span id="filescreenauditfiles"></span><span id="FILESCREENAUDITFILES"></span>**FileScreenAuditFiles** (9)


</dt> <dd>

Lists file screening events that have occurred for any files that match the **ReportFileScreenAuditDaysSince**, **ReportFileScreenAuditUser**, and **ReportFileScreenAuditEnable** properties of the [**MSFT\_FSRMSettings**](msft-fsrmsettings.md) class, up to the limit specified by the **ReportLimitMaxFileScreenEvent** property of the **MSFT\_FSRMSettings** class.

</dd> <dt>

<span id="FilesByProperty"></span><span id="filesbyproperty"></span><span id="FILESBYPROPERTY"></span>

<span id="FilesByProperty"></span><span id="filesbyproperty"></span><span id="FILESBYPROPERTY"></span>**FilesByProperty** (10)


</dt> <dd>

Lists files, grouped by property value, that matches the **ReportPropertyName** and **ReportPropertyFilePattern** properties of the [**MSFT\_FSRMSettings**](msft-fsrmsettings.md) class up to the limits specified by the **ReportLimitMaxPropertyValue** and **ReportLimitMaxFilesPerPropertyValue** properties of the **MSFT\_FSRMSettings** class.

</dd> </dl> </dd> <dt>

*RunLimitInterval* \[in\]
</dt> <dd>

Specifies the minimum number of minutes between runs of the action. 0xffffffff specifies that there is no limit.

</dd> <dt>

*Action* \[out\]
</dt> <dd>

Receives a [**MSFT\_FSRMAction**](msft-fsrmaction.md) instance upon successful completion.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| Header<br/>                   | <dl> <dt>Fsrmscreen.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_FSRMAction**](msft-fsrmaction.md)
</dt> </dl>

 

 





