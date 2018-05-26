---
title: MSFT\_FSRMStorageReport class
description: Represents a storage report.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9fd915a7-1315-4c49-8088-c418d5aecdb4
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMStorageReport class File Server Resource Manager
- MSFT_FSRMStorageReport class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMStorageReport
- MSFT_FSRMStorageReport.Name
- MSFT_FSRMStorageReport.Namespace
- MSFT_FSRMStorageReport.Interactive
- MSFT_FSRMStorageReport.ReportType
- MSFT_FSRMStorageReport.FileScreenAuditDaysSince
- MSFT_FSRMStorageReport.FileScreenAuditUser
- MSFT_FSRMStorageReport.FileGroupIncluded
- MSFT_FSRMStorageReport.FileOwnerUser
- MSFT_FSRMStorageReport.FileOwnerFilePattern
- MSFT_FSRMStorageReport.PropertyName
- MSFT_FSRMStorageReport.FolderPropertyName
- MSFT_FSRMStorageReport.PropertyFilePattern
- MSFT_FSRMStorageReport.LargeFileMinimum
- MSFT_FSRMStorageReport.LargeFilePattern
- MSFT_FSRMStorageReport.LeastAccessedMinimum
- MSFT_FSRMStorageReport.LeastAccessedFilePattern
- MSFT_FSRMStorageReport.MostAccessedMaximum
- MSFT_FSRMStorageReport.MostAccessedFilePattern
- MSFT_FSRMStorageReport.QuotaMinimumUsage
- MSFT_FSRMStorageReport.ReportFormat
- MSFT_FSRMStorageReport.MailTo
- MSFT_FSRMStorageReport.LastError
- MSFT_FSRMStorageReport.Status
- MSFT_FSRMStorageReport.LastRun
- MSFT_FSRMStorageReport.LastReportPath
- MSFT_FSRMStorageReport.Schedule
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_FSRMStorageReport class

