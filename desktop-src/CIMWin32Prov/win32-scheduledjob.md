---
description: Represents a job created with the AT command.
ms.assetid: 2fa69e3f-9a6c-4aa9-8a6c-ea28eb4342ca
ms.tgt_platform: multiple
title: Win32_ScheduledJob class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ScheduledJob
- Win32_ScheduledJob.Caption
- Win32_ScheduledJob.Description
- Win32_ScheduledJob.InstallDate
- Win32_ScheduledJob.Name
- Win32_ScheduledJob.Status
- Win32_ScheduledJob.ElapsedTime
- Win32_ScheduledJob.Notify
- Win32_ScheduledJob.Owner
- Win32_ScheduledJob.Priority
- Win32_ScheduledJob.TimeSubmitted
- Win32_ScheduledJob.UntilTime
- Win32_ScheduledJob.Command
- Win32_ScheduledJob.DaysOfMonth
- Win32_ScheduledJob.DaysOfWeek
- Win32_ScheduledJob.InteractWithDesktop
- Win32_ScheduledJob.JobId
- Win32_ScheduledJob.JobStatus
- Win32_ScheduledJob.RunRepeatedly
- Win32_ScheduledJob.StartTime
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_ScheduledJob class

The **Win32\_ScheduledJob** [WMI class](../wmisdk/retrieving-a-class.md) represents a job created with the **AT** command.

