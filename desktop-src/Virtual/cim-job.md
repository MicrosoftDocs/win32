---
title: CIM\_Job class
description: A logical element that represents a unit of work to execute, such as a script or a print job. A job is distinct from a process because a job can be scheduled or queued, and its execution is not limited to a single system.
ms.assetid: 84c3e098-66a9-456a-a173-689b2ef53bd5
keywords:
- CIM_Job class Hyper-V
- CIM_Job class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_Job
- CIM_Job.Caption
- CIM_Job.Description
- CIM_Job.ElementName
- CIM_Job.InstallDate
- CIM_Job.Name
- CIM_Job.OperationalStatus
- CIM_Job.StatusDescriptions
- CIM_Job.Status
- CIM_Job.HealthState
- CIM_Job.JobStatus
- CIM_Job.TimeSubmitted
- CIM_Job.ScheduledStartTime
- CIM_Job.StartTime
- CIM_Job.ElapsedTime
- CIM_Job.JobRunTimes
- CIM_Job.RunMonth
- CIM_Job.RunDay
- CIM_Job.RunDayOfWeek
- CIM_Job.RunStartInterval
- CIM_Job.LocalOrUtcTime
- CIM_Job.UntilTime
- CIM_Job.Notify
- CIM_Job.Owner
- CIM_Job.Priority
- CIM_Job.PercentComplete
- CIM_Job.DeleteOnCompletion
- CIM_Job.ErrorCode
- CIM_Job.ErrorDescription
- CIM_Job.ErrorSummaryDescription
- CIM_Job.RecoveryAction
- CIM_Job.OtherRecoveryAction
api_location:
- Root\virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_Job class

