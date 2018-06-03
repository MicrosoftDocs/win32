---
title: MSFT\_FSRMScheduledTask class
description: Represents a FSRM scheduled task object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8ed0ec1c-3af2-4c49-92cf-0911473fb33a
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMScheduledTask class File Server Resource Manager
- MSFT_FSRMScheduledTask class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMScheduledTask
- MSFT_FSRMScheduledTask.Time
- MSFT_FSRMScheduledTask.RunDuration
- MSFT_FSRMScheduledTask.Weekly
- MSFT_FSRMScheduledTask.Monthly
- MSFT_FSRMScheduledTask.NextRunTime
- MSFT_FSRMScheduledTask.LegacyTaskName
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMScheduledTask class

Represents a FSRM scheduled task object

The following syntax is simplified from Managed Object Format (*MOF*) code and includes all of the inherited properties.

**Windows Server 2008 R2 and Windows Server 2008:** To schedule a task or manage scheduled tasks use the [**IFsrmReportScheduler**](/previous-versions/windows/desktop/api/FsrmReports/nn-fsrmreports-ifsrmreportscheduler) interface.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMScheduledTask
{
  datetime Time;
  sint32   RunDuration;
  uint32   Weekly[];
  sint32   Monthly[];
  datetime NextRunTime;
  string   LegacyTaskName;
};
```

## Members

The **MSFT\_FSRMScheduledTask** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMScheduledTask** class has these methods.



| Method                                                                    | Description                                                                     |
|:--------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| [**CreateScheduledTask**](msft-fsrmscheduledtask-createscheduledtask.md) | Creates a scheduled task object that will be consumed by other jobs.<br/> |



 

### Properties

The **MSFT\_FSRMScheduledTask** class has these properties.

<dl> <dt>

**LegacyTaskName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of an incompatible schedule task object that is not supported. This will happen in upgrade scenarios. This value should be the name of the task. This property will be empty if the schedule is compatible with the current schema. If this property exists it's recommended to re-create the scheduled task.

</dd> <dt>

**Monthly**
</dt> <dd> <dl> <dt>

Data type: **sint32** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

<dt>

1 31
</dt> <dd>

Represents the specified day of the month.

</dd> <dt>

-1
</dt> <dd>

Represents the last day of the month.

</dd> </dl>

An optional array of integers between -1 and 31 representing the days of the month on which the task should be run.

The value -1 refers to the last day of a month.

An error will be returned if a value of 0 is specified.

Required if the **Weekly** property is not specified and may not be specified if the **Weekly** property is specified.

</dd> <dt>

**NextRunTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies when the task is next scheduled to run.

</dd> <dt>

**RunDuration**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of hours to continue the task before termination. Optional.

</dd> <dt>

**Time**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Date Time value in standard *UTC* formats. Required.

</dd> <dt>

**Weekly**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of days on which to execute the task. Required if the **Monthly** property is not specified and may not be specified if the **Monthly** property is specified.

<dt>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>

**Sunday** (0)


</dt> <dd></dd> <dt>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>

**Monday** (1)


</dt> <dd></dd> <dt>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>

**Tuesday** (2)


</dt> <dd></dd> <dt>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>

**Wednesday** (3)


</dt> <dd></dd> <dt>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>

**Thursday** (4)


</dt> <dd></dd> <dt>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>

**Friday** (5)


</dt> <dd></dd> <dt>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>

**Saturday** (6)


</dt> <dd></dd> </dl>

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

 

 