Represents a storage report.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMStorageReport
{
  string                 Name;
  string                 Namespace[];
  boolean                Interactive;
  uint32                 ReportType[];
  uint32                 FileScreenAuditDaysSince = 0;
  string                 FileScreenAuditUser[] = {};
  string                 FileGroupIncluded[] = {};
  string                 FileOwnerUser[] = {};
  string                 FileOwnerFilePattern = "";
  string                 PropertyName = "";
  string                 FolderPropertyName = "";
  string                 PropertyFilePattern = "";
  uint64                 LargeFileMinimum = 0;
  string                 LargeFilePattern = "";
  uint32                 LeastAccessedMinimum = 0;
  string                 LeastAccessedFilePattern = "";
  uint32                 MostAccessedMaximum = 0;
  string                 MostAccessedFilePattern = "";
  uint32                 QuotaMinimumUsage;
  uint32                 ReportFormat[] = {Dhtml, Xml};
  string                 MailTo = "";
  string                 LastError;
  uint32                 Status;
  datetime               LastRun;
  string                 LastReportPath;
  MSFT_FSRMScheduledTask Schedule;
};
```

## Members

The **MSFT\_FSRMStorageReport** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMStorageReport** class has these methods.



| Method                                        | Description                                                                    |
|:----------------------------------------------|:-------------------------------------------------------------------------------|
| [**Start**](msft-fsrmstoragereport-start.md) | Starts the generation of the provided storage report on the server.<br/> |
| [**Stop**](msft-fsrmstoragereport-stop.md)   | Stops the execution of the provided storage report on the server.<br/>   |
| [**Wait**](msft-fsrmstoragereport-wait.md)   | Waits for the report to complete its execution.<br/>                     |



 

### Properties

The **MSFT\_FSRMStorageReport** class has these properties.

<dl> <dt>

**FileGroupIncluded**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of valid file groups to include in the report. Each string must be less than 1KB. Total size must be under 25KB. Optional. The default value is an empty list, which indicates all users.

</dd> <dt>

**FileOwnerFilePattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string of file pattern files to include in the file by owner report. The string must be less than 1KB and allow wildcard characters \* and ?. Optional. The default value is an empty string.

</dd> <dt>

**FileOwnerUser**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of users in "domain\\user" format to include files for in the file by owner report. Each string must be less than 1KB. Total size must be under 25KB. The default value is an empty list, which indicates all users.

</dd> <dt>

**FileScreenAuditDaysSince**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum number of days since the audit event to include in the report. Default is 0.

</dd> <dt>

**FileScreenAuditUser**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of user email addresses to include audit events for. Each string must be less than 1KB. Total size must be under 25KB. Optional. The default value is an empty list, which indicates all users.

</dd> <dt>

**FolderPropertyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A valid property name to report on for the file by property report. String must be less than 1KB. Optional. The default value is an empty string.

</dd> <dt>

**Interactive**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether the report is interactive (generated immediately) or will have a schedule for running the report. If this property is **True**, the report is interactive and the **Schedule** property should be empty.

When this property is **True**,

-   The report will not require a schedule
-   The report cannot be modified
-   The report is started once created
-   These reports are automatically removed from the system once completed.

</dd> <dt>

**LargeFileMinimum**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum file size to include in the large file report. The default value is 0. Optional.

</dd> <dt>

**LargeFilePattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string of file pattern files to include in the large file report. The string must be less than 1KB and allow wildcard characters \* and ?. Optional. The default value is an empty string.

</dd> <dt>

**LastError**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error message from the last time this storage report was run.

</dd> <dt>

**LastReportPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of the last report run.

</dd> <dt>

**LastRun**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When the storage report was last run.

</dd> <dt>

**LeastAccessedFilePattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string of file pattern files to include in the least frequently accessed file report. The string must be less than 1KB and allow wildcard characters \* and ?. Optional. The default value is an empty string.

</dd> <dt>

**LeastAccessedMinimum**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum number of days since last accessed to include in least frequently accessed report. The default value is 0. Optional.

</dd> <dt>

**MailTo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A semicolon-separated list of email addresses. "\[Admin Email\]" is an acceptable email address. The default value is an empty string, which indicates not to send an email.

</dd> <dt>

**MostAccessedFilePattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string of file pattern files to include in the least frequently accessed file report. The string must be less than 1KB and allow wildcard characters \* and ?. Optional. The default value is an empty string.

</dd> <dt>

**MostAccessedMaximum**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of days since last accessed to include in least frequently accessed report. The default value is 0. Optional.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A string up to 1KB in length. If not specified, a standard name will be generated. Required if the **Interactive** property is specified.

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings representing valid local paths to folders or valid values for the **FolderUsage** classification property. If providing **FolderUsage** properties, the format "\[FolderUsage\_MS=*value*\]" must be used. Each string must not exceed the length of **MAX\_PATH**. Required.

</dd> <dt>

**PropertyFilePattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string of file pattern files to include in the file by property report. The string must be less than 1KB and allow wildcard characters \* and ?. Optional. The default value is an empty string.

</dd> <dt>

**PropertyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A valid property name to report on for the file by property report. String must be less than 1KB. Optional. The default value is an empty string.

</dd> <dt>

**QuotaMinimumUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum quota usage level to include in quota usage report. The default value is 0. Optional.

</dd> <dt>

**ReportFormat**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The formats of the classification report being generated. No duplicates can be in the array, and the array length must be greater than 0. The default value is V{Dhtml, Xml}.

<dt>

<span id="DHtml"></span><span id="dhtml"></span><span id="DHTML"></span>

<span id="DHtml"></span><span id="dhtml"></span><span id="DHTML"></span>**DHtml** (1)


</dt> <dd>

The report is in Dynamic HTML format.

</dd> <dt>

<span id="Html"></span><span id="html"></span><span id="HTML"></span>

<span id="Html"></span><span id="html"></span><span id="HTML"></span>**Html** (2)


</dt> <dd>

The report is in HTML format.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>**Text** (3)


</dt> <dd>

The report is in text format.

</dd> <dt>

<span id="Csv"></span><span id="csv"></span><span id="CSV"></span>

<span id="Csv"></span><span id="csv"></span><span id="CSV"></span>**Csv** (4)


</dt> <dd>

The report is in CSV format.

</dd> <dt>

<span id="Xml"></span><span id="xml"></span><span id="XML"></span>

<span id="Xml"></span><span id="xml"></span><span id="XML"></span>**Xml** (5)


</dt> <dd>

The report is in XML.

</dd> </dl>

</dd> <dt>

**ReportType**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array describing the report types. No duplicates in the array are allowed. The array must have a length greater than 0. Required.

<dt>

<span id="LargeFiles"></span><span id="largefiles"></span><span id="LARGEFILES"></span>

<span id="LargeFiles"></span><span id="largefiles"></span><span id="LARGEFILES"></span>**LargeFiles** (1)


</dt> <dd>

Lists files that are larger than a specified size. Set the filter value to the size, in bytes.

</dd> <dt>

<span id="FilesByFileGroup"></span><span id="filesbyfilegroup"></span><span id="FILESBYFILEGROUP"></span>

<span id="FilesByFileGroup"></span><span id="filesbyfilegroup"></span><span id="FILESBYFILEGROUP"></span>**FilesByFileGroup** (2)


</dt> <dd>

Lists groups of files. Create a file group and use file name patterns to specify the members of the group. Set the filter value to the name of the file group.

</dd> <dt>

<span id="LeastRecentlyAccessed"></span><span id="leastrecentlyaccessed"></span><span id="LEASTRECENTLYACCESSED"></span>

<span id="LeastRecentlyAccessed"></span><span id="leastrecentlyaccessed"></span><span id="LEASTRECENTLYACCESSED"></span>**LeastRecentlyAccessed** (3)


</dt> <dd>

Lists files that have not been accessed in the last *n* days. Specify the filter value in days.

</dd> <dt>

<span id="MostRecentlyAccessed"></span><span id="mostrecentlyaccessed"></span><span id="MOSTRECENTLYACCESSED"></span>

<span id="MostRecentlyAccessed"></span><span id="mostrecentlyaccessed"></span><span id="MOSTRECENTLYACCESSED"></span>**MostRecentlyAccessed** (4)


</dt> <dd>

Lists files that have been accessed in the last *n* days. Specify the filter value in days.

</dd> <dt>

<span id="QuotaUsage"></span><span id="quotausage"></span><span id="QUOTAUSAGE"></span>

<span id="QuotaUsage"></span><span id="quotausage"></span><span id="QUOTAUSAGE"></span>**QuotaUsage** (5)


</dt> <dd>

Lists quotas that exceed the specified threshold. Set the filter value to the threshold.

</dd> <dt>

<span id="FilesByOwner"></span><span id="filesbyowner"></span><span id="FILESBYOWNER"></span>

<span id="FilesByOwner"></span><span id="filesbyowner"></span><span id="FILESBYOWNER"></span>**FilesByOwner** (6)


</dt> <dd>

Lists files grouped by their owner. Set the filter value to the list of owners whose files you want included in the report.

</dd> <dt>

<span id="DuplicateFiles"></span><span id="duplicatefiles"></span><span id="DUPLICATEFILES"></span>

<span id="DuplicateFiles"></span><span id="duplicatefiles"></span><span id="DUPLICATEFILES"></span>**DuplicateFiles** (8)


</dt> <dd>

Lists duplicate files. All files with the same file name, file size, and last modify time under the scope of the report job are considered duplicates. For example, if the scope of the report is C:\\ and D:\\ and file file1.txt exists in C:\\*folder1*\\, C:\\*folder2*\\ and D:\\*folder1*\\ with the same modify time and file size, then the files are considered duplicates.

</dd> <dt>

<span id="FileScreenAuditFiles"></span><span id="filescreenauditfiles"></span><span id="FILESCREENAUDITFILES"></span>

<span id="FileScreenAuditFiles"></span><span id="filescreenauditfiles"></span><span id="FILESCREENAUDITFILES"></span>**FileScreenAuditFiles** (9)


</dt> <dd>

Lists file screening events that have occurred.

</dd> <dt>

<span id="FilesByProperty"></span><span id="filesbyproperty"></span><span id="FILESBYPROPERTY"></span>

<span id="FilesByProperty"></span><span id="filesbyproperty"></span><span id="FILESBYPROPERTY"></span>**FilesByProperty** (10)


</dt> <dd>

Lists files, grouped by property value, that contain the specified property (you can specify only one property on which to report).

</dd> <dt>

<span id="FoldersByProperty"></span><span id="foldersbyproperty"></span><span id="FOLDERSBYPROPERTY"></span>

<span id="FoldersByProperty"></span><span id="foldersbyproperty"></span><span id="FOLDERSBYPROPERTY"></span>**FoldersByProperty** (13)


</dt> <dd>

Lists folders, grouped by property value, that contain the specified property (you can specify only one property on which to report).

</dd> </dl>

</dd> <dt>

**Schedule**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMScheduledTask**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md)")
</dt> </dl>

An [**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md) instance that represents the schedule for this storage report job. Required if the **Interactive** property is **False**, and must be empty if the **Interactive** property is **True**.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current status of the report.

<dt>

<span id="NotRunning"></span><span id="notrunning"></span><span id="NOTRUNNING"></span>

<span id="NotRunning"></span><span id="notrunning"></span><span id="NOTRUNNING"></span>**NotRunning** (1)


</dt> <dd>

The report is not running.

</dd> <dt>

<span id="Queued"></span><span id="queued"></span><span id="QUEUED"></span>

<span id="Queued"></span><span id="queued"></span><span id="QUEUED"></span>**Queued** (2)


</dt> <dd>

The report has been queued.

</dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>**Running** (3)


</dt> <dd>

The report is running.

</dd> </dl>

</dd> </dl>

## Examples

For an example see [Scheduling a Storage Report using WMI](scheduling-a-report-job-using-wmi.md).

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

 

 





