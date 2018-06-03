---
title: MSFT\_FSRMFileManagementJob class
description: Defines a file management job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1ce33602-0ada-4d82-aebb-9dee7dc8b2f3
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMFileManagementJob class File Server Resource Manager
- MSFT_FSRMFileManagementJob class File Server Resource Manager , described
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMFileManagementJob class

Defines a file management job. The job specifies a schedule, conditions, a command or actions to execute if a file meets all the conditions, user notifications, and reporting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMFileManagementJob
{
  string                   Name;
  string                   Description = "";
  string                   Namespace[];
  boolean                  Disabled = False;
  MSFT_FSRMFMJCondition    Condition[] = {};
  MSFT_FSRMFMJAction       Action = null;
  uint32                   ReportFormat[] = {Dhtml, Xml};
  string                   MailTo = "";
  uint32                   ReportLog[] = {};
  MSFT_FSRMFMJNotification Notification[] = {};
  boolean                  Continuous = False;
  boolean                  ContinuousLog = False;
  uint64                   ContinuousLogSize;
  string                   Parameters[] = {};
  uint32                   Status;
  datetime                 LastRun;
  string                   LastReportPath;
  uint32                   Flags[];
  MSFT_FSRMScheduledTask   Schedule;
  string                   TaskName;
  string                   LastError;
};
```

## Members

The **MSFT\_FSRMFileManagementJob** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMFileManagementJob** class has these methods.



| Method                                            | Description                                                                                              |
|:--------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| [**Start**](msft-fsrmfilemanagementjob-start.md) | Starts the file management job.<br/>                                                               |
| [**Stop**](msft-fsrmfilemanagementjob-stop.md)   | Stops the running instance of a file management job.<br/>                                          |
| [**Wait**](msft-fsrmfilemanagementjob-wait.md)   | Waits for the specified period of time or until the file management job has finished running.<br/> |



 

### Properties

The **MSFT\_FSRMFileManagementJob** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMFMJAction**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMFMJAction**](msft-fsrmfmjaction.md)")
</dt> </dl>

An instance of the [**MSFT\_FSRMFMJAction**](msft-fsrmfmjaction.md) class representing a file management job action object. Required. The default value is null.

</dd> <dt>

**Condition**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMFMJCondition** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMFMJCondition**](msft-fsrmfmjcondition.md)")
</dt> </dl>

A list of instances of the [**MSFT\_FSRMFMJCondition**](msft-fsrmfmjcondition.md) class representing file management job condition objects. Optional. The default value is an empty list. If the **Continuous** property is **True** then the **Property** properties of the **MSFT\_FSRMFMJCondition** instances must not contain "File.DateCreated""File.DateLastModified", or "File.DateLastAccessed".

</dd> <dt>

**Continuous**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, enables the real time file management task. Optional. The default value is **False**. If this property is **True** then the **Property** properties of the [**MSFT\_FSRMFMJCondition**](msft-fsrmfmjcondition.md) instances in the **Condition** property must not contain "File.DateCreated", "File.DateLastModified", or "File.DateLastAccessed".

</dd> <dt>

**ContinuousLog**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, enables the real time classification logs. Optional. The default value is **False**. This property should only be specified if the **Continuous** property is **True**.

</dd> <dt>

**ContinuousLogSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum size to which a real time file management job log may grow. Optional. The default value is 0. This property should only be specified if the **Continuous** property is **True**.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string up to 10KB in size. Optional. The default value is an empty string.

</dd> <dt>

**Disabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the file management job is disabled. The default value is **False**.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of flags describing the file management job.

<dt>

<span id="Deprecated"></span><span id="deprecated"></span><span id="DEPRECATED"></span>

<span id="Deprecated"></span><span id="deprecated"></span><span id="DEPRECATED"></span>**Deprecated** (1)


</dt> <dd>

The rule is deprecated.

</dd> </dl>

</dd> <dt>

**LastError**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**LastReportPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of the last report generated for this file management job.

</dd> <dt>

**LastRun**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When the file management job was last run.

</dd> <dt>

**MailTo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A semicolon-separated list of email addresses. "\[Admin Email\]" is an acceptable email address. The default value is an empty string. This member is optional.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of the file management job.

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings that represent either valid local paths to a folder on the server or valid values for the server's definition of **FolderUsage**. If providing **FolderUsage** properties, the format "\[Folder Usage\_MS=*value*\]" must be used. Strings must not exceed the **MAX\_PATH** length. This member is required.

</dd> <dt>

**Notification**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMFMJNotification** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMFMJNotification**](msft-fsrmfmjnotification.md)")
</dt> </dl>

A list of instances of the [**MSFT\_FSRMFMJNotification**](msft-fsrmfmjnotification.md) class representing file management job notification objects. Optional. The default value is an empty list.

</dd> <dt>

**Parameters**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of strings of the format "&lt;name&gt;=&lt;value&gt;", as accepted by the [**Parameters**](/previous-versions/windows/desktop/api/FsrmReports/nf-fsrmreports-ifsrmfilemanagementjob-get_parameters) property of the [**IFsrmFileManagementJob**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmreports-ifsrmfilemanagementjob) interface. Optional. The default value is an empty list.

</dd> <dt>

**ReportFormat**
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

**ReportLog**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The types of logs being generated for classification. The default value is an empty list. This member is optional.

<dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (1)


</dt> <dd></dd> <dt>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>

**Information** (2)


</dt> <dd></dd> <dt>

<span id="Audit"></span><span id="audit"></span><span id="AUDIT"></span>

**Audit** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**Schedule**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMScheduledTask**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md)")
</dt> </dl>

A [**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md) instance that represents the schedule for this file management job.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The running status of file management job.

<dt>

<span id="NotRunning"></span><span id="notrunning"></span><span id="NOTRUNNING"></span>

<span id="NotRunning"></span><span id="notrunning"></span><span id="NOTRUNNING"></span>**NotRunning** (1)


</dt> <dd>

The job is not running.

</dd> <dt>

<span id="Queued"></span><span id="queued"></span><span id="QUEUED"></span>

<span id="Queued"></span><span id="queued"></span><span id="QUEUED"></span>**Queued** (2)


</dt> <dd>

The job has been queued.

</dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>**Running** (3)


</dt> <dd>

The job is running.

</dd> </dl>

</dd> <dt>

**TaskName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

</dd> </dl>

## Remarks

When a file management job runs, it scans the files in the specified folders and if a file in the folder meets the conditions specified by the job, FSRM moves the file to the specified expired files folder if the type is expiration, or runs the custom action if defined. If notifications or actions are specified, FSRM sends the notifications and performs the actions.

FSRM performs a logical AND on all the conditions to determine if the file meets those conditions.

FSRM does not expire files in the system directories (for example, \\Windows and \\System Volume Information).

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

 

 





