---
title: CreateScheduledTask method of the MSFT\_FSRMScheduledTask class
description: Creates a scheduled task object that will be consumed by other jobs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 56faee26-bdb0-442f-aec1-1e5d97e798e6
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- CreateScheduledTask method File Server Resource Manager
- CreateScheduledTask method File Server Resource Manager , MSFT_FSRMScheduledTask class
- MSFT_FSRMScheduledTask class File Server Resource Manager , CreateScheduledTask method
topic_type:
- apiref
api_name:
- MSFT_FSRMScheduledTask.CreateScheduledTask
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateScheduledTask method of the MSFT\_FSRMScheduledTask class

Creates a scheduled task object that will be consumed by other jobs.

**Windows Server 2008 R2 and Windows Server 2008:** To schedule a task use the [**IFsrmReportScheduler**](/windows/previous-versions/FsrmReports/nn-fsrmreports-ifsrmreportscheduler?branch=master) interface.

## Syntax


```mof
uint64 CreateScheduledTask(
  [in]  datetime               Time,
  [in]  sint32                 RunDuration,
  [in]  uint32                 Weekly[],
  [in]  sint32                 Monthly[],
  [out] MSFT_FSRMScheduledTask ScheduledTask
);
```



## Parameters

<dl> <dt>

*Time* \[in\]
</dt> <dd>

Date Time value in standard *UTC* formats. Required.

</dd> <dt>

*RunDuration* \[in\]
</dt> <dd>

The number of hours to continue the task before termination. Optional.

</dd> <dt>

*Weekly* \[in\]
</dt> <dd>

A list of days on which to execute the task. Optional.

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


</dt> <dd></dd> </dl> </dd> <dt>

*Monthly* \[in\]
</dt> <dd>

An integer between -1 and 31. Optional.

The value -1 refers to the last day of a month.

An error will be returned if a value of 0 is specified.

</dd> <dt>

*ScheduledTask* \[out\]
</dt> <dd>

Returns an instance of the [**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md) class.

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

[**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md)
</dt> </dl>

 

 