> [!Note]  
> The **Win32\_ScheduledJob** class does not represent a job created with the Scheduled Task Wizard from the Control Panel. You cannot change a task created by WMI in the Scheduled Tasks UI. For more information, see the Remarks section.

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4E0-5FBB-11D2-AAC1-006008C78BC7}"), SupportsCreate, CreateBy("Create"), SupportsDelete, DeleteBy("Delete"), AMENDMENT]
class Win32_ScheduledJob : CIM_Job
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  datetime ElapsedTime;
  string   Notify;
  string   Owner;
  uint32   Priority;
  datetime TimeSubmitted;
  datetime UntilTime;
  string   Command;
  uint32   DaysOfMonth;
  uint32   DaysOfWeek;
  boolean  InteractWithDesktop;
  uint32   JobId;
  string   JobStatus;
  boolean  RunRepeatedly;
  datetime StartTime;
};
```

## Members

The **Win32\_ScheduledJob** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_ScheduledJob** class has these methods.



| Method                                                      | Description                                                                                                           |
|:------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**Create**](create-method-in-class-win32-scheduledjob.md) | Class method that submits a job to the operating system for execution at a specified future time and date.<br/> |
| [**Delete**](delete-method-in-class-win32-scheduledjob.md) | Class method that deletes a scheduled job.<br/>                                                                 |



 

### Properties

The **Win32\_ScheduledJob** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Caption")
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Command**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**AT\_INFO**](/windows/win32/api/lmat/ns-lmat-at_info)\|**Command**")
</dt> </dl>

Name of the command, batch program, or binary file (and command-line arguments) that the schedule service uses to invoke the job.

Example: "**defrag** **/q/f**"

</dd> <dt>

**DaysOfMonth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**AT\_INFO**](/windows/win32/api/lmat/ns-lmat-at_info)\|**DaysOfMonth**")
</dt> </dl>

Days of the month when the job is scheduled to run. If a job is scheduled to run on multiple days of the month, these values can be joined in a logical OR. For example, if a job is to run on the 1st and 16th of each month, the value of the **DaysOfMonth** property would be 1 OR 32768.

<dt>

<span id="1"></span>

<span id="1"></span>**1** (1)


</dt> <dd>

1st

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2** (2)


</dt> <dd>

2nd

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3** (4)


</dt> <dd>

3rd

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4** (8)


</dt> <dd>

4th

</dd> <dt>

<span id="5"></span>

<span id="5"></span>**5** (16)


</dt> <dd>

5th

</dd> <dt>

<span id="6"></span>

<span id="6"></span>**6** (32)


</dt> <dd>

6th

</dd> <dt>

<span id="7"></span>

<span id="7"></span>**7** (64)


</dt> <dd>

7th

</dd> <dt>

<span id="8"></span>

<span id="8"></span>**8** (128)


</dt> <dd>

8th

</dd> <dt>

<span id="9"></span>

<span id="9"></span>**9** (256)


</dt> <dd>

9th

</dd> <dt>

<span id="10"></span>

<span id="10"></span>**10** (512)


</dt> <dd>

10th

</dd> <dt>

<span id="11"></span>

<span id="11"></span>**11** (1024)


</dt> <dd>

11th

</dd> <dt>

<span id="12"></span>

<span id="12"></span>**12** (2048)


</dt> <dd>

12th

</dd> <dt>

<span id="13"></span>

<span id="13"></span>**13** (4096)


</dt> <dd>

13th

</dd> <dt>

<span id="14"></span>

<span id="14"></span>**14** (8192)


</dt> <dd>

14th

</dd> <dt>

<span id="15"></span>

<span id="15"></span>**15** (16384)


</dt> <dd>

15th

</dd> <dt>

<span id="16"></span>

<span id="16"></span>**16** (32768)


</dt> <dd>

16th

</dd> <dt>

<span id="17"></span>

<span id="17"></span>**17** (65536)


</dt> <dd>

17th

</dd> <dt>

<span id="18"></span>

<span id="18"></span>**18** (131072)


</dt> <dd>

18th

</dd> <dt>

<span id="19"></span>

<span id="19"></span>**19** (262144)


</dt> <dd>

19th

</dd> <dt>

<span id="20"></span>

<span id="20"></span>**20** (524288)


</dt> <dd>

20th

</dd> <dt>

<span id="21"></span>

<span id="21"></span>**21** (1048576)


</dt> <dd>

21st

</dd> <dt>

<span id="22"></span>

<span id="22"></span>**22** (2097152)


</dt> <dd>

22nd

</dd> <dt>

<span id="23"></span>

<span id="23"></span>**23** (4194304)


</dt> <dd>

23rd

</dd> <dt>

<span id="24"></span>

<span id="24"></span>**24** (8388608)


</dt> <dd>

24th

</dd> <dt>

<span id="25"></span>

<span id="25"></span>**25** (16777216)


</dt> <dd>

25th

</dd> <dt>

<span id="26"></span>

<span id="26"></span>**26** (33554432)


</dt> <dd>

26th

</dd> <dt>

<span id="27"></span>

<span id="27"></span>**27** (67108864)


</dt> <dd>

27th

</dd> <dt>

<span id="28"></span>

<span id="28"></span>**28** (134217728)


</dt> <dd>

28th

</dd> <dt>

<span id="29"></span>

<span id="29"></span>**29** (268435456)


</dt> <dd>

29th

</dd> <dt>

<span id="30"></span>

<span id="30"></span>**30** (536870912)


</dt> <dd>

30th

</dd> <dt>

<span id="31"></span>

<span id="31"></span>**31** (1073741824)


</dt> <dd>

31st

</dd> </dl>

</dd> <dt>

**DaysOfWeek**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**AT\_INFO**](/windows/win32/api/lmat/ns-lmat-at_info)\|**DaysOfWeek**")
</dt> </dl>

Days of the week when a job is scheduled to run. If a job is scheduled to run on multiple days of the week, the values can be joined in a logical OR. For example, if a job is scheduled to run on Mondays, Wednesdays, and Fridays the value of the **DaysOfWeek** property would be 1 OR 4 OR 16.

<dt>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>

**Monday** (1)


</dt> <dd></dd> <dt>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>

**Tuesday** (2)


</dt> <dd></dd> <dt>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>

**Wednesday** (4)


</dt> <dd></dd> <dt>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>

**Thursday** (8)


</dt> <dd></dd> <dt>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>

**Friday** (16)


</dt> <dd></dd> <dt>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>

**Saturday** (32)


</dt> <dd></dd> <dt>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>

**Sunday** (64)


</dt> <dd></dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Description")
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ElapsedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Length of time the job has been executing.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Install Date")
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InteractWithDesktop**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**AT\_INFO**](/windows/win32/api/lmat/ns-lmat-at_info)\|**Flags**\|**JOB\_NONINTERACTIVE**")
</dt> </dl>

Specified job is interactive, which means that a user can give input to a scheduled job while it is executing.

</dd> <dt>

**JobId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/key-qualifier.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**AT\_ENUM**](/windows/win32/api/lmat/ns-lmat-at_enum)\|**JobId**")
</dt> </dl>

Identifying number of the job. It is used by methods as a handle to one job being scheduled on this computer.

</dd> <dt>

**JobStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("JobStatus"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**AT\_ENUM**](/windows/win32/api/lmat/ns-lmat-at_enum)\|**Flags**\|**JOB\_EXEC\_ERROR**")
</dt> </dl>

Status of execution the last time this job was scheduled to run.

<dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

**Success** ("Success")


</dt> <dd></dd> <dt>

<span id="Failure"></span><span id="failure"></span><span id="FAILURE"></span>

**Failure** ("Failure")


</dt> <dd></dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Name")
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Notify**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

User is notified upon job completion or failure.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

User who submitted the job.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Importance of a job's execution.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**RunRepeatedly**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**AT\_INFO**](/windows/win32/api/lmat/ns-lmat-at_info)\|**Flags**\|**JOB\_RUN\_PERIODICALLY**")
</dt> </dl>

Scheduled job runs repeatedly on the days that the job is scheduled. If **False**, then the job is run one time.

</dd> <dt>

**StartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("StartTime"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**AT\_ENUM**](/windows/win32/api/lmat/ns-lmat-at_enum)\|**JobTime**")
</dt> </dl>

UTC time to run the job, in the form of "YYYYMMDDHHMMSS.MMMMMM(+-)OOO", where "YYYYMMDD" must be replaced by "\*\*\*\*\*\*\*\*". The replacement is necessary because the scheduling service only allows jobs to be configured to run one time, or run on a day of the month or week. A job cannot be run on a specific date.

The "(+-)OOO" section of the **StartTime** property value is the current bias for local time translation. The bias is the difference between the UTC time and local time. To calculate the bias for your time zone, multiply the number of hours that your time zone is ahead or behind Greenwich Mean Time (GMT) by 60 (use a positive number for the number of hours if your time zone is ahead of GMT and a negative number if your time zone is behind GMT). Add an additional 60 to your calculation if your time zone is using daylight savings time. For example, the Pacific Standard Time zone is eight hours behind GMT, therefore the bias is equals to -420 (-8 \* 60 + 60) when daylight savings time is in use and -480 (-8 \* 60) when daylight savings time is not in use. You can also determine the value of the bias by querying the bias property of the [**Win32\_TimeZone**](win32-timezone.md) class.

For example: "\*\*\*\*\*\*\*\*123000.000000-420" specifies 14.30 (2:30 P.M.) PST with daylight savings time in effect.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (10), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Status")
</dt> </dl>

String that indicates the current status of the object. Operational and non-operational status can be defined. Operational status can include "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates that an element is functioning properly, but is predicting a failure (for example, a SMART-enabled hard disk drive).

Non-operational status can include "Error", "Starting", "Stopping", and "Service". "Service" can apply during disk mirror-resilvering, reloading a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> <dt>

**TimeSubmitted**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time that the job was submitted.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**UntilTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time at which the job is invalid or should be stopped.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> </dl>

## Remarks

Each job scheduled against the schedule service is stored persistently (the scheduler can start a job after a reboot), and is executed at the specified time and day of the week or month. If the computer is not active, or if the scheduled service is not running at the specified job time, the schedule service runs the specified job on the next day at the specified time.

Jobs are scheduled according to Coordinated Universal Time (UTC) with bias offset from Greenwich Mean Time (GMT), which means that a job can be specified using any time zone. The **Win32\_ScheduledJob** class returns the local time with UTC offset when enumerating an object, and converts to local time when creating new jobs. For example, a job specified to run on a computer in Boston at 10:30 P.M. Monday PST time will be scheduled to run locally at 1:30 A.M. Tuesday EST.

> [!Note]  
> A client must take into account whether or not daylight savings time is in operation on the local computer, and if it is, then subtract a bias of 60 minutes from the UTC offset.

 

The **Win32\_ScheduledJob** class is derived from [**CIM\_Job**](cim-job.md). You must be a member of the administrators group to create a scheduled job using this class.

The **Win32\_ScheduledJob** class is internally using the AT protocol, which is bound to deprecation starting with Windows 8 and Windows Server 2012. As a first step the AT protocol is disabled by default. If the protocol is disabled, for example calling the [**Create**](create-method-in-class-win32-scheduledjob.md) method on a **Win32\_ScheduledJob** object will fail with error 0x8. You can turn the AT protocol back on by adding the following registry entry:

``` syntax
Key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\Configuration 
Name: EnableAt 
Type: REG_DWORD
Value: 1
```

You may need to restart the machine to make the setting effective.

Because **Win32\_ScheduledJob** is based on the [**NetScheduleJobGetInfo**](/windows/win32/api/lmat/nf-lmat-netschedulejobgetinfo) Win32 API, you cannot use this class in conjunction with the Task Scheduler. If you wish to use Task Scheduler, use the Task Scheduler API. For more information, see the [Task Scheduler Reference](../taskschd/task-scheduler-reference.md).

## Examples

The following VBScript code example schedules Notepad.exe to run interactively at 1:25 by the local computer time every Wednesday.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\Root\CIMv2")
Set objNewJob = objWMIService.Get("Win32_ScheduledJob")
errJobCreated = objNewJob.Create("Notepad.exe", "********012500.000000-420", True , 4, , True, JobId) 
If errJobCreated <> 0 Then
Wscript.Echo "Error on task creation"
Else
Wscript.Echo "Task created"
End If
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Job**](cim-job.md)
</dt> <dt>

[Operating System Classes](./operating-system-classes.md)
</dt> <dt>

[WMI Tasks: Scheduled Tasks](../wmisdk/wmi-tasks--scheduled-tasks.md)
</dt> </dl>

 

 
