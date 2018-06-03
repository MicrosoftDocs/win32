---
title: MSFT\_FSRMSettings class
description: Represents the FSRM settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e0b9918e-d87a-4135-aea6-dbab1cdebcd9
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMSettings class File Server Resource Manager
- MSFT_FSRMSettings class File Server Resource Manager , described
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMSettings class

Represents the FSRM settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMSettings
{
  string  Server;
  string  FromEmailAddress;
  string  AdminEmailAddress;
  sint32  EmailNotificationLimit;
  sint32  EventNotificationLimit;
  sint32  CommandNotificationLimit;
  sint32  ReportNotificationLimit;
  sint32  ReportLimitMaxFile;
  sint32  ReportLimitMaxFileGroup;
  sint32  ReportLimitMaxOwner;
  sint32  ReportLimitMaxFilesPerFileGroup;
  sint32  ReportLimitMaxFilesPerOwner;
  sint32  ReportLimitMaxFilesPerDuplicateGroup;
  sint32  ReportLimitMaxDuplicateGroup;
  sint32  ReportLimitMaxQuota;
  sint32  ReportLimitMaxFileScreenEvent;
  sint32  ReportLimitMaxPropertyValue;
  sint32  ReportLimitMaxFilesPerPropertyValue;
  string  ReportLocationIncident;
  string  ReportLocationScheduled;
  string  ReportLocationOnDemand;
  sint32  ReportFileScreenAuditDaysSince;
  string  ReportFileScreenAuditUser[] = {};
  string  ReportFileGroupIncluded[] = {};
  string  ReportFileOwnerUser[] = {};
  string  ReportFileOwnerFilePattern = "";
  string  ReportPropertyName = "";
  string  ReportPropertyFilePattern = "";
  uint64  ReportLargeFileMinimum = 0;
  string  ReportLargeFilePattern = "";
  sint32  ReportLeastAccessedMinimum = 0;
  string  ReportLeastAccessedFilePattern = "";
  sint32  ReportMostAccessedMaximum = 0;
  string  ReportMostAccessedFilePattern = "";
  sint32  ReportQuotaMinimumUsage = 0;
  boolean ReportFileScreenAuditEnable = False;
  uint32  ReportClassificationFormat[] = {Dhtml, Xml};
  string  ReportClassificationMailTo = "";
  uint32  ReportClassificationLog[];
  string  SmtpServer;
};
```

## Members

The **MSFT\_FSRMSettings** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMSettings** class has these methods.



| Method                                                                      | Description                                                                                                               |
|:----------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| [**GetActionRunLimitInterval**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmsetting-getactionrunlimitinterval) | Gets the time that an action that uses the global run limit interval must wait before the action is run again.<br/> |
| [**SendTestEmail**](msft-fsrmsettings-sendtestemail.md)                    | Send a test email to the specified email address.<br/>                                                              |
| [**SetActionRunLimitInterval**](/previous-versions/windows/desktop/api/Fsrm/nf-fsrm-ifsrmsetting-setactionrunlimitinterval) | Sets the time that an action that uses the global run limit interval must wait before the action is run again.<br/> |



 

### Properties

The **MSFT\_FSRMSettings** class has these properties.

<dl> <dt>

**AdminEmailAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The email address for the administrator. Optional.

</dd> <dt>

**CommandNotificationLimit**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If multiple command notifications are raised, they will only be performed if at least this many minutes have passed since the last such action was performed. Optional.

</dd> <dt>

**EmailNotificationLimit**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If multiple email notifications are raised, they will only be performed if at least this many minutes have passed since the last such action was performed. Optional.

</dd> <dt>

**EventNotificationLimit**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If multiple event notifications are raised, they will only be performed if at least this many minutes have passed since the last such action was performed. Optional.

</dd> <dt>

**FromEmailAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The default email address from which email messages are sent. Optional.

</dd> <dt>

**ReportClassificationFormat**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The formats of the classification report being generated. The default value is {Dhtml, Xml}.

<dt>

<span id="DHtml"></span><span id="dhtml"></span><span id="DHTML"></span>

<span id="DHtml"></span><span id="dhtml"></span><span id="DHTML"></span>**DHtml** (1)


</dt> <dd>

The report is rendered in Dynamic HTML (DHTML).

</dd> <dt>

<span id="Html"></span><span id="html"></span><span id="HTML"></span>

<span id="Html"></span><span id="html"></span><span id="HTML"></span>**Html** (2)


</dt> <dd>

The report is rendered in HTML.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>**Text** (3)


</dt> <dd>

The report is rendered as a text file.

</dd> <dt>

<span id="Csv"></span><span id="csv"></span><span id="CSV"></span>

<span id="Csv"></span><span id="csv"></span><span id="CSV"></span>**Csv** (4)


</dt> <dd>

The report is rendered as a comma-separated value file.

</dd> <dt>

<span id="Xml"></span><span id="xml"></span><span id="XML"></span>

<span id="Xml"></span><span id="xml"></span><span id="XML"></span>**Xml** (5)


</dt> <dd>

The report is rendered in XML.

</dd> </dl>

</dd> <dt>

**ReportClassificationLog**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of flag values indicating the type and content of logs generated for classification. Optional.

<dt>

<span id="ClassificationsInLogFile"></span><span id="classificationsinlogfile"></span><span id="CLASSIFICATIONSINLOGFILE"></span>

<span id="ClassificationsInLogFile"></span><span id="classificationsinlogfile"></span><span id="CLASSIFICATIONSINLOGFILE"></span>**ClassificationsInLogFile** (1)


</dt> <dd>

Put classification information in the XML log file.

</dd> <dt>

<span id="ErrorsInLogFile"></span><span id="errorsinlogfile"></span><span id="ERRORSINLOGFILE"></span>

<span id="ErrorsInLogFile"></span><span id="errorsinlogfile"></span><span id="ERRORSINLOGFILE"></span>**ErrorsInLogFile** (2)


</dt> <dd>

Put classification errors in the XML log file.

</dd> <dt>

<span id="ClassificationsInSystemLog"></span><span id="classificationsinsystemlog"></span><span id="CLASSIFICATIONSINSYSTEMLOG"></span>

<span id="ClassificationsInSystemLog"></span><span id="classificationsinsystemlog"></span><span id="CLASSIFICATIONSINSYSTEMLOG"></span>**ClassificationsInSystemLog** (4)


</dt> <dd>

Put classification information in the system event log.

</dd> <dt>

<span id="ErrorsInSystemLog"></span><span id="errorsinsystemlog"></span><span id="ERRORSINSYSTEMLOG"></span>

<span id="ErrorsInSystemLog"></span><span id="errorsinsystemlog"></span><span id="ERRORSINSYSTEMLOG"></span>**ErrorsInSystemLog** (8)


</dt> <dd>

Put classification errors in the system event log.

</dd> </dl>

</dd> <dt>

**ReportClassificationMailTo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A semicolon-separated list of email addresses. "\[Admin Email\]" is an acceptable email address. The default value is an empty string. Optional.

</dd> <dt>

**ReportFileGroupIncluded**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of file groups to include in report. Each string must be the name of a valid file group and be less than 1KB in size. The default value is an empty list, which indicates all file groups.

</dd> <dt>

**ReportFileOwnerFilePattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A file pattern string that indicates which files to include in the file by owner report. The string must be less than 1KB and allows the wildcard characters \* and ?. The default value is an empty string.

</dd> <dt>

**ReportFileOwnerUser**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

List of users, in "domain\\user" format, to include files for in the file by owner report. Each string must be less than 1KB in size. The default value is an empty list, which indicates all users.

</dd> <dt>

**ReportFileScreenAuditDaysSince**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum number of days since the audit event to include in the report.

</dd> <dt>

**ReportFileScreenAuditEnable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** if file screen auditing is enabled. The default value is **False**. Optional.

</dd> <dt>

**ReportFileScreenAuditUser**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of user email addresses to include audit events for. Each string must be less than 1KB in size. The default value is an empty list, which indicates all users.

</dd> <dt>

**ReportLargeFileMinimum**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum file size to include in the large file report. The default valu is 0. Optional.

</dd> <dt>

**ReportLargeFilePattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string of files to include in the file by property report. The string must be less than 1KB and allows the wildcard characters \* and ?. The default value is an empty string.

</dd> <dt>

**ReportLeastAccessedFilePattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string of files to include in the least frequently accessed report. The string must be less than 1KB and allows the wildcard characters \* and ?. The default value is an empty string.

</dd> <dt>

**ReportLeastAccessedMinimum**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum number of days since the report was last accessed, to include in the least frequently accessed report. The default value is 0. Optional.

</dd> <dt>

**ReportLimitMaxDuplicateGroup**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

In a duplicate files report, the maximum number of groups of duplicate files found.

</dd> <dt>

**ReportLimitMaxFile**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of files to include in a storage report.

</dd> <dt>

**ReportLimitMaxFileGroup**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of file groups to include in a files by file group report.

</dd> <dt>

**ReportLimitMaxFileScreenEvent**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of file screens events to include in a files by file screen audit report.

</dd> <dt>

**ReportLimitMaxFilesPerDuplicateGroup**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

In a duplicate files report, the maximum number of files in an individual duplicate group.

</dd> <dt>

**ReportLimitMaxFilesPerFileGroup**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

In a file by file group report, the maximum number of files in any file group.

</dd> <dt>

**ReportLimitMaxFilesPerOwner**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

In a files by owner report, the maximum number of files in for each owner.

</dd> <dt>

**ReportLimitMaxFilesPerPropertyValue**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

In a files by property report, the maximum number of files for each property value.

</dd> <dt>

**ReportLimitMaxOwner**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

In a files by owner report, the maximum number owners in the report.

</dd> <dt>

**ReportLimitMaxPropertyValue**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

In a files by property report, the maximum number of property values per report.

</dd> <dt>

**ReportLimitMaxQuota**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of quotas in a quota report.

</dd> <dt>

**ReportLocationIncident**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A local or remote path to a folder. Must not exceed the value of **MAX\_PATH**. Permissions on the folder are assumed to be set so that *FSRM* can write data to it.

</dd> <dt>

**ReportLocationOnDemand**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A local or remote path to a folder. Must not exceed the value of **MAX\_PATH**. Permissions on the folder are assumed to be set so that *FSRM* can write data to it.

</dd> <dt>

**ReportLocationScheduled**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A local or remote path to a folder. Must not exceed the value of **MAX\_PATH**. Permissions on the folder are assumed to be set so that *FSRM* can write data to it.

</dd> <dt>

**ReportMostAccessedFilePattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string of files to include in the most frequently accessed report. The string must be less than 1KB and allows the wildcard characters \* and ?. The default value is an empty string.

</dd> <dt>

**ReportMostAccessedMaximum**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of days since the report was last accessed, to include in the least frequently accessed report. The default value is 0. Optional.

</dd> <dt>

**ReportNotificationLimit**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If multiple report notifications are raised, they will only be performed if at least this many minutes have passed since the last such action was performed. Optional.

</dd> <dt>

**ReportPropertyFilePattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string of files to include in the file by property report. The string must be less than 1KB and allows the wildcard characters \* and ?. The default value is an empty string.

</dd> <dt>

**ReportPropertyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The property name to report on for file by property report. The string must be a valid property name and must not exceed 1KB in size. The default value is an empty string. Optional.

</dd> <dt>

**ReportQuotaMinimumUsage**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum quota usage level to include in the quota usage report. The default value is 0. Optional.

</dd> <dt>

**Server**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The SMTP server that FSRM uses to send email.

</dd> <dt>

**SmtpServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

</dd> </dl>

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

 

 





