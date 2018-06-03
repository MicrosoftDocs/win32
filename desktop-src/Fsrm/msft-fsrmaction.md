---
title: MSFT\_FSRMAction class
description: Represents a FSRM action that can be triggered in response to a quota, file management job, or file screen event (for example, a quota is exceeded or a file violates a file screen).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 55bacec3-c6d1-40ce-902c-8c38eb9a9e7b
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMAction class File Server Resource Manager
- MSFT_FSRMAction class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMAction
- MSFT_FSRMAction.Type
- MSFT_FSRMAction.MailTo
- MSFT_FSRMAction.MailCC
- MSFT_FSRMAction.MailBCC
- MSFT_FSRMAction.Subject
- MSFT_FSRMAction.Body
- MSFT_FSRMAction.EventType
- MSFT_FSRMAction.Command
- MSFT_FSRMAction.WorkingDirectory
- MSFT_FSRMAction.CommandParameters
- MSFT_FSRMAction.SecurityLevel
- MSFT_FSRMAction.KillTimeOut
- MSFT_FSRMAction.ShouldLogError
- MSFT_FSRMAction.ReportTypes
- MSFT_FSRMAction.RunLimitInterval
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMAction class

Represents a FSRM action that can be triggered in response to a quota, file management job, or file screen event (for example, a quota is exceeded or a file violates a file screen).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMAction
{
  uint32  Type;
  string  MailTo = "";
  string  MailCC = "";
  string  MailBCC = "";
  string  Subject = "";
  string  Body = "";
  uint32  EventType;
  string  Command;
  string  WorkingDirectory = "";
  string  CommandParameters = "";
  uint32  SecurityLevel = 2;
  sint32  KillTimeOut = -1;
  boolean ShouldLogError = false;
  uint32  ReportTypes[];
  sint32  RunLimitInterval = 60;
};
```

## Members

The **MSFT\_FSRMAction** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMAction** class has these methods.



| Method                                               | Description                                             |
|:-----------------------------------------------------|:--------------------------------------------------------|
| [**CreateAction**](msft-fsrmaction-createaction.md) | Creates a new **MSFT\_FSRMAction** instance.<br/> |



 

### Properties

The **MSFT\_FSRMAction** class has these properties.

<dl> <dt>

**Body**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The content of the event or email. This property is used (and required) if the **Type** property is 1 (Event) or 2 (Email) and is limited to 10 KB.

</dd> <dt>

**Command**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The full path to the executable program or script to run. This property is used if the **Type** property is 3 (Command.) See the [**ExecutablePath**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactioncommand-get_executablepath) property of [**IFsrmActionCommand**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactioncommand).

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

**KillTimeOut**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The timeout period, in minutes, after which the process created by the action will be terminated, or -1 (0xffffffff, the default value) if the process is not to be terminated. This property is used if the **Type** property is 3 (Command.) See the [**KillTimeOut**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactioncommand-get_killtimeout) property of [**IFsrmActionCommand**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactioncommand).

</dd> <dt>

**MailBCC**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A semicolon-separated list of email addresses that are to be on the BCC line of the mail. This property is used if the **Type** property is 2 (Email.)

</dd> <dt>

**MailCC**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A semicolon-separated list of email addresses that are to be on the CC line of the mail. This property is used if the **Type** property is 2 (Email.)

</dd> <dt>

**MailTo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A semicolon-separated list of email addresses that are to be on the TO line of the mail. This property is used if the **Type** property is 2 (Email) or 4 (Report.)

</dd> <dt>

**ReportTypes**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the type of the report to be generated by this action. This property is used if the **Type** property is 4 (Report.) See the [**FsrmReportType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmreporttype) enumeration type.

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

</dd> </dl>

</dd> <dt>

**RunLimitInterval**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the minimum number of minutes between runs of the action. 60 is the default and 0xffffffff specifies that there is no limit.

</dd> <dt>

**SecurityLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The account under which the executable program or script will be run. This property is used if the **Type** property is 3 (Command.) See the [**FsrmAccountType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmaccounttype) enumeration.

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

**ShouldLogError**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, error codes from executed commands are logged in the event log. This property defaults to **false**.This property is used if the **Type** property is 3 (Command. See the [**LogResult**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactioncommand-get_logresult) property of [**IFsrmActionCommand**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactioncommand).

</dd> <dt>

**Subject**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The subject of the email. This property is used (and required) if the **Type** property is 2 (Email) and is limited to 1 KB.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of the action, which determines the action that is taken in response to a quota or file screen event. See the [**FsrmActionType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmactiontype) enumeration.

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

</dd> </dl>

</dd> <dt>

**WorkingDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The working directory in which the executable program or script will run. This property is used if the **Type** property is 3 (Command.) See the [**WorkingDirectory**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmactioncommand-get_workingdirectory) property of [**IFsrmActionCommand**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactioncommand).

</dd> </dl>

## Remarks

Not all action types support every property in the class. The table below indicates which properties in this class are supported by each action type in the **Type** property.



| Property/Type        | Event (1) | Email (2) | Command (3) | Report (4) |
|----------------------|-----------|-----------|-------------|------------|
| **MailTo**           | Yes       | No        | No          | Yes        |
| **MailCC**           | Yes       | No        | No          | No         |
| **MailBCC**          | Yes       | No        | No          | No         |
| **Subject**          | Yes       | No        | No          | No         |
| **Body**             | Yes       | Yes       | No          | No         |
| **EventType**        | No        | No        | No          | No         |
| **IncludeFileList**  | No        | No        | No          | No         |
| **Command**          | No        | No        | Yes         | No         |
| **WorkingDirectory** | No        | No        | Yes         | No         |
| **Parameters**       | No        | No        | Yes         | No         |
| **SecurityLevel**    | No        | No        | Yes         | No         |
| **KillTimeOut**      | No        | No        | Yes         | No         |
| **ShouldLogError**   | No        | No        | Yes         | No         |
| **ReportTypes**      | No        | No        | No          | Yes        |



 

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

 

 