A logical element that represents a unit of work to execute, such as a script or a print job. A job is distinct from a process because a job can be scheduled or queued, and its execution is not limited to a single system.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.10.0"), AMENDMENT]
class CIM_Job : CIM_LogicalElement
{
  string   Caption;
  string   Description;
  string   ElementName;
  datetime InstallDate;
  string   Name;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  string   JobStatus;
  datetime TimeSubmitted;
  datetime ScheduledStartTime;
  datetime StartTime;
  datetime ElapsedTime;
  uint32   JobRunTimes = 1;
  uint8    RunMonth;
  sint8    RunDay;
  sint8    RunDayOfWeek;
  datetime RunStartInterval;
  uint16   LocalOrUtcTime;
  datetime UntilTime;
  string   Notify;
  string   Owner;
  uint32   Priority;
  uint16   PercentComplete;
  boolean  DeleteOnCompletion;
  uint16   ErrorCode;
  string   ErrorDescription;
  string   ErrorSummaryDescription;
  uint16   RecoveryAction;
  string   OtherRecoveryAction;
};
```

## Members

The **CIM\_Job** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_Job** class has these methods.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>KillJob</strong>](cim-job-killjob.md)</td>
<td style="text-align: left;">This method is deprecated. Instead, use the <strong>RequestStateChange</strong> method.<br/>
<blockquote>
[!Note]<br />
Deprecated description: Shuts down a job.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **CIM\_Job** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DeleteOnCompletion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to delete the job upon completion; otherwise, **false**.

> [!Note]  
> This property will not delete jobs that complete before this property is set to **True**.

 

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElapsedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**SubType**](https://msdn.microsoft.com/library/aa393651) ("Interval")
</dt> </dl>

The duration for which the job has run.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**ErrorDescription**")
</dt> </dl>

A vendor-specific error code that captures processing information for recurring jobs. The value must be set to zero if the job completed without error.

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**ErrorCode**")
</dt> </dl>

A free-form string that contains a description of the corresponding error code in the **ErrorCode** property.

</dd> <dt>

**ErrorSummaryDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**ErrorCode**")
</dt> </dl>

A summary description of the error.

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current health of the element. This attribute expresses the health of this element, but not necessarily the health of its subcomponents.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The implementation cannot report on **HealthState** at this time.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

The element is fully functional and operates within normal operational parameters and without error.

</dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>**Degraded/Warning** (10)


</dt> <dd>

The element is in working order, and all functionality is provided. However, the element does not function to the best of its abilities. For example, the element might not operate at optimal performance, or it might report recoverable errors.

</dd> <dt>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>**Minor failure** (15)


</dt> <dd>

All functionality is available, but some functionality might be degraded.

</dd> <dt>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>**Major failure** (20)


</dt> <dd>

The element is failing. It is possible that some or all of the functionality of this component is degraded or does not work.

</dd> <dt>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>**Critical failure** (25)


</dt> <dd>

The element is nonfunctional, and recovery might not be possible.

</dd> <dt>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-recoverable error** (30)


</dt> <dd>

The element has completely failed, and recovery is not possible. All functionality that this element provides has been lost.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the object was installed. The lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**JobRunTimes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of times to run the job.

The possible values are.

<dt>

0
</dt> <dd>

Repeat the job until the time specified by the **UntilTime** property or until it is manually shut down.

</dd> <dt>



 (1)


</dt> <dd>

Run the job once. This is the default value.

</dd> <dt>

2 4294967295
</dt> <dd>

Run the job for the specified number of times.

</dd> </dl>

</dd> <dt>

**JobStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

A free-form string that represents the status of the job.

</dd> <dt>

**LocalOrUtcTime**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the times in the **RunStartInterval** and **UntilTime** properties represent local times or UTC times.

The possible values are.

<dt>

<span id="Local_Time"></span><span id="local_time"></span><span id="LOCAL_TIME"></span>

<span id="Local_Time"></span><span id="local_time"></span><span id="LOCAL_TIME"></span>**Local Time** (1)


</dt> <dd>

Local time.

</dd> <dt>

<span id="UTC_Time"></span><span id="utc_time"></span><span id="UTC_TIME"></span>

<span id="UTC_Time"></span><span id="utc_time"></span><span id="UTC_TIME"></span>**UTC Time** (2)


</dt> <dd>

UTC time.

</dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

The label by which the object is known. When subclassed, the **Name** property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Notify**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The user to notify when a job completes or fails.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**StatusDescriptions**")
</dt> </dl>

Contains indicators of the current status of the element. The first value of the **OperationalStatus** property should contain the primary status for the element.

> [!Note]  
> The **OperationalStatus** property replaces the deprecated **Status** property. Due to the widespread use of the existing **Status** property in management applications, we strongly recommend that providers or instrumentation provide both the **Status** and **OperationalStatus** properties. When instrumented, **Status**, because it is a single-valued property, should also provide the primary status of the element.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

Indicates that the implementation cannot report on the **OperationalStatus** property at this time.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

Indicates an undefined state.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd>

Indicates full functionality without errors.

</dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)


</dt> <dd>

Indicates that the element is in working order and that all functionality is provided. However, the element does not function to the best of its abilities. For example, the element might not operate at optimal performance, or it might report recoverable errors.

</dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)


</dt> <dd>

Indicates that the element functions, but requires attention. Overload and overheated are examples of **Stressed** states.

</dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)


</dt> <dd>

Indicates that an element functions nominally, but predicts a failure in the near future.

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)


</dt> <dd>

Indicates that an error has occurred.

</dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)


</dt> <dd>

Indicates that a nonrecoverable error has occurred.

</dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)


</dt> <dd>

Indicates that the job is starting.

</dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)


</dt> <dd>

Indicates that the job is stopping.

</dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)


</dt> <dd>

Indicates that the element has been intentionally stopped.

</dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)


</dt> <dd>

Indicates that the element is in process to be configured, maintained, cleaned, or otherwise administered.

</dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)


</dt> <dd>

Indicates that the monitoring system has information about this element, but has never been able to establish communications with it.

</dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)


</dt> <dd>

Indicates that the monitoring system has successfully contacted this element in the past, but it is currently unavailable.

</dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)


</dt> <dd>

Indicates that the job stopped in an unexpected way. The state and configuration of the job might require an update.

</dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)


</dt> <dd>

Indicates that the job is inactive.

</dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)


</dt> <dd>

Indicates that an element on which this job depends is in error. This element might be **OK** but cannot function because of the state of a dependent element. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)


</dt> <dd>

Indicates that the job has completed its operation. This value should be combined with either **OK**, **Error**, or **Degraded** to indicate to a client whether the complete operation **Completed** with **OK** and passed, or completed with **Error** and failed, or completed with **Degraded** and finished the operation, but did not complete OK or did not report an error.

</dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>**Power Mode** (18)


</dt> <dd>

Indicates that the element has additional power model information that is contained in the associated power management service.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

</dd> <dt>

**OtherRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**RecoveryAction**")
</dt> </dl>

A string that describes the recovery action when the **RecoveryAction** property is **Other** ("1").

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_OwningJobElement")
</dt> </dl>

The user that submitted the Job, or the service or method name that requested the job.

</dd> <dt>

**PercentComplete**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percent"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (101)
</dt> </dl>

The percentage of the job that is complete.

> [!Note]  
> The value "101" is undefined and will be not be allowed in the next major revision of the specification.

 

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The importance of the job. The lower the number, the higher the priority.

</dd> <dt>

**RecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**OtherRecoveryAction**")
</dt> </dl>

Describes the recovery action to take when a run job fails.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

Unknown.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

Take the action specified in the **OtherRecoveryAction** property.

</dd> <dt>

<span id="Do_Not_Continue"></span><span id="do_not_continue"></span><span id="DO_NOT_CONTINUE"></span>

<span id="Do_Not_Continue"></span><span id="do_not_continue"></span><span id="DO_NOT_CONTINUE"></span>**Do Not Continue** (2)


</dt> <dd>

Stop the job and update its status.

</dd> <dt>

<span id="Continue_With_Next_Job"></span><span id="continue_with_next_job"></span><span id="CONTINUE_WITH_NEXT_JOB"></span>

<span id="Continue_With_Next_Job"></span><span id="continue_with_next_job"></span><span id="CONTINUE_WITH_NEXT_JOB"></span>**Continue With Next Job** (3)


</dt> <dd>

Run the next job in the queue.

</dd> <dt>

<span id="Re-run_Job"></span><span id="re-run_job"></span><span id="RE-RUN_JOB"></span>

<span id="Re-run_Job"></span><span id="re-run_job"></span><span id="RE-RUN_JOB"></span>**Re-run Job** (4)


</dt> <dd>

Re-run job.

</dd> <dt>

<span id="Run_Recovery_Job"></span><span id="run_recovery_job"></span><span id="RUN_RECOVERY_JOB"></span>

<span id="Run_Recovery_Job"></span><span id="run_recovery_job"></span><span id="RUN_RECOVERY_JOB"></span>**Run Recovery Job** (5)


</dt> <dd>

Run the recovery job.

</dd> </dl>

</dd> <dt>

**RunDay**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (-31), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (31), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**RunMonth**", "**CIM\_Job**.**RunDayOfWeek**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

An integer that is used on conjunction with the **RunDayOfWeek** property to indicate the day when the job is processed; or, if **RunDayOfWeek** is set to zero, **RunDay** indicates the day of the month when the job is processed. If **RunDay** is a negative integer, it specifies a day relative to the end of the month, or if **RunDay** is a positive integer, it specifies a day relative to the beginning of the month.

</dd> <dt>

**RunDayOfWeek**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**RunMonth**", "**CIM\_Job**.**RunDay**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

An integer that is used on conjunction with the **RunDay** property to indicate the day when the job is processed; or, if **RunDayOfWeek** is set to zero, **RunDay** indicates the day of the month when the job is processed.

The possible values are.

<dt>

<span id="-Saturday"></span><span id="-saturday"></span><span id="-SATURDAY"></span>

<span id="-Saturday"></span><span id="-saturday"></span><span id="-SATURDAY"></span>**-Saturday** (-7)


</dt> <dd>

The job is processed on the last Saturday on or before the day specified by **RunDay**.

</dd> <dt>

<span id="-Friday"></span><span id="-friday"></span><span id="-FRIDAY"></span>

<span id="-Friday"></span><span id="-friday"></span><span id="-FRIDAY"></span>**-Friday** (-6)


</dt> <dd>

The job is processed on the last Friday on or before the day specified by **RunDay**.

</dd> <dt>

<span id="-Thursday"></span><span id="-thursday"></span><span id="-THURSDAY"></span>

<span id="-Thursday"></span><span id="-thursday"></span><span id="-THURSDAY"></span>**-Thursday** (-5)


</dt> <dd>

The job is processed on the last Thursday on or before the day specified by **RunDay**.

</dd> <dt>

<span id="-Wednesday"></span><span id="-wednesday"></span><span id="-WEDNESDAY"></span>

<span id="-Wednesday"></span><span id="-wednesday"></span><span id="-WEDNESDAY"></span>**-Wednesday** (-4)


</dt> <dd>

The job is processed on the last Wednesday on or before the day specified by **RunDay**.

</dd> <dt>

<span id="-Tuesday"></span><span id="-tuesday"></span><span id="-TUESDAY"></span>

<span id="-Tuesday"></span><span id="-tuesday"></span><span id="-TUESDAY"></span>**-Tuesday** (-3)


</dt> <dd>

The job is processed on the last Tuesday on or before the day specified by **RunDay**.

</dd> <dt>

<span id="-Monday"></span><span id="-monday"></span><span id="-MONDAY"></span>

<span id="-Monday"></span><span id="-monday"></span><span id="-MONDAY"></span>**-Monday** (-2)


</dt> <dd>

The job is processed on the last Monday on or before the day specified by **RunDay**.

</dd> <dt>

<span id="-Sunday"></span><span id="-sunday"></span><span id="-SUNDAY"></span>

<span id="-Sunday"></span><span id="-sunday"></span><span id="-SUNDAY"></span>**-Sunday** (-1)


</dt> <dd>

The job is processed on the last Sunday on or before the day specified by **RunDay**.

</dd> <dt>

<span id="ExactDayOfMonth"></span><span id="exactdayofmonth"></span><span id="EXACTDAYOFMONTH"></span>

<span id="ExactDayOfMonth"></span><span id="exactdayofmonth"></span><span id="EXACTDAYOFMONTH"></span>**ExactDayOfMonth** (0)


</dt> <dd>

**RunDay** indicates the day of the month when the job is processed.

</dd> <dt>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>**Sunday** (1)


</dt> <dd>

The job is processed on the first Sunday on or after the day specified by **RunDay**.

</dd> <dt>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>**Monday** (2)


</dt> <dd>

The job is processed on the first Monday on or after the day specified by **RunDay**.

</dd> <dt>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>**Tuesday** (3)


</dt> <dd>

The job is processed on the first Tuesday on or after the day specified by **RunDay**.

</dd> <dt>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>**Wednesday** (4)


</dt> <dd>

The job is processed on the first Wednesday on or after the day specified by **RunDay**.

</dd> <dt>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>**Thursday** (5)


</dt> <dd>

The job is processed on the first Thursday on or after the day specified by **RunDay**.

</dd> <dt>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>**Friday** (6)


</dt> <dd>

The job is processed on the first Friday on or after the day specified by **RunDay**.

</dd> <dt>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>**Saturday** (7)


</dt> <dd>

The job is processed on the first Saturday on or after the day specified by **RunDay**.

</dd> </dl>

</dd> <dt>

**RunMonth**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**RunDay**", "**CIM\_Job**.**RunDayOfWeek**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

The month when the job is processed.

The possible values are.

<dt>

<span id="January"></span><span id="january"></span><span id="JANUARY"></span>

**January** (0)


</dt> <dd></dd> <dt>

<span id="February"></span><span id="february"></span><span id="FEBRUARY"></span>

**February** (1)


</dt> <dd></dd> <dt>

<span id="March"></span><span id="march"></span><span id="MARCH"></span>

**March** (2)


</dt> <dd></dd> <dt>

<span id="April"></span><span id="april"></span><span id="APRIL"></span>

**April** (3)


</dt> <dd></dd> <dt>

<span id="May"></span><span id="may"></span><span id="MAY"></span>

**May** (4)


</dt> <dd></dd> <dt>

<span id="June"></span><span id="june"></span><span id="JUNE"></span>

**June** (5)


</dt> <dd></dd> <dt>

<span id="July"></span><span id="july"></span><span id="JULY"></span>

**July** (6)


</dt> <dd></dd> <dt>

<span id="August"></span><span id="august"></span><span id="AUGUST"></span>

**August** (7)


</dt> <dd></dd> <dt>

<span id="September"></span><span id="september"></span><span id="SEPTEMBER"></span>

**September** (8)


</dt> <dd></dd> <dt>

<span id="October"></span><span id="october"></span><span id="OCTOBER"></span>

**October** (9)


</dt> <dd></dd> <dt>

<span id="November"></span><span id="november"></span><span id="NOVEMBER"></span>

**November** (10)


</dt> <dd></dd> <dt>

<span id="December"></span><span id="december"></span><span id="DECEMBER"></span>

**December** (11)


</dt> <dd></dd> </dl>

</dd> <dt>

**RunStartInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**SubType**](https://msdn.microsoft.com/library/aa393651) ("Interval"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**RunMonth**", "**CIM\_Job**.**RunDay**", "**CIM\_Job**.**RunDayOfWeek**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

The time interval after midnight when the job is be processed. For example, "00000000020000.000000:000" indicates that the job is be run on or after two o'clock local time, or UTC time (UTC is specified with the **LocalOrUtcTime** property).

</dd> <dt>

**ScheduledStartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("**CIM\_Job**.**RunMonth**", "**CIM\_Job**.**RunDay**", "**CIM\_Job**.**RunDayOfWeek**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

> [!Note]  
> This property is deprecated. Instead we recommend that you use the **RunMonth**, **RunDay**, **RunDayOfWeek**, and **RunStartInterval** properties.

 

The time when the current job is scheduled to start. This time can be represented by a date and time, or an interval relative to the time when the property is requested. A value of all zeroes indicates that the job is already executing.

</dd> <dt>

**StartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the job started. This time can be represented by a date and time, or by an interval relative to the time when the property is requested.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Indicates the primary status of the object.

> [!Note]  
> This property is deprecated. It is replaced by the **OperationalStatus** property. If you choose to use the **Status** property for backward compatibility, it should be secondary to the **OperationalStatus** property.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Indicates descriptions of the corresponding values in the **OperationalStatus** array. For example, if an element in the **OperationalStatus** property contains the value **Stopping**, then the element at the same array index in this property might contain an explanation as to why an object is being stopped.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**TimeSubmitted**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the job was submitted. A value of all zeroes indicates that the parent element is not capable of reporting a date and time.

</dd> <dt>

**UntilTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**LocalOrUtcTime**")
</dt> </dl>

The time after which the job becomes invalid or should be stopped. The time can be represented by a date and time, or by an interval relative to the time when this property is requested. A value of all nines indicates that the job can run indefinitely.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalElement**](cim-logicalelement.md)
</dt> </dl>

 

 





